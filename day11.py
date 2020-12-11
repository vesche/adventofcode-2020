with open('input11.txt') as f:
    grid = [list(i) for i in f.read().splitlines()]

grid_b = [_[:] for _ in grid]
coords = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def find_occ_p1(grid, i, j):
    x, l, c = 0, len(grid), len(grid[0])
    for a, b in coords:
        ia, jb = i+a, j+b
        if 0 <= ia < l and 0 <= jb < c and grid[ia][jb] == '#':
            x += 1
    return x

def find_occ_p2(grid, i, j):
    x, l, c = 0, len(grid), len(grid[0])
    for a, b in coords:
        ia, jb = i+a, j+b
        while 0 <= ia < l and 0 <= jb < c:
            if grid[ia][jb] == '#':
                x += 1; break
            elif grid[ia][jb] == 'L':
                break
            ia += a
            jb += b
    return x

def solve(p1=True):
    while True:
        same, grid_copy = True, [_[:] for _ in grid]
        for i, row in enumerate(grid_copy):
            for j, col in enumerate(row):
                if p1:
                    n = find_occ_p1(grid_copy, i, j)
                    nx = 4
                else:
                    n = find_occ_p2(grid_copy, i, j)
                    nx = 5
                if col == 'L' and n == 0:
                    grid[i][j] = '#'

                elif col == '#' and n >= nx:
                    grid[i][j] = 'L'
                same &= row[j] == grid[i][j]
        if same:
            break

def count_occ(grid):
    return ''.join([''.join(i) for i in grid]).count('#')

solve()
print(count_occ(grid))

grid = grid_b
solve(p1=False)
print(count_occ(grid))
