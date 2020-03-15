import hashlib
import random
import string
import time
import statistics

import matplotlib.pyplot as plt
import numpy

correctHash =    "04bb14edf208831df2dcdd7f3cae2448cf818baf2de0cf9b3b0b1a58d3ad584d"
goodEnoughHash = "________________________________________________________________"
stopwatchVector = []
timeResultsMatrix = []
for i in range(64):
    timeResultsMatrix.append([])

random.seed()

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def hash_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def valid(hashValue):
    global timeResultsMatrix
    global stopwatchVector
    for i in range(0, len(goodEnoughHash)):
        if goodEnoughHash[i] == hashValue[i]:
            if i>1:
                print i, time.time() - stopwatchVector[i]
            timeResultsMatrix[i].append(time.time() - stopwatchVector[i])
            stopwatchVector[i] = time.time()
            continue
        if goodEnoughHash[i] == "_":
            continue
        if goodEnoughHash[i] != hashValue[i]:
            return False
    return True

def setGoalHash(goal=4):
    global goodEnoughHash
    hashLength = 64
    goodEnoughHash = "0" * goal + "_" * (hashLength - goal)

startTime = time.time()

def main():
    global stopwatchVector
    stopwatchVector = [time.time()]*64
    nr_of_zeros = 5
    for g in range(1, nr_of_zeros + 1):
        setGoalHash(g)
        toHash = randomString(10)
        while not valid(hash_string(toHash)):
            toHash = randomString(10)

    _x = range(1, nr_of_zeros + 1)
    for i in range(0,4):
        print i, len(timeResultsMatrix[i])
    _y = map(statistics.mean, timeResultsMatrix[:len(_x)])

    fig, ax = plt.subplots()
    ax.grid()
    ax.scatter(_x, _y, color='r')
    ax.set_xlabel('Fixed digits')
    ax.set_ylabel('Time (s)')
    ax.set_title('Time to create specific hash')
    plt.xticks(_x)
    plt.show()


main()
