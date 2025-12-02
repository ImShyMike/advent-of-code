dial = 50
with open("2025/01/input.txt") as f:
    val = f.read().strip()
password1 = 0
password2 = 0
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
            password2 += 1
    
    if dial == 0:
        password1 += 1

print(f"challenge 1: {password1} - challenge 2: {password2}")