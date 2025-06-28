#!/usr/bin/env python3
"""
Test script for chat functionality
"""

import os
from dotenv import load_dotenv
from utils import get_gemini_response

def test_chat():
    """Test the chat functionality"""
    
    load_dotenv()
    
    print("🧪 Testing Chat Functionality...")
    print("=" * 50)
    
    # Test 1: Check API key configuration
    api_key = os.getenv('GOOGLE_API_KEY')
    print(f"API Key configured: {'Yes' if api_key and api_key != 'your_google_gemini_api_key_here' else 'No'}")
    
    # Test 2: Test a simple query
    test_prompt = "What is health insurance?"
    print(f"\nTesting query: '{test_prompt}'")
    
    try:
        response, plan_names = get_gemini_response(test_prompt)
        print(f"✅ Response received: {len(response)} characters")
        print(f"📋 Plan names extracted: {plan_names}")
        
        # Show first 200 characters of response
        print(f"\n📝 Response preview:")
        print(response[:200] + "..." if len(response) > 200 else response)
        
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print("🎯 Test completed!")

if __name__ == "__main__":
    test_chat() 