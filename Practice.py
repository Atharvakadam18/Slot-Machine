import random
import tkinter as tk
from tkinter import messagebox

# Constants
MAX_BET = 1000
MIN_BET = 100
symbols = "!@#$%&?"
balance = 0

# Function to deposit money
def deposit():
    global balance
    try:
        amount = int(deposit_entry.get())
        if amount > 0:
            balance = amount
            balance_label.config(text=f"Balance: ₹{balance}")
            messagebox.showinfo("Deposit Successful", f"You deposited ₹{amount}")
        else:
            messagebox.showerror("Error", "Deposit amount must be greater than 0")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Function to spin the slot machine
def spin():
    global balance
    try:
        bet = int(bet_entry.get())
        if bet < MIN_BET or bet > MAX_BET:
            messagebox.showerror("Error", f"Bet must be between ₹{MIN_BET} - ₹{MAX_BET}")
            return
        if bet > balance:
            messagebox.showerror("Error", "Insufficient balance!")
            return

        slot_result = [random.choice(symbols) for _ in range(3)]
        slot_display.config(text=" ".join(slot_result))

        if slot_result[0] == slot_result[1] == slot_result[2]:  # Jackpot!
            winnings = bet * 3
            balance += winnings
            messagebox.showinfo("Jackpot!", f"🎉 You won ₹{winnings}!")
        else:
            balance -= bet
            messagebox.showinfo("Try Again", "Better luck next time!")

        balance_label.config(text=f"Balance: ₹{balance}")
        
        if balance == 0:
            messagebox.showwarning("Game Over", "You ran out of money! Restarting...")
            reset_game()

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid bet amount")

# Reset game
def reset_game():
    global balance
    balance = 0
    balance_label.config(text="Balance: ₹0")
    slot_display.config(text="❓ ❓ ❓")

# GUI Setup
root = tk.Tk()
root.title("Slot Machine Game 🎰")
root.geometry("400x400")

# Deposit Section
tk.Label(root, text="Deposit Amount:").pack()
deposit_entry = tk.Entry(root)
deposit_entry.pack()
tk.Button(root, text="Deposit", command=deposit).pack()

# Balance Display
balance_label = tk.Label(root, text="Balance: ₹0", font=("Arial", 14, "bold"))
balance_label.pack()

# Betting Section
tk.Label(root, text="Bet Amount:").pack()
bet_entry = tk.Entry(root)
bet_entry.pack()
tk.Button(root, text="Spin 🎰", command=spin).pack()

# Slot Machine Display
slot_display = tk.Label(root, text="❓ ❓ ❓", font=("Arial", 24, "bold"))
slot_display.pack()

# Run Tkinter Main Loop
root.mainloop()