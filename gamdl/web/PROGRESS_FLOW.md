# Progress Flow Visualization

## How Progress Updates Work

### CLI Mode

```
User runs: gamdl "https://music.apple.com/playlist/..."
    ↓
[CLI] Processing URL 1/1
    ↓
[Downloader] get_download_queue() called
    ↓
┌─────────────────────────────────────────────────────┐
│ STAGE 1: Fetching Playlist Pages                    │
├─────────────────────────────────────────────────────┤
│ > Fetching playlist tracks (page 1, 300 so far)...  │
│ > Fetching playlist tracks (page 2, 600 so far)...  │
│ > Fetching playlist tracks (page 3, 900 so far)...  │
│ > ...                                                │
│ > Fetched 13000 tracks total. Processing metadata...│
└─────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────┐
│ STAGE 2: Processing Metadata (10 concurrent)        │
├─────────────────────────────────────────────────────┤
│ > Processing metadata: 1300/13000 tracks (10.0%)    │
│ > Processing metadata: 2600/13000 tracks (20.0%)    │
│ > Processing metadata: 3900/13000 tracks (30.0%)    │
│ > ...                                                │
│ > Finished processing metadata for 13000 tracks.    │
└─────────────────────────────────────────────────────┘
    ↓
[CLI] Download queue ready with 13000 items
    ↓
┌─────────────────────────────────────────────────────┐
│ STAGE 3: Downloading Tracks (sequential)            │
├─────────────────────────────────────────────────────┤
│ > [Track 1/13000] Downloading: Song Title 1         │
│ > [Track 1/13000] Completed: Song Title 1           │
│ > [Track 2/13000] Downloading: Song Title 2         │
│ > [Track 2/13000] Completed: Song Title 2           │
│ > ...                                                │
└─────────────────────────────────────────────────────┘
    ↓
[CLI] Finished with 0 error(s)
```

### Web UI Mode

```
User opens browser → http://127.0.0.1:8080
    ↓
User enters URL and clicks "Start Download"
    ↓
[Frontend] POST /api/download
    ↓
[Backend] Creates session with UUID
    ↓
[Frontend] Opens WebSocket: WS /ws/{session_id}
    ↓
    ╔═══════════════════════════════════════════════╗
    ║           WebSocket Connection Open            ║
    ╚═══════════════════════════════════════════════╝
    ↓
┌─────────────────────────────────────────────────────┐
│ Browser receives messages via WebSocket:            │
├─────────────────────────────────────────────────────┤
│                                                      │
│ {"type": "log", "message": "Initializing..."}       │
│ {"type": "log", "message": "API initialized"}       │
│                                                      │
│ STAGE 1: Pagination                                 │
│ {"type": "log", "message": "Fetching page 1..."}    │
│ {"type": "log", "message": "Fetching page 2..."}    │
│ ...                                                  │
│                                                      │
│ STAGE 2: Metadata Processing                        │
│ {"type": "log", "message": "1300/13000 (10%)"}      │
│ {"type": "log", "message": "2600/13000 (20%)"}      │
│ ...                                                  │
│                                                      │
│ STAGE 3: Downloads                                  │
│ {"type": "log", "message": "Track 1/13000: ..."}    │
│ {"type": "log", "message": "Track 2/13000: ..."}    │
│ ...                                                  │
│                                                      │
│ {"type": "complete"}                                 │
└─────────────────────────────────────────────────────┘
    ↓
[Frontend] Displays in color-coded log window
    ↓
[Frontend] Updates status indicator (pulsing green dot)
```

## Code Flow

### Stage 1: Pagination (downloader.py)

```python
async def get_collection_download_items(self, collection_metadata):
    tracks_metadata = [initial 300 tracks]
    page_count = 1
    
    # Progress logging added here
    logger.info(f"Fetching page {page_count}, {len(tracks_metadata)} so far")
    
    async for extended_data in api.extend_api_data(...):
        tracks_metadata.extend(extended_data["data"])
        page_count += 1
        
        # Progress logging added here
        logger.info(f"Fetching page {page_count}, {len(tracks_metadata)} so far")
```

### Stage 2: Metadata Processing (downloader.py + utils.py)

```python
# In downloader.py
def progress_callback(completed: int, total: int):
    interval = max(10, total // 10)  # Every 10 tracks or 10%, whichever is more
    if completed % interval == 0 or completed == total:
        percentage = (completed / total) * 100
        logger.info(f"Processing: {completed}/{total} ({percentage:.1f}%)")

# In utils.py
async def safe_gather(*tasks, progress_callback=None):
    completed_count = 0
    
    async def bounded_task(task):
        nonlocal completed_count
        result = await task
        if progress_callback:
            completed_count += 1
            progress_callback(completed_count, total_count)  # Trigger callback
        return result
```

### Stage 3: Downloads (cli.py - unchanged)

```python
for download_index, download_item in enumerate(download_queue, 1):
    # Already had progress logging
    logger.info(f"[Track {download_index}/{len(download_queue)}] Downloading...")
```

## WebSocket Message Flow

### Message Types

1. **Log Messages**
   ```json
   {
     "type": "log",
     "message": "Some informational message",
     "level": "info"  // info, warning, error, success
   }
   ```

2. **Error Messages**
   ```json
   {
     "type": "error",
     "message": "Error description"
   }
   ```

3. **Completion**
   ```json
   {
     "type": "complete"
   }
   ```

### Frontend Handling

```javascript
ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    
    if (data.type === 'log') {
        // Add colored log line to terminal display
        addLog(data.message, data.level);
    } else if (data.type === 'error') {
        // Show error in red
        addLog(`ERROR: ${data.message}`, 'error');
        updateStatus('Error occurred', false);
    } else if (data.type === 'complete') {
        // Mark as complete, enable download button
        updateStatus('Completed', false);
    }
};
```

## Progress Intervals

### Pagination Stage
- **Frequency**: Every page (~300 songs per page)
- **Example**: For 13,000 songs = ~43 updates

### Metadata Stage
- **Frequency**: Every 10% OR every 10 tracks (whichever is MORE frequent)
- **Small playlists** (< 100 tracks): Every 10 tracks
- **Large playlists** (13,000 tracks): Every 1,300 tracks (10%)
- **Example**: For 13,000 songs = 10 updates (10%, 20%, ..., 100%)

### Download Stage
- **Frequency**: Every track
- **Example**: For 13,000 songs = 13,000 updates

## Performance Considerations

### Why These Intervals?

1. **Pagination**: Low overhead (only 43 log calls for 13k songs)
2. **Metadata**: Balanced (10 updates instead of 13,000)
3. **Downloads**: Every track is reasonable (user wants to see each song)

### Why Not More Frequent?

- Too many log messages can slow down processing
- Terminal/browser can't render thousands of updates per second efficiently
- 10% intervals provide good feedback without overwhelming the system

### Concurrency

- **Pagination**: Sequential (Apple Music API limitation)
- **Metadata**: 10 concurrent (via `safe_gather(limit=10)`)
- **Downloads**: Sequential (avoid overwhelming network/disk)

## Timeline Example (13,000 songs)

```
Time    | Stage           | Progress
--------|-----------------|------------------------------------------
0:00    | Pagination      | Fetching page 1, 300 tracks so far...
0:02    | Pagination      | Fetching page 2, 600 tracks so far...
...     | ...             | ...
1:26    | Pagination      | Fetched 13000 tracks total
1:26    | Metadata        | Processing metadata...
1:27    | Metadata        | 1300/13000 tracks (10.0%)
1:28    | Metadata        | 2600/13000 tracks (20.0%)
...     | ...             | ...
1:36    | Metadata        | Finished processing 13000 tracks
1:36    | Downloads       | [Track 1/13000] Downloading: Song 1
1:36    | Downloads       | [Track 1/13000] Completed: Song 1
1:37    | Downloads       | [Track 2/13000] Downloading: Song 2
...     | ...             | ...
```

Note: Actual times vary based on network speed, server response, etc.
