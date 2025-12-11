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