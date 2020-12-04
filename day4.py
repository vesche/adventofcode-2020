    with open('input4.txt') as f:
        data = [i.split('\n') for i in f.read().split('\n\n')]

    fields = {'byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'}

    def check(k, v):
        if k == 'byr':
            return 1920 <= int(v) <= 2002
        elif k == 'iyr':
            return 2010 <= int(v) <= 2020
        elif k == 'eyr':
            return 2020 <= int(v) <= 2030
        elif k == 'hgt':
            if v.endswith('cm'):
                return 150 <= int(v.rstrip('cm')) <= 193
            elif v.endswith('in'):
                return 59 <= int(v.rstrip('in')) <= 76
        elif k == 'hcl':
            if v.startswith('#'):
                v = v.lstrip('#')
                return len(''.join([c for c in v if c in '0123456789abcdef'])) == 6
        elif k == 'ecl':
            return v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif k == 'pid':
            return len(v) == 9
        return False

    def solve(part1=True):
        valid = 0
        for pairs in [' '.join(chunk).split() for chunk in data]:
            passport = set()
            for k, v in [pair.split(':') for pair in pairs]:
                if part1 or check(k, v):
                    passport.add(k)
            if 'cid' in passport:
                passport.remove('cid')
            if passport == fields:
                valid += 1
        return valid

    print(solve())
    print(solve(part1=False))
