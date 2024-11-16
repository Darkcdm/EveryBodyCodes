
class Block:
    height = 0
    mineable = False

    def __init__(self, height:int = 0, mineable:bool = False) -> None:
        self.height = height
        self.mineable = mineable

def calculate_mined_max(game_map) -> int:
    minedBlocks = 0

    for y in range(len(game_map)):
        for x in range(len(game_map[y])):
            block = game_map[y][x]
            if block.mineable:
                if (game_map[y][x-1].height >= block.height and\
                    game_map[y][x+1].height >= block.height and\
                    game_map[y-1][x].height >= block.height and\
                    game_map[y+1][x].height >= block.height and\
                    game_map[y+1][x+1].height >= block.height and\
                    game_map[y+1][x-1].height >= block.height and\
                    game_map[y-1][x+1].height >= block.height and\
                    game_map[y-1][x-1].height >= block.height):

                    block.height += 1

                    minedBlocks += 1

    if minedBlocks == 0:
        return minedBlocks
    else:
        return minedBlocks + calculate_mined_max(game_map)







game_map = []

input_data = ""
with open('/home/duser/code/EveryBodyCodes/Quest_3/Part_1/input', 'r') as file:
    input_data = file.read()


for line in input_data.split('\n'):
    map_line = []

    for char in line:
        if char == '#':
            map_line.append(Block(0, True))
        elif char == '.':
            map_line.append(Block(0, False))
        else:
            raise ValueError('Invalid character')

    game_map.append(map_line)

    # Add a non-mineable border around the game_map
    width = len(game_map[0])
    height = len(game_map)

    # Add top and bottom borders
    game_map.insert(0, [Block(0, False)] * width)
    game_map.append([Block(0, False)] * width)

    # Add left and right borders
    for row in game_map:
        row.insert(0, Block(0, False))
        row.append(Block(0, False))
        
result = calculate_mined_max(game_map)

for y in range(len(game_map)):
    for x in range(len(game_map[y])):
        print(game_map[y][x].height, end=" ")
    print()

print(result)   