#!/usr/bin/env python3
"""
Little Petya loves presents. His mum bought him two strings of the same size for his birthday. The strings consist of uppercase and lowercase Latin letters. Now Petya wants to compare those two strings lexicographically. The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter. Help Petya perform the comparison.
Input

Each of the first two lines contains a bought string. The strings' lengths range from 1 to 100 inclusive. It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.
Output

If the first string is less than the second one, print "-1". If the second string is less than the first one, print "1". If the strings are equal, print "0". Note that the letters' case is not taken into consideration when the strings are compared.
"""

firstInput = input().lower()
secondInput = input().lower()

firstLast = ""
secondLast = ""

if len(firstInput) >= len(secondInput):
    n = len(firstInput)
else:
    n = len(secondInput)

for i in range(n):
    if firstInput[i] != secondInput[i]:
        firstLast = firstInput[i]
        secondLast = secondInput[i]
        break

        
if firstLast == "":
    firstLast = firstInput[-1]
if secondLast == "":
    secondLast = secondInput[-1]

if len(firstInput) > len(secondInput) or firstLast > secondLast:
    print(1)
elif len(firstInput) < len(secondInput) or firstLast < secondLast:
    print(-1)
else:
    print(0)