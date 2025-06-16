# madlib.py
# A fun word game where you create a silly story by filling in blanks

def play():
    print("🎉 Create a story by filling in the blanks! 🎉")
    print("Let's begin...\n")

    print(f"Today I went to a ___________ zoo.")
    adjective1 = input("Enter an adjective (description): ")

    print(f"In an exhibit, I saw a _________.")
    noun1 = input("Enter a noun (person, place, or thing): ")

    print(f"It was __________ and _______!")
    adjective2 = input("Enter an adjective (description): ")
    verb1 = input("Enter a verb ending with 'ing': ")

    print(f"Overall, I was feeling ___________.")
    adjective3 = input("Enter an adjective (description): ")

    print("\n📝 Here is your silly story!\n")
    print(f"Today I went to a {adjective1} zoo.")
    print(f"In an exhibit, I saw a {noun1}.")
    print(f"The {noun1} was {adjective2} and {verb1}!")
    print(f"Overall, I was feeling {adjective3}.")

# Optional: allows you to test this game standalone
if __name__ == "__main__":
    play()
