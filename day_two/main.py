total_invalid_ids = 0

with open("input.txt") as f:
    for line in f:
        ids = line.strip().split(',')
        for id in ids:
            print(id)
            start_id, stop_id = id.split('-')
            for i in range(int(start_id), int(stop_id) + 1):
                s = str(i)
                id_length = len(str(i))
                is_invalid = False
                for j in range(1, id_length//2 + 1):
                    if id_length % j != 0:
                        continue
                    comp = s[:j]

                    if comp * (id_length // j) == s:
                        print(f"Invalid ID found: {i}")
                        total_invalid_ids += i
                        break
print(total_invalid_ids)