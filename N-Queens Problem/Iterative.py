import time
class Board:
    def __init__(self, size):
        self.N = size
        self.queens = [] # list of columns, where the index represents the row
        self.num = 0

    def is_queen_safe(self, row, col):
        for r, c in enumerate(self.queens):
            if r == row or c == col or abs(row - r) == abs(col - c):
                return False
        return True

    def print_the_board(self):
        print ("solution:")
        for row in range(self.N):
            line = ['.'] * self.N
            if row < len(self.queens):
                line[self.queens[row]] = 'Q'
            print(''.join(line))

    def solution(self):
        self.queens = []
        col = row = 0
        while True:
            while col < self.N and not self.is_queen_safe(row, col):
                col += 1
            if col < self.N:
                self.queens.append(col)
                if row + 1 >= self.N:
                    #self.print_the_board()
                    self.num += 1
                    self.queens.pop()
                    col = self.N
                else:
                    row += 1
                    col = 0
            if col >= self.N:
                # not possible to place a queen in this row anymore
                if row == 0:
                    return # all combinations were tried
                col = self.queens.pop() + 1
                row -= 1

if __name__ == "__main__":
    user_input = int(input("Enter input : "))
    q = Board(user_input)
    t0 = time.time()
    q.solution()
    t1 = time.time()
    print("Number of solutionsz = {}".format(q.num))
    print(f'Time(Iteration): {t1-t0:.8} seconds')
