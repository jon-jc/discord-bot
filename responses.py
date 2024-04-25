from random import choice, randint


# This dictionary will hold the progress
progress_tracker = {}  # Key: (user_id, book_id), Value: (current_page, total_pages)



def get_response(user_input: str) -> str:
    lowered = user_input.strip().lower()

    # Help command to guide users
    if lowered == '!help':
        return "📚 Commands available:\n!start [book_id] - Start a new book club.\n!join [club_id] - Join an existing book club.\n!progress - Check your reading progress."

    # Starting a new book club
    elif lowered.startswith('!start'):
        book_id = lowered.split()[1] if len(lowered.split()) > 1 else None
        if book_id:
            return f"🚀 Great! You've started a book club for book {book_id}. Invite friends with !invite [user_id] or check progress with !progress."
        else:
            return "🔍 Please specify a book ID to start a club. For example, '!start 123'."

    # Joining an existing book club
    elif lowered.startswith('!join'):
        club_id = lowered.split()[1] if len(lowered.split()) > 1 else None
        if club_id:
            return f"📖 Awesome! You've joined the book club {club_id}. Use !meetings to see upcoming discussions."
        else:
            return "🔍 Please specify a club ID to join. For example, '!join 456'."

    # Checking progress
    elif lowered.startswith('!progress'):
        return "📈 Checking your progress... Use !update [page_number] to update your reading status."

    # Default response if command is not recognized
    return "❓ I didn't recognize that command. Try !help for a list of valid commands."
