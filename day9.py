from itertools import combinations

with open('input9.txt') as f:
    data = list(map(int, f.read().splitlines()))

def part1():
    for i, n in enumerate(data):
        if i < 25:
            continue
        pairs = [sum(x) for x in combinations(data[i-25:i], 2)]
        if n not in pairs:
            return n

def part2(p1):
    for i, n in enumerate(data):
        li = [n]
        for j in data[i+1:]:
            li.append(j)
            if sum(li) == p1:
                return li
            if sum(li) > p1:
                break

p1 = part1()
p2 = part2(p1)
print(p1, min(p2) + max(p2))
