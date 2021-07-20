import random

class Item(object):
   def __init__(self, n, v, w):
       self.name = n
       self.value = v
       self.weight = w
   def getName(self):
       return self.name
   def getValue(self):
       return self.value
   def getWeight(self):
       return self.weight
   def __str__(self):
       result = '<' + self.name + ', ' + str(self.value) \
                + ', ' + str(self.weight) + '>'
       return result
    
def buildItems():
   names = ['clock','painting','radio','vase','book','computer']
   values = [175,90,20,50,10,200]
   weights = [10,9,4,2,1,20]
   Items = []
   for i in range(len(values)):
       Items.append(Item(names[i], values[i], weights[i]))
   return Items

def chooseBest(pset, maxWeight, getVal, getWeight):
   bestVal = 0.0
   bestSet = None
   for items in pset:
       itemsVal = 0.0
       itemsWeight = 0.0
       for item in items:
           itemsVal += getVal(item)
           itemsWeight += getWeight(item)
       if itemsWeight <= maxWeight and itemsVal > bestVal:
           bestVal = itemsVal
           bestSet = items
   return (bestSet, bestVal)

def getBinaryRep(n, numDigits):
   result = ''
   while n > 0:
       result = str(n%2) + result
       n //= 2
   if len(result) > numDigits:
       raise ValueError('not enough digits')
   for i in range(numDigits-len(result)):
       result = '0' + result
   return result

def genPowerset(L):
   powerset = []
   for i in range(0, 2**len(L)):
       binStr = getBinaryRep(i, len(L))
       subset = []
       for j in range(len(L)):
           if binStr[j] == '1':
               subset.append(L[j])
       powerset.append(subset)
   return powerset

def testBest(maxWeight = 20):
   items = buildItems()
   pset = genPowerset(items)
   taken, val = chooseBest(pset, maxWeight, Item.getValue, Item.getWeight)
   print('Total value of items taken is', val)
   for item in taken:
       print(item)

#testBest()

def maxVal(toConsider, avail):
   if toConsider == [] or avail == 0:
       result = (0, ())
   elif toConsider[0].getWeight() > avail:
       result = maxVal(toConsider[1:], avail)
   else:
       nextItem = toConsider[0]
       leftVal, leftTake = maxVal(toConsider[1:], avail - \
                           nextItem.getWeight())
       leftVal += nextItem.getValue()
       rightVal, rightTake = maxVal(toConsider[1:], avail)
       if leftVal > rightVal:
           result = (leftVal, leftTake + (nextItem,))
       else:
           result = (rightVal, rightTake)
   return result

def smallTest():
   names = ['a', 'b', 'c', 'd']
   vals = [6, 7, 8, 9]
   weights = [3, 3, 2, 5]
   Items = []
   for i in range(len(vals)):
       Items.append(Item(names[i], vals[i], weights[i]))
   val, taken = maxVal(Items, 5)
   for item in taken:
       print(item)
   print('Total value of items taken:', val)

def buildManyItems(numItems, maxVal, maxWeight):
   items = []
   for i in range(numItems):
       items.append(Item(str(i), \
                    random.randint(1, maxVal), \
                    random.randint(1, maxWeight)))
   return items

def fastMaxVal(toConsider, avail, memo={}):
   if (len(toConsider), avail) in memo:
       result = memo[(len(toConsider), avail)]
   elif toConsider == [] or avail == 0:
       result = (0, ())
   elif toConsider[0].getWeight() > avail:
       result = fastMaxVal(toConsider[1:], avail, memo)
   else:
       nextItem = toConsider[0]
       leftVal, leftTake = fastMaxVal(toConsider[1:], \
                           avail - nextItem.getWeight(), memo)
       leftVal += nextItem.getValue()
       rightVal, rightTake = fastMaxVal(toConsider[1:], \
                             avail, memo)
       if leftVal > rightVal:
           result = (leftVal, leftTake + (nextItem,))
       else:
           result = (rightVal, rightTake)
   memo[(len(toConsider), avail)] = result
   return result

def bigTest(numItems, fast=True):
   items = buildManyItems(numItems, 10, 10)
   if fast:
       val, taken = fastMaxVal(items, 50)
   else:
       val, taken = maxVal(items, 50)
   print('Items taken')
   for item in taken:
       print(item)
   print('Total value of items taken:', val)

bigTest(128)