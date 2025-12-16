total = 0
with open("input.txt") as f:
    for line in f:
        highest = 0
        int_list = [int(x) for x in line.strip()]
        for i, i_val in enumerate(int_list):
            for j, j_val in enumerate(int_list):
                if i < j:
                    if i_val*10 + j_val > highest:
                        highest = i_val*10 + j_val
        total += highest
print(total)

with open("input.txt") as f:
    total = 0
    target_length = 12
    
    for line in f:
        line = line.strip()
        if not line: continue # Skip empty lines
        
        # Calculate how many digits we MUST remove
        drops_needed = len(line) - target_length
        
        # If the number is already too short, skip or handle accordingly
        if drops_needed < 0:
            print(f"Skipping line: too short ({len(line)} digits)")
            continue

        stack = []
        
        for digit in line:
            num = int(digit)
            
            # While we have a stack, the top of the stack is smaller than current number,
            # and we still have "drops" available: Pop the stack.
            while stack and stack[-1] < num and drops_needed > 0:
                stack.pop()
                drops_needed -= 1
            
            stack.append(num)
        
        # If we finished the loop but still have drops left (e.g., input was "54321"),
        # we just cut off the end.
        final_sequence = stack[:target_length]
        
        # Join and add to total
        total += int("".join(map(str, final_sequence)))

    print(total)