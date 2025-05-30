# Gemini AI Chatbot with Voice Output and System Controls

A Python-based chatbot that uses Google's Gemini AI model for conversation, includes text-to-speech capabilities, and can open applications and websites.

## Features

- Interactive chat interface with Gemini AI
- Text-to-speech output for AI responses
- Asynchronous speech processing for uninterrupted interaction
- System controls to open applications and websites
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

### Chat Commands

- Type your messages and press Enter to chat
- Type 'exit' or 'quit' to end the conversation
- AI responses will be displayed and spoken automatically

### System Commands

Open applications:
```
open app notepad
open app calculator
open app paint
open app word
open app excel
open app cmd
open app explorer
```

Open websites:
```
open website google.com
open website github.com
open google.com   (direct format also works)
```

## Project Structure

- `main.py` - Main application logic, chat interface, and system controls
- `config.py` - API key configuration and setup
- `requirements.txt` - Project dependencies
- `.env` - Environment variables (not tracked in git)

## Dependencies

- google-generativeai - Google's Generative AI library
- python-dotenv - Environment variable management
- pyttsx3 - Text-to-speech engine
- webbrowser - For opening websites
- subprocess - For launching applications

## Customization

You can add more applications to the `app_paths` dictionary in the `open_app` function to expand the list of supported applications.

## License

MIT

## Contributing

Contributions, issues, and feature requests are welcome!