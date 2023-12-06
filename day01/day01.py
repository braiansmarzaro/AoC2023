import matplotlib.pyplot as plt
with open('day01/input.txt') as f:  # Opens the file and get rid of '\n'
    data = f.read().split()

# For every line, filters all valid digit and links first and last into a number and sums all of them. Doesn't crash to single number lines.
'''total = 0
for line in data:
    valid_nums = [x for x in line if x.isdigit()]
    num = int(valid_nums[0]+valid_nums[-1])
    total += num
print(total)
'''

# Part 2
digit_names = {'zero': 'z0o',
               'one': 'o1e',
               'two': 't2o',
               'three': 't3e',
               'four': 'f4r',
               'five': 'f5e',
               'six': 's6x',
               'seven': 's7n',
               'eight': 'e8t',
               'nine': 'n9e'}

new_data = []
for line in data:
    for k,v in digit_names.items():
        line = line.replace(k,v)
    new_data.append(line)

total = 0
for line in new_data:
    print(line)
    valid_nums = [x for x in line if x.isdigit()]
    num = int(valid_nums[0]+valid_nums[-1])
    total += num
print(total)