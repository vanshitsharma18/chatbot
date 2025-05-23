# Gemini AI Chatbot with Voice Output

A Python-based chatbot that uses Google's Gemini AI model for conversation and includes text-to-speech capabilities.

## Features

- Interactive chat interface with Gemini AI
- Text-to-speech output for AI responses
- Asynchronous speech processing
- Simple command-line interface

## Prerequisites

- Python 3.x
- Google Cloud API key for Gemini AI

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd chatbot
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Configure your environment:
   - Create a `.env` file in the project root
   - Add your Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## Usage

Run the chatbot:
```bash
python main.py
```

- Type your messages and press Enter to chat
- Type 'exit' or 'quit' to end the conversation
- AI responses will be displayed and spoken automatically

## Project Structure

- `main.py` - Main application logic and chat interface
- `config.py` - API key configuration and setup
- `requirements.txt` - Project dependencies
- `.env` - Environment variables (not tracked in git)

## Dependencies

- google-generativeai - Google's Generative AI library
- python-dotenv - Environment variable management
- pyttsx3 - Text-to-speech engine

## License

MIT

## Contributing

Contributions, issues, and feature requests are welcome!