import random

# 1. Setup the 5 words and their hints
word_hint_db = {
    "python": "A popular programming language named after a snake",
    "coding": "The act of writing instructions for a computer",
    "intern": "A student or trainee working to gain experience",
    "script": "A file containing a program or sequence of instructions",
    "levels": "Different stages of difficulty in a game"
}

# Pick a random word from our predefined list
all_secret_words = list(word_hint_db.keys())
secret_word = random.choice(all_secret_words)
word_hint = word_hint_db[secret_word]

# Create the hidden word display list of underscores
guessed_word = ["_"] * len(secret_word)

# Game initialization variables
lives = 6
guessed_letters = []

print("=== WELCOME TO HANGMAN ===")

# 2. Main Game Loop
while lives > 0 and "_" in guessed_word:
    print("\n------------------------------------")
    print("HINT: " + word_hint)
    
    # Show the current progress of the hidden word
    current_progress = " ".join(guessed_word)
    print("Word to guess: " + current_progress.upper())
    print("Lives remaining: " + str(lives))
    
    # Show guessed letters safely
    if len(guessed_letters) > 0:
        print("Letters tried: " + ", ".join(guessed_letters).upper())
    else:
        print("Letters tried: None")
    print("------------------------------------")
    
    # Take user input
    guess = input("Guess a letter: ")
    guess = guess.lower()
    guess = guess.strip()
    
    # Input verification checks
    if len(guess) != 1:
        print("Error: Please enter exactly one letter.")
        continue
        
    if guess.isalpha() == False:
        print("Error: Please enter a valid alphabet letter.")
        continue
        
    if guess in guessed_letters:
        print("Error: You already guessed that letter. Try again.")
        continue
        
    # Add valid guess to our tracking list
    guessed_letters.append(guess)
    
    # 3. Check the letter against the secret word
    if guess in secret_word:
        print("Good job! That letter is correct.")
        # Loop through indices to replace underscores (Fix applied here!)
        for position in range(len(secret_word)):
            if secret_word[position] == guess:
                guessed_word[position] = guess
    else:
        print("Wrong! That letter is not in the word.")
        lives = lives - 1

# 4. Final Game Results
print("\n==============================")
if "_" not in guessed_word:
    print("CONGRATULATIONS! YOU WIN!")
    print("The correct word was: " + secret_word.upper())
else:
    print("GAME OVER! YOU LOST!")
    print("The correct word was: " + secret_word.upper())
print("==============================")