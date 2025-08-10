          
import tkinter as tk
import random
from tkinter  import messagebox






#  Erstes Spielfenster Class Deklaration

class TreasureHunt: 
    # Constructor             
    def __init__(self, root):
        self.root = root
        self.root.title("Treasure Hunt Game Level 1")

        self.grid_size = 5  # 5x5 grid
        self.buttons = []
        self.score = 0

        self.treasure_row = random.randint(0, self.grid_size - 1)
        self.treasure_col = random.randint(0, self.grid_size - 1)

        self.create_widgets()
        self.update_score()

    # Methoden

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for row in range(self.grid_size):
            row_buttons = []
            for col in range(self.grid_size):
                btn = tk.Button(frame, text="❓", width=6, height=3,
                                command=lambda r=row, c=col: self.check_treasure(r, c))
                btn.grid(row=row, column=col)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

        self.score_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.score_label.pack(pady=10)

    def update_score(self):
        self.score_label.config(text=f"Score (Attempts): {self.score}")

    def check_treasure(self, row, col):
        if row == self.treasure_row and col == self.treasure_col:
            self.buttons[row][col].config(text="💰", bg="green", state="disabled")
            messagebox.showinfo("Congratulations!", f"You found the treasure in {self.score + 1} attempts!")
            self.disable_all_buttons()
        else:
            if self.buttons[row][col]["state"] == "normal":
                self.buttons[row][col].config(text="❌", bg="red", state="disabled")
                self.score += 1
                self.update_score()

    def disable_all_buttons(self):
        for row_buttons in self.buttons:
            for btn in row_buttons:
                btn.config(state="disabled")
                
                
    