#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and not (s[i] >= "A" and s[i] <= "Z"):
    i = i + 1

if i < len(s):
    print(s[i], i)



# i = 0
# s = input()

# while i < len(s) and ("a" <= s[i] and s[i] <= "z" or s[i] == " "):
#   i = i + 1

# if i < len(s) and s[i] != ".":
#   print(s[i], i)
