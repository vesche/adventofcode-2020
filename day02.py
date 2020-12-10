with open('input02.txt') as f:
    data = f.read().splitlines()

part1, part2 = 0, 0

for line in data:
    n, l, password = line.split()
    n1, n2 = map(int, n.split('-'))
    letter = l.rstrip(':')

    if n1 <= password.count(letter) <= n2:
        part1 += 1

    s = password[n1-1] + password[n2-1]
    if s.count(letter) == 1:
        part2 += 1

print(part1)
print(part2)