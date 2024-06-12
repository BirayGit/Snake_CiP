import tkinter as tk
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
window = tk.Tk()
window.geometry("400x400")
window.title("Snake")


canvas = tk.Canvas(window, bg="white", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()
# if you make this larger, the game will go slower
# DELAY = 0.1


def generate_player():
    start_x = 0
    start_y = 0
    end_x = start_x + SIZE
    end_y = start_x + SIZE

    player = canvas.create_rectangle(start_x, start_y, end_x, end_y, fill="blue")
    return player


def generate_food():
    start_x = random.randint(0, CANVAS_WIDTH - SIZE)
    start_y = random.randint(0, CANVAS_HEIGHT - SIZE)
    end_x = start_x + 20
    end_y = start_y + 20

    food = canvas.create_rectangle(start_x, start_y, end_x, end_y, fill="orange")
    return food


generate_player()
generate_food()
window.mainloop()
