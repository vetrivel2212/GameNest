import random

def spin_row(symbols):
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 2
        elif row[0] == '🍉':
            return bet * 3
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 8
        elif row[0] == '⭐':
            return bet * 10
    return 0

def play():
    print("🎰 Welcome to the Slot Machine!")
    balance = 100
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    print("Available Symbols:")
    for symbol in symbols:
        print(symbol, end=" ")
    print("\n")

    is_playing = True

    while is_playing:
        print("#################################")
        if balance <= 0:
            print("💸 You're out of balance!")
            print("Game Over.....")
            break

        print(f"💰 Your Balance: {balance}")
        bet = input("💵 Place your bet amount: ")

        if not bet.isdigit():
            print("❌ Invalid entry. Please enter a number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("❗ Insufficient funds.")
            continue
        if bet <= 0:
            print("❗ Bet amount must be greater than zero.")
            continue

        balance -= bet
        print("🎲 Spinning...\n")
        row = spin_row(symbols)
        print_row(row)

        payout = get_payout(row, bet)
        balance += payout

        if payout > 0:
            print(f"🎉 You won {payout}! 💸")
        else:
            print("😢 No match. Better luck next time!")

        print(f"💼 New Balance: {balance}")
        choice = input("Do you want to continue? (y/n): ").lower()
        if choice != 'y':
            print("\n👋 Thanks for playing!")
            print(f"Final Balance: {balance}")
            is_playing = False

if __name__ == '__main__':
    play()
