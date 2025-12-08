with open("2025/06/input.txt") as f:
    raw_lines = f.read().splitlines()

line_width = max(len(line) for line in raw_lines)
rows = [line.ljust(line_width) for line in raw_lines]
ops_row = rows[-1]
grid_rows = rows[:-1]

col_starts = [idx for idx, ch in enumerate(ops_row) if ch in {"+", "*"}]
col_starts.append(line_width)

remade_cols: list[tuple[list[str], str]] = []
for idx, start in enumerate(col_starts[:-1]):
    end = col_starts[idx + 1]
    if start == end:
        continue

    column_slices = [row[start:end] for row in grid_rows]
    numbers: list[str] = []

    for char_idx in range(end - start - 1, -1, -1):
        digits = "".join(
            slice_[char_idx]
            for slice_ in column_slices
            if slice_[char_idx].isdigit()
        )
        if digits:
            numbers.append(digits)

    remade_cols.append((numbers, ops_row[start]))

print("final:")

result = 0
for numbers, op in reversed(remade_cols):
    if op == "+":
        val = sum(int(num) for num in numbers)
    elif op == "*":
        val = 1
        for num in numbers:
            val *= int(num)
    else:
        val = 0

    print(op, numbers, val)
    result += val

print("\nchallenge 2:", result)
