with open('input5.txt') as f:
    data = f.read().splitlines()

seat_ids = list()

for line in data:
    row_a, row_b = 0, 127
    col_a, col_b = 0, 7
    fb, lr = line[:7], line[7:]

    for i in fb:
        if i == 'F':
            row_b = (row_b + row_a) // 2
        elif i == 'B':
            row_a = (row_b + row_a) // 2 + 1

    for i in lr:
        if i == 'L':
            col_b = (col_b + col_a) // 2
        if i == 'R':
            col_a = (col_b + col_a) // 2 + 1

    seat_ids.append(row_a*8+col_a)

print(max(seat_ids))

for seat in range(seat_ids[0], seat_ids[-1]):
    if seat not in seat_ids:
        print(seat)
