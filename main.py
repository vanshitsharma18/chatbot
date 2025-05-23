# main.py
from config import load_api_key
import google.generativeai as genai
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def chat_with_gemini():
    load_api_key()
    model = genai.GenerativeModel('gemini-1.5-flash')  # Faster, limited capabilities
  # Use valid model for free tier
    chat = model.start_chat()

    print("🤖 Gemini Chatbot (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        try:
            response = chat.send_message(user_input)
            reply = response.text
            print("Gemini:", reply)
            speak(reply)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat_with_gemini()
