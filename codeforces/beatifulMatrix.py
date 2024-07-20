#!/usr/bin/env python3
"""
You've got a 5 × 5 matrix, consisting of 24 zeroes and a single number one. Let's index the matrix rows by numbers from 1 to 5 from top to bottom, let's index the matrix columns by numbers from 1 to 5 from left to right. In one move, you are allowed to apply one of the two following transformations to the matrix:

    Swap two neighboring matrix rows, that is, rows with indexes i and i + 1 for some integer i (1 ≤ i < 5).
    Swap two neighboring matrix columns, that is, columns with indexes j and j + 1 for some integer j (1 ≤ j < 5). 

You think that a matrix looks beautiful, if the single number one of the matrix is located in its middle (in the cell that is on the intersection of the third row and the third column). Count the minimum number of moves needed to make the matrix beautiful.
Input

The input consists of five lines, each line contains five integers: the j-th integer in the i-th line of the input represents the element of the matrix that is located on the intersection of the i-th row and the j-th column. It is guaranteed that the matrix consists of 24 zeroes and a single number one.
Output

Print a single integer — the minimum number of moves needed to make the matrix beautiful.
"""

matrix = []
matrixList = []
for _ in range(5):
    matrix.append(input().split())

for j in range(5):
    for i in range(5):
        matrixList.append(matrix[j][i])
index = matrixList.index("1")

listIndex = index % 5
subIndex = index // 5

if listIndex >= 2:
    listMove = listIndex - 2
else:
    listMove = 2 - listIndex

if subIndex >= 2:
    subMove = subIndex - 2
else:
    subMove = 2 - subIndex

print(listMove + subMove)
