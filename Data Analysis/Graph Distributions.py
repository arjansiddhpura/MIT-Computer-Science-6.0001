# Exponential and Geometric Distributions

import pylab
import random


def clear(n, p, steps):
   numRemaning = []
   for t in range(steps):
       numRemaning.append(n * ((1 - p) ** t))
   pylab.plot(numRemaning)
   pylab.xlabel("Time")
   pylab.ylabel("Molecules Remaining")
   pylab.title("Clearence of Drug")


# clear(1000, 0.01, 1000)
# pylab.show()


def successfulStarts(successProb, numTrials):
   triesBeforeSuccess = []
   for t in range(numTrials):
       consecFailures = 0
       while random.random() > successProb:
           consecFailures += 1
       triesBeforeSuccess.append(consecFailures)
   return triesBeforeSuccess


# probOfSuccess = 0.5
# numTrials = 5000
# distribution = successfulStarts(probOfSuccess, numTrials)
# pylab.hist(distribution, bins = 14, edgecolor="black")
# pylab.xlabel("Tries Before Success")
# pylab.ylabel("Number of Occuerrences Out of " + str(numTrials))
# pylab.title("Probability of Starting Each Try = " + str(probOfSuccess))
# pylab.show()


def collisionProb(n, k):
   prob = 1.0
   xVals, yVals = [], []
   for i in range(1, k + 1):
       xVals.append(i)
       prob = prob * ((n - i) / n)
       yVals.append(1 - prob)
   pylab.plot(xVals, yVals, "k:")


# collisionProb(366, 100)
# pylab.show()


def simInsertions(numIndices, numInsertions):
   choices = range(numIndices)
   used = []
   for i in range(numInsertions):
       hashVal = random.choice(choices)
       if hashVal in used:
           return 1
       else:
           used.append(hashVal)
   return 0


def findProb(numIndices, numInsertions, numTrials):
   collisions = 0
   for t in range(numTrials):
       collisions += simInsertions(numIndices, numInsertions)
   return collisions / numTrials


# print("Actual probability of a collision =", collisionProb(1000, 50))
# print("Est. probabilty of a collision =", findProb(1000, 50, 10000))
# print("Actual probability of a collision =", collisionProb(1000, 200))
# print("Est. probabilty of a collision =", findProb(1000, 200, 10000))
