with open('input08.txt') as f:
    data = f.read().splitlines()

nops = [data.index(i) for i in data if 'nop' in i]
jmps = [data.index(i) for i in data if 'jmp' in i]

def solve(ins1=None, ins2=None, li=[0], part1=False):
    for n in li:
        ip = 0
        accumulator = 0
        seen_instructions = list()

        test_data = data[:]
        if not part1:
            test_data[n] = test_data[n].replace(ins1, ins2)

        for x in range(len(test_data)*2):
            if ip == len(test_data):
                return accumulator

            line = test_data[ip]
            if part1 and (ip, line) in seen_instructions:
                return accumulator
            seen_instructions.append((ip, line))

            ins, val = line.split()
            if ins == 'jmp':
                ip += int(val)
                continue
            elif ins == 'acc':
                accumulator += int(val)
            ip += 1

print(solve(part1=True))
print(solve(ins1='nop', ins2='jmp', li=nops) or solve(ins1='jmp', ins2='nop', li=jmps))
