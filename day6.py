with open('input6.txt') as f:
    data = f.read().split('\n\n')

part1, part2 = 0, 0

for group in data:
    letters = set(''.join(group.split('\n')))
    part1 += len(letters)

    for letter in letters:
        for person in group.split('\n'):
            if letter not in person:
                break
        else:
            part2 += 1

print(part1, part2)