dial = 50
zero_count = 0
i = 0

with open("input.txt") as f:
    for x in f:
        print(dial, x[0], int(x[1:]))
        direction = x[0]
        distance = int(x[1:])
        if direction == 'L':
            dial = (dial - distance + 100) % 100
        if direction == 'R':
            dial = (dial + distance) % 100

        print(dial)
        if dial == 0:
            zero_count += 1

print(zero_count)