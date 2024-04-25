from random import choice, randint


# This dictionary will hold the progress
progress_tracker = {}  # Key: (user_id, book_id), Value: (current_page, total_pages)



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
    
def start_book(user_id, book_id, total_pages):
    key = (user_id, book_id)
    if key in progress_tracker:
        return "You are already tracking this book."
    progress_tracker[key] = (0, total_pages)
    return f"Tracking started for book {book_id} with {total_pages} total pages."


def update_progress(user_id, book_id, current_page):
    key = (user_id, book_id)
    if key not in progress_tracker:
        return "You haven't started tracking this book yet."
    total_pages = progress_tracker[key][1]
    progress_tracker[key] = (current_page, total_pages)
    return f"Progress updated: you are on page {current_page} of {total_pages}."

def get_progress(user_id, book_id):
    key = (user_id, book_id)
    if key not in progress_tracker:
        return "No progress found for this book."
    current_page, total_pages = progress_tracker[key]
    return f"You are currently on page {current_page} of {total_pages}."
