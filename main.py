import google.generativeai as genai
import pywhatkit
import datetime
import os
import time
from dotenv import load_dotenv
import logging

# Hide those annoying Google warning messages
os.environ['GRPC_VERBOSITY'] = 'ERROR'
os.environ['GLOG_minloglevel'] = '2'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)
logging.getLogger('google.auth.transport.grpc').setLevel(logging.ERROR)

# Load your API key from the .env file
load_dotenv()

# Get your Gemini API key
try:
    API_KEY = os.getenv("GEMINI_API_KEY")
    if not API_KEY:
        raise ValueError("API key is empty")
except Exception:
    print("❌ Oops! I can't find your API key in the .env file.")
    print("Make sure you have a .env file with your GEMINI_API_KEY in it.")
    exit()

# Set up the AI
genai.configure(api_key=API_KEY)

# Safety settings - keeps conversations appropriate
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Start up the AI brain
ai = genai.GenerativeModel('gemini-2.0-flash', safety_settings=safety_settings)
chat = ai.start_chat(history=[])

# Simple helper functions
def ask_user(question):
    """Ask the user a question and get their answer."""
    try:
        answer = input(question).strip()
        return answer if answer else None
    except (KeyboardInterrupt, EOFError):
        print("\n👋 See you later!")
        return None

def create_whatsapp_message(idea):
    """Ask the AI to write a WhatsApp message based on your idea."""
    print("\n🤖 Let me write that message for you...")
    try:
        prompt = f"Write a friendly WhatsApp message for this: '{idea}'. Keep it natural and casual."
        response = ai.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Sorry, I had trouble writing that message. Error: {e}"

def whatsapp_helper():
    """Help you send WhatsApp messages with AI assistance."""
    print("\n📱 WhatsApp Message Helper")
    print("I'll help you write and send messages!")
    print("Type 'back' anytime to return to chat.")

    # Step 1: Get phone number
    while True:
        phone = ask_user("📞 Who are you sending to? (phone with country code, like +919876543210): ")
        if phone is None or phone.lower() == 'back':
            print("👈 Going back to chat...")
            return
        if phone.startswith('+') and phone[1:].isdigit():
            break
        else:
            print("❌ Please use this format: +919876543210 (+ followed by numbers)")

    # Step 2: Get message idea
    while True:
        idea = ask_user("💭 What should the message be about? (e.g., 'wish happy birthday'): ")
        if idea is None or idea.lower() == 'back':
            print("👈 Going back to chat...")
            return
        if idea.strip():
            break
        else:
            print("❌ Please tell me what the message should be about.")

    # Step 3: Create and approve message
    while True:
        # Let AI write the message
        message = create_whatsapp_message(idea)
        print(f"\n📝 Here's your message:")
        print(f"┌─────────────────────────────────")
        print(f"│ {message}")
        print(f"└─────────────────────────────────")

        # Ask if they like it
        approval = ask_user("\n👍 Like this message? (y)es / (n)ew one / (e)dit it myself: ").lower()
        if approval is None or approval == 'back':
            print("👈 Going back to chat...")
            return
        elif approval in ['y', 'yes']:
            break  # They like it!
        elif approval in ['e', 'edit']:
            # Let them write their own
            custom = ask_user("✏️  Write your message: ")
            if custom is None or custom.lower() == 'back':
                print("👈 Going back to chat...")
                return
            if custom.strip():
                message = custom
                break
            else:
                print("❌ Message can't be empty.")
        elif approval in ['n', 'new']:
            print("🔄 Creating a new message...")
            continue  # Try again
        else:
            print("❌ Please type 'y', 'n', or 'e'")

    # Step 4: When to send?
    while True:
        when = ask_user("⏰ Send (n)ow or (s)chedule for later? [n/s]: ").lower()
        if when is None or when == 'back':
            print("👈 Going back to chat...")
            return

        if when == 's':
            # Schedule it
            while True:
                time_input = ask_user("🕐 What time? (24-hour format like 14:30): ")
                if time_input is None or time_input.lower() == 'back':
                    print("👈 Going back to chat...")
                    return
                try:
                    hour, minute = map(int, time_input.split(':'))
                    if 0 <= hour <= 23 and 0 <= minute <= 59:
                        pywhatkit.sendwhatmsg(phone, message, hour, minute)
                        print(f"\n✅ Message scheduled for {hour:02d}:{minute:02d}!")
                        print("🌐 Your browser will open when it's time to send.")
                        print("📱 Make sure you're logged into WhatsApp Web.")
                        print("👈 Going back to chat...")
                        return
                    else:
                        print("❌ Hour: 0-23, Minutes: 0-59. Try again!")
                except ValueError:
                    print("❌ Use format like 14:30. Try again!")
                except Exception as e:
                    print(f"❌ Something went wrong: {e}")
                    print("Let's try again...")

        elif when == 'n':
            # Send now
            try:
                pywhatkit.sendwhatmsg_instantly(phone, message)
                print("\n✅ Opening WhatsApp Web to send your message!")
                print("📱 Make sure you're logged into WhatsApp Web.")
                print("👈 Going back to chat...")
                return
            except Exception as e:
                print(f"❌ Oops! Something went wrong: {e}")
                retry = ask_user("🔄 Try again? (y/n): ").lower()
                if retry in ['y', 'yes']:
                    continue
                else:
                    print("👈 Going back to chat...")
                    return
        else:
            print("❌ Please type 'n' for now or 's' for schedule")


def main():
    """Start the chatbot - your friendly AI assistant!"""
    print("🤖 Hi! I'm your AI Assistant")
    print("💬 Chat with me about anything!")
    print("📱 Type 'whatsapp' to send WhatsApp messages")
    print("👋 Type 'quit' or 'exit' when you're done")

    while True:
        message = ask_user("\n😊 You: ")

        if message is None or message.lower() in ["quit", "exit", "bye"]:
            print("👋 Thanks for chatting! See you soon!")
            break

        if message.lower() == 'whatsapp':
            whatsapp_helper()
            continue

        try:
            # Talk to the AI
            response = chat.send_message(message)
            print(f"\n🤖 AI: {response.text}")

        except Exception as e:
            print(f"😅 Oops! Something went wrong: {e}")
            print("🔄 Let's try again in a moment...")
            time.sleep(2)

if __name__ == "__main__":
    main()
