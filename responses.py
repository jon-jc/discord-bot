from random import choice, randint


# This dictionary will hold the progress
progress_tracker = {}  # Key: (user_id, book_id), Value: (current_page, total_pages)


# This dictionary will hold the state of each user's book club setup process
user_state = {}

def get_response(user_id: int, user_input: str) -> str:
    lowered = user_input.strip().lower()

    # Managing user state
    current_state = user_state.get(user_id, 'START')

    # Start or reset book club setup
    if lowered == '!start':
        user_state[user_id] = 'ASK_BOOK_ID'
        return "📘 Let's start a new book club! First, what's the ID of the book you want to discuss? Please enter it like '!bookid 123'."

    # Asking for book ID
    if current_state == 'ASK_BOOK_ID' and lowered.startswith('!bookid'):
        book_id = lowered.split()[1] if len(lowered.split()) > 1 else None
        if book_id:
            user_state[user_id] = 'ASK_MEMBERS'
            return f"📚 Book ID {book_id} noted! Now, who would you like to invite? Enter usernames separated by commas like '!invite user1, user2'."
        else:
            return "🔍 Please specify a valid book ID. For example, '!bookid 123'."

    # Asking for members to invite
    if current_state == 'ASK_MEMBERS' and lowered.startswith('!invite'):
        members = lowered[7:].replace(' ', '').split(',') if len(lowered.split()) > 1 else []
        if members:
            user_state[user_id] = 'CONFIRM_SETUP'
            return f"👥 You've added {', '.join(members)} to your book club. Ready to finalize? Type '!confirm' to complete setup or '!cancel' to start over."
        else:
            return "Please specify at least one user to invite. For example, '!invite user1, user2'."

    # Confirm setup
    if current_state == 'CONFIRM_SETUP':
        if lowered == '!confirm':
            user_state[user_id] = 'START'
            return "🎉 All set! Your book club is ready to go. Use '!schedule' to plan your first meeting."
        elif lowered == '!cancel':
            user_state[user_id] = 'START'
            return "Setup canceled. You can start over by typing '!start'."

    # Help command
    if lowered == '!help':
        return "📚 Help Guide:\n!start - Begin setting up a new book club.\n!bookid [id] - Specify the book ID.\n!invite [usernames] - Invite members to the club.\n!confirm - Finish setup.\n!cancel - Cancel setup."

    # Default response if command is not recognized
    return "❓ I didn't recognize that command. Try !help for a list of valid commands."
