from graphics import *

class Cell:
    def __init__(self, win=None):
        self._x1 = None
        self._y1 = None
        self._x2 = None 
        self._y2 = None 
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True 
        self.has_bottom_wall = True
        self._win = win
        self.visited = False

    def draw(self,x1, x2, y1, y2):
        if self._win is None:
            return
        
        self.clear_cell(x1, x2, y1, y2)
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            #print("drawing left wall")
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2,y1), Point(x2,y2))
            #print("drawing right wall")
            self._win.draw_line(line)
        if self.has_top_wall: 
            line = Line(Point(x2,y1), Point(x1,y1))
            #print("drawing top wall")
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1,y2), Point(x2,y2)) 
            #print("drawing bottom wall")
            self._win.draw_line(line)

    def clear_cell(self, x1, x2, y1, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        line = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(line, "white")
        line = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(line, "white")
        line = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(line, "white")
        line = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(line, "white")
    def draw_move(self, to_cell, undo=False):
        
        if not undo:
            line_colour = "red"
        else:
            line_colour = "grey"

        start_x = (self._x1 + self._x2) // 2
        start_y = (self._y1 + self._y2) // 2
        end_x = (to_cell._x1 + to_cell._x2) // 2
        end_y = (to_cell._y1 + to_cell._y2) // 2

        line = Line(Point(start_x, start_y), Point(end_x, end_y))
        self._win.draw_line(line, line_colour)


