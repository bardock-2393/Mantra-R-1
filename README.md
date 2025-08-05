# AI Video Detective - Live Investigation Studio

Advanced AI video analysis application with comprehensive understanding capabilities, featuring autonomous analysis, context-aware conversations, and professional-grade reporting.

## 🚀 Features

- **Autonomous Video Analysis**: Multi-modal understanding with comprehensive coverage
- **Context-Aware Conversations**: Memory-enabled AI agent with conversation history
- **Professional Analysis Types**: Safety investigation, performance analysis, pattern detection, and more
- **Real-time Evidence Generation**: Automatic screenshot and video clip creation
- **Advanced Agent Capabilities**: Proactive insights and adaptive focus
- **Session Management**: Redis-backed session storage with automatic cleanup
- **Default Video Support**: Built-in demo video for immediate testing and demonstration

## 📁 Project Structure

```
ai_video_detective/
├── app.py                      # Main Flask application
├── main.py                     # Startup script
├── config.py                   # Configuration settings
├── analysis_templates.py       # Analysis templates and prompts
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── STARTUP_GUIDE.md           # Setup instructions
├── test_setup.py              # Setup testing script
├── routes/                     # Flask route modules
│   ├── __init__.py
│   ├── main_routes.py         # Core routes (upload, analysis)
│   ├── chat_routes.py         # Chat functionality
│   └── api_routes.py          # API endpoints
├── services/                   # Business logic services
│   ├── __init__.py
│   ├── session_service.py     # Redis session management
│   └── ai_service.py          # Gemini API integration
├── utils/                      # Utility modules
│   ├── __init__.py
│   ├── video_utils.py         # Video processing utilities
│   └── text_utils.py          # Text processing utilities
├── templates/                  # HTML templates
│   └── index.html
└── static/                     # Static files
    ├── css/
    ├── js/
    └── uploads/               # Video uploads and evidence
```

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd ai_video_detective
```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

   **Note**: The requirements.txt includes all necessary dependencies with specific versions that are tested and compatible with the application.

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   SECRET_KEY=your_secret_key_here
   ```

5. **Get Gemini API Key**
   - Visit [Google AI Studio](https://aistudio.google.com/)
   - Create a new API key
   - Add it to your `.env` file

## 🚀 Quick Start

### Option 1: Using main.py (Recommended)
```bash
python main.py
```

### Option 2: Using app.py directly
```bash
python app.py
```

### Option 3: Using Flask CLI
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

The application will be available at `http://localhost:5000`

## 🎬 Default Video Feature

The application includes a built-in default video for testing and demonstration purposes:

- **Default Video**: `BMW M4 - Ultimate Racetrack - BMW Canada (720p, h264).mp4`
- **Automatic Loading**: If no video is uploaded, the application automatically uses the default video
- **Seamless Experience**: Users can start analyzing immediately without needing to upload a file
- **Testing Ready**: Perfect for testing the application's capabilities and features

### How It Works
1. When a user submits the upload form without selecting a file
2. The application automatically copies the default video to the uploads folder
3. The video is processed normally with full analysis capabilities
4. Users receive a success message indicating the default video was loaded

This feature ensures the application is always ready for immediate use and demonstration.

## 📋 Analysis Types

The application supports multiple specialized analysis types:

### 1. Comprehensive Analysis
- Complete multi-dimensional analysis covering all aspects
- Visual, audio, temporal, and spatial understanding
- Behavioral and interaction analysis
- Technical and quality assessment

### 2. Safety Investigation
- Comprehensive safety analysis with risk assessment
- Safety violations and compliance evaluation
- Emergency preparedness assessment
- Corrective action planning

### 3. Performance Analysis
- Efficiency and quality evaluation
- Productivity metrics and benchmarking
- Competency and behavioral assessment
- Improvement opportunity identification

### 4. Pattern Detection
- Advanced pattern recognition and behavioral analysis
- Temporal and spatial pattern analysis
- Social and cognitive pattern detection
- Anomaly detection and prediction

### 5. Creative Review
- Comprehensive creative and aesthetic analysis
- Visual aesthetics and storytelling evaluation
- Brand alignment and messaging assessment
- Innovation and creativity analysis

## 🔧 Configuration

### Environment Variables
- `GOOGLE_API_KEY`: Your Gemini API key (required)
- `SECRET_KEY`: Flask secret key for sessions
- `REDIS_URL`: Redis connection URL (configured by default)

### Application Settings
All configuration is centralized in `config.py`:
- File upload settings (size limits, allowed extensions)
- Session management (expiry times, cleanup intervals)
- AI analysis parameters (temperature, token limits)
- Agent capabilities and tools

## 🏗️ Architecture

### Modular Design
The application follows a clean, modular architecture:

1. **Routes Layer**: Handles HTTP requests and responses
2. **Services Layer**: Contains business logic and external integrations
3. **Utils Layer**: Provides utility functions for common operations
4. **Config Layer**: Centralized configuration management

### Key Components

#### Routes
- `main_routes.py`: Core functionality (upload, analysis)
- `chat_routes.py`: AI conversation handling
- `api_routes.py`: REST API endpoints

#### Services
- `session_service.py`: Redis session management
- `ai_service.py`: Gemini API integration

#### Utils
- `video_utils.py`: Video processing and metadata extraction
- `text_utils.py`: Text processing and timestamp extraction

## 🔄 Session Management

The application uses Redis for session storage with automatic cleanup:

- **Session Expiry**: 1 hour by default
- **File Cleanup**: 2 hours for uploaded files
- **Background Cleanup**: Runs every 30 minutes
- **Evidence Generation**: Automatic screenshot and video clip creation

## 🤖 AI Agent Capabilities

The AI agent features advanced capabilities:

- **Autonomous Analysis**: Self-directed comprehensive analysis
- **Multi-Modal Understanding**: Visual, audio, temporal, and spatial comprehension
- **Context Awareness**: Memory-enabled conversations
- **Proactive Insights**: Beyond-request information and observations
- **Adaptive Focus**: Dynamic response depth based on content complexity
- **Comprehensive Reporting**: Professional-grade structured outputs

## 📊 API Endpoints

### Core Endpoints
- `GET /`: Main application interface
- `POST /upload`: Video file upload
- `POST /analyze`: Video analysis request
- `POST /chat`: AI conversation

### API Endpoints
- `GET /health`: Health check
- `GET /api/agent-info`: Agent capabilities information
- `GET /api/analysis-types`: Available analysis types
- `GET /session/status`: Current session status
- `POST /session/cleanup`: Clean up current session

### Utility Endpoints
- `POST /capture-screenshots`: Manual screenshot capture
- `POST /auto-capture-screenshots`: Automatic timestamp-based capture
- `GET /screenshot/<filename>`: Serve screenshot files

## 🧪 Testing

Run the setup test to verify your configuration:
```bash
python test_setup.py
```

## 🔍 Troubleshooting

### Common Issues

1. **Redis Connection Error**
   - Ensure Redis is running and accessible
   - Check the Redis URL in config.py

2. **Gemini API Errors**
   - Verify your API key is correct
   - Check API quota and limits
   - Ensure the API key has video analysis permissions

3. **File Upload Issues**
   - Check file size limits (100MB default)
   - Verify file format is supported
   - Ensure upload directory has write permissions

4. **Session Issues**
   - Clear browser cookies and cache
   - Restart the application
   - Check Redis connection

### Debug Mode
Enable debug mode for detailed error information:
```python
app.run(debug=True)
```

## 📈 Performance

### Optimization Features
- **Asynchronous Processing**: Non-blocking video analysis
- **Background Cleanup**: Automatic resource management
- **Efficient File Handling**: Stream-based uploads and processing
- **Redis Caching**: Fast session data access

### Resource Requirements
- **Memory**: 2GB+ recommended for video processing
- **Storage**: Adequate space for video uploads and evidence
- **Network**: Stable connection for API calls

## 🔒 Security

### Security Features
- **File Validation**: Extension and size checking
- **Session Security**: Secure session management
- **Input Sanitization**: Request validation and sanitization
- **Error Handling**: Secure error responses

### Best Practices
- Use HTTPS in production
- Regularly rotate API keys
- Monitor Redis access
- Implement rate limiting for production use

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Check the troubleshooting section
- Review the STARTUP_GUIDE.md
- Run the test_setup.py script
- Check application logs for detailed error information

---

**AI Video Detective** - Advanced video analysis powered by AI agents with comprehensive understanding capabilities. 