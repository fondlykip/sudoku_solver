"""A Module of functions to solve a Sudoku puzzle"""
import time
import copy
from sudoku_puzzle import SudokuMatrix


class SudokuSolver():
    def __init__(self, sudoku_puzzle: list[list[int]]):
        
        self.puzzle = SudokuMatrix(sudoku_puzzle)

        self.max_turns = 20
        self.possibility_matrix = SudokuMatrix([[set() for _ in range(0,9)] for _ in range(0,9)])
        self.update_possibility_matrix()

        self.unsolved_cells = []
        for row_num, row in enumerate(self.puzzle.rows()):
            for col_num, val in enumerate(row):
                if val == 0:
                    self.unsolved_cells.append((col_num, row_num))
    


    def exclusive_possibility(self, coordinate):
        """return possibilities that are exclusive to this cell
        within the related row, column, and or quadrant"""
        x,y = coordinate
        row_sets = copy.deepcopy(self.possibility_matrix.row(y))
        _ = row_sets.pop(x)
        column_sets = copy.deepcopy(self.possibility_matrix.column(x))
        _ = column_sets.pop(y)
        quadrant_groups = [s for s in self.possibility_matrix.quadrant_values(coordinate)]
        _ = quadrant_groups.pop((3*(y%3))+(x%3))
        poss_groups = [row_sets, column_sets, quadrant_groups]
        for poss_group in poss_groups:
            _c_poss = copy.deepcopy(self.possibility_matrix.cell(coordinate))
            for poss_set in poss_group:
                _c_poss -= poss_set
            if len(_c_poss) == 1:
                return _c_poss
            else:
                del _c_poss
        return None


    def solve_cell(self, coordinate):
        c_poss = self.possibility_matrix.cell(coordinate)
        if len(c_poss) == 1:
            return list(c_poss)[0]
        e_poss = self.exclusive_possibility(coordinate)
        if e_poss and len(e_poss) == 1:
            return list(e_poss)[0]
    

    def solve_puzzle(self):
        _turn = 0
        while (len(self.unsolved_cells) > 0) and (_turn < self.max_turns):
            still_unsolved = []
            # print(f"============================")
            # print(f"Turn: {_turn}")
            # print(f"puzzle starting state:")
            # for row in self.puzzle.rows():
            #     print(row)
            # print(f"----------------------------")
            # print(f"possibilities starting state:")
            # for row in self.possibility_matrix.rows():
            #     print(row)
            for coordinate in self.unsolved_cells:
                cell_solution = self.solve_cell(coordinate)
                if cell_solution:
                    self.puzzle.set_cell(coordinate, cell_solution)
                    self.update_possibility_matrix()
                else:
                    still_unsolved.append(coordinate)

            self.unsolved_cells = still_unsolved
            _turn += 1
        
        print(f"============================")
        print(f"Final State.")
        print(f"------------")
        print(f"remaining unsolved cells: {len(self.unsolved_cells)}")
        print(f"turns completed: {_turn}")
        print(f"Puzzle:")
        for row in self.puzzle.rows():
            print(row)

        print(f"----------------------------")
        print(f"Possibility Matrix: ")
        for row in self.possibility_matrix.rows():
            print(row)

        self.solved = (len(self.unsolved_cells) == 0)
        return self.solved

    def compute_cell_possibilities(self, coordinate: tuple[int, int]) -> set:
        """Compute the possibile values of this cell given the numbers already present
        in the related column, cell, and quadrant"""
        x, y = coordinate
        if self.puzzle.cell(coordinate) > 0:
            return set()
        possibilities = set(range(1,10))
        in_row = set(self.puzzle.row(y))
        in_column = set(self.puzzle.column(x))
        in_section = set(self.puzzle.quadrant_values(coordinate))
        possibilities = possibilities - in_row - in_column - in_section
        return possibilities


    def update_possibility_matrix(self):
        for y in range(0,9):
            for x in range(0,9):
                self.possibility_matrix.set_cell((x,y), self.compute_cell_possibilities((x,y)))
        return self.possibility_matrix              
                
                
    


# def
#         # if (TURN != 0) and (solves_this_turn == 0):
#         #     print(f"State not changed in this turn {TURN} - blocked?")
#         #     break
#         print(f"=============================")
#         print(f"Turn: {TURN}")
#         print(f"puzzle grid:")
#         for row in puzzle.rows():
#             print(row)
#         print(f"-----------------------------")
#         print(f"possibility_matrix")
#         for row in puzzle.possibility_matrix:
#             print(row)
        
#         TURN += 1
#     solve_time = time.time() - stime

#     if solved_count >= 81:
#         print(f"solved in {TURN+1} passes ({solve_time} seconds!)")
#         return True
#     for row in puzzle.rows():
#         print(row)
#     return False