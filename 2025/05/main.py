with open("2025/05/input.txt") as f:
    val = f.read().strip().splitlines()

split_point = val.index('')
ranges, ids = val[:split_point], val[split_point+1:]
valid_ranges = [rg.split('-') for rg in ranges]
valid_ranges = [(int(x[0]), int(x[1])) for x in valid_ranges]

fresh = 0
for item in ids:
    for small, big in valid_ranges:
        item_id = int(item)
        if small < item_id < big:
            fresh += 1
            break

print("challenge 1:", fresh)
