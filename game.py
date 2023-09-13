import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner of the game
def determine_winner(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    result = ""

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = f"You win! Computer chose {computer_choice}."
    else:
        result = f"You lose! Computer chose {computer_choice}."

    messagebox.showinfo("Result", result)

# Function to handle button clicks
def on_button_click(choice):
    determine_winner(choice)
    try_again_button.pack(pady=10)

# Function to reset the game for another round
def try_again():
    try_again_button.pack_forget()

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Add a main heading
heading = tk.Label(root, text="Rock Paper Scissors Game", font=("Helvetica", 16, "bold"))
heading.pack(pady=20)

# Create buttons for Rock, Paper, and Scissors
rock_button = tk.Button(root, text="Rock", command=lambda: on_button_click('Rock'))
paper_button = tk.Button(root, text="Paper", command=lambda: on_button_click('Paper'))
scissors_button = tk.Button(root, text="Scissors", command=lambda: on_button_click('Scissors'))

# Create a "Try Again" button
try_again_button = tk.Button(root, text="Try Again", command=try_again)
try_again_button.pack_forget()

# Place buttons on the window
rock_button.pack(pady=10)
paper_button.pack(pady=10)
scissors_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
