import os, math

file_path = os.path.dirname(os.path.abspath(__file__))

input_string = ""
with open(f'{file_path}/input', 'r') as file:
    input_string = file.read()


input_data = input_string.split('\n')

input_data = list(map(lambda x: int(x), input_data))


min_value = min(input_data)
max_value = max(input_data)




strike_count = float('inf')

    
for test_value in range(min_value, max_value + 1):
    strike = 0
    for nail in input_data:
        if nail < test_value:
            strike += test_value - nail
        elif nail > test_value:
            strike += nail - test_value



    if strike < strike_count:
        strike_count = strike


print(strike_count)