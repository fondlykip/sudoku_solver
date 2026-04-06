import copy
from sudoku_solver import SudokuSolver

def read_puzzle_file(file_name):
    puzzles = []
    with open("./data/test_sudokus.txt") as f:
        puzzle = []
        for l in f.readlines():
            if l.startswith("Grid 01"):
                continue
            elif l.startswith("Grid"):
                puzzles.append(copy.deepcopy(puzzle))
                puzzle = []
            else:
                row = [int(c) for c in l.strip()]
                puzzle.append(row)
    return puzzles


def main():
    test_puzzles = read_puzzle_file("./test_sudokus.txt")
    solved_count = 0
    for puzzle in test_puzzles:
        solver = SudokuSolver(puzzle)
        solved = solver.solve_puzzle()
        if solved:
            solved_count += 1
    print(f"solved {solved_count} out of {len(test_puzzles)} puzzles.")

if __name__ == "__main__":
    main()
