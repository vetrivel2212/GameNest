# number_guessing.py
# A fun number guessing game for GameNest

import random

def play():
    low = 1
    high = 100
    answer = random.randint(low, high)

    print("🎯 Welcome to the Number Guessing Game!")
    print(f"Guess a number between {low} and {high}.\n")

    guesses = 0
    while True:
        guess = input("🔢 Enter your guess: ")
        if not guess.isdigit():
            print("⚠️ Please enter a valid number.")
            continue

        guess = int(guess)
        guesses += 1

        if guess < low or guess > high:
            print("🚫 That number is out of bounds!")
        elif guess < answer:
            print("📉 Too low!")
        elif guess > answer:
            print("📈 Too high!")
        else:
            print("✅ You got it right!")
            print(f"🎉 The number was {answer}")
            print(f"🔁 You guessed it in {guesses} tries.")
            break

# Optional: Run standalone for testing
if __name__ == "__main__":
    play()
