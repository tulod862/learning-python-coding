import random

def display_word(word, guessed_letters):
    """Display the current state of the word with guessed letters and underscores."""
    return ' '.join([letter if letter in guessed_letters or letter == ' ' else '_' for letter in word])

def play_hangman():
    words = ["iris", "daisy", "orchid", "sunflower", "rose", "leucanthemum", "rudbeckia",
             "marigold", "aster", "tulip", "lilium lancifolium", "gerbera", "poppy",
               "wisteria", "bougainvillea", "calla lioly"]
    
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6 
    word_guessed = False
    
    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))
    
    while attempts > 0 and not word_guessed:
        guess = input("Guess a letter:").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            else:
                guessed_letters.add(guess)
                if guess in word:
                    print("Correct guess!")
                else:
                    attempts -= 1
                    print("Incorrect guess.")
                    
                current_display = display_word(word, guessed_letters)
                print(current_display)

                if '_' not in current_display:
                    word_guessed = True
                    print("Congratulations! You've guessed the word correctly!")
        else:
            print("Invalid input. Please guess a single letter.")
        
        print(f"Remaining attempts: {attempts}")

    if not word_guessed:
        print(f"You lost the game! The word was '{word}'")


if __name__ == "__main__":()
                    