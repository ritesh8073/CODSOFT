def simple_chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return  "I'm doing well. How about you?"

    elif "your name" in user_input:
        return "I'm a chatbot. You can call me Sara."

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day."
    
    elif "fine" in user_input or "good" in user_input :
        return "well how can i help you !"
    
    elif "whats the weather" in user_input or "whats the weather today" in user_input :
        return "you have a fine day for walk"    

    else :
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"

while True:
    user_input = input("ASK ME :")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)   