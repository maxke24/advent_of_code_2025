with open("input.txt") as f:
    grid = [list(line.strip()) for line in f if line.strip()]
    total = 0
    print(grid)
    for row in range(len(grid)):
        for cell, value in enumerate(grid[row]):
            print(f"Row {row} Cell {cell} Value {value}")
            adjacent_values = []
            for direction in [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]:
                x = row + direction[0]
                y = cell + direction[1]
                if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                    print(f"  Direction {direction} goes out of bounds")
                    continue
                adjacent_values.append(grid[x][y])
                print(f"  Direction {direction} has value {grid[x][y]}")
            print(f"  Adjacent values: {adjacent_values}")
            symbol = "@"
            count = adjacent_values.count(symbol)
            print(f"  Count of '{symbol}': {count}")
            if count < 4 and value == symbol:
                total += 1
    print(total)