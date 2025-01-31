import unittest
from mazes import Maze
from cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
    def test_maze_initialization(self):
        num_cols = 8
        num_rows = 6
        m2 = Maze(5, 5, num_rows, num_cols, 15, 15, None)
        self.assertEqual(m2._x1, 5)
        self.assertEqual(m2._y1, 5)
        self.assertEqual(m2._num_rows, num_rows)
        self.assertEqual(m2._num_cols, num_cols)
        self.assertEqual(m2._cell_size_x, 15)
        self.assertEqual(m2._cell_size_y, 15)
        self.assertIsNone(m2._win)

    def test_maze_cells_content(self):
        num_cols = 5
        num_rows = 5
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        for row in m3._cells:
            for cell in row:
                self.assertIsInstance(cell, Cell)
    
    def test_cell_initialization(self):
        c1 = Cell(None)
        self.assertIsNone(c1._x1)
        self.assertIsNone(c1._y1)
        self.assertIsNone(c1._x2)
        self.assertIsNone(c1._y2)
        self.assertTrue(c1.has_left_wall)
        self.assertTrue(c1.has_right_wall)
        self.assertTrue(c1.has_top_wall)
        self.assertTrue(c1.has_bottom_wall)
        self.assertIsNone(c1._win)
    
    def test_maze_cell_access(self):
        num_cols = 4
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    
    # Test that we can access cells using [row][col]
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
    def test_maze_cell_access(self):
        num_cols = 4
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    
    # Test that we can access cells using [row][col]
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
    def test_minimal_maze(self):
        size = 1  # 1x1 maze
        m1 = Maze(0, 0, size, size, 10, 10)
    
        self.assertEqual(
            len(m1._cells),
            size,
        )
        self.assertEqual(
            len(m1._cells[0]),
            size,
        )
    def test_break_entrance_and_exit(self):
    # Create a small test maze (maybe 3x3)
        num_cols = num_rows = 3
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
    
    # Verify entrance (top-left cell)
        self.assertFalse(maze._cells[0][0].has_top_wall)
    
    # Verify exit (bottom-right cell)
        self.assertFalse(maze._cells[-1][-1].has_bottom_wall)


    def test_break_walls_r_with_seed(self):
        num_cols = 5
        num_rows = 5
        seed = 42

        maze1 = Maze(0, 0, num_rows, num_cols, 10, 10, None, seed)
        maze2 = Maze(0, 0, num_rows, num_cols, 10, 10, None, seed)

        for i in range(num_rows):
            for j in range(num_cols):
                self.assertEqual(maze1._cells[i][j].has_top_wall, maze2._cells[i][j].has_top_wall)
                self.assertEqual(maze1._cells[i][j].has_bottom_wall, maze2._cells[i][j].has_bottom_wall)
                self.assertEqual(maze1._cells[i][j].has_left_wall, maze2._cells[i][j].has_left_wall)
                self.assertEqual(maze1._cells[i][j].has_right_wall, maze2._cells[i][j].has_right_wall)
    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )

if __name__ == "__main__":
    unittest.main()
