import random

MAX_BET = 1000
MIN_BET = 100

symbols = ["🪣", "🧻", "🏺", "🪬", "🧪", "🧨", "⚠️"]

# This function is used to take some initial amount from the user 
def deposit():
    while True:
        amount = input("How much would you like to deposit? ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")

    return amount
   
# This function asks user the amount to bet on each of slot machine
def get_bet():
    while True:
        amount = input("How much would you like to bet? ₹")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ₹{MIN_BET} - ₹{MAX_BET}")
        else:
            print("Please enter a number")

    return amount

# This function spins the slot machine and generates 3 random value based on that it declares the result
def spin(symbols, bet, balance):
    slot = [random.choice(symbols) for _ in range(3)]
    print("Result:", *slot)

    if slot[0] == slot[1] == slot[2]:
        balance += bet * 3
        print(f"Congratulation, Jackpot!!! You won ₹{bet * 3}")
    elif slot[0] == slot[1] or slot[0] == slot[2] or slot[1] == slot[2]:
        balance += bet * 2
        print(f"Congratulation, you won {bet * 2}")
    else:
        print("Better Luck Next Time!!!")
        balance -= bet

    return balance

# This function is to call other function on repeat
def main():
    balance = deposit()

    # This while loop check if the entered bet amount dosen't exceed the balance 
    while True:
        bet = get_bet()
        if bet > balance:
            print(f"You don't have enough balance to bet, your current balance is: ₹{balance}")
        else:
            pass
        balance = spin(symbols, bet, balance)
        if balance == 0:
            break
        again = input(f"Your balance is: ₹{balance}. Do you want to play again? (y/n) = ").capitalize()
        if again != 'Y':
            break  
      
main()
