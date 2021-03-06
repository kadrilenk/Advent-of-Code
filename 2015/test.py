import numpy as np

x = 123
y = 456
d = x & y
e = x | y
f = x << 2
g = y >> 2
h = ~x + 65536
i = ~y + 65536

print("d:", d)
print("e:", e)
print("f:", f)
print("g:", g)
print("h:", h)
print("i:", i)
print("x:", x)
print("y:", y)