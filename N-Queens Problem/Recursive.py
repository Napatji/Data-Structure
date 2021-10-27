import time
def is_safe(board, x, y, c):
    for p in [board[i] for i in range(0, c)]:
        if p[0] == x or p[1] == y or x + y == p[0] + p[1] or x - y == p[0] - p[1]:
            return False

    return True


def nqueen_nrec(n):
    num = 0
    c = 0
    step = [0 for x in range(0, n + 1)]
    board = [(x, x) for x in range(0, n)]

    while c != -1:
        if c == n:
            num += 1
            #print(board)
            c -= 1
            step[c] += 1
        elif step[c] == n:
            c -= 1
            step[c] += 1
        elif is_safe(board, step[c], c, c):
            board[c] = (step[c], c)
            c += 1
            step[c] = 0
        else:
            step[c] += 1
    print("Number of solution = {}".format(num))

if __name__ == "__main__":
    user_input = int(input("Enter input : "))
    t0 = time.time()
    c = nqueen_nrec(user_input)
    t1 = time.time()
    print(f'Time(Iteration): {t1-t0:.8} seconds')