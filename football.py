#!/usr/bin/env python3
"""
"""
listInput = []
listInput[:] = input()
zeroCount = 0
oneCount = 0
dangrous = False
for i in range(len(listInput) - 1):
    if listInput[i] == '0':
        if listInput[i + 1] == '1' and zeroCount == 7:
            dangrous = True
            break
        if listInput[i + 1] == '1' and zeroCount < 7:
            zeroCount = 0
        else:
            zeroCount += 1
            continue
    if listInput[i] == "1":
        
        if listInput[i + 1] == '0' and oneCount == 7:
            dangrous = True
            break
        if listInput[i + 1] == '0' and oneCount < 7:
            oneCount = 0
        else:
            oneCount += 1
            continue
if dangrous == True:
    print("YES")
else:
    print("NO")