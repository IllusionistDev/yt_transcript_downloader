# 🚀 Robust YouTube Transcript Downloader

A "zero-config" Python utility designed to extract transcripts from YouTube videos reliably. Unlike many other tools that rely on fragile XML parsing or deprecated APIs, this script leverages `yt-dlp` to bypass bot detection and handle various URL formats (Shorts, Mobile, Embeds).

---

## ✨ Features

* **Auto-Dependency Management:** Automatically detects and installs/updates `yt-dlp` on the first run.
* **Highly Resilient:** Bypasses "No element found" and "403 Forbidden" errors common in lighter libraries.
* **Cleans Formatting:** Automatically strips VTT/SRT timestamps and metadata to give you a clean, readable text file.
* **Universal URL Support:** Works with standard URLs, `youtu.be` links, and YouTube Shorts.
* **Multi-language Support:** Fetch transcripts in any available language code (e.g., `en`, `es`, `fr`, `hi`).

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com/IllusionistDev/yt_transcript_downloader
   cd yt-transcript-downloader
   ```

2. **Python Version:**
   Ensure you have **Python 3.7+** installed. No manual `pip install` is required; the script handles it for you on the first execution.

---

## 🚀 Usage

Run the script directly from your terminal or command prompt:

### Basic Usage (English)
```bash
python get_yt.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### Specify Language and Output File
```bash
python get_yt.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --lang es --out my_transcript.txt
```

### Command Line Arguments

| Argument | Description | Default |
| :--- | :--- | :--- |
| `url` | The full YouTube video URL (Required) | N/A |
| `--lang` | The ISO language code for the transcript | `en` |
| `--out` | The filename for the saved transcript | `transcript.txt` |

---

## 🛡️ Why this exists
Many scripts fail because YouTube frequently updates its security headers to block automated XML requests. This script uses `yt-dlp`—the industry standard—which mimics real browser behavior to ensure reliable data retrieval even when YouTube updates its site.

---

## 📝 Troubleshooting

* **"Language not found":** Not all videos have captions. The script will output a list of available language codes if your requested language isn't found.
* **"Video Unavailable":** Ensure the video is public or unlisted. Private videos cannot be accessed without authentication.

---

## ⚖️ License
Distributed under the MIT License. See `LICENSE` for more information.
