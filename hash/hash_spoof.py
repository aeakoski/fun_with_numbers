import hashlib
import random
import string
import time
import statistics

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

correctHash =    "04bb14edf208831df2dcdd7f3cae2448cf818baf2de0cf9b3b0b1a58d3ad584d"
goodEnoughHash = "________________________________________________________________"

random.seed()

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def valid(hashValue):
    global results
    global startTime

    for i in range(len(goodEnoughHash)):
        if goodEnoughHash[i] == hashValue[i]:
            results[i+1].append(time.time() - startTime)
        if goodEnoughHash[i] == "_":
            continue
        if goodEnoughHash[i] != hashValue[i]:
            return False
    return True

def setGoal(goal=4):
    global goodEnoughHash
    hashLength = 64
    goodEnoughHash = "0" * goal + "_" * (hashLength - goal)

startTime = time.time()

results = {}

def main():
    global results
    nr_of_zeros = 6
    results = [[]]*nr_of_zeros
    results[0].append(0)
    for g in range(1,nr_of_zeros):
        startTime = time.time()

        results[g] = []

        setGoal(g)
        toHash = randomString(10)
        while not valid(encrypt_string(toHash)):
            toHash = randomString(10)

        print toHash
        print encrypt_string(toHash)
        print goodEnoughHash
        print("%s" % (time.time() - startTime))
        print ""

    _x = range(0, nr_of_zeros)
    _y = map(statistics.mean, results)
    print results
    print _y
    fig, ax = plt.subplots()
    ax.grid()
    ax.scatter(_x, _y, color='r')
    ax.set_xlabel('Fixed digits')
    ax.set_ylabel('Time')
    ax.set_title('Time to create specific hash')
    plt.show()


main()
