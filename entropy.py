#!/usr/bin/env python3
import random
import time
from decimal import Decimal

n = 6

initial_entropy = [[0 for col in range(n)] for row in range(n)]

print("Number of bits is {} and the possible combinations are {:e}".format(n*n, Decimal(2**(n*n))))

while True:

    final_entropy = [[random.getrandbits(1)  for col in range(n)] for row in range(n)]

    if initial_entropy == final_entropy:
        print("entropy decreased!")
        break

    for row in final_entropy:
        print (row)
  
    print("\r")
    time.sleep(3)
