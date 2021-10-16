# minesweeper grid(2x3) with 3 randomly-placed mines
import random


def minesweeper(n):
    arr = [[0 for row in range(n)] for column in range(n)]
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    arr[y][x] = 'X'
    print(y, x)

    if 1 <= x <= 3:
        arr[y][x + 1] += 1  # center right
        arr[y][x - 1] += 1  # center left

    if x == 0:
        arr[y][x + 1] += 1  # center right

    if x == 4:
        arr[y][x - 1] += 1  # center left

    if 1 <= x <= 4 and 1 <= y <= 4:
        arr[y - 1][x - 1] += 1  # top left

    if 0 <= x <= 3 and 1 <= y <= 4:
        arr[y - 1][x + 1] += 1  # top right

    if 0 <= x <= 4 and 1 <= y <= 4:
        arr[y - 1][x] += 1  # top center

    if 0 <= x <= 3 and 0 <= y <= 3:
        arr[y + 1][x + 1] += 1  # bottom right

    if 1 <= x <= 4 and 0 <= y <= 3:
        arr[y + 1][x - 1] += 1  # bottom left

    if 0 <= x <= 4 and 0 <= y <= 3:
        arr[y + 1][x] += 1  # bottom center

    for row in arr:
        print(" ".join(str(cell) for cell in row))
        print(" ")


if __name__ == "__main__":
    minesweeper(5)
