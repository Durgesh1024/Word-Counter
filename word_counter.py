def count_words(text):
    """
    Count the number of words in the given text.

    Args:
    text (str): The input text.

    Returns:
    int: The number of words in the text.
    """
    if not text.strip():
        return 0  # Return 0 if the input is empty or contains only whitespace

    words = text.split()
    return len(words)

def get_user_input():
    """
    Prompt the user to enter a sentence or paragraph.

    Returns:
    str: The user-inputted text.
    """
    print("Please enter a sentence or paragraph:")
    return input()

def display_word_count(word_count):
    """
    Display the word count to the console.

    Args:
    word_count (int): The number of words to display.
    """
    print(f"\nWord Count: {word_count}")

def word_counter():
    """
    Main function to run the Word Counter program.
    """
    print("Welcome to the Word Counter Program!")
    
    # Get user input
    user_input = get_user_input()
    
    # Count words and handle errors
    word_count = count_words(user_input)
    
    # Display the result
    display_word_count(word_count)

if __name__ == "__main__":
    word_counter()
