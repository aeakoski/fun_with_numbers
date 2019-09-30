#!/usr/bin/python

import sys
import random
import tqdm
import numpy as np
import matplotlib.pyplot as plt

from permut import *

class Experiment():
    def __init__(self, b):
        self.bit_length = b
        self.key = random.randint(0,2**self.bit_length +1)
    def incremental(self):
        return self.key
    def randomness(self):
        c = 0
        while True:
            c += 1
            if random.randint(0,2**self.bit_length +1) == self.key:
                return c
    def smart_random_tries(self):
        c = 0
        onces = (self.bit_length/2)
        zeros = (self.bit_length-onces)
        g = ["1"]*onces + ["0"]*zeros
        a = list(perm_unique(g))
        for l in a:
            c +=1
            if int("".join(l), 2) == self.key:
                return c
        for i in range(1, self.bit_length/2+1):
            onces = (self.bit_length/2 - i)
            zeros = (self.bit_length-onces)
            g = ["1"]*onces + ["0"]*zeros
            a = list(perm_unique(g))
            for l in a:
                c +=1
                if int("".join(l), 2) == self.key:
                    return c
            onces = (self.bit_length/2 + i)
            zeros = (self.bit_length-onces)
            g = ["1"]*onces + ["0"]*zeros
            a = list(perm_unique(g))
            for l in a:
                c +=1
                if int("".join(l), 2) == self.key:
                    return c

bits = sys.argv[1]
print("Bits: " + str(bits))
print("Max value: " + str(2**int(bits)))
no_of_tries = 10

increment_tries = []
random_tries = []
smart_tries = []
for i in tqdm.tqdm(range(no_of_tries)):
    e = Experiment(int(bits))
    increment_tries.append(e.incremental())
    random_tries.append(e.randomness())
    smart_tries.append(e.smart_random_tries())

plt.title("Number of tries for a sucesfull brute force\naccording to different methods")
plt.xlabel("Methods")
plt.ylabel("No. of tries")
plt.ylim(0, 100000)

my_xticks = ['Incremental guess','Random guess','Smart random guess']
plt.xticks([1,2,3], my_xticks, rotation=45)
plt.violinplot(increment_tries, [1], showmeans = True, showextrema = True)
plt.violinplot(random_tries, [2], showmeans = True, showextrema = True)
plt.violinplot(smart_tries, [3], showmeans = True, showextrema = True)

# Create line for average value
iy = sum(increment_tries)/len(increment_tries)
ry = sum(random_tries)/len(random_tries)
sy = sum(smart_tries)/len(smart_tries)
plt.plot(range(0,5),[iy]*5, alpha=0.5, color="lightblue")
plt.plot(range(0,5),[ry]*5, alpha=0.5, color="orange")
plt.plot(range(0,5),[sy]*5, alpha=0.3, color="green")

plt.scatter([1]*len(increment_tries), increment_tries)
plt.scatter([2]*len(random_tries), random_tries)
plt.scatter([3]*len(smart_tries), smart_tries)

plt.tight_layout()
plt.show()

# Run with input-parameter equal to the number of bits you want to run the guessing experiment on
# main.py 16 guesses an integer 2^16
# Argument needs to be a positive integer
