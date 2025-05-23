from config import load_api_key
import google.generativeai as genai
import pyttsx3
import threading  #  Needed for async speech

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speak_async(text):
    # Runs the speak function in a separate thread
    threading.Thread(target=speak, args=(text,)).start()

def chat_with_gemini():
    load_api_key()
    model = genai.GenerativeModel('gemini-1.5-flash')   # Use free-tier compatible model
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
            speak_async(reply)  # 🔊 Speak without blocking
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat_with_gemini()
