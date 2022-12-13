#!/usr/bin/env python3
"""
"""
x = int(input())
cube = list(map(int, input().split()))
cube.sort()

for i in cube:
    print(i, end=" ")
