import random

# 🎲 Dice Art (1 to 6)
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"),
}

def play():
    print("🎲 Welcome to Dice Roller 🎲\n")
    
    while True:
        try:
            number_of_dice = int(input("How many dice would you like to roll? 🎯: "))
            if number_of_dice <= 0:
                print("⚠️ Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

    # 🔄 Roll Dice
    dice = [random.randint(1, 6) for _ in range(number_of_dice)]

    # 🖼️ Print Dice Side-by-Side
    print("\n🎲 Rolling the dice...\n")
    for i in range(5):  # Each die has 5 lines
        for die in dice:
            print(dice_art[die][i], end=' ')
        print()

    # ➕ Show Total
    total = sum(dice)
    print(f"\n🎯 Total Value: {total}")
    print(f"🎲 Individual Rolls: {dice}")

    print("\nThanks for playing with GameNest Dice Roller! 🎉")

if __name__ == "__main__":
    play()
