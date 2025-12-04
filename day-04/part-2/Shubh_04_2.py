with open("input/d4.in", "r") as f:
    lines = f.readlines()

grid = [list(line.strip()) for line in lines]

def count(grid):
    copy = [row[:] for row in grid]
    tot = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != '@':
                continue
            # check all 8 possible directions
            count = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy == 0 and dx == 0:
                        continue
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < len(grid) and 0 <= nx < len(row):
                        if grid[ny][nx] == '@':
                            count += 1
            if count < 4:
                copy[y][x] = '.'
                tot += 1
    return tot, copy

truetot = 0
while (True):
    tot, new_grid = count(grid)
    truetot += tot
    if tot == 0:
        break
    grid = new_grid
print(truetot)