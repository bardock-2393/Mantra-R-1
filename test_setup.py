#!/usr/bin/env python3
"""
AI Video Detective - Setup Test Script
Tests the configuration and dependencies for the AI Video Detective application.
"""

import os
import sys
import importlib
from pathlib import Path

def test_python_version():
    """Test Python version compatibility"""
    print("🐍 Testing Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Requires Python 3.8+")
        return False

def test_imports():
    """Test required package imports"""
    print("\n📦 Testing package imports...")
    
    required_packages = [
        ('flask', 'Flask'),
        ('redis', 'Redis'),
        ('google.genai', 'Google Gemini'),
        ('dotenv', 'python-dotenv'),
        ('werkzeug', 'Werkzeug'),
        ('cv2', 'OpenCV'),
        ('numpy', 'NumPy'),
        ('asyncio', 'asyncio')
    ]
    
    all_imports_ok = True
    
    for package, name in required_packages:
        try:
            importlib.import_module(package)
            print(f"✅ {name} - Imported successfully")
        except ImportError as e:
            print(f"❌ {name} - Import failed: {e}")
            all_imports_ok = False
    
    return all_imports_ok

def test_environment():
    """Test environment configuration"""
    print("\n🔧 Testing environment configuration...")
    
    # Load .env file if it exists
    env_file = Path('.env')
    if env_file.exists():
        print("✅ .env file found")
        try:
            from dotenv import load_dotenv
            load_dotenv()
            print("✅ .env file loaded successfully")
        except Exception as e:
            print(f"❌ Failed to load .env file: {e}")
            return False
    else:
        print("⚠️  .env file not found - create one with your API keys")
    
    # Check API key
    api_key = os.getenv('GOOGLE_API_KEY')
    if api_key:
        print("✅ Google Gemini API key found")
    else:
        print("❌ Google Gemini API key not found - add GOOGLE_API_KEY to .env")
        return False
    
    # Check secret key
    secret_key = os.getenv('SECRET_KEY')
    if secret_key:
        print("✅ Flask secret key found")
    else:
        print("⚠️  Flask secret key not found - using default")
    
    return True

def test_directories():
    """Test directory structure"""
    print("\n📁 Testing directory structure...")
    
    required_dirs = [
        'static',
        'static/css',
        'static/js',
        'static/uploads',
        'templates'
    ]
    
    all_dirs_ok = True
    
    for dir_path in required_dirs:
        if Path(dir_path).exists():
            print(f"✅ {dir_path}/ - Directory exists")
        else:
            print(f"❌ {dir_path}/ - Directory missing")
            all_dirs_ok = False
    
    return all_dirs_ok

def test_files():
    """Test required files"""
    print("\n📄 Testing required files...")
    
    required_files = [
        'app.py',
        'requirements.txt',
        'README.md',
        'static/css/style.css',
        'static/js/app.js',
        'templates/index.html'
    ]
    
    all_files_ok = True
    
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✅ {file_path} - File exists")
        else:
            print(f"❌ {file_path} - File missing")
            all_files_ok = False
    
    return all_files_ok

def test_redis_connection():
    """Test Redis connection"""
    print("\n🔴 Testing Redis connection...")
    
    try:
        import redis
        # Using the configured Redis URL from app.py
        redis_url = "redis://default:nswO0Z95wT9aeXIIOZMMphnDhsPY3slG@redis-10404.c232.us-east-1-2.ec2.redns.redis-cloud.com:10404"
        redis_client = redis.from_url(redis_url)
        redis_client.ping()
        print("✅ Redis connection successful")
        return True
    except Exception as e:
        print(f"❌ Redis connection failed: {e}")
        print("⚠️  The app will work without Redis, but session persistence will be limited")
        return False

def test_gemini_api():
    """Test Gemini API connection"""
    print("\n🤖 Testing Gemini API connection...")
    
    try:
        from google import genai
        from google.genai import types
        
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            print("❌ No API key found")
            return False
        
        client = genai.Client(api_key=api_key)
        
        # Test with a simple text generation
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=["Hello, this is a test message."],
            config=types.GenerateContentConfig(
                temperature=0.1,
                max_output_tokens=50,
            )
        )
        
        if response.text:
            print("✅ Gemini API connection successful")
            return True
        else:
            print("❌ Gemini API returned empty response")
            return False
            
    except Exception as e:
        print(f"❌ Gemini API connection failed: {e}")
        return False

def test_flask_app():
    """Test Flask application"""
    print("\n🌐 Testing Flask application...")
    
    try:
        # Import the Flask app
        from app import app
        
        # Test basic app configuration
        if app.config.get('UPLOAD_FOLDER'):
            print("✅ Flask app configured with upload folder")
        else:
            print("❌ Flask app missing upload folder configuration")
            return False
        
        if app.secret_key:
            print("✅ Flask app has secret key")
        else:
            print("⚠️  Flask app missing secret key")
        
        print("✅ Flask application ready")
        return True
        
    except Exception as e:
        print(f"❌ Flask application test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 AI Video Detective - Setup Test")
    print("=" * 50)
    
    tests = [
        ("Python Version", test_python_version),
        ("Package Imports", test_imports),
        ("Environment", test_environment),
        ("Directories", test_directories),
        ("Files", test_files),
        ("Redis Connection", test_redis_connection),
        ("Gemini API", test_gemini_api),
        ("Flask App", test_flask_app)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test failed with exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Summary")
    print("=" * 50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Your AI Video Detective is ready to run.")
        print("\nTo start the application:")
        print("  python app.py")
        print("\nThen open: http://localhost:5000")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please fix the issues above.")
        
        if not any(name == "Environment" and result for name, result in results):
            print("\n💡 Quick fix for environment issues:")
            print("1. Create a .env file with your API keys:")
            print("   GOOGLE_API_KEY=your_api_key_here")
            print("   SECRET_KEY=your_secret_key_here")
            print("2. Get your API key from: https://aistudio.google.com/")
        
        if not any(name == "Package Imports" and result for name, result in results):
            print("\n💡 Quick fix for import issues:")
            print("1. Install dependencies: pip install -r requirements.txt")
            print("2. Activate virtual environment if using one")

if __name__ == "__main__":
    main() 