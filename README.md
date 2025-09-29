# Whatsapp-AI-Chatbot

A Python-based AI-powered chatbot for WhatsApp that enables automated and intelligent interactions with users. This project demonstrates how to integrate AI Natural Language Processing (NLP) models with WhatsApp messaging, delivering an interactive and customizable chatbot experience.

## Features

- **Seamless WhatsApp Integration**: Connects directly to WhatsApp for real-time messaging.
- **AI-powered Conversations**: Utilizes NLP to understand and respond to user inputs intelligently.
- **Customizable Responses**: Easily modify intents, actions, and chatbot behavior.
- **Extensible Architecture**: Add new features, commands, or AI models as desired.
- **Full Python Stack**: Written entirely in Python for easy setup and modification.

## Demo

![Whatsapp AI Chatbot GIF](demo/demo.gif) <!-- Add your demo GIF or screenshot here if available -->

## Getting Started

### Prerequisites

- Python 3.7+
- [pip](https://pip.pypa.io/en/stable/)
- WhatsApp account
- (Optional) [ngrok](https://ngrok.com/) for exposing local servers

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/sakshamm0507/Whatsapp-AI-Chatbot.git
    cd Whatsapp-AI-Chatbot
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Environment Variables:**
    - Create a `.env` file and add necessary credentials/tokens (see project code or documentation for specific variables).

4. **Run the bot:**
    ```bash
    python main.py
    ```

5. **Connect to WhatsApp:**
    - Follow the on-screen instructions to scan the QR code using WhatsApp Web.

---

## Usage

- Start a chat with the linked WhatsApp account.
- Send messages; the bot will respond intelligently using AI/NLP.
- Customize commands, intents, or plug in additional AI models as needed.

## Folder Structure

```
Whatsapp-AI-Chatbot/
│
├── main.py              # Entry point
├── requirements.txt     # Python dependencies
├── bot/                 # Core bot logic and modules
├── ai/                  # AI/NLP integration (models, utilities)
├── utils/               # Helper functions
└── README.md
```

## Customization

- **Intents/Responses:** Modify files in the `bot/` or `ai/` directories to change how the bot understands and responds.
- **Extend Features:** Add new Python modules for extra capabilities (e.g., weather, jokes, reminders).
- **Integrate with APIs:** Enhance functionality by connecting to third-party APIs as needed.

## Contributing

Contributions are welcome! Please open issues and submit pull requests to help improve this project.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [OpenAI](https://openai.com/) (for AI/NLP inspiration)
- [yowsup](https://github.com/tgalal/yowsup) / [Baileys](https://github.com/adiwajshing/Baileys) / [Twilio API](https://www.twilio.com/whatsapp) (for WhatsApp integration, depending on implementation)
- Python community

---

> Made with ❤️ by [sakshamm0507](https://github.com/sakshamm0507)
