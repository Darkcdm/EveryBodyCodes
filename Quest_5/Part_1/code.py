import os


def dance():
    pass



file_path = os.path.dirname(os.path.abspath(__file__))
DANCEROUNDS = 4


input_string = ""
with open(f'{file_path}/input', 'r') as file:
    input_string = file.read()




danceFloor = []


for index, y in enumerate(input_string.split("\n")):
    if len(danceFloor) <= index:
        danceFloor.append([])
    for x in y.split():
        danceFloor[index].append(int(x))
        


dancerIndex = 0
for round in range(DANCEROUNDS):
    if dancerIndex >= len(danceFloor):
        dancerIndex = 0

    dancerCollum = danceFloor[dancerIndex]
    dancer = dancerCollum[0]
    newDancerCollum = danceFloor[-len(danceFloor) + 1 + dancerIndex]


    div =  len(newDancerCollum) / dancer
    mod =  dancer % len(newDancerCollum) 

    print(f"Dancer:{dancer} CollLen:{len(newDancerCollum)} Div: {div} Mod: {mod}")


    dancerIndex += 1