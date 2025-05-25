from flask import Flask, render_template, request, redirect, url_for
import yt_dlp
import os
import re

app = Flask(__name__)
app.config['DOWNLOAD_FOLDER'] = 'videos'

# Create download folder if missing
if not os.path.exists(app.config['DOWNLOAD_FOLDER']):
    os.makedirs(app.config['DOWNLOAD_FOLDER'])

def is_valid_youtube_url(url):
    """Validate YouTube URLs using regex"""
    patterns = [
        r'^https?://(www\.)?youtube\.com/watch\?v=[\w-]{11}',
        r'^https?://youtu\.be/[\w-]{11}',
        r'^https?://(www\.)?youtube\.com/shorts/[\w-]{11}'
    ]
    return any(re.match(pattern, url) for pattern in patterns)

def download_video(url):
    """Download video using yt-dlp with error handling"""
    ydl_opts = {
        'outtmpl': f"{app.config['DOWNLOAD_FOLDER']}/%(title)s.%(ext)s",
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'merge_output_format': 'mp4',
        'postprocessor_args': [
            '-c:v', 'copy',
            '-c:a', 'aac',
            '-b:a', '192k',
            '-strict', 'experimental'
        ],
        'verbose': True,
        'ignoreerrors': False,
        'geo_bypass': True,
        'cookiefile': 'cookies.txt' if os.path.exists('cookies.txt') else None
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            if info is None:
                raise ValueError("Failed to extract video info")
        return True
    except Exception as e:
        print(f"⛔ Download Error: {str(e)}")
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url', '').strip()
        
        if not url:
            return redirect(url_for('index', error="empty_url"))
        
        if not is_valid_youtube_url(url):
            return redirect(url_for('index', error="invalid_url"))
        
        if download_video(url):
            return redirect(url_for('index', success=True))
        else:
            return redirect(url_for('index', error="download_failed"))

    error = request.args.get('error')
    success = request.args.get('success')
    return render_template('index.html', success=success, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)