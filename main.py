from simple_graphics import *
import random

board_height = 8
board_width = 8 
chip_size = 12 

def draw_board(board: list[list]):
    for x in range(len(board)):
        for y in range(len(x)):
            c = Circle(x,y, radius = 20, color = 'red')

cells = []
for y in range(board_height):
    row = [] 
    for x in range(board_width):
        cell = Circle(
            x * 30 + 30,
            y * 30 + 30,
            radius = chip_size,
            color = 'gray'
        )
        row.append(cell)
    cells.append(row)

color = 'red'
@on_click
def drop_chip():
    global color
    for y in range(board_height):
        for x in range(board_width):
             if cells[y][x].is_obj_over(mouse.x, mouse.y) and (cells[y][x]).color == 'gray':
                 (cells[y][x]).color = color
                 color = 'yellow' if color == 'red' else 'red'
run(width=400, height=400, caption="My Graphics App")
