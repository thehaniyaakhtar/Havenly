#!/usr/bin/env python3
"""
Havenly Insurance Advisor - Startup Script
This script helps you start both the React frontend and Streamlit backend.
"""

import subprocess
import sys
import os
import time
import webbrowser
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed."""
    print("🔍 Checking dependencies...")
    
    # Check Python
    try:
        import streamlit
        print("✅ Streamlit is installed")
    except ImportError:
        print("❌ Streamlit not found. Please run: pip install -r requirements.txt")
        return False
    
    # Check Node.js
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Node.js is installed")
        else:
            print("❌ Node.js not found. Please install Node.js from https://nodejs.org/")
            return False
    except FileNotFoundError:
        print("❌ Node.js not found. Please install Node.js from https://nodejs.org/")
        return False
    
    # Check npm
    try:
        result = subprocess.run(['npm', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ npm is installed")
        else:
            print("❌ npm not found")
            return False
    except FileNotFoundError:
        print("❌ npm not found")
        return False
    
    return True

def install_react_dependencies():
    """Install React dependencies if needed."""
    if not os.path.exists('node_modules'):
        print("📦 Installing React dependencies...")
        try:
            subprocess.run(['npm', 'install'], check=True)
            print("✅ React dependencies installed")
        except subprocess.CalledProcessError:
            print("❌ Failed to install React dependencies")
            return False
    else:
        print("✅ React dependencies already installed")
    return True

def start_react_app():
    """Start the React development server."""
    print("🚀 Starting React app...")
    try:
        # Start React in background
        react_process = subprocess.Popen(
            ['npm', 'start'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("✅ React app started (http://localhost:3000)")
        return react_process
    except Exception as e:
        print(f"❌ Failed to start React app: {e}")
        return None

def start_streamlit_app():
    """Start the Streamlit app."""
    print("🚀 Starting Streamlit app...")
    try:
        # Start Streamlit in background
        streamlit_process = subprocess.Popen(
            [sys.executable, '-m', 'streamlit', 'run', 'Home.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("✅ Streamlit app started (http://localhost:8501)")
        return streamlit_process
    except Exception as e:
        print(f"❌ Failed to start Streamlit app: {e}")
        return None

def main():
    """Main function to start both applications."""
    print("🛡️ Havenly Insurance Advisor - Startup Script")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        print("\n❌ Please install missing dependencies and try again.")
        return
    
    # Install React dependencies
    if not install_react_dependencies():
        print("\n❌ Failed to install React dependencies.")
        return
    
    print("\n🚀 Starting applications...")
    
    # Start React app
    react_process = start_react_app()
    if not react_process:
        return
    
    # Wait a bit for React to start
    time.sleep(3)
    
    # Start Streamlit app
    streamlit_process = start_streamlit_app()
    if not streamlit_process:
        react_process.terminate()
        return
    
    # Wait for Streamlit to start
    time.sleep(5)
    
    print("\n🎉 Both applications are starting!")
    print("\n📱 React Frontend: http://localhost:3000")
    print("🔧 Streamlit Backend: http://localhost:8501")
    print("\n💡 Tips:")
    print("   - React handles the UI/UX and user interactions")
    print("   - Streamlit provides the AI backend and data processing")
    print("   - Both apps work together seamlessly")
    print("\n⏹️  Press Ctrl+C to stop both applications")
    
    # Open browsers
    try:
        webbrowser.open('http://localhost:3000')
        time.sleep(2)
        webbrowser.open('http://localhost:8501')
    except:
        pass
    
    try:
        # Keep the script running
        while True:
            time.sleep(1)
            # Check if processes are still running
            if react_process.poll() is not None:
                print("❌ React app stopped unexpectedly")
                break
            if streamlit_process.poll() is not None:
                print("❌ Streamlit app stopped unexpectedly")
                break
    except KeyboardInterrupt:
        print("\n🛑 Stopping applications...")
    
    # Cleanup
    if react_process:
        react_process.terminate()
        print("✅ React app stopped")
    
    if streamlit_process:
        streamlit_process.terminate()
        print("✅ Streamlit app stopped")
    
    print("👋 Goodbye!")

if __name__ == "__main__":
    main() 