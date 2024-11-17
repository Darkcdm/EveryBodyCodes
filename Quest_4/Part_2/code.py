input_string = ""
with open('/home/duser/EveryBodyCodes/Quest_4/Part_2/input', 'r') as file:
    input_string = file.read()


input_data = input_string.split('\n')

input_data = list(map(lambda x: int(x), input_data))

lowest = min(input_data)


strike_count = 0

for nail in input_data:
    strike_count += int(nail) - int(lowest)
    
    
print(strike_count)