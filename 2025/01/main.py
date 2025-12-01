dial = 50
with open("2025/01/input.txt") as f:
    val = f.read().strip()
password = 0
items = val.split("\n")

for item in items:
    dir = item[0]
    num = int(item[1:])
    
    if dir == "R":
        dial += num
    elif dir == "L":
        dial -= num

    if dial % 100 == 0:
        password += 1

print("password:", password)