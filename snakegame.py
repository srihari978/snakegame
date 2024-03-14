import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.master.geometry("400x400")

        self.canvas = tk.Canvas(master, bg="black", width=400, height=400)
        self.canvas.pack()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.create_food()
        self.direction = "Right"

        self.master.bind("<Key>", self.change_direction)

        self.update_game()

    def create_food(self):
        x = random.randint(1, 39) * 10
        y = random.randint(1, 39) * 10
        self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="red", tags="food")
        return x, y

    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

    def update_game(self):
        head = self.snake[0]
        if self.direction == "Up":
            new_head = (head[0], head[1] - 10)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + 10)
        elif self.direction == "Left":
            new_head = (head[0] - 10, head[1])
        elif self.direction == "Right":
            new_head = (head[0] + 10, head[1])
        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.create_food()
        else:
            self.canvas.delete("snake")
            self.snake.pop()

        self.canvas.delete("food")
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + 10, self.food[1] + 10, fill="red",
                                     tags="food")

        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green",
                                         tags="snake")

        if (
            new_head[0] < 0
            or new_head[1] < 0
            or new_head[0] >= 400
            or new_head[1] >= 400
            or new_head in self.snake[1:]
        ):
            self.game_over()
            return

        self.master.after(100, self.update_game)

    def game_over(self):
        self.canvas.create_text(200, 200, text="Game Over", fill="white", font=("Helvetica", 16))


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
