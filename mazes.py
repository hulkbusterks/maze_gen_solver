from cell import *
from graphics import *
import time
import random



class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        #self._seed = seed

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_enterance_and_exit()
        self._mark_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                cell = Cell(self._win)
                row.append(cell)
            self._cells.append(row)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        x1 = self._x1 + j * self._cell_size_x
        y1 = self._y1 + i * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, x2, y1, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.005)
    
    def _break_enterance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False

    def _mark_entrance_and_exit(self):
        if self._win is None:
            return
        
    # Draw entrance marker (top of first cell)
        entrance_line = Line(
            Point(self._x1, self._y1),
            Point(self._x1 + self._cell_size_x, self._y1)
        )
        self._win.draw_line(entrance_line, "green")
    
    # Draw exit marker (bottom of last cell)
        exit_x = self._x1 + (self._num_cols - 1) * self._cell_size_x
        exit_y = self._y1 + self._num_rows * self._cell_size_y
        exit_line = Line(
            Point(exit_x, exit_y),
            Point(exit_x + self._cell_size_x, exit_y)
        )
        self._win.draw_line(exit_line, "red")

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((-1, 0))
            if i < self._num_rows - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((1, 0))

            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((0, -1))
            if j < self._num_cols - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((0, 1))
            
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                break
            else:
                direction = random.choice(to_visit)
                if direction[0] == -1:
                    self._cells[i][j].has_top_wall = False
    
                    self._cells[i - 1][j].has_bottom_wall = False
                elif direction[0] == 1:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i + 1][j].has_top_wall = False
                elif direction[1] == -1:    
                    self._cells[i][j].has_left_wall = False
                    self._cells[i][j - 1].has_right_wall = False
                elif direction[1] == 1:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i][j + 1].has_left_wall = False
# After breaking walls:
                print(f"Breaking wall at {i}, {j} in direction {direction}")
                self._draw_cell(i, j)
                self._draw_cell(i + direction[0], j + direction[1])
                self._animate()
                self._break_walls_r(direction[0] + i, direction[1] + j)
    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False

    def solve(self):
        is_solved = self._solve_r(0,0)
        self._reset_cells_visited()
        print(f"Maze solved: {is_solved}")
        return is_solved

    def _solve_r(self,i,j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True

        while True:
            to_visit = []
            if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_top_wall:
                to_visit.append((-1, 0))
            if i < self._num_rows - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_bottom_wall:
                to_visit.append((1, 0))
            if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_left_wall:
                to_visit.append((0, -1))
            if j < self._num_cols - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].has_right_wall:
                to_visit.append((0, 1))
            
            if len(to_visit) == 0:
                return i == self._num_rows - 1 and j == self._num_cols - 1
            else:  
                direction = random.choice(to_visit)
                next_i = i + direction[0]
                next_j = j + direction[1]
                # When trying a direction
                current_cell = self._cells[i][j]
                next_cell = self._cells[next_i][next_j]
                current_cell.draw_move(next_cell)
                self._animate()
                if self._solve_r(next_i, next_j):
                    return True
                self._animate()
                current_cell.draw_move(next_cell, True)  # undo the move
            
