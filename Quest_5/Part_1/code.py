import os

file_path = os.path.dirname(os.path.abspath(__file__))

input_string = ""
with open(f'{file_path}/input', 'r') as file:
    input_string = file.read()


danceFloor = []


for y in input_string.split("\n"):
    line = []
    for x in y.split():
        line.append(int(x))
        
    danceFloor.append(line)
    
