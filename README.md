# YouTube Video Downloader 📺

A modern, user-friendly web application for downloading YouTube videos built with Flask and yt-dlp. Features a beautiful glassmorphism UI design with responsive layout and robust error handling.

![YouTube Downloader Screenshot](https://img.shields.io/badge/Status-Active-brightgreen) ![Python](https://img.shields.io/badge/Python-3.7+-blue) ![Flask](https://img.shields.io/badge/Flask-2.0+-red)

## ✨ Features

- **Modern UI Design**: Beautiful glassmorphism interface with gradient backgrounds
- **Multi-format Support**: Downloads YouTube videos, shorts, and various URL formats
- **High Quality Downloads**: Automatically selects best available quality in MP4 format
- **Real-time Validation**: Client-side URL validation with instant feedback
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Error Handling**: Comprehensive error messages and user feedback
- **Loading States**: Visual feedback during download processing

## 🚀 Supported URLs

- Regular YouTube videos: `https://www.youtube.com/watch?v=VIDEO_ID`
- YouTube Shorts: `https://www.youtube.com/shorts/VIDEO_ID`
- Short URLs: `https://youtu.be/VIDEO_ID`

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/IshanNaikele/youtube-video-downloader.git
   cd youtube-video-downloader
   ```

2. **Install required dependencies**
   ```bash
   pip install flask yt-dlp
   ```

3. **Create the template directory structure**
   ```bash
   mkdir templates
   # Move the HTML file to templates/index.html
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your web browser and navigate to `http://localhost:5000`

## 📁 Project Structure

```
youtube-video-downloader/
│
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Frontend template
├── videos/               # Downloaded videos folder (auto-created)
├── cookies.txt           # Optional: YouTube cookies for enhanced access
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## 📦 Dependencies

Create a `requirements.txt` file with the following content:

```txt
Flask==2.3.3
yt-dlp==2023.9.24
```

Then install with:
```bash
pip install -r requirements.txt
```

## 🔧 Configuration

### Download Settings

The application is pre-configured with optimal settings:

- **Output Format**: MP4 with best quality
- **Download Location**: `./videos/` directory
- **Audio Quality**: 192k AAC
- **Video Codec**: Copy original (no re-encoding)

### Optional: Cookie Support

For enhanced access to age-restricted or region-locked content:

1. Export your browser cookies to `cookies.txt`
2. Place the file in the project root directory
3. The application will automatically use it if detected

## 🚦 Usage

1. **Start the Application**
   ```bash
   python app.py
   ```

2. **Open in Browser**
   Navigate to `http://localhost:5000`

3. **Download Videos**
   - Paste a YouTube URL in the input field
   - Click "Download Video"
   - Wait for processing (loading indicator will show)
   - Check the `videos/` folder for your downloaded content

## ⚠️ Error Handling

The application handles various error scenarios:

- **Empty URL**: Prompts user to enter a URL
- **Invalid URL**: Validates YouTube URL format
- **Download Failures**: Network issues, unavailable videos, etc.
- **Processing Errors**: Extraction and conversion problems

## 🎨 UI Features

- **Glassmorphism Design**: Modern translucent card design
- **Gradient Backgrounds**: Eye-catching color schemes
- **Smooth Animations**: Hover effects and loading states
- **Mobile Responsive**: Optimized for all screen sizes
- **Form Validation**: Real-time URL validation
- **Visual Feedback**: Success/error alerts with animations

## 🔒 Legal Notice

**Important**: Please respect copyright laws and YouTube's Terms of Service when using this tool. Only download content you have permission to download or content that is available under appropriate licenses.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Ishan Naikele**
- GitHub: [@IshanNaikele](https://github.com/IshanNaikele)

## 🐛 Issues & Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/IshanNaikele/youtube-video-downloader/issues) page
2. Create a new issue with detailed information
3. Include error messages, Python version, and OS details

## 🔄 Updates & Changelog

### Version 1.0.0
- Initial release
- Modern glassmorphism UI
- Support for YouTube videos, shorts, and short URLs
- Comprehensive error handling
- Mobile-responsive design

## 📊 Technical Details

- **Backend**: Flask (Python web framework)
- **Video Processing**: yt-dlp (YouTube download library)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Design**: Glassmorphism, CSS Grid/Flexbox
- **Validation**: Client-side and server-side URL validation

## 🚀 Deployment

For production deployment, consider:

1. **Using a WSGI server** (Gunicorn, uWSGI)
2. **Setting up reverse proxy** (Nginx, Apache)
3. **Environment variables** for configuration
4. **Docker containerization** for easy deployment

Example Dockerfile:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

---

⭐ **Don't forget to star this repository if you found it helpful!**
