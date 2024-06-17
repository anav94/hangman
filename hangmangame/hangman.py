import random
import os
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
display = []
print(hangman_art.logo)

# Determine the length of the chosen word
word_length = len(chosen_word)

# Number of lives
lives = 6

# Initialize the display with underscores
for _ in range(word_length):
    display.append("_")
print(display)

# Game loop
end_of_game = False
while not end_of_game:
    guess = input("Choose a letter:\n").lower()

    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Check if the guessed letter is in the chosen word and update the display
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess in display:
        print(f"You have guessed {guess}")

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word. Lives remaining: {lives}")
        if lives == 0:
            end_of_game = True
            print(f"You lose!\nThe word was {chosen_word}")

    print(display)

    # Check if the game is over
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(hangman_art.stages[lives])
