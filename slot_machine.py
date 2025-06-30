import random
import time
import os

# Function to clear the terminal screen (works on Windows and Unix-based systems)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to randomly generate a row of 3 slot symbols
def spin_row():
    symbols = ['🍒', '🔔', '💎', '⭐', '🍋']  # List of possible symbols
    return [random.choice(symbols) for _ in range(3)]  # Randomly choose 3 symbols

# Function to display the slot row in a formatted way
def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

# Function to calculate payout based on the result of the spin and bet amount
def get_payout(row, bet):
    # Check if all three symbols in the row are the same
    if row[0] == row[1] == row[2]:
        symbol = row[0]
        # Determine payout multiplier based on the matching symbol
        if symbol == '🍒':
            return bet * 3
        elif symbol == '🍋':
            return bet * 4
        elif symbol == '🔔':
            return bet * 6
        elif symbol == '💎':
            return bet * 10
        elif symbol == '⭐':
            return bet * 20
    return 0  # No payout if symbols don't match

# Main function to run the slot machine game
def main():
    balance = 100  # Initial player balance

    # Game introduction
    print("************************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🔔 💎 ⭐ 🍋")
    print("************************")

    # Game loop: keep playing until balance is 0 or user quits
    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Place your bet amount: ")

        # Validate that the bet is a number
        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        # Check for sufficient balance and valid bet amount
        if bet > balance:
            print("Insufficient funds")
            continue
        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        # Deduct the bet from the balance
        balance -= bet

        # Clear screen and simulate spinning
        clear_screen()
        print("Spinning...\n")
        time.sleep(1)

        # Spin and display result
        row = spin_row()
        print_row(row)

        # Calculate winnings and update balance
        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
            if payout >= bet * 20:
                print("🎉 JACKPOT!!! 🎉")
        else:
            print("Sorry you lost this round")

        balance += payout  # Add winnings to balance

        # Ask if the player wants to continue
        play_again = input("Do you want to spin again? (Y/N): ").upper()
        if play_again != 'Y':
            break

    # Game over message
    print("******************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("******************************************")

# Run the game
if __name__ == "__main__":
    main()