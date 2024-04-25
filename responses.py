from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered =='':
        return "I'm sorry, I didn't understand that. Please say something."
    elif 'hello' in lowered:
        return "Hello! How can I help you today?"
    elif 'goodbye' in lowered:
        return "Goodbye! Have a great day!"
    elif 'how are you' in lowered:
        return "I'm doing well, thank you for asking!"
    elif 'your name' in lowered:
        return "I'm a bot, so I don't have a name."
    else:
        return choice(['I do not understand that.', 'Could you please rephrase that?', 'I am not sure what you mean.'])
    
