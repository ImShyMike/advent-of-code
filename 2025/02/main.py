with open("2025/02/input.txt") as f:
    val = f.read().strip()

invalid_ids: "list[str]" = [] # challenge 1
full_invalid_ids: "list[str]" = [] # challenge 2

# split into ID ranges
for id_range in val.split(","):
    # get the start and end for each range
    start, end = id_range.split("-")
    
    for value in range(int(start), int(end)+1):
        value = str(value)
        size = len(value)

        # challenge 1
        # if the first half is equal to the second half, it's invalid
        if value[0:size//2] == value[size//2:size]:
            invalid_ids.append(value)

        # challenge 2
        # iterate over half the lenth of the ID
        for n in range(1, size//2+1):
            # divide the ID by n-sized chunks
            parts = [value[i:i+n] for i in range(0, size, n)]
            
            # iterate over every chunk
            for part in parts:
                # sequence check (iterate over every number and break if the previous number != current number - 1)
                prev = int(part[0])
                for x in part[1:]:
                    if prev != int(x)-1:
                        break
                    prev = int(x)
                
                # if the size if a list is 1 after being turned into a set then all of it's items are equal
                if len(set(parts)) == 1:
                    # this is an invalid ID, store it
                    full_invalid_ids.append(value)
                    break

            else: # if the loop wasn't broken, continue
                continue
            break # otherwise, stop checking this ID

# turn all items in the list into integers and print the total sum
print("challenge 1:", sum([int(i) for i in invalid_ids]))
print("challenge 2:", sum([int(i) for i in full_invalid_ids]))
