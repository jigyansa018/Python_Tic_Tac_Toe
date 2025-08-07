import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Global variables
current_player = "X"
winner = False
buttons = []

# Function to toggle player
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

# Function to check for a winner
def check_winner():
    global winner
    combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in combos:
        b1 = buttons[combo[0]]
        b2 = buttons[combo[1]]
        b3 = buttons[combo[2]]
        if b1["text"] != "" and b1["text"] == b2["text"] == b3["text"]:
            b1.config(bg="green")
            b2.config(bg="green")
            b3.config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {b1['text']} wins!")
            winner = True
            return

# Function for button click
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

# Create buttons in a 3x3 grid
for i in range(9):
    btn = tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=i // 3, column=i % 3)
    buttons.append(btn)

# Label to show current player's turn
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Start the main loop
root.mainloop()
