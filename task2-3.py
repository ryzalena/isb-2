import math
import numpy as np
from numbers import pseudorandom, number

M = 8
count = number/M
sequences = np.array_split(pseudorandom, count)
for i in sequences:
    print(list(i))

# 01001100 - 2
# 01100111 - 3
# 10111100 - 4
# 00101111 - 4
# 11011111 - 5
# 00100000 - 1
# 01010110 - 2
# 01101101 - 2
# 00101010 - 1
# 10101100 - 2
# 01111111 - 7
# 10110101 - 2
# 10111111 - 6
# 10111100 - 4
# 11100110 - 3
# 01101000 - 2

v1 = (2) # <= 1
v2 = (6) #  = 2
v3 = (2) #  = 3
v4 = (6) # >= 4

X_2 = 4.37592
P = 0.22362858
