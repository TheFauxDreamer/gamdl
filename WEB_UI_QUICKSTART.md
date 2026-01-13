# gamdl Web UI - Quick Start Guide

Get started with the gamdl web interface in 3 simple steps!

## Step 1: Install with Web Support

```bash
# Install gamdl with web UI dependencies
pip install -e ".[web]"
```

## Step 2: Start the Web Server

```bash
gamdl-web
```

You should see:
```
🎵 gamdl Web UI starting...
📡 Server: http://127.0.0.1:8080
⚡ Press Ctrl+C to stop
```

## Step 3: Open in Browser

1. Open your browser to: **http://127.0.0.1:8080**
2. Enter your Apple Music URLs (one per line)
3. Set your cookies path (e.g., `~/.gamdl/cookies.txt`)
4. Click "Start Download"

## What You'll See

### For Large Playlists (13,000+ songs)

The web UI shows real-time progress at every stage:

**Stage 1: Fetching Pages**
```
Fetching playlist tracks (page 1, 300 tracks so far)...
Fetching playlist tracks (page 2, 600 tracks so far)...
Fetching playlist tracks (page 43, 12900 tracks so far)...
Fetched 13000 tracks total. Processing metadata...
```

**Stage 2: Processing Metadata**
```
Processing metadata: 1300/13000 tracks (10.0%)
Processing metadata: 2600/13000 tracks (20.0%)
Processing metadata: 3900/13000 tracks (30.0%)
...
Processing metadata: 13000/13000 tracks (100.0%)
Finished processing metadata for 13000 tracks.
```

**Stage 3: Downloading**
```
[Track 1/13000] Downloading: Song Title
[Track 1/13000] Completed: Song Title
[Track 2/13000] Downloading: Another Song
...
```

## Advanced Options

Click "⚙️ Advanced Options" to configure:

- **Song Codec**: AAC, ALAC, Atmos, etc.
- **Cover Size**: Resolution in pixels
- **Video Resolution**: Up to 4K
- **Metadata**: Skip cover, skip lyrics, fetch extra tags

## Custom Host/Port

```bash
# Listen on all interfaces
gamdl-web --host 0.0.0.0 --port 3000

# Then access from any device on your network:
# http://YOUR_IP:3000
```

## Troubleshooting

**"Cookies file not found"**
- Export cookies from your browser using a cookies extension
- Save in Netscape format to `~/.gamdl/cookies.txt`

**No progress showing**
- Check browser console for WebSocket errors
- Ensure firewall isn't blocking the port

**Download fails**
- Verify Apple Music subscription is active
- Check cookies are valid and not expired

## More Information

- Full documentation: [gamdl/web/README.md](gamdl/web/README.md)
- CLI documentation: [README.md](README.md)

---

**Enjoy your new web interface with real-time progress tracking!** 🎵
