from dataclasses import dataclass
from simple_graphics import *
#this import may be slow the first time, the doofus behind the library is probably working 
#on ways to speed it up #https://github.com/Max-Hillyer/Simple_graphics

board_height = 6
board_width = 7 
chip_size = 15 
set_bg('black')

def generate_board():
    cells = []
    for y in range(board_height):
        row = [] 
        for x in range(board_width):
            cell = Circle(
                x * 50 + 30,
                y * 50 + 30,
                radius = chip_size,
                color = 'gray'
            )
            row.append(cell)
        cells.append(row)
    return cells


@dataclass
class GameState:
    cells: list[list[Circle]]
    color: str
    won: bool

gameState = GameState(generate_board(), "red", False)

print(gameState)

def check_board():
    for current_color in ['yellow', 'red']:
        for r in range(board_height):
            for c in range(board_width):
                if gameState.cells[r][c].color != current_color:
                    continue

                if c + 3 < board_width and all(gameState.cells[r][c + i].color == current_color for i in range(4)):
                    return current_color
                if r + 3 < board_height and all(gameState.cells[r + i][c].color == current_color for i in range(4)):
                    return current_color
                if r + 3 < board_height and c + 3 < board_width and all(gameState.cells[r + i][c + i].color == current_color for i in range(4)):
                    return current_color
                if r - 3 >= 0 and c + 3 < board_width and all(gameState.cells[r - i][c + i].color == current_color for i in range(4)):
                    return current_color
    return 0

@on_press('q')
def quit():
    exit(0)

@on_press('r')
def restart():
    gameState.won = False
    gameState.color = 'red'
    clear_screen()
    gameState.cells = generate_board()

@on_click
def drop_chip():
    if gameState.won:
        return

    for y in range(board_height):
        for x in range(board_width):
            if gameState.cells[y][x].is_obj_over(mouse.x, mouse.y) and gameState.cells[y][x].color == 'gray':
                for i in range(board_height - 1, -1, -1):
                    if gameState.cells[i][x].color == 'gray':
                        player = gameState.color
                        gameState.cells[i][x].color = player
                        winner = check_board()
                        if winner != 0:
                            Text(0, 0, f'{winner.upper()} WINS', winner)
                            gameState.won = True
                        else:
                            gameState.color = 'yellow' if player == 'red' else 'red'
                        return
                return
                 
run(width=360, height=330, caption="Connect 4")
