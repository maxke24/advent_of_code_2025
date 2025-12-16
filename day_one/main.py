from math import floor

dial = 50
zero_count = 0

with open("input.txt") as f:
    for x in f:
        direction = x[0]
        distance = int(x[1:])
        if direction == 'L':
            dial = (dial - distance + 100) % 100
        if direction == 'R':
            dial = (dial + distance) % 100

        if dial == 0:
            zero_count += 1

dial = 50
zero_pass = 0

with open("input.txt") as f:
    for line in f:

        direction = line[0]
        distance = int(line[1:])

        step = -1 if direction == 'L' else 1

        # walk one unit at a time
        for _ in range(distance):
            dial = (dial + step) % 100  # wrap 0–99
            if dial == 0:
                zero_pass += 1

print(zero_count, zero_pass)