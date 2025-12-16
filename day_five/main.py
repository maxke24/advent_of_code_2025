ranges_collected = False

counter = 0

def is_in_ranges(num, ranges):
    """Check if a number falls within any of the ranges."""
    for start, end in ranges:
        if start <= num <= end:
            return True
    return False

with open("input.txt") as f:
    ranges = []
    for line in f:
        print(line.strip())
        if line.strip() == "":
            ranges_collected = True
            continue
        if not ranges_collected:
            parts = line.strip().split("-")
            print(parts)

            # Store as (start, end) tuple instead of expanding
            ranges.append((int(parts[0]), int(parts[1])))

        else:
            num = int(line.strip())
            if is_in_ranges(num, ranges):
                print(f'{num} found in ranges')
                counter += 1
            else:
                print(f'{num} not found in ranges')
    print(f"Total ranges: {len(ranges)}")
    print(f"Counter: {counter}")