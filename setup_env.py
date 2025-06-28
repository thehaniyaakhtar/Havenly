#!/usr/bin/env python3
"""
Setup script for Google Gemini API configuration
"""

import os

def create_env_file():
    """Create .env file with Google Gemini API key configuration"""
    
    env_content = """# Google Gemini API Configuration
# Get your API key from: https://makersuite.google.com/app/apikey
GOOGLE_API_KEY=your_google_gemini_api_key_here

# Instructions:
# 1. Replace 'your_google_gemini_api_key_here' with your actual API key
# 2. Save the file
# 3. Restart your Streamlit application
"""
    
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ Created .env file successfully!")
        print("\n📝 Next steps:")
        print("1. Open the .env file")
        print("2. Replace 'your_google_gemini_api_key_here' with your actual Google Gemini API key")
        print("3. Save the file")
        print("4. Restart your Streamlit application")
        print("\n🔗 Get your API key from: https://makersuite.google.com/app/apikey")
        
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")

if __name__ == "__main__":
    print("🔧 Setting up Google Gemini API configuration...")
    create_env_file() 