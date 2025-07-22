import tkinter as tk
from tkinter import scrolledtext
import random
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there! How can I help you?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I didn't understand that."
def generate_friendly_response(user_input):
    user_input = user_input.lower()

    greetings = ["hello", "hi", "hey", "good morning", "good evening"]
    how_are_you = ["how are you", "how's it going", "how do you do"]
    feelings = ["sad", "tired", "happy", "angry", "depressed", "excited", "upset", "bored"]
    thanks = ["thank you", "thanks", "thx", "appreciate"]
    help_keywords = ["help", "assist", "support", "need help", "what can you do"]

    if any(word in user_input for word in greetings):
        return random.choice([
            "Hi there! 👋",
            "Hey! How can I help you today?",
            "Hello! I'm here for you 😊"
        ])
    elif any(phrase in user_input for phrase in how_are_you):
        return random.choice([
            "I'm just a bunch of Python code, but I'm feeling great!",
            "Doing awesome, thanks for asking! How about you?",
            "I'm functioning perfectly 😄"
        ])
    elif any(word in user_input for word in feelings):
        return random.choice([
            "It's totally okay to feel that way. I'm here for you 💛",
            "That sounds tough. Want to talk more about it?",
            "Emotions make us human. You’re not alone!"
        ])
    elif any(word in user_input for word in thanks):
        return random.choice([
            "You're very welcome! 😊",
            "Glad I could help!",
            "Anytime! Let me know if you need anything else."
        ])
    elif any(word in user_input for word in help_keywords):
        return random.choice([
            "I can chat with you, tell the time, give info, or just keep you company!",
            "Need support with something specific?",
            "Sure! What do you need help with today?"
        ])
    elif "who are you" in user_input or "what are you" in user_input:
        return "I'm your friendly chatbot buddy 🤖 built in Python! How can I assist you?"

    return random.choice([
        "Hmm... I didn't get that. Could you rephrase it?",
        "Interesting! Tell me more 😊",
        "Let's keep chatting — I'm all ears!"
    ])
        
class ChatBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 Simple ChatBot")
        self.root.geometry("500x500")
        self.root.config(bg="#2c3e50")

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
        self.chat_area.config(state='disabled')
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.input_frame = tk.Frame(root, bg="#2c3e50")
        self.input_frame.pack(pady=10, padx=10, fill=tk.X)

        self.user_input = tk.Entry(self.input_frame, font=("Arial", 14))
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.input_frame, text="Send", font=("Arial", 12, "bold"), bg="#27ae60", fg="white", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

    def send_message(self, event=None):
        message = self.user_input.get().strip()
        if message:
            self.insert_message("You", message)
            bot_reply = generate_friendly_response(message)
            self.insert_message("Bot", bot_reply)
            self.user_input.delete(0, tk.END)

    def insert_message(self, sender, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{sender}: {message}\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotGUI(root)

    
    root.mainloop()
