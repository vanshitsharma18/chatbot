from config import load_api_key
import google.generativeai as genai
import pyttsx3
import threading  # Needed for async speech
import subprocess
import webbrowser
import re
import os

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speak_async(text):
    # Runs the speak function in a separate thread
    threading.Thread(target=speak, args=(text,)).start()

def open_app(app_name):
    try:
        # Dictionary of common Windows apps and their paths
        app_paths = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "paint": "mspaint.exe",
            "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
            "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
            "cmd": "cmd.exe",
            "explorer": "explorer.exe",
            # Add more apps as needed
        }
        
        app_name = app_name.lower()
        if app_name in app_paths:
            subprocess.Popen(app_paths[app_name])
            return f"Opening {app_name}..."
        else:
            return f"Sorry, I don't know how to open {app_name}."
    except Exception as e:
        return f"Error opening {app_name}: {str(e)}"

def open_website(url):
    try:
        # Add https:// if not present
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        webbrowser.open(url)
        return f"Opening {url}..."
    except Exception as e:
        return f"Error opening {url}: {str(e)}"

def process_command(user_input):
    # Check if it's a command to open an app
    app_match = re.search(r'open\s+app\s+([\w\s]+)', user_input, re.IGNORECASE)
    if app_match:
        app_name = app_match.group(1).strip()
        response = open_app(app_name)
        return response, True
        
    # Check if it's a command to open a website
    web_match = re.search(r'open\s+(?:website|site|url|web)\s+([\w\.]+)', user_input, re.IGNORECASE)
    if web_match:
        website = web_match.group(1).strip()
        response = open_website(website)
        return response, True
        
    # Check for direct website opening (example: "open google.com")
    direct_web_match = re.search(r'open\s+((?:www\.)?[\w\.]+\.\w+)', user_input, re.IGNORECASE)
    if direct_web_match and not app_match:
        website = direct_web_match.group(1).strip()
        response = open_website(website)
        return response, True
    
    return None, False

def chat_with_gemini():
    load_api_key()
    model = genai.GenerativeModel('gemini-1.5-flash')   # Use free-tier compatible model
    chat = model.start_chat()

    print("🤖 Gemini Chatbot (type 'exit' to quit)\n")
    print("You can ask me to open apps: 'open app notepad'")
    print("Or websites: 'open website google.com'\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
            
        # First check if it's a command to open an app or website
        response, is_command = process_command(user_input)
        if is_command:
            print("Gemini:", response)
            speak_async(response)
            continue
            
        # If not a command, process as a normal chat message
        try:
            response = chat.send_message(user_input)
            reply = response.text
            print("Gemini:", reply)
            speak_async(reply)  # 🔊 Speak without blocking
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat_with_gemini()
