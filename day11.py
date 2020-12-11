with open('input11.txt') as f:
    data = f.read().splitlines()

foo = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

new_data = [['']*len(data[0]) for i in range(len(data))]

x = 0

while True:
    if x:
        data2 = new_data[:]
    else:
        data2 = data
    x += 1
    new_data = [['']*len(data[0]) for i in range(len(data))]

    for i, line in enumerate(data):
        for j, seat in enumerate(line):
            if seat == '.':
                new_data[i][j] = '.'
                continue

            around = list()
            for a, b in foo:
                try:
                    y, x = i+a, j+b
                    if (x < 0 or y < 0):
                        continue
                    around.append(data2[y][x])
                except:
                    pass

            if set(around) == {'L', '.'} or set(around) == {'L'}:
                new_data[i][j] = '#'
            elif seat == '#' and around.count('#') >= 4:
                new_data[i][j] = 'L'
            else:
                new_data[i][j] = seat

    if new_data == data2:
        break

print(''.join([''.join(i) for i in new_data]).count('#'))
