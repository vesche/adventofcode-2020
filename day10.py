with open('input10.txt') as f:
    data = list(map(int, f.read().splitlines()))

rated = max(data) + 3

for n in data:
    print(n)

print(rated)