#!/usr/bin/env python3

i = 0
n = 10
total = 0

while i < n:
  x = int(input())
  if x < 0:
    x = -x
  total = total + x % 10
  i = i + 1

print(total)
