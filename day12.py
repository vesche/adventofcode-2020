import math
from collections import deque

with open('input12.txt') as f:
    data = [(i[0], int(i[1:])) for i in f.read().splitlines()]

direction = deque(['East', 'South', 'West', 'North'])

def change_direction(instruction, n):
    turns = n // 90
    if instruction == 'L':
        direction.rotate(turns)
    elif instruction == 'R':
        direction.rotate(-turns)
    return direction

def rotate(origin, point, angle):
    # source: https://stackoverflow.com/a/34374437
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(round(qx)), int(round(qy))

def part1():
    coord = {'x': 0, 'y': 0}
    for line in data:
        instruction, n = line
        if instruction == 'N':
            coord['y'] += n
        elif instruction == 'S':
            coord['y'] -= n
        elif instruction == 'E':
            coord['x'] += n
        elif instruction == 'W':
            coord['x'] -= n
        elif instruction == 'F':
            facing = direction[0]
            if facing == 'North':
                coord['y'] += n
            elif facing == 'South':
                coord['y'] -= n
            elif facing == 'East':
                coord['x'] += n
            elif facing == 'West':
                coord['x'] -= n
        elif instruction in ['L', 'R']:
            direction = change_direction(instruction, n)
    return abs(coord['x']) + abs(coord['y'])

def part2():
    coord = {'x': 0, 'y': 0}
    waypoint = {'x': 10, 'y': 1}
    for line in data:
        instruction, n = line
        if instruction == 'N':
            waypoint['y'] += n
        elif instruction == 'S':
            waypoint['y'] -= n
        elif instruction == 'E':
            waypoint['x'] += n
        elif instruction == 'W':
            waypoint['x'] -= n
        elif instruction == 'F':
            coord['y'] += waypoint['y'] * n
            coord['x'] += waypoint['x'] * n
        elif instruction in ['L', 'R']:
            if instruction == 'R':
                n = -n
            waypoint['x'], waypoint['y'] = rotate(
                (0, 0), (waypoint['x'], waypoint['y']), math.radians(n)
            )
    return abs(coord['x']) + abs(coord['y'])

print(part1())
print(part2())
