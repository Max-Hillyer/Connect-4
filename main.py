from simple_graphics import *
import random

board_height = 6
board_width = 7 
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

def check_board():
    for current_color in ['yellow', 'red']:
        for r in range(board_height):
            for c in range(board_width):
                if cells[r][c].color != current_color:
                    continue

                if c + 3 < board_width and all(cells[r][c + i].color == current_color for i in range(4)):
                    return current_color
                if r + 3 < board_height and all(cells[r + i][c].color == current_color for i in range(4)):
                    return current_color
                if r + 3 < board_height and c + 3 < board_width and all(cells[r + i][c + i].color == current_color for i in range(4)):
                    return current_color
                if r - 3 >= 0 and c + 3 < board_width and all(cells[r - i][c + i].color == current_color for i in range(4)):
                    return current_color
    return 0

won = False

@on_click
def drop_chip():
    global color
    global won

    if won:
        return

    for y in range(board_height):
        for x in range(board_width):
            if cells[y][x].is_obj_over(mouse.x, mouse.y) and cells[y][x].color == 'gray':
                for i in range(board_height - 1, -1, -1):
                    if cells[i][x].color == 'gray':
                        player = color
                        cells[i][x].color = player
                        winner = check_board()
                        if winner != 0:
                            Text(0, 0, f'{winner} WINS', winner)
                            won = True
                        else:
                            color = 'yellow' if player == 'red' else 'red'
                        return
                return
                 
run(width=400, height=400, caption="My Graphics App")
