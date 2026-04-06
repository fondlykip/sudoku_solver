from typing import Iterable


class SudokuMatrix():
    """A class that represents a Sudoku puzzle and 
    provides some methods of accessing it's attributes.
    """
    def __init__(self, puzzle:list[list[int]]):
        self.matrix = puzzle

    def rows(self):
        """A functions to get all the rows of the puzzle as lists"""
        return self.matrix

    def row(self, row_idx: int):
        """A function to get a single row of the puzzle as a list"""
        if not isinstance(row_idx, int):
            raise ValueError("An integer index is required to fetch individual rows")
        return self.matrix[row_idx]
    
    def columns(self):
        """A function to get all the columns of the puzzle as a list"""
        return [[row[index] for row in self.matrix] for index in range(0, 9)]
    
    def column(self, col_idx: int):
        """A function to get a specific column of the puzzle as a list"""
        return [row[col_idx] for row in self.matrix]

    
    def quadrant(self, coordinate: tuple[int, int]):
        """Return the current values of a quadrant given a coordinate that lies within that
        quadran."""
        x,y = coordinate
        top_left_x, top_left_y = ((x-(x%3)), (y-(y%3)))
        quadrant = []
        for row_index in range(top_left_y, top_left_y+3):
            quad_row = []
            for col_index in range(top_left_x, top_left_x+3):
                matrix = self.matrix
                quad_row.append(matrix[row_index][col_index])
            quadrant.append(quad_row)
        return quadrant
    
    def quadrant_values(self, coordinate: tuple[int, int]) -> Iterable:
        """A function to get the set of unique values that lie within a quadrant by passing
        a coordinate that lies within that quadrant."""
        for row in self.quadrant(coordinate):
            for value in row:
                yield value

    def cell(self, coordinate: tuple[int]):
        """A function to fetch a cell's value given a tuple coordinate of the
        cells position on the grid"""
        x, y = coordinate
        return self.matrix[y][x]
    
    def set_cell(self, coordinate: tuple[int,int], value: int):
        """A function to update a cell's value and run an update of the puzzle's
        possibility matrix"""
        x, y = coordinate
        self.matrix[y][x] = value
        return True


    


    
    


