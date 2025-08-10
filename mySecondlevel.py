
import tkinter as tk
import random



from math import sqrt



# Zweites Spielfenster Class Deklaration

GRID_SIZE = 8
TREASURE_COUNT = 3
MAX_MOVES = 25

class TreasureHuntGame:

    # Constructor
    def __init__(self, root): 
        self.root = root
        self.root.title("Treasure Hunt Game Leve 2")
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        
        self.status_label = tk.Label(root, text="Use arrow keys to find treasures!", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.cell_size = 400 // GRID_SIZE
        self.treasures = set()
        self.moves_left = MAX_MOVES
        self.last_distance = None
        self.score = 0

        self.place_treasures()
        self.draw_grid()
        self.player_pos = (0, 0)
        self.draw_player()

        self.root.bind("<Key>", self.move_player)
    # Methoden

    def place_treasures(self):
        while len(self.treasures) < TREASURE_COUNT:
            pos = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
            if pos != (0, 0):
                self.treasures.add(pos)

    def draw_grid(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black")

    def draw_player(self):
        self.canvas.delete("player")
        x, y = self.player_pos
        x1 = x * self.cell_size + 5
        y1 = y * self.cell_size + 5
        x2 = x1 + self.cell_size - 10
        y2 = y1 + self.cell_size - 10
        self.canvas.create_oval(x1, y1, x2, y2, fill="blue", tags="player")

    def move_player(self, event):
        if self.moves_left <= 0 or not self.treasures:
            return

        x, y = self.player_pos
        if event.keysym == "Up" and y > 0:
            y -= 1
        elif event.keysym == "Down" and y < GRID_SIZE - 1:
            y += 1
        elif event.keysym == "Left" and x > 0:
            x -= 1
        elif event.keysym == "Right" and x < GRID_SIZE - 1:
            x += 1
        else:
            return

        self.player_pos = (x, y)
        self.draw_player()
        self.moves_left -= 1

        self.check_for_treasure()
        self.give_clue()

        if not self.treasures:
            self.status_label.config(text=f"You found all treasures! Score: {self.score}")
        elif self.moves_left == 0:
            self.status_label.config(text="Game Over! Out of moves.")

    def check_for_treasure(self):
        if self.player_pos in self.treasures:
            self.treasures.remove(self.player_pos)
            self.score += 100
            cx = self.player_pos[0] * self.cell_size + self.cell_size // 2
            cy = self.player_pos[1] * self.cell_size + self.cell_size // 2
            self.canvas.create_text(cx, cy, text="💎", font=("Arial", 18))

    def give_clue(self):
        if not self.treasures:
            return
        distances = [self.distance(self.player_pos, t) for t in self.treasures]
        min_dist = min(distances)
        if self.last_distance is None:
            clue = f"{self.moves_left} moves left. Searching..."
        elif min_dist < self.last_distance:
            clue = f"Getting warmer! ({self.moves_left} moves left)"
        elif min_dist > self.last_distance:
            clue = f"Getting colder... ({self.moves_left} moves left)"
        else:
            clue = f"Same distance... ({self.moves_left} moves left)"

        self.last_distance = min_dist
        self.status_label.config(text=clue)

    def distance(self, a, b):
        return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    