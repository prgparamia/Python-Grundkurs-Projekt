
import tkinter as tk
import random
from tkinter  import messagebox








# Drietes Spiefenster
    

GRID_SIZE = 8
NUM_TREASURES = 3
NUM_TRAPS = 5
MAX_ATTEMPTS = 20

class TreasureHuntHarder:
    # Constructor
    def __init__(self, root):
        self.root = root
        self.root.title(" Treasure Hunt Level 3")
        self.grid = []
        self.attempts = MAX_ATTEMPTS
        self.treasures_found = 0
        self.treasure_positions = set()
        self.trap_positions = set()
        self.buttons = {}

        self.status_label = tk.Label(root, text=f"Attempts left: {self.attempts}", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.create_grid()
        self.place_items()

    # Methoden

    def create_grid(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                btn = tk.Button(frame, text="?", width=4, height=2,
                                command=lambda r=row, c=col: self.click_cell(r, c))
                btn.grid(row=row, column=col)
                self.buttons[(row, col)] = btn

    def place_items(self):
        # Randomly place treasures
        while len(self.treasure_positions) < NUM_TREASURES:
            pos = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
            self.treasure_positions.add(pos)

        # Randomly place traps (not overlapping treasures)
        while len(self.trap_positions) < NUM_TRAPS:
            pos = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
            if pos not in self.treasure_positions:
                self.trap_positions.add(pos)

    def click_cell(self, row, col):
        if self.attempts <= 0:
            return

        btn = self.buttons[(row, col)]
        if btn["state"] == "disabled":
            return

        self.attempts -= 1
        pos = (row, col)

        if pos in self.treasure_positions:
            btn.config(text="💎", bg="gold")
            self.treasures_found += 1
        elif pos in self.trap_positions:
            btn.config(text="💀", bg="red")
        else:
            btn.config(text="❌", bg="gray")

        btn.config(state="disabled")
        self.status_label.config(text=f"Attempts left: {self.attempts}")

        if self.treasures_found == NUM_TREASURES:
            messagebox.showinfo("Victory!", "🏆 You found all the treasures!")
            self.disable_all_buttons()
        elif self.attempts == 0:
            messagebox.showwarning("Game Over", "😢 You're out of attempts!")
            self.reveal_all()

    def disable_all_buttons(self):
        for btn in self.buttons.values():
            btn.config(state="disabled")

    def reveal_all(self):
        for pos, btn in self.buttons.items():
            if pos in self.treasure_positions:
                btn.config(text="💎", bg="gold")
            elif pos in self.trap_positions:
                btn.config(text="💀", bg="red")
            btn.config(state="disabled")
    