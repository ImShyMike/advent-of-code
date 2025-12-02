with open("2025/01/input.txt") as f:
    val = f.read().strip()
moves = val.split("\n")

dial = 50 # start the dial at 50

password1 = 0 # challenge 1
password2 = 0 # challenge 2

# iterate over every move
for move in moves:
    dir = move[0] # direction (L/R)
    n = int(move[1:]) # # number of rotations
    
    # i hate this but im way too sleepy to think of
    # how to do this with math so a for loop it is
    # (rotate the dial n times)
    for _ in range(n):
        # increase or decrease based on L/R
        if dir == "R":
            dial += 1
        elif dir == "L":
            dial -= 1
        
        # overflow the value
        dial %= 100
        
        # if the dial passes 0, increment the password2
        if dial == 0:
            password2 += 1
    
    # if the dial lands on 0, increment the password1
    if dial == 0:
        password1 += 1

print("challenge 1:", password1)
print("challenge 2:", password2)
