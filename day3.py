with open('input3.txt') as f:
    data = f.read().splitlines()

def travel(right, down):
    trees, column = 0, 0
    for i in range(0, len(data), down):
        line = data[i]
        if line[column % len(line)] == '#':
            trees += 1
        column += right
    return trees

print(travel(3, 1))
print(travel(1, 1) * travel(3, 1) * travel(5, 1) * travel(7, 1) * travel(1, 2))
