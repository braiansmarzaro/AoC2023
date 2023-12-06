with open('day04/input.txt') as f:
    data = f.read().strip().split('\n')

def part1():
    total = 0
    for l in data:
        card, nums = l.split(':')
        winning_nums, my_nums = nums.split('|')
        winning_nums = set(map(int, winning_nums.split()))
        my_nums = set(map(int, my_nums.split()))
        print(my_nums)
        intersection = (my_nums.intersection(winning_nums))
        print(intersection)
        points = 2**(len(intersection)-1) if intersection else 0
        print(points)
        total += points

    print(total)

# Part 2
def part2():
    copies = {x:1 for x in range(1,len(data)+1)}
    for index,l in enumerate(data[:]):
        card, nums = l.split(':')
        card = int(card.split()[1])
        winning_nums, my_nums = nums.split('|')
        winning_nums = set(map(int, winning_nums.split()))
        my_nums = set(map(int, my_nums.split()))
        intersection = (my_nums.intersection(winning_nums))
        new_cards = len(intersection)
        for c in range(index+1,index+1+new_cards):
            copies[c+1]+=copies[index+1]
    print(sum(copies.values()))

part2()