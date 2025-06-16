# play_place.py

import madlib
import hangman
import quiz
import number_guessing
import rock_paper_scissor
import dice_roller
import slot_machine

def main():
    while True:
        print("\n🎮 Welcome to GameNest 🐣")
        print("Choose a game to play:")
        print("1. Madlib")
        print("2. Quiz")
        print("3. Number Guessing")
        print("4. Rock Paper Scissors")
        print("5. Dice Roller")
        print("6. Slot Machine")
        print("7. Hangman")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            madlib.play()
        elif choice == '2':
            quiz.play()
        elif choice == '3':
            number_guessing.play()
        elif choice == '4':
            rock_paper_scissor.play()
        elif choice == '5':
            dice_roller.play()
        elif choice == '6':
            slot_machine.play()
        elif choice == '7':
            hangman.play()
        elif choice == '8':
            print("Thanks for playing GameNest! 🐣🎉")
            break
        else:
            print("Invalid choice! Please select a number from 1 to 8.")

if __name__ == "__main__":
    main()
