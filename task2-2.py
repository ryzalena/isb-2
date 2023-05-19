import math
from numbers import pseudorandom, number

percentage = (1/number)*sum(pseudorandom)
print(percentage) #0.578125

left = percentage - 0.5
print(left) #0.078125

right = 2/math.sqrt(number)
print(right) #0.17677669529663687

if left < right:
    count = 0
    for i in range(len(pseudorandom)-1):
        if(pseudorandom[i]!=pseudorandom[i+1]):
            count += 1
    print(count) #62

    top = count-(2*number*percentage*(1-percentage))
    if top < 0:
        top *= -1
    bottom = 2*math.sqrt(2*number)*percentage*(1-percentage)
    P = math.erfc(top/bottom)
else:
    P = 0
print(P) #0.9368137041187848