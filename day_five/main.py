ranges_collected = False

counter = 0

def is_in_ranges(num, ranges):
    """Check if a number falls within any of the ranges."""
    for start, end in ranges:
        if start <= num <= end:
            return True
    return False

def merge_ranges(ranges):
    """Merge overlapping ranges and return the merged list."""
    if not ranges:
        return []

    # Sort ranges by start position
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]

    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]

        # Check if current range overlaps with the last merged range
        if current_start <= last_end + 1:
            # Merge by extending the end if necessary
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            # No overlap, add as new range
            merged.append((current_start, current_end))

    return merged

with open("input.txt") as f:
    ranges = []
    for line in f:
        print(line.strip())
        if line.strip() == "":
            ranges_collected = True
            continue
        if not ranges_collected:
            parts = line.strip().split("-")

            # Store as (start, end) tuple instead of expanding
            ranges.append((int(parts[0]), int(parts[1])))

        else:
            num = int(line.strip())
            if is_in_ranges(num, ranges):
                counter += 1
    print(f"Total ranges: {len(ranges)}")
    print(f"Counter: {counter}")

    # Merge overlapping ranges and calculate total unique numbers
    merged_ranges = merge_ranges(ranges)
    total_numbers = sum(end - start + 1 for start, end in merged_ranges)
    print(f"Total numbers in all ranges (accounting for overlaps): {total_numbers}")
    print(f"Original ranges: {len(ranges)}, Merged ranges: {len(merged_ranges)}")