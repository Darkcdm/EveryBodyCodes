charMap = []
keyWords = []

with open('input', 'r') as file:
    input = file.read()
    for line in input.split("\n"):
        charMap.append(list(line))  # Convert each line to a list of characters

with open('keys', 'r') as file:
    input = file.read()
    for word in input.split(","):
        keyWords.append(word)

output = [list(row) for row in charMap]  # Create a copy of charMap as lists of lists

def checkMatch(x, y, Vx, Vy, word):
    if len(word) == 0:
        return True
    
    char = word[0]

    if y+Vy > len(charMap)  - 1 or y+Vy < 0:
        return False

    if x+Vx > len(charMap[y]) - 1:
        x = -1

    if charMap[y+Vy][x+Vx] == char:
        if checkMatch(x+Vx, y+Vy, Vx, Vy, word[1:]):
            output[y+Vy][x+Vx] = output[y+Vy][x+Vx].lower()
            return True

    return False


print(charMap)
print(keyWords)

for y in range(len(charMap)):
    for x in range(len(charMap[y])):
        if x == 5 and y == 0:
            print("x", x, "y", y)
        char = charMap[y][x]
        for index in range(len(keyWords)):
                  
            if keyWords[index][0] == char:

                if checkMatch(x, y,1,0, keyWords[index][1:]):


                    output[y][x] = output[y][x].lower()
                
                if checkMatch(x, y,0,1, keyWords[index][1:]):
                    output[y][x] = output[y][x].lower()

                if checkMatch(x, y,-1,0, keyWords[index][1:]):
                    output[y][x] = output[y][x].lower()

                if checkMatch(x, y,0,-1, keyWords[index][1:]):
                    output[y][x] = output[y][x].lower()

# Convert output back to list of strings for printing
output = [''.join(row) for row in output]

print(output)

flattened_output = ''.join(output)
lower_case_count = sum(flattened_output.count(c) for c in set(flattened_output) if c.islower() and not c.isspace() and not c == '\n')
print("Number of lowercase characters in output:", lower_case_count)