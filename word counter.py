# Word Counter Program

def count_words(text):
    """
    This function counts the number of words in the given text.
    
    Parameters:
    text (str): The input string (sentence or paragraph) provided by the user.
    
    Returns:
    int: The number of words in the input text.
    """
    words = text.split()  # Splits the text into a list of words
    return len(words)  # Returns the length of the list, which is the word count

def main():
    print("Welcome to the Word Counter Program!")
    # Prompt the user to enter a sentence or paragraph
    text = input("Please enter a sentence or paragraph: ").strip()
    
    # Error handling for empty input
    if not text:
        print("Error: No input provided. Please enter a valid text.")
        return
    
    # Counting words using the count_words function
    word_count = count_words(text)
    
    # Displaying the word count to the user
    print(f"The total word count is: {word_count}")

# Run the program
while True:
    main()
    # Ask the user if they want to run the program again
    run_again = input("Do you want to run the program again? (yes/no): ").strip().lower()
    if run_again != "yes":
        break