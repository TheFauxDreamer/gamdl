import logging

import httpx

from ..utils import raise_for_status, safe_json
from .constants import ITUNES_LOOKUP_API_URL, ITUNES_PAGE_API_URL, STOREFRONT_IDS

ITUNES_SEARCH_API_URL = "https://itunes.apple.com/search"

logger = logging.getLogger(__name__)


class ItunesApi:
    def __init__(
        self,
        storefront: str = "us",
        language: str = "en-US",
    ) -> None:
        self.storefront = storefront
        self.language = language
        self.initialize()

    def initialize(self) -> None:
        self._initialize_storefront_id()
        self._initialize_client()

    def _initialize_storefront_id(self) -> None:
        try:
            self.storefront_id = STOREFRONT_IDS[self.storefront.upper()]
        except KeyError:
            raise Exception(f"No storefront id for {self.storefront}")

    def _initialize_client(self) -> None:
        self.client = httpx.AsyncClient(
            params={
                "country": self.storefront,
                "lang": self.language,
            },
            headers={
                "X-Apple-Store-Front": f"{self.storefront_id} t:music31",
            },
            timeout=300.0,
        )

    async def get_lookup_result(
        self,
        media_id: str,
        entity: str = "album",
    ) -> dict:
        response = await self.client.get(
            ITUNES_LOOKUP_API_URL,
            params={
                "id": media_id,
                "entity": entity,
            },
        )
        raise_for_status(response)

        lookup_result = safe_json(response)
        if "results" not in lookup_result:
            raise Exception("Error getting lookup result:", response.text)
        logger.debug(f"Lookup result: {lookup_result}")

        return lookup_result

    async def get_itunes_page(
        self,
        media_type: str,
        media_id: str,
    ) -> dict:
        response = await self.client.get(
            f"{ITUNES_PAGE_API_URL}/{media_type}/{media_id}"
        )
        raise_for_status(response)

        itunes_page = safe_json(response)
        if "storePlatformData" not in itunes_page:
            raise Exception("Error getting iTunes page:", response.text)
        logger.debug(f"iTunes page: {itunes_page}")

        return itunes_page

    async def search_podcasts(
        self,
        term: str,
        limit: int = 50,
        offset: int = 0,
    ) -> dict:
        """Search for podcasts by name/keyword using iTunes Search API."""
        response = await self.client.get(
            ITUNES_SEARCH_API_URL,
            params={
                "term": term,
                "entity": "podcast",
                "limit": limit,
                "offset": offset,
                "media": "podcast",
            },
        )
        raise_for_status(response)

        search_result = safe_json(response)
        if "results" not in search_result:
            raise Exception("Error searching podcasts:", response.text)
        logger.debug(f"Podcast search result: {search_result}")

        return search_result

    async def get_podcast_episodes(
        self,
        podcast_id: int,
        limit: int = 200,
    ) -> dict:
        """Get episodes for a specific podcast using iTunes Lookup API."""
        response = await self.client.get(
            ITUNES_LOOKUP_API_URL,
            params={
                "id": podcast_id,
                "entity": "podcastEpisode",
                "limit": limit,
            },
        )
        raise_for_status(response)

        lookup_result = safe_json(response)
        if "results" not in lookup_result:
            raise Exception("Error getting podcast episodes:", response.text)
        logger.debug(f"Podcast episodes result: {lookup_result}")

        return lookup_result
