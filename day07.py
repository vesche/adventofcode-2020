import collections

with open('input07.txt') as f:
    data = f.read().splitlines()

bags = list()

for line in data:
    line = [i.strip() for i in line.split('bag') if len(i) > 2]
    root_bag = line[0]
    sub_bags = collections.OrderedDict({root_bag: 1})
    if not 'no other' in ' '.join(line):
        for s in line[1:]:
            for c in s:
                if c.isdecimal():
                    n = int(c)
                    break
            sub_bags[' '.join(s.split()[-2:])] = n
    bags.append(sub_bags)

root, sub = collections.defaultdict(set), collections.defaultdict(list)
for bag in bags:
    root_color = list(bag)[0]
    for sub_color in list(bag)[1:]:
        root[sub_color].add(root_color)
        sub[root_color].append((sub_color, bag[sub_color]))

crack = 'shiny gold'

g = set()
def find(color):
    for c in root[color]:
        g.add(c); find(c)
find(crack)

def count(color):
    return sum([n + (n * count(sub_color)) for sub_color, n in sub[color]])

print(len(g), count(crack))