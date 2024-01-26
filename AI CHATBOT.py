def simple_chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm doing well. How about you?"

    elif "your name" in user_input:
        return "I'm a chatbot. You can call me Sara."

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day."

    elif "fine" in user_input or "good" in user_input :
        return "Well, how can I help you?"

    elif "what's the weather" in user_input or "what's the weather today" in user_input :
        return "You have a fine day for a walk."

    elif "how old are you" in user_input:
        return "I don't have an age. I'm just a computer program!"

    elif "tell me a joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"

    elif "what can you do" in user_input or "help" in user_input:
        return "I can answer questions, tell jokes, and chat with you!"

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"

while True:
    user_input = input("ASK ME I AM SARA  ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
