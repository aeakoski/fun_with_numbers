from tkinter import *
from tqdm import *

nonPrimeColor = "#090912"
primeColor = "#4855A9"
significantLineColor = "#8DA0C4"
canvasSide = 1000
DIRECTIONS = ["right", "up", "left", "down"]
TIME_TO_INCREADE_DISTANCE = False

def is_prime(n):

    """
    Just something i shalesly copy pasted form stackoverflow
    """
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6.
    f = 5
    while f <= r:
        #print('\t',f)
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True

def takeTheNextStep(coordinates, lastDirection, distanceTraveled, nextTurnDistance, lastTraveledLeg):
    """
        takeNextStep() takes the next step in the ulam spiral in the current direction. After a step has been performed,
        the function calculates if it is time to turn in any direction in order to stay on the right track.

        In order to take a step we need to keep track of where we have been, what direction we traveled and where to turn next
    """
    global DIRECTIONS
    global TIME_TO_INCREADE_DISTANCE

    if lastDirection[0] == "right":
        coordinates = (coordinates[0]+1, coordinates[1])
    elif lastDirection[0] == "up":
        coordinates = (coordinates[0], coordinates[1]+1)
    elif lastDirection[0] == "left":
        coordinates = (coordinates[0]-1, coordinates[1])
    elif lastDirection[0] == "down":
        coordinates = (coordinates[0], coordinates[1]-1)

    if distanceTraveled == nextTurnDistance:
        if lastDirection[0] == "down":
            lastDirection[0] = "right"
        else:
            lastDirection.insert(0, DIRECTIONS[DIRECTIONS.index(lastDirection[0])+1])
            lastDirection.pop()
        if TIME_TO_INCREADE_DISTANCE:
            lastTraveledLeg +=1
        nextTurnDistance += lastTraveledLeg
        TIME_TO_INCREADE_DISTANCE = not TIME_TO_INCREADE_DISTANCE

    return (coordinates, lastDirection, nextTurnDistance, lastTraveledLeg)

class Line:
    """
        We create lines y = kx + m for k = 1 and k = -1 for all m where m is a whole numer. I.e all diagonal lines on the canvas.
        This so that we later can go through all the diagonal lines to see if they contain an unusual amount of primes or not.
    """
    def __init__(self, m, isPositive):
        self.m = m,
        self.isPositive = isPositive
        self.allCount = 0
        self.primeCoords = []
    def addPoint(self, point, isPrime):
        if isPrime:
            self.primeCoords.append(point)
        self.allCount += 1
    def isSpecial(self):
        ## Does the line instance contain unusually many primes?
        if (float(len(self.primeCoords)) / float(self.allCount)) > 0.27:
            return True
        else:
            return False

def addPointToLineCounter(coordinates, isPrime):
    """
        Add the point located at the coordinate to the two possible diagonal lines it can be part of.
        If a linedoes not exist for a specific point, then thet line is created.
    """
    global positiveLines
    global negativeLines
    try:
        positiveLines[coordinates[1]-coordinates[0]].addPoint((coordinates[0], coordinates[1]), isPrime)
    except KeyError:
        positiveLines[coordinates[1]-coordinates[0]] = Line(coordinates[1]-coordinates[0], True)
        positiveLines[coordinates[1]-coordinates[0]].addPoint((coordinates[0], coordinates[1]), isPrime)

    try:
        negativeLines[coordinates[1]+coordinates[0]].addPoint((coordinates[0], coordinates[1]), isPrime)
    except KeyError:
        negativeLines[coordinates[1]+coordinates[0]] = Line(coordinates[1]+coordinates[0], False)
        negativeLines[coordinates[1]+coordinates[0]].addPoint((coordinates[0], coordinates[1]), isPrime)


master = Tk()
w = Canvas(master,
           width=canvasSide,
           height=canvasSide)
w.pack()

"""
    The first two steps are preformed manually since they dont quite follow the same algorithm as the rest of the steps in the speiral does.
    After the steps has been taken, prepare the differnt step parameters for further steps into the spiral.
"""
currentPosition = (int(canvasSide / 2), int(canvasSide / 2))
w.create_line(currentPosition[0], currentPosition[1], currentPosition[0] + 1, currentPosition[1], fill=nonPrimeColor)
currentPosition = (int(canvasSide / 2)+1, int(canvasSide / 2))
w.create_line(currentPosition[0], currentPosition[1], currentPosition[0] + 1, currentPosition[1], fill=primeColor)
currentPosition = (int(canvasSide / 2), int(canvasSide / 2)+1)
w.create_line(currentPosition[0], currentPosition[1], currentPosition[0] + 1, currentPosition[1], fill=primeColor)

lastDirection = ["left"]
nextTurnDistance = 5
lastTraveledLeg = 2

positiveLines = {}
negativeLines = {}

primes = 2
nonPrimes = 1

## Step through the spiral, one step at a time and add points on the canvas as we go along
for i in tqdm(range(4, canvasSide*canvasSide)):
    (currentPosition, lastDirection, nextTurnDistance, lastTraveledLeg) = takeTheNextStep(currentPosition, lastDirection, i, nextTurnDistance, lastTraveledLeg)
    if is_prime(i):
        w.create_line(currentPosition[0], currentPosition[1], currentPosition[0] + 1, currentPosition[1], fill=primeColor, tags=("basicPrime",) )
        addPointToLineCounter(currentPosition, True)
        primes+=1
    else:
        nonPrimes+=1
        w.create_line(currentPosition[0], currentPosition[1], currentPosition[0] + 1, currentPosition[1], fill=nonPrimeColor)
        addPointToLineCounter(currentPosition, False)

## Go through all possible diagonal lines and see if any of them contain an unusual number of primes. If htey do, colorize the line in a brigheter color
for m in positiveLines.keys():
    if positiveLines[m].isSpecial():
        for coord in positiveLines[m].primeCoords:
            w.create_line(coord[0], coord[1], coord[0] + 1, coord[1], fill=significantLineColor, tags=("specialPrime",))
for m in negativeLines.keys():
    if negativeLines[m].isSpecial():
        for coord in negativeLines[m].primeCoords:
            w.create_line(coord[0], coord[1], coord[0] + 1, coord[1], fill=significantLineColor, tags=("specialPrime",))

print("Primes: " + str(primes))
print("Non-primes: " + str(nonPrimes))

mainloop()
