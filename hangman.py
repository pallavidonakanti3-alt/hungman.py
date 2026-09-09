import random

# List of predefined words
words = ["python", "computer", "programming", "developer", "machine"]

# Select a random word
word = random.choice(words)

# Create blanks for the word
guessed_word = ["_"] * len(word)

# Maximum incorrect guesses
max_attempts = 6
wrong_guesses = 0

# Store letters already guessed
guessed_letters = []

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

while wrong_guesses < max_attempts and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses:", wrong_guesses, "/", max_attempts)

    guess = input("Enter a letter: ").lower()

    # Check whether input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check the letter
    if guess in word:
        print("✅ Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        print("❌ Wrong guess!")
        wrong_guesses += 1

# Final result
if "_" not in guessed_word:
    print("\n🎉 Congratulations!")
    print("You guessed the word:", word)
else:
    print("\n😢 Game Over!")
    print("The correct word was:", word)