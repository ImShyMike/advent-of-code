with open("2025/05/input.txt") as f:
    val = f.read().strip().splitlines()

split_point = val.index('')
ranges = val[:split_point]

def merge_ranges(values: "list[tuple[int, int]]") -> "list[tuple[int, int]]":
    sorted_ranges = sorted(values, key=lambda pair: pair[0])
    if not sorted_ranges:
        return []

    merged: "list[tuple[int, int]]" = [sorted_ranges[0]]
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged

valid_ranges: "list[tuple[int, int]]" = []
for rg in ranges:
    start, end = rg.split('-')
    valid_ranges.append((int(start), int(end)))

merged_ranges = merge_ranges(valid_ranges)
print("merged:", merged_ranges)
total = sum(end - start + 1 for start, end in merged_ranges)

print("challenge 2:", total)
