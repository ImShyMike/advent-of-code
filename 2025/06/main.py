with open("2025/06/input.txt") as f:
    val = f.read().strip().splitlines()

cols: "list[list[str]]" = []
for row in val:
    row_items = [i for i in row.split(" ") if i not in ("", " ")]
    if cols == []:
        for _ in range(len(row_items)):
            cols.append([])
    for n, i in enumerate(row_items):
        cols[n].append(i)

result = 0
for col in cols:
    op = col[-1]
    nums = col[:-1]
    print(op, nums)

    if op == "+":
        val = sum([int(i) for i in nums])
    elif op == "*":
        val = 1
        for i in nums:
            val *= int(i)
    else:
        val = 0
    result += val

print("\nchallenge 1:", result)
