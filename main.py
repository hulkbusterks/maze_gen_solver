from graphics import *
from cell import *
from mazes import *



def main():
    num_rows = 30
    num_cols = 30
    margin = 10
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=1)
    maze.solve()
    
    win.wait_for_close()

main()
