with open('input.txt') as f: # Opens the file and get rid of '\n'
    data = f.read().split()

# For every line, filters all valid digit and links first and last into a number and sums all of them. Doesn't crash to single number lines.
total = 0
for line in data:
    valid_nums = [x for x in line if x.isdigit()]
    num = int(valid_nums[0]+valid_nums[-1])
    total+=num

print(total)