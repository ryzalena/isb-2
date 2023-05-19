import math
from numbers import pseudorandom, number

pseudorandom1 = pseudorandom
pseudorandom2 = []

for i in pseudorandom:
    if i == 1:
        pseudorandom2.append(i)
    elif i == 0:
        pseudorandom2.append(-1)

S = sum(pseudorandom2)/math.sqrt(number)
print(S) #1.7677669529663687
P = math.erfc(S/math.sqrt(2))
print(P) #0.07709987174354183