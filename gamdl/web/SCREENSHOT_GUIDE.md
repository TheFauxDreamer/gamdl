# Web UI Screenshot Guide

This document describes what the web UI looks like for documentation purposes.

## Main Interface

### Landing Page

When you first open `http://127.0.0.1:8080`, you see:

```
┌────────────────────────────────────────────────────────────┐
│  gamdl Web UI                                              │
│  Download Apple Music songs, albums, and playlists        │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Apple Music URLs (one per line)                          │
│  ┌────────────────────────────────────────────────────┐   │
│  │ https://music.apple.com/us/album/...              │   │
│  │ https://music.apple.com/us/playlist/...           │   │
│  │                                                    │   │
│  └────────────────────────────────────────────────────┘   │
│                                                            │
│  Cookies Path (Netscape format)                           │
│  ┌────────────────────────────────────────────────────┐   │
│  │ /path/to/cookies.txt                              │   │
│  └────────────────────────────────────────────────────┘   │
│                                                            │
│  Output Path                                              │
│  ┌────────────────────────────────────────────────────┐   │
│  │ ./downloads                                       │   │
│  └────────────────────────────────────────────────────┘   │
│                                                            │
│  ⚙️ Advanced Options (click to expand)                    │
│                                                            │
│  ┌───────────────────────┐                                │
│  │ Start Download        │                                │
│  └───────────────────────────────────┘                    │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### Advanced Options (Expanded)

```
┌────────────────────────────────────────────────────────────┐
│  ⚙️ Advanced Options (click to expand)                    │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Song Codec              Cover Size (px)                  │
│  ┌──────────────┐        ┌──────────────┐                │
│  │ Default (AAC)│        │ 1200         │                │
│  └──────────────┘        └──────────────┘                │
│                                                            │
│  Music Video Resolution  Cover Format                     │
│  ┌──────────────┐        ┌──────────────┐                │
│  │ Best Available│       │ Default (JPG)│                │
│  └──────────────┘        └──────────────┘                │
│                                                            │
│  ☐ Skip cover art download                                │
│  ☐ Skip lyrics download                                   │
│  ☐ Fetch extra tags from Apple Music preview             │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

## Progress Display

### Active Download (Small Playlist - 50 songs)

```
┌────────────────────────────────────────────────────────────┐
│  ● Connected - Processing...                              │
├────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────┐ │
│  │ [19:30:15] Session started                           │ │
│  │ [19:30:15] Initializing Apple Music API...           │ │
│  │ [19:30:16] API initialized successfully              │ │
│  │ [19:30:16] Processing 1 URL(s)...                    │ │
│  │ [19:30:16] [URL 1/1] Processing: https://...        │ │
│  │ [19:30:16] Fetching metadata for https://...         │ │
│  │ [19:30:17] Fetching page 1, 50 tracks so far...      │ │
│  │ [19:30:17] Fetched 50 tracks total                   │ │
│  │ [19:30:17] Processing metadata...                    │ │
│  │ [19:30:18] Processing metadata: 10/50 (20.0%)        │ │
│  │ [19:30:19] Processing metadata: 20/50 (40.0%)        │ │
│  │ [19:30:20] Processing metadata: 30/50 (60.0%)        │ │
│  │ [19:30:21] Processing metadata: 40/50 (80.0%)        │ │
│  │ [19:30:22] Processing metadata: 50/50 (100.0%)       │ │
│  │ [19:30:22] Finished processing metadata              │ │
│  │ [19:30:22] Found 50 track(s) to download             │ │
│  │ [19:30:22] [Track 1/50] Downloading: Song Title 1   │ │
│  │ [19:30:23] [Track 1/50] Completed: Song Title 1     │ │
│  │ [19:30:23] [Track 2/50] Downloading: Song Title 2   │ │
│  │ █                                                     │ │
│  └──────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────┘
```

### Active Download (Large Playlist - 13,000 songs)

```
┌────────────────────────────────────────────────────────────┐
│  ● Connected - Processing...                              │
├────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────┐ │
│  │ [19:30:15] Session started                           │ │
│  │ [19:30:15] Initializing Apple Music API...           │ │
│  │ [19:30:16] API initialized successfully              │ │
│  │ [19:30:16] Processing 1 URL(s)...                    │ │
│  │ [19:30:16] [URL 1/1] Processing: https://...        │ │
│  │ [19:30:16] Fetching metadata for https://...         │ │
│  │                                                       │ │
│  │ ───── STAGE 1: Pagination ─────                      │ │
│  │ [19:30:17] Fetching page 1, 300 tracks so far...     │ │
│  │ [19:30:18] Fetching page 2, 600 tracks so far...     │ │
│  │ [19:30:19] Fetching page 3, 900 tracks so far...     │ │
│  │ [19:30:20] Fetching page 4, 1200 tracks so far...    │ │
│  │ [19:30:21] Fetching page 5, 1500 tracks so far...    │ │
│  │ ...                                                   │ │
│  │ [19:31:40] Fetching page 43, 12900 tracks so far...  │ │
│  │ [19:31:41] Fetching page 44, 13000 tracks so far...  │ │
│  │ [19:31:41] Fetched 13000 tracks total                │ │
│  │                                                       │ │
│  │ ───── STAGE 2: Metadata Processing ─────             │ │
│  │ [19:31:41] Processing metadata...                    │ │
│  │ [19:31:50] Processing: 1300/13000 tracks (10.0%)     │ │
│  │ [19:32:00] Processing: 2600/13000 tracks (20.0%)     │ │
│  │ [19:32:10] Processing: 3900/13000 tracks (30.0%)     │ │
│  │ [19:32:20] Processing: 5200/13000 tracks (40.0%)     │ │
│  │ [19:32:30] Processing: 6500/13000 tracks (50.0%)     │ │
│  │ [19:32:40] Processing: 7800/13000 tracks (60.0%)     │ │
│  │ [19:32:50] Processing: 9100/13000 tracks (70.0%)     │ │
│  │ [19:33:00] Processing: 10400/13000 tracks (80.0%)    │ │
│  │ [19:33:10] Processing: 11700/13000 tracks (90.0%)    │ │
│  │ [19:33:20] Processing: 13000/13000 tracks (100.0%)   │ │
│  │ [19:33:20] Finished processing metadata              │ │
│  │                                                       │ │
│  │ ───── STAGE 3: Downloads ─────                       │ │
│  │ [19:33:20] Found 13000 track(s) to download          │ │
│  │ [19:33:20] [Track 1/13000] Downloading: Song 1      │ │
│  │ [19:33:21] [Track 1/13000] Completed: Song 1        │ │
│  │ [19:33:21] [Track 2/13000] Downloading: Song 2      │ │
│  │ █                                                     │ │
│  └──────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────┘
```

### Completed Download

```
┌────────────────────────────────────────────────────────────┐
│  ○ Completed                                               │
├────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────┐ │
│  │ [19:30:15] Session started                           │ │
│  │ ...                                                   │ │
│  │ [20:45:30] [Track 13000/13000] Completed: Last Song │ │
│  │ [20:45:30] All downloads completed!                  │ │
│  │ [20:45:30] Connection closed                         │ │
│  └──────────────────────────────────────────────────────┘ │
│                                                            │
│  ┌───────────────────────┐                                │
│  │ Start Download        │  (button enabled again)        │
│  └───────────────────────────────────┘                    │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### Error State

```
┌────────────────────────────────────────────────────────────┐
│  ○ Error occurred                                          │
├────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────┐ │
│  │ [19:30:15] Session started                           │ │
│  │ [19:30:15] Initializing Apple Music API...           │ │
│  │ [19:30:16] ERROR: Cookies file not found             │ │
│  │ [19:30:16] Please provide a valid cookies.txt file   │ │
│  │ [19:30:16] Connection closed                         │ │
│  └──────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────┘
```

## Color Coding

The terminal-style log uses different colors for different message types:

- **Green** (info): `#4ec9b0` - Regular progress messages
- **Yellow** (warning): `#dcdcaa` - Warnings and skipped items
- **Red** (error): `#f48771` - Errors and failures
- **Light Green** (success): `#b5cea8` - Completion messages

## Status Indicator

The status indicator (circle) at the top shows:

- **Gray** (○): Idle/Disconnected
- **Green with pulse** (●): Active/Processing (animated pulsing effect)

## Responsive Design

The interface is responsive and works on:

- Desktop browsers (Chrome, Firefox, Safari, Edge)
- Tablets (iPad, Android tablets)
- Mobile phones (portrait and landscape)

The layout adapts to smaller screens by stacking form elements vertically.

## Browser Compatibility

Tested and works on:

- ✅ Chrome/Chromium 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

WebSocket support is required (all modern browsers have this).

## Accessibility

- Semantic HTML structure
- Keyboard navigation support
- Screen reader friendly labels
- High contrast colors
- Clear focus indicators

## Performance

- Real-time updates via WebSocket (minimal latency)
- Efficient DOM updates (only append new log lines)
- Auto-scroll to bottom on new messages
- Max log height with scrollbar to prevent page bloat
- Session cleanup after completion

## Future UI Enhancements

Potential visual improvements:

- Progress bar showing overall completion percentage
- Estimated time remaining
- Download speed indicator
- Pause/resume buttons
- Download history list
- Dark mode toggle
- Tabbed interface for multiple concurrent downloads
- File tree view of downloaded files
- Preview of downloaded cover art
