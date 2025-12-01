dial = 50
with open("2025/01/input.txt") as f:
    val = f.read().strip()
password = 0
items = val.split("\n")

for item in items:
    dir = item[0]
    num = int(item[1:])
    
    # i hate this but im way too sleepy to think of
    # how to do this with math so a for loop it is
    for _ in range(num):
        if dir == "R":
            dial += 1
        elif dir == "L":
            dial -= 1
        
        dial %= 100
        
        if dial == 0:
            password += 1

print("password:", password)