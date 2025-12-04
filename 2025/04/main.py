with open("2025/04/input.txt") as f:
    val = f.read().strip().splitlines()

rolls = [list(row) for row in val]
first_counter = 0
counter = 0
check_matrix: "list[tuple[int, int]]" = [
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
]


def can_reach(table: "list[list[str]]", x: int, y: int) -> bool:
    adjacent = 0
    # iterate through every adjacent position
    for dx, dy in check_matrix:
        nx, ny = x + dx, y + dy
        # check if position is inside the list bounds
        if 0 <= nx < len(table[0]) and 0 <= ny < len(table):
            # if it's a roll, increment the adjacent rolls counter
            if table[ny][nx] == "@":
                adjacent += 1
                # return early if there are more than 3 adjacent rolls
                if adjacent > 3:
                    return False
    # no early exit means that there are under 4 rolls (the position is reachable)
    return True


# iterate until nothing can be removed anymore
while True:
    removed = 0
    # remake the inner list to avoid unwanted list changes
    changed = [list(row) for row in rolls]
    for y, row in enumerate(rolls):
        for x, item in enumerate(row):
            # if a roll is reachable, increment counters and remove it
            if rolls[y][x] == "@" and can_reach(rolls, x, y):
                changed[y][x] = "."
                counter += 1
                removed += 1

    rolls = changed

    # challenge 1
    # save the first result
    if first_counter == 0:
        first_counter = counter

    # challenge 2
    # exit if nothing is removed
    if removed == 0:
        break

print("\n".join("".join(row) for row in rolls))
print("challenge 1:", first_counter)
print("challenge 2:", counter)
