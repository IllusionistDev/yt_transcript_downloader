import sys
import argparse
import subprocess
import os

# --- AUTO-INSTALLER ---
def install_dependencies():
    try:
        import yt_dlp
    except ImportError:
        print("Required library 'yt-dlp' not found. Installing the latest version...")
        # We install/upgrade to ensure we have the latest bypasses
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "yt_dlp"])
        print("Installation successful.\n")

install_dependencies()
import yt_dlp

def download_transcript(url, lang='en', output_file='transcript.txt'):
    """
    Uses yt-dlp to fetch subtitles/transcripts. 
    yt-dlp is much more resilient to 'No element found' errors.
    """
    
    # Configure yt-dlp options
    ydl_opts = {
        'skip_download': True,        # We don't want the video file
        'writesubtitles': True,       # Get manual subtitles
        'writeautomaticsub': True,   # Get auto-generated if manual is missing
        'subtitleslangs': [lang],     # Target language
        'quiet': True,
        'no_warnings': True,
    }

    print(f"Connecting to YouTube for: {url}")
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            # Subtitles are stored in the 'requested_subtitles' or 'subtitles' key
            subtitles = info.get('requested_subtitles')
            
            if not subtitles or lang not in subtitles:
                # Fallback: check if any subs exist at all
                available = info.get('subtitles', {}).keys() or info.get('automatic_captions', {}).keys()
                raise ValueError(f"Language '{lang}' not found. Available: {list(available)}")

            # Get the URL of the subtitle file (usually in VTT or JSON format)
            sub_url = subtitles[lang]['url']
            
            # Download the actual content using yt-dlp's internal downloader
            # To keep this script 'full robust' and dependency-light, we use a simple request
            import urllib.request
            response = urllib.request.urlopen(sub_url)
            content = response.read().decode('utf-8')

            # Clean up VTT formatting to give a clean transcript
            clean_text = clean_vtt(content)

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(clean_text)
            
            print(f"Successfully saved transcript to: {output_file}")

    except Exception as e:
        print(f"CRITICAL ERROR: {str(e)}")
        sys.exit(1)

def clean_vtt(vtt_text):
    """Simple parser to remove VTT timestamps and headers for a clean text file."""
    lines = vtt_text.splitlines()
    clean_lines = []
    for line in lines:
        # Skip VTT headers, timestamps, and empty lines
        if "-->" in line or "WEBVTT" in line or line.isdigit() or not line.strip():
            continue
        # Remove duplicate consecutive lines (common in auto-generated subs)
        if not clean_lines or line.strip() != clean_lines[-1]:
            clean_lines.append(line.strip())
    return "\n".join(clean_lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reliable YouTube Transcript Downloader")
    parser.add_argument("url", help="YouTube Video URL")
    parser.add_argument("--lang", default="en", help="Language code (e.g., en, es, fr)")
    parser.add_argument("--out", default="transcript.txt", help="Output filename")

    args = parser.parse_args()
    download_transcript(args.url, args.lang, args.out)
