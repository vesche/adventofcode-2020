from itertools import permutations

with open('input10.txt') as f:
    data = list(map(int, f.read().splitlines()))

adapter = max(data)+3
data2 = sorted(data[:])
current, ones, threes = 0, 0, 0

while data:
    x = min(data)
    diff = x - current
    if diff == 1:
        ones += 1
    elif diff == 3:
        threes += 1
    if diff > 3:
        break
    current = x
    data.remove(x)

print(ones*(threes+1))

d = dict()
def p2(adapters, outlet):
    k = (len(adapters), outlet)
    if k in d:
        return d[k]
    chains = 0
    if 0 <= adapter - outlet <= 3:
        chains += 1
    if not adapters:
        return chains
    fa, aa = adapters[0], adapters[1:]
    if 0 <= fa - outlet <= 3:
        chains += p2(aa, fa)
    chains += p2(aa, outlet)
    d[k] = chains
    return chains

print(p2(sorted(data2), 0))
