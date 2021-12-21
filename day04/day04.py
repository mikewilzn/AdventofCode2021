from timeit import default_timer
import numpy as np

class BingoBoard:
    def __init__(self, rows):
        rows = [row.split() for row in rows]
        self.grid = np.array(rows, dtype=int)
    
    def mark_hit(self, num):
        self.grid[self.grid == num] = -1

    def get_score(self, last_number):
        return np.sum((self.grid != -1) * self.grid) * last_number
    
    def is_winner(self):
        if any(np.sum(self.grid, axis = 0) == -5):
            return True
        elif any(np.sum(self.grid, axis = 1) == -5):
            return True
        else:
            return False

def main():
    start_time = default_timer()

    with open('D:\Code Workspaces\AdventofCode2021\day04\input.txt') as f:
        draws = list(map(int, f.readline().split(',')))
        boards = f.read()[1:].split('\n\n') #[1:] Ignored blank line between draws and the boards

    boards = [BingoBoard(board.split('\n')) for board in boards]
    
    scores = []
    for num in draws:
        # Mark hits on each board
        [board.mark_hit(num) for board in boards]
        # Adds winning boards to list of scores
        scores += [board.get_score(num) for board in boards if board.is_winner()]
        # Remove winning boards
        boards = [board for board in boards if not board.is_winner()]

    end_time = default_timer()
    
    print("Part 1: ", scores[0])
    print("Part 2: ", scores[-1])
    print(f'Time: {1000*(end_time-start_time):.3f}ms')

if __name__ == '__main__':
    main()