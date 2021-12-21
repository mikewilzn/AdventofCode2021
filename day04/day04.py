from timeit import default_timer
import numpy as np

# Parses boards input into 3d array
def setup_boards(boards_array):
    for board in boards_array:
        board = board.split('\n')
    return np.array(boards_array)

def main():
    start_time = default_timer()

    with open('input.txt') as f:
        draws = list(map(int, f.readline().split(',')))
        boards = f.read()[1:].split("\n\n") #[1:] Ignored blank line between draws and the boards
    
    boards = setup_boards(boards)
    print(boards[0][0])
    """ for num in draws:
        for board in boards:
            for row in board:
                for col in row:
                    if(int(col) == num):
                        col = -1 """

    end_time = default_timer()
    
    print(f'Time: {1000*(end_time-start_time):.3f}ms')

if __name__ == '__main__':
    main()