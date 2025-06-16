# hangman.py
# Classic Hangman game for GameNest

import random

def display_hangman(hangman, wrong_guesses):
    for line in hangman[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def play():
    hangman = {
        0: ("", "", ""),
        1: (" o ", "   ", "   "),
        2: (" o ", " | ", "   "),
        3: (" o ", "/| ", "   "),
        4: (" o ", "/|\\", "   "),
        5: (" o ", "/|\\", "/  "),
        6: (" o ", "/|\\", "/ \\")
    }

    words = [
        "apple", "banana", "cherry", "date", "elderberry",
        "fig", "grape", "honeydew", "kiwi", "lemon",
        "mango", "nectarine", "orange", "papaya", "quince",
        "raspberry", "strawberry", "tangerine", "ugli", "watermelon"
    ]

    answer = random.choice(words)
    hint = ["_"] * len(answer)
    guessed_letters = []
    wrong_guesses = 0

    print("🎯 Welcome to Hangman!")
    print("Guess the fruit name!")

    while True:
        print("\n###############################")
        display_hangman(hangman, wrong_guesses)
        display_hint(hint)

        guess = input("Enter your guess (one letter): ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"⚠️ You've already guessed '{guess}'. Try another.")
            continue

        guessed_letters.append(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
            print("✅ Good guess!")
        else:
            wrong_guesses += 1
            print("❌ Wrong guess!")

        if "_" not in hint:
            print("\n🎉 You Win!!! 🎉")
            display_hangman(hangman, wrong_guesses)
            print(f"The correct word was: {answer}")
            break
        elif wrong_guesses >= len(hangman) - 1:
            print("\n💀 You Lose!")
            display_hangman(hangman, wrong_guesses)
            print(f"The correct word was: {answer}")
            break

# Optional for testing
if __name__ == '__main__':
    play()
