def minesweeper(n):
    arr = [[0 for row in range(n)] for column in range(n)]
    for row in arr:
        print(" ".join(str(cell) for cell in row))
        print("")
if __name__ == "__main__":
    minesweeper(5)
    