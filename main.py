# main.py
from config import load_api_key
import google.generativeai as genai

def chat_with_gemini():
    load_api_key()
    model = genai.GenerativeModel('gemini-1.5-flash')  # Faster, limited capabilities
    chat = model.start_chat()

    print("🤖 Gemini Chatbot (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        try:
            response = chat.send_message(user_input)
            print("Gemini:", response.text)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat_with_gemini()
