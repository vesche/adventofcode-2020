with open('input01.txt') as f:
    data = list(map(int, f.read().splitlines()))

def part1():
    for a in data:
        for b in data:
            if a + b == 2020:
                return f'part 1: {a * b}'

def part2():
    for a in data:
        for b in data:
            for c in data:
                if a + b + c == 2020:
                    return f'part 2: {a * b * c}'

print(part1())
print(part2())