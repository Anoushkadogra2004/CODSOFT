import re   # Import regex module

def chatbot_response(user_input):
    # Convert input to lowercase for easy matching
    user_input = user_input.lower()

    # Rule 1: Greetings (matches "hi", "hello", "hey" in any form)
    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return "Hello! How can I help you today?"

    # Rule 2: Asking about well-being
    elif re.search(r"how (are|r) (you|u)", user_input):
        return "I'm just a bot, but I'm doing great! How about you?"

    # Rule 3: Asking chatbot's name (matches "what is your name", "tell me your name")
    elif re.search(r"(your name|who are you)", user_input):
        return "I am ChatBot, your AI assistant!"

    # Rule 4: Exit (matches "bye", "goodbye", "exit", "quit")
    elif re.search(r"\b(bye|goodbye|exit|quit)\b", user_input):
        return "Goodbye! Have a nice day!"

    # Default response (when no rules match)
    else:
        return "Sorry, I didn't understand that."

# Main program loop
print("ChatBot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("ChatBot:", response)

    # Exit condition
    if re.search(r"\b(bye|goodbye|exit|quit)\b", user_input.lower()):
        break