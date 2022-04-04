#!/usr/bin/env python3

t = 0
x = 1
y = 100
alpha = 0.0001
while t < 1000:
    print(t, x, y)
    t += 1
    tmp = x
    x = x * (1 - y)
    y = alpha * y * (x - 1)
print(f"x = {x}\ny = {y}")