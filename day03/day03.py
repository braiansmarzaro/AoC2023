import numpy as np
import pandas as pd

with open('day03/input.txt') as f:
    data = f.read().strip().split()
    data = np.array([list(x) for x in data])

def check_numbers(index, pos, mat=data):
    seen_digit:list[int,int] = []

    """Check surrounding numbers around the signal

    Args:
        index (_type_): _description_
        pos (_type_): _description_
        mat (_type_, optional): _description_. Defaults to data.
    """
    def get_number(row, col):
        """From a found digit, get the whole number"""
        number = []
        i = 1
        predecessor = mat[row][col-i]
        while predecessor.isdigit() and [row,col-i] not in seen_digit:
            number.insert(0, predecessor)
            seen_digit.append([row,col-i])
            i += 1
            predecessor = mat[row][col-i]

        if [row,col] not in seen_digit:
            number.append(mat[row][col])
            seen_digit.append([row,col])

        i = 1
        sucessor = mat[row][col+i]
        while sucessor.isdigit() and [row,col+i] not in seen_digit:
            number.append(sucessor)
            seen_digit.append([row,col+i])

            i += 1
            if col+i >= len(mat[0]):
                break
            sucessor = mat[row][col+i]
        print(number)
        if number:
            return int(''.join(number))
        return 0

    total = 0
    for row in range(index-1, index+2):
        for col in range(pos-1, pos+2):
            if row == index and col == pos:
                continue
            if row >= len(mat) or col >= len(mat[0]):
                continue

            if mat[row][col].isdigit():
                num = get_number(row, col)
                total += num
                #print(mat[row][col])
    return total


# Para cada elemento que não é ponto ou número, olha em volta se tem números
total = 0
for index, line in enumerate(data):
    for pos, character in enumerate(line):
        if character == '.' or character.isdigit():
            continue
        
        total += check_numbers(index, pos)

r, l =22,12
print(total)

