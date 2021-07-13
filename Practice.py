# def fib(x):
#    """Assumes x an int >= 0
#    Returns Fibonacci of x"""
#    global numFibCalls
#    numFibCalls += 1
#    if x == 0 or x == 1:
#        return 1
#    else:
#        return fib(x-1) + fib(x-2)
#
# def testFib(n):
#    for i in range(n+1):
#        global numFibCalls
#        numFibCalls = 0
#        print('fib of', i, '=', fib(i))
#        print('fib called', numFibCalls, 'times.')
#
# print(testFib(6))


# nameHandle = open('kids', 'a')
# nameHandle.write('David\n')
# nameHandle.write('Andrea\n')
# nameHandle.close()
# nameHandle = open('kids', 'r')
# for line in nameHandle:
#    print(line[:-1])
# nameHandle.close()


# t1 = ()
# t2 = (1, 'two', 3)
# t3 = (1, )
# print(t1)
# print(t2)
# print(t3)


# t1 = (1, 'two', 3)
# t2 = (t1, 3.25)
# print(t2)
# print((t1 + t2))
# print((t1 + t2)[3])
# print((t1 + t2)[2:5])
#
# def intersect(t1, t2):
#    """Assumes t1 and t2 are tuples
#    Returns a tuple containing elements that are in
#    both t1 and t2"""
#    result = ()
#    for e in t1:
#        if e in t2:
#            result += (e,)
#    return result


# def findExtremeDivisors(n1, n2):
#    """Assumes that n1 and n2 are positive ints
#    Returns a tuple containing the smallest common divisor > 1 and
#    the largest common divisor of n1 and n2. If no common divisor,
#    returns (None, None)"""
#    minVal, maxVal = None, None
#    for i in range(2, min(n1, n2) + 1):
#        if n1%i == 0 and n2%i == 0:
#            if minVal == None:
#                minVal = i
#            maxVal = i
#    return (minVal, maxVal)
#
# print(findExtremeDivisors(5, 6))


# L1 = [1,2,3]
# L2 = [4,5,6]
# L3 = L1 + L2
# print('L3 =', L3)
# L1.extend(L2)
# print('L1 =', L1)
# L1.append(L2)
# print('L1 =', L1)
#
# def removeDups(L1, L2):
#    """Assumes that L1 and L2 are lists.
#    Removes any element from L1 that also occurs in L2"""
#    for e1 in L1:
#        if e1 in L2:
#            L1.remove(e1)
# L1 = [1,2,3,4]
# L2 = [1,2,5,6]
# removeDups(L1, L2)
# print('L1 =', L1)


# def cube(x):
#    x=x**3
#    return x
#
# def applyToEach(L, f):
#    for i in range(len(L)):
#        L[i]=f(L[i])
#
# L=[1, 2, 3, 4, 5]
# print('L= ', L)
# print('Apply cube to each element of L.')
# applyToEach(L, cube)
# print('L= ', L)
#
# def fib(n):
#    """Assumes n int >= 0
#    Returns Fibonacci of n"""
#    if n == 0 or n == 1:
#        return 1
#    else:
#        return fib(n-1) + fib(n-2)
#
# def testFib(n):
#    for i in range(n+1):
#        print('fib of', i, '=', fib(i))
#
# for i in map(fib, [2, 6, 4]):
#    print(i)
#
# L1 = [1, 36]
# L2 = [2, 57, 9]
# for i in map(min, L1, L2):
#    print(i)
#
# L = []
# for i in map(lambda x, y: x**y, L1, L2):
#    L.append(i)
# print(L)


# def keySearch(L, k):
#    for elem in L:
#        if elem[0] == k:
#            return elem[1]
#    return None


# birthStones = {'Jan':'Garnet', 'Feb':'Amethyst', 'Mar':'Acquamarine',
#'Apr':'Diamond', 'May':'Emerald'}
# months = birthStones.keys()
# print(months)
# birthStones['June'] = 'Pearl'
# print(list(months))


# def copy(L1, L2):
#    """Assumes L1, L2 are lists
#    Mutates L2 to be a copy of L1"""
#    if L1 != L2:
#        while len(L2) > 0: #remove all elements from L2
#            L2.pop() #remove last element of L2
#        for e in L1: #append L1's elements to initially empty L2
#            L2.append(e)
#    else:
#        print("given lists are the same, no copying necessary")
#
# Ly=[1, 3, 5, 7, 9, 11, 13, 15]
# Lz=[2, 4, 6, 8, 10, 12, 14, 16]
#
# print(Lz)
# copy(Ly, Lz)
# print(Lz)


# L=["3", "5", "0", 9]
# def isEven(l):
#        for i in l:
#                if i % 2 == 0:
#                        return i
#        raise ValueError("No even numbers in list!")
# print(isEven(L))


# def getRatios(vect1, vect2):
#    """Assumes: vect1 and vect2 are equal length lists of numbers
#    Returns: a list containing the meaningful values of
#    vect1[i]/vect2[i]"""
#    ratios = []
#    for index in range(len(vect1)):
#        try:
#            ratios.append(vect1[index]/vect2[index])
#        except ZeroDivisionError:
#            ratios.append(float('nan')) #nan = Not a Number
#        except:
#            raise ValueError('getRatios called with bad arguments')
#    return ratios
#
# try:
#    print(getRatios([1.0,2.0,7.0,6.0], [1.0,2.0,0.0,3.0]))
#    print(getRatios([], []))
#    print(getRatios([1.0, 2.0], [3.0]))
# except ValueError as msg:
#    print(msg)


# BAD CODE
# def getRatios(vect1, vect2):
#    """Assumes: vect1 and vect2 are lists of equal length of numbers
#    Returns: a list containing the meaningful values of
#    vect1[i]/vect2[i]"""
#    ratios = []
#    if len(vect1) != len(vect2):
#        raise ValueError('getRatios called with bad arguments')
#    for index in range(len(vect1)):
#        vect1Elem = vect1[index]
#        vect2Elem = vect2[index]
#    if (type(vect1Elem) not in (int, float))\
#    or (type(vect2Elem) not in (int, float)):
#        raise ValueError('getRatios called with bad arguments')
#    if vect2Elem == 0.0:
#        ratios.append(float('NaN')) #NaN = Not a Number
#    else:
#        ratios.append(vect1Elem/vect2Elem)
#    return ratios


# def getGrades(fname):
#    try:
#        gradesFile = open(fname, 'r') #open file for reading
#    except IOError:
#        raise ValueError('getGrades could not open ' + fname)
#    grades = []
#    for line in gradesFile:
#        try:
#            grades.append(float(line))
#        except:
#            raise ValueError('Unable to convert line to float')
#    return grades
#
# try:
#    grades = getGrades('quiz1grades.txt')
#    grades.sort()
#    median = grades[len(grades)//2]
#    print('Median grade is', median)
#    assert median == 49.0, "Are you sure it is not 49.0?"
# except ValueError as errorMsg:
#    print('Whoops.', errorMsg)
# except AssertionError as error:
#    print(error)


# class IntSet(object):
#    """An intSet is a set of integers"""
#    #Information about the implementation (not the abstraction)
#    #Value of the set is represented by a list of ints, self.vals.
#    #Each int in the set occurs in self.vals exactly once.
#
#    def __init__(self):
#        """Create an empty set of integers"""
#        self.vals = []
#
#    def insert(self, e):
#        """Assumes e is an integer and inserts e into self"""
#        if e not in self.vals:
#            self.vals.append(e)
#
#    def member(self, e):
#        """Assumes e is an integer
#        Returns True if e is in self, and False otherwise"""
#        return e in self.vals
#
#    def remove(self, e):
#        """Assumes e is an integer and removes e from self
#        Raises ValueError if e is not in self"""
#        try:
#            self.vals.remove(e)
#        except:
#            raise ValueError(str(e) + ' not found')
#
#    def getMembers(self):
#        """Returns a list containing the elements of self.
#        Nothing can be assumed about the order of the elements"""
#        return self.vals[:]
#
#    def __str__(self):
#        """Returns a string representation of self"""
#        self.vals.sort()
#        result = ''
#        for e in self.vals:
#            result = result + str(e) + ','
#        return '{' + result[:-1] + '}' #-1 omits trailing comma
#
# s = IntSet()
# s.insert(6)
# s.insert(4)
# print(s)


##Class Person
# import datetime
#
# class Person(object):
#
#    def __init__(self, name):
#        """Create a person"""
#        self.name = name
#        try:
#            lastBlank = name.rindex(' ')
#            self.lastName = name[lastBlank+1:]
#        except:
#            self.lastName = name
#        self.birthday = None
#
#    def getName(self):
#        """Returns self's full name"""
#        return self.name
#
#    def getLastName(self):
#        """Returns self's last name"""
#        return self.lastName
#
#    def setBirthday(self, birthdate):
#        """Assumes birthdate is of type datetime.date
#        Sets self's birthday to birthdate"""
#        self.birthday = birthdate
#
#    def getAge(self):
#        """Returns self's current age in days"""
#        if self.birthday == None:
#            raise ValueError
#        return (datetime.date.today() - self.birthday).days
#
#    def __lt__(self, other):
#        """Returns True if self precedes other in alphabetical
#        order, and False otherwise. Comparison is based on last
#        names, but if these are the same full names are
#        compared."""
#        if self.lastName == other.lastName:
#            return self.name < other.name
#        return self.lastName < other.lastName
#
#
#    def __str__(self):
#        """Returns self's name"""
#        return self.name
#
##Class MIT Person
# class MITPerson(Person):
#
#    nextIdNum = 0 #identification number
#
#    def __init__(self, name):
#        Person.__init__(self, name)
#        self.idNum = MITPerson.nextIdNum
#        MITPerson.nextIdNum += 1
#
#    def getIdNum(self):
#        return self.idNum
#
#    def isStudent(self):
#        return isinstance(self, Student)
#
#    def __lt__(self, other):
#        try:
#            return self.idNum < other.idNum
#        except AttributeError:
#            print(MITPerson.getName(self) + ' has no ID Number. Get him one!')
#
##Class Student
# class Student(MITPerson):
#    pass
#
# class UG(Student):
#    def __init__(self, name, classYear):
#        MITPerson.__init__(self, name)
#        self.year = classYear
#    def getClass(self):
#        return self.year
#
# class Grad(Student):
#    pass
#
##me = Person('Arjan Siddhpura')
##him = Person('Barack Obama')
##her = Person('Madonna')
##print(him.getLastName())
##him.setBirthday(datetime.date(1961, 8, 4))
##her.setBirthday(datetime.date(1958, 8, 16))
##print(him.getName(), 'is', him.getAge(), 'days old.')
##people = [me, him, her]
##people.sort()
##people.reverse()
##for p in people:
##    print(p)
#
# p1 = MITPerson('Mark Guttag')
# p2 = MITPerson('Billy Bob Beaver')
# p3 = MITPerson('Billy Bob Beaver')
# p4 = Person('Billy Bob Beaver')
# p5 = Grad('Buzz Aldrin')
# p6 = UG('Billy Beaver', 1984)
#
##print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))
##print('And ' + str(p2) + '\'s id number is ' + str(p2.getIdNum()))
# print(p5, 'is a graduate student is', type(p5) == Grad)
# print(p5, 'is an undergraduate student is', type(p5) == UG)
# print(p5, 'is a student is', p5.isStudent())
# print(p3, 'is a student is', p3.isStudent())
##print('p4 < p1 = ', p4 < p1)
##print('p1 < p4 = ', p1 < p4)


##Class Mortgage
#
# def findPayment(loan, r, m):
#    """Assumes: loan and r are floats, m an int
#    Returns the monthly payment for a mortgage of size
#    loan at a monthly rate of r for m months"""
#    return loan*((r*(1+r)**m)/((1+r)**m - 1))
#
# class Mortgage(object):
#    """Abstract class for building different kinds of mortgages"""
#
#    def __init__(self, loan, annRate, months):
#        """Assumes: loan and annRate are floats, months an int
#        Creates a new mortgage of size loan, duration months, and
#        annual rate annRate"""
#        self.loan = loan
#        self.rate = annRate/12
#        self.months = months
#        self.paid = [0.0]
#        self.outstanding = [loan]
#        self.payment = findPayment(loan, self.rate, months)
#        self.legend = None #description of mortgage
#
#    def makePayment(self):
#        """Make a payment"""
#        self.paid.append(self.payment)
#        reduction = self.payment - self.outstanding[-1]*self.rate
#        self.outstanding.append(self.outstanding[-1] - reduction)
#
#    def getTotalPaid(self):
#        """Return the total amount paid so far"""
#        return sum(self.paid)
#
#    def __str__(self):
#        return self.legend
#
# class Fixed(Mortgage):
#    def __init__(self, loan, r, months):
#        Mortgage.__init__(self, loan, r, months)
#        self.legend = 'Fixed, ' + str(round(r*100, 2)) + '%'
#
# class FixedWithPts(Mortgage):
#    def __init__(self, loan, r, months, pts):
#        Mortgage.__init__(self, loan, r, months)
#        self.pts = pts
#        self.paid = [loan*(pts/100)]
#        self.legend = 'Fixed, ' + str(round(r*100, 2)) + '%, '\
#        + str(pts) + ' points'
#
# class TwoRate(Mortgage):
#    def __init__(self, loan, r, months, teaserRate, teaserMonths):
#        Mortgage.__init__(self, loan, teaserRate, months)
#        self.teaserMonths = teaserMonths
#        self.teaserRate = teaserRate
#        self.nextRate = r/12
#        self.legend = str(teaserRate*100)\
#        + '% for ' + str(self.teaserMonths)\
#        + ' months, then ' + str(round(r*100, 2)) + '%'
#
#    def makePayment(self):
#        if len(self.paid) == self.teaserMonths + 1:
#            self.rate = self.nextRate
#            self.payment = findPayment(self.outstanding[-1],
#            self.rate,
#            self.months - self.teaserMonths)
#        Mortgage.makePayment(self)
#
# def compareMortgages(amt, years, fixedRate, pts, ptsRate,
#                     varRate1, varRate2, varMonths):
#    totMonths = years*12
#    fixed1 = Fixed(amt, fixedRate, totMonths)
#    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
#    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
#    morts = [fixed1, fixed2, twoRate]
#    for m in range(totMonths):
#        for mort in morts:
#            mort.makePayment()
#    for m in morts:
#        print(m)
#        print(' Total Payments = $' + str(int(m.getTotalPaid())))
#
# compareMortgages(amt=200000, years=30, fixedRate=0.07, pts=3.25,
#                 ptsRate=0.05, varRate1=0.045, varRate2=0.095, varMonths=48)


# Integer to String Convertor
# def intToStr(i):
#    digits = '0123456789'
#    result = ''
#    if i == 0:
#        return '0'
#    while i > 0:
#        result = digits[i%10] + result
#        i //= 10
#    return result
#
# def addDigits(n):
#    stringRep = intToStr(n)
#    val = 0
#    for c in stringRep:
#        val += int(c)
#    return val
#
# print(addDigits(123))


# Implementation of a Subset Test
# def isSubset(L1, L2):
#    for e1 in L1:
#        matched = False
#        for e2 in L2:
#            if e1 == e2:
#                matched = True
#                break
#        if not matched:
#            return False
#    return True
#
# print(isSubset(L1=[5, 3], L2=[1, 2, 3, 4, 5]))


##Generating a Power Set
# def getBinaryRep(n, numDigits):
#    result = ''
#    while n > 0:
#        result = str(n%2) + result
#        n //= 2
#    if len(result) > numDigits:
#        raise ValueError('not enough digits')
#    for i in range(numDigits-len(result)):
#        result = '0' + result
#    return result
#
# def genPowerset(L):
#    powerset = []
#    for i in range(0, 2**len(L)):
#        binStr = getBinaryRep(i, len(L))
#        subset = []
#        for j in range(len(L)):
#            if binStr[j] == '1':
#                subset.append(L[j])
#        powerset.append(subset)
#    return powerset
#
# print(genPowerset(L=[1, 3, 5]))


# Linear Search of a Sorted List
# def search(L, e):
#    for i in range(len(L)):
#        if L[i] == e:
#            return True
#        if L[i] > e:
#            return False
#    return False
#
# L=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(search(L, 12))


# Recursive Binary Search
# def search(L, e):
#    """Assumes L is a sorted list in ascending order"""
#
#    def bSearch(L, e, low, high):
#        #Decrements high - low
#        if high == low:
#            return L[low] == e
#        mid = (low + high)//2
#        if L[mid] == e:
#            return True
#        elif L[mid] > e:
#            if low == mid: #Nothing left to search
#                return False
#            else:
#                return bSearch(L, e, mid + 1, high)
#
#    if len(L) == 0:
#        return False
#    else:
#        return bSearch(L, e, 0, len(L) - 1)


# Merge Sort Algorithm
# def merge(left, right, compare):
#
#    result = []
#    i, j = 0, 0
#    while i < len(left) and j < len(right):
#        if compare(left[i], right[j]):
#            result.append(left[i])
#            i += 1
#        else:
#            result.append(right[j])
#            j += 1
#    while (i < len(left)):
#        result.append(left[i])
#        i += 1
#    while (j < len(right)):
#        result.append(right[j])
#        j += 1
#    return result
#
# def mergeSort(L, compare = lambda x, y: x < y):
#    if len(L) <= 1:
#        return L[:]
#    else:
#        middle = len(L)//2
#        left = mergeSort(L[:middle])
#        right = mergeSort(L[middle:])
#        return merge(left, right, compare)
#
# L = [1, 90, 15, 13, 11, 10, 9, 66, -5, -9, -99, 31, 2, 95, 82, 66, 3]
# sortedL = mergeSort(L)
# print(sortedL)


# Hashing Tables
# class intDict(object):
#
#    def __init__(self, numBuckets):
#        self.buckets = []
#        self.numBuckets = numBuckets
#        for i in range(numBuckets):
#            self.buckets.append([])
#
#    def addEntry(self, key, dictVal):
#        hashBucket = self.buckets[key%self.numBuckets]
#        for i in range(len(hashBucket)):
#            if hashBucket[i][0] == key:
#                hashBucket[i] = (key, dictVal)
#                return
#        hashBucket.append((key, dictVal))
#
#    def getValue(self, key):
#        hashBucket = self.buckets[key%self.numBuckets]
#        for e in hashBucket:
#            if e[0] == key:
#                return e[1]
#        return None
#
#    def __str__(self):
#        result = '{'
#        for b in self.buckets:
#            for e in b:
#                result = result + str(e[0]) + ':' + str(e[1]) + ','
#        return result[:-1] + '}'
#
# import random
# D = intDict(10)
# for i in range(20):
#    key = random.choice(range(10**2))
#    D.addEntry(key, i)
# print('\nThe value of the intDict is:')
# print(D)
# print('\n', 'The buckets are:')
# for hashBucket in D.buckets:
#    print(' ', hashBucket)


##PyLab Works
# import pylab
#
# def findPayment(loan, r, m):
#    """Assumes: loan and r are floats, m an int
#    Returns the monthly payment for a mortgage of size
#    loan at a monthly rate of r for m months"""
#    return loan*((r*(1+r)**m)/((1+r)**m - 1))
#
# class Mortgage(object):
#    def __init__(self, loan, annRate, months):
#        self.loan = loan
#        self.rate = annRate/12.0
#        self.months = months
#        self.paid = [0.0]
#        self.outstanding = [loan]
#        self.payment = findPayment(loan, self.rate, months)
#        self.legend = None
#
#    def makePayment(self):
#        self.paid.append(self.payment)
#        reduction = self.payment - self.outstanding[-1] * self.rate
#        self.outstanding.append(self.outstanding[-1] - reduction)
#
#    def getTotalPaid(self):
#        return sum(self.paid)
#    def __str__(self):
#        return self.legend
#
#    def plotPayments(self, style):
#        pylab.plot(self.paid[1:], style, label = self.legend)
#
#    def plotBalance(self, style):
#        pylab.plot(self.outstanding, style, label = self.legend)
#
#    def plotTotPd(self, style):
#        totPd = [self.paid[0]]
#        for i in range(1, len(self.paid)):
#            totPd.append(totPd[-1] + self.paid[i])
#        pylab.plot(totPd, style, label = self.legend)
#
#    def plotNet(self, style):
#        totPd = [self.paid[0]]
#        for i in range(1, len(self.paid)):
#            totPd.append(totPd[-1] + self.paid[i])
#        equityAcquired = pylab.array([self.loan] * \
#                         len(self.outstanding))
#        equityAcquired = equityAcquired - \
#                         pylab.array(self.outstanding)
#        net = pylab.array(totPd) - equityAcquired
#        pylab.plot(net, style, label = self.legend)
#
# class Fixed(Mortgage):
#    def __init__(self, loan, r, months):
#        Mortgage.__init__(self, loan, r, months)
#        self.legend = 'Fixed, ' + str(r*100) + '%'
#
# class FixedWithPts(Mortgage):
#    def __init__(self, loan, r, months, pts):
#        Mortgage.__init__(self, loan, r, months)
#        self.pts = pts
#        self.paid = [loan*(pts/100.0)]
#        self.legend = 'Fixed, ' + str(r*100) + '%, '\
#                    + str(pts) + ' points'
#
# class TwoRate(Mortgage):
#    def __init__(self, loan, r, months, teaserRate, teaserMonths):
#        Mortgage.__init__(self, loan, teaserRate, months)
#        self.teaserMonths = teaserMonths
#        self.teaserRate = teaserRate
#        self.nextRate = r/12.0
#        self.legend = str(teaserRate*100)\
#                    + '% for ' + str(self.teaserMonths)\
#                    + ' months, then ' + str(r*100) + '%'
#
#    def makePayment(self):
#        if len(self.paid) == self.teaserMonths + 1:
#            self.rate = self.nextRate
#            self.payment = findPayment(self.outstanding[-1],
#                                       self.rate,
#                                       self.months - self.teaserMonths)
#        Mortgage.makePayment(self)
#
# def plotMortgages(morts, amt):
#    def labelPlot(figure, title, xLabel, yLabel):
#        pylab.figure(figure)
#        pylab.title(title)
#        pylab.xlabel(xLabel)
#        pylab.ylabel(yLabel)
#        pylab.legend(loc = 'best')
#    styles = ['k-', 'k-.', 'k:']
#    #Give names to figure numbers
#    payments, cost, balance, netCost = 0, 1, 2, 3
#    for i in range(len(morts)):
#        pylab.figure(payments)
#        morts[i].plotPayments(styles[i])
#        pylab.figure(cost)
#        morts[i].plotTotPd(styles[i])
#        pylab.figure(balance)
#        morts[i].plotBalance(styles[i])
#        pylab.figure(netCost)
#        morts[i].plotNet(styles[i])
#    labelPlot(payments, 'Monthly Payments of $' + str(amt) +
#             ' Mortgages', 'Months', 'Monthly Payments')
#    labelPlot(cost, 'Cash Outlay of $' + str(amt) +
#             ' Mortgages', 'Months', 'Total Payments')
#    labelPlot(balance, 'Balance Remaining of $' + str(amt) +
#             ' Mortgages', 'Months', 'Remaining Loan Balance of $')
#    labelPlot(netCost, 'Net Cost of $' + str(amt) + ' Mortgages',
#             'Months', 'Payments - Equity $')
#
# def compareMortgages(amt, years, fixedRate, pts, ptsRate,
#                     varRate1, varRate2, varMonths):
#    totMonths = years*12
#    fixed1 = Fixed(amt, fixedRate, totMonths)
#    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
#    tworate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
#    morts = [fixed1, fixed2, tworate]
#    for m in range(totMonths):
#        for mort in morts:
#            mort.makePayment()
#    plotMortgages(morts, amt)
#
# compareMortgages(amt=200000, years=30, fixedRate=0.07, pts=3.25,
#                 ptsRate=0.05, varRate1=0.045, varRate2=0.095, varMonths=48)
#
# pylab.show()


# Graph Optimization Problems
# class Node(object):
#    def __init__(self, name):
#        self.name = name
#    def getName(self):
#        return self.name
#    def __str__(self):
#        return self.name
#
# class Edge(object):
#    def __init__(self, src, dest):
#        self.src = src
#        self.dest = dest
#    def getSource(self):
#        return self.src
#    def getDestination(self):
#        return self.dest
#    def __str__(self):
#        return self.src.getName() + '->' + self.dest.getName()
#
# class WeightedEdge(Edge):
#    def __init__(self, src, dest, weight = 1.0):
#        self.src = src
#        self.dest = dest
#        self.weight = weight
#    def getWeight(self):
#        return self.weight
#    def __str__(self):
#        return self.src.getName() + '->(' + str(self.weight) + ')->' + \
#            self.dest.getName()
#
# class Digraph(object):
#    def __init__(self):
#        self.nodes = []
#        self.edges = {}
#    def addNode(self, node):
#        if node in self.nodes:
#            raise ValueError('Duplicate Node')
#        else:
#            self.nodes.append(node)
#            self.edges[node] = []
#    def addEdge(self, edge):
#        src = edge.getSource()
#        dest = edge.getDestination()
#        if not (src in self.nodes and dest in self.nodes):
#            raise ValueError('Node not in Graph')
#        self.edges[src].append(dest)
#    def childrenOf(self, node):
#        return self.edges[node]
#    def hasNode(self, node):
#        return node in self.nodes
#    def __str__(self):
#        result = ''
#        for src in self.nodes:
#            for dest in self.edges[src]:
#                result = result + src.getName() + '->' \
#                    + dest.getName() + '\n'
#        return result[:-1]
#
# class Graph(Digraph):
#    def addEdge(self, edge):
#        Digraph.addEdge(self, edge)
#        rev = Edge(edge.getDestination(), edge.getSource())
#        Digraph.addEdge(self, rev)
#
# def printPath(path):
#    result = ''
#    for i in range(len(path)):
#        result = result + str(path[i])
#        if i != len(path) - 1:
#            result = result + '->'
#    return result
#
# def DFS(graph, start, end, path, shortest, toPrint = False):
#    path = path + [start]
#    if toPrint:
#        print('Current DFS Path:', printPath(path))
#    if start == end:
#        return path
#    for node in graph.childrenOf(start):
#        if node not in path:
#            if shortest == None or len(path) < len(shortest):
#                newPath = DFS(graph, node, end, path, shortest, toPrint)
#                if newPath != None:
#                    shortest = newPath
#    return shortest
#
# def BFS(graph, start, end, toPrint = False):
#    initPath = [start]
#    pathQueue = [initPath]
#    if toPrint:
#        print('Current BFS path:', printPath(initPath))
#    while len(pathQueue) != 0:
#        tmpPath = pathQueue.pop(0)
#        print('Current BFS path:', printPath(tmpPath))
#        lastNode = tmpPath[-1]
#        if lastNode == end:
#            return tmpPath
#        for nextNode in graph.childrenOf(lastNode):
#            if nextNode not in tmpPath:
#                newPath = tmpPath + [nextNode]
#                pathQueue.append(newPath)
#    return None
#
# def shortestPath(graph, start, end, toPrint = False):
#    return DFS(graph, start, end, [], None, toPrint)
#
# def testSP():
#    nodes = []
#    for name in range(6):
#        nodes.append(Node(str(name)))
#    g = Digraph()
#    for n in nodes:
#        g.addNode(n)
#    g.addEdge(Edge(nodes[0], nodes[1]))
#    g.addEdge(Edge(nodes[1], nodes[2]))
#    g.addEdge(Edge(nodes[2], nodes[3]))
#    g.addEdge(Edge(nodes[2], nodes[4]))
#    g.addEdge(Edge(nodes[3], nodes[4]))
#    g.addEdge(Edge(nodes[3], nodes[5]))
#    g.addEdge(Edge(nodes[0], nodes[2]))
#    g.addEdge(Edge(nodes[1], nodes[0]))
#    g.addEdge(Edge(nodes[3], nodes[1]))
#    g.addEdge(Edge(nodes[4], nodes[0]))
#    sp = shortestPath(g, nodes[0], nodes[5], toPrint = True)
#    print('Shortest path found by DFS:', printPath(sp), '\n')
#    sp = BFS(g, nodes[0], nodes[5])
#    print('Shortest path found by BFS:', printPath(sp))
#
# testSP()


# Fast Fibonacci with Dynamic Programming
# def fib(n):
#    if n == 0 or n == 1:
#        return 1
#    else:
#        return fib(n-1) + fib(n-2)
#
# def fastFib(n, memo = {}):
#    if n == 0 or n == 1:
#        return 1
#    try:
#        return memo[n]
#    except KeyError:
#        result = fastFib(n-1, memo) + fastFib(n-2, memo)
#        memo[n] = result
#        return result
#
# print(fastFib(500))


##0/1 Knapsach Problems and Dynamic Programming
# import random
#
# class Item(object):
#    def __init__(self, n, v, w):
#        self.name = n
#        self.value = v
#        self.weight = w
#    def getName(self):
#        return self.name
#    def getValue(self):
#        return self.value
#    def getWeight(self):
#        return self.weight
#    def __str__(self):
#        result = '<' + self.name + ', ' + str(self.value) \
#                 + ', ' + str(self.weight) + '>'
#        return result
#
# def value(item):
#    return item.getValue()
#
# def weightInverse(item):
#    return 1.0/item.getWeight()
#
# def density(item):
#    return item.getValue()/item.getWeight()
#
# def greedy(items, maxWeight, keyFunction):
#    itemsCopy = sorted(items, key=keyFunction, reverse=True)
#    result = []
#    totalValue, totalWeight = 0.0, 0.0
#    for i in range(len(itemsCopy)):
#        if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
#            result.append(itemsCopy[i])
#            totalWeight += itemsCopy[i].getWeight()
#            totalValue += itemsCopy[i].getValue()
#    return (result, totalValue)
#
# def buildItems():
#    names = ['clock','painting','radio','vase','book','computer']
#    values = [175,90,20,50,10,200]
#    weights = [10,9,4,2,1,20]
#    Items = []
#    for i in range(len(values)):
#        Items.append(Item(names[i], values[i], weights[i]))
#    return Items
#
# def testGreedy(items, maxWeight, keyFunction):
#    taken, val = greedy(items, maxWeight, keyFunction)
#    print('Total value of items taken is', val)
#    for item in taken:
#        print('  ', item)
#
# def testGreedys(maxWeight = 20):
#    items = buildItems()
#    print('Use greedy by value to fill knapsack of size', maxWeight)
#    testGreedy(items, maxWeight, value)
#    print('\nUse greedy by weight to fill knapsack of size', maxWeight)
#    testGreedy(items, maxWeight, weightInverse)
#    print('\nUse greedy by density to fill knapsack of size', maxWeight)
#    testGreedy(items, maxWeight, density)
#
##testGreedys()
#
# def chooseBest(pset, maxWeight, getVal, getWeight):
#    bestVal = 0.0
#    bestSet = None
#    for items in pset:
#        itemsVal = 0.0
#        itemsWeight = 0.0
#        for item in items:
#            itemsVal += getVal(item)
#            itemsWeight += getWeight(item)
#        if itemsWeight <= maxWeight and itemsVal > bestVal:
#            bestVal = itemsVal
#            bestSet = items
#    return (bestSet, bestVal)
#
# def getBinaryRep(n, numDigits):
#    result = ''
#    while n > 0:
#        result = str(n%2) + result
#        n //= 2
#    if len(result) > numDigits:
#        raise ValueError('not enough digits')
#    for i in range(numDigits-len(result)):
#        result = '0' + result
#    return result
#
# def genPowerset(L):
#    powerset = []
#    for i in range(0, 2**len(L)):
#        binStr = getBinaryRep(i, len(L))
#        subset = []
#        for j in range(len(L)):
#            if binStr[j] == '1':
#                subset.append(L[j])
#        powerset.append(subset)
#    return powerset
#
# def testBest(maxWeight = 20):
#    items = buildItems()
#    pset = genPowerset(items)
#    taken, val = chooseBest(pset, maxWeight, Item.getValue, Item.getWeight)
#    print('Total value of items taken is', val)
#    for item in taken:
#        print(item)
#
##testBest()
#
# def maxVal(toConsider, avail):
#    if toConsider == [] or avail == 0:
#        result = (0, ())
#    elif toConsider[0].getWeight() > avail:
#        result = maxVal(toConsider[1:], avail)
#    else:
#        nextItem = toConsider[0]
#        leftVal, leftTake = maxVal(toConsider[1:], avail - \
#                            nextItem.getWeight())
#        leftVal += nextItem.getValue()
#        rightVal, rightTake = maxVal(toConsider[1:], avail)
#        if leftVal > rightVal:
#            result = (leftVal, leftTake + (nextItem,))
#        else:
#            result = (rightVal, rightTake)
#    return result
#
# def smallTest():
#    names = ['a', 'b', 'c', 'd']
#    vals = [6, 7, 8, 9]
#    weights = [3, 3, 2, 5]
#    Items = []
#    for i in range(len(vals)):
#        Items.append(Item(names[i], vals[i], weights[i]))
#    val, taken = maxVal(Items, 5)
#    for item in taken:
#        print(item)
#    print('Total value of items taken:', val)
#
# def buildManyItems(numItems, maxVal, maxWeight):
#    items = []
#    for i in range(numItems):
#        items.append(Item(str(i), \
#                     random.randint(1, maxVal), \
#                     random.randint(1, maxWeight)))
#    return items
#
# def fastMaxVal(toConsider, avail, memo={}):
#    if (len(toConsider), avail) in memo:
#        result = memo[(len(toConsider), avail)]
#    elif toConsider == [] or avail == 0:
#        result = (0, ())
#    elif toConsider[0].getWeight() > avail:
#        result = fastMaxVal(toConsider[1:], avail, memo)
#    else:
#        nextItem = toConsider[0]
#        leftVal, leftTake = fastMaxVal(toConsider[1:], \
#                            avail - nextItem.getWeight(), memo)
#        leftVal += nextItem.getValue()
#        rightVal, rightTake = fastMaxVal(toConsider[1:], \
#                              avail, memo)
#        if leftVal > rightVal:
#            result = (leftVal, leftTake + (nextItem,))
#        else:
#            result = (rightVal, rightTake)
#    memo[(len(toConsider), avail)] = result
#    return result
#
# def bigTest(numItems, fast=True):
#    items = buildManyItems(numItems, 10, 10)
#    if fast:
#        val, taken = fastMaxVal(items, 50)
#    else:
#        val, taken = maxVal(items, 50)
#    print('Items taken')
#    for item in taken:
#        print(item)
#    print('Total value of items taken:', val)
#
# bigTest(128)


# Random Walks
# import random
# from matplotlib.pyplot import xcorr
#
#
# class Location(object):
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#
#     def move(self, deltaX, deltaY):
#         return Location(self.x + deltaX, self.y + deltaY)
#
#     def getX(self):
#         return self.x
#
#     def getY(self):
#         return self.y
#
#     def distFrom(self, other):
#         ox, oy = other.x, other.y
#         xDist, yDist = self.x - ox, self.y - oy
#         return (xDist ** 2 + yDist ** 2) ** 0.5
#
#     def __str__(self):
#         return "<" + str(self.x) + ", " + str(self.y) + ">"
#
#
# class Field(object):
#     def __init__(self):
#         self.drunks = {}
#
#     def addDrunk(self, drunk, loc):
#         if drunk in self.drunks:
#             raise ValueError("Duplicate drunk")
#         else:
#             self.drunks[drunk] = loc
#
#     def moveDrunk(self, drunk):
#         if drunk not in self.drunks:
#             raise ValueError("Drunk not in field")
#         xDist, yDist = drunk.takeStep()
#         currentLocation = self.drunks[drunk]
#         self.drunks[drunk] = currentLocation.move(xDist, yDist)
#
#     def getLoc(self, drunk):
#         if drunk not in self.drunks:
#             raise ValueError("Drunk not in field")
#         return self.drunks[drunk]
#
#
# class Drunk(object):
#     def __init__(self, name=None):
#         self.name = name
#
#     def __str__(self):
#         if self != None:
#             return self.name
#         return "Anonymous"
#
#
# class UsualDrunk(Drunk):
#     def takeStep(self):
#         stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         return random.choice(stepChoices)
#
#
# def walk(f, d, numSteps):
#     start = f.getLoc(d)
#     for s in range(numSteps):
#         f.moveDrunk(d)
#     return start.distFrom(f.getLoc(d))
#
#
# def simWalks(numSteps, numTrials, dClass):
#     Homer = dClass()
#     origin = Location(0, 0)
#     distances = []
#     for t in range(numTrials):
#         f = Field()
#         f.addDrunk(Homer, origin)
#         distances.append(round(walk(f, Homer, numSteps), 1))
#     return distances
#
#
# def drunkTest(walkLengths, numTrials, dClass):
#     for numSteps in walkLengths:
#         distances = simWalks(numSteps, numTrials, dClass)
#         print(dClass.__name__, "random walk of", numSteps, "steps")
#         print(" Mean = ", round(sum(distances) / len(distances), 4))
#         print(" Max = ", max(distances), "Min = ", min(distances))
#
#
# # drunkTest((10, 100, 1000), 100, UsualDrunk)
#
#
# class ColdDrunk(Drunk):
#     def takeStep(self):
#         stepChoices = [(0.0, 1.0), (0.0, -2.0), (1.0, 0.0), (-1.0, 0.0)]
#         return random.choice(stepChoices)
#
#
# class EWDrunk(Drunk):
#     def takeStep(self):
#         stepChoices = [(1.0, 0.0), (-1.0, 0.0)]
#         return random.choice(stepChoices)
#
#
# def simAll(drunkKinds, walkLengths, numTrials):
#     for dClass in drunkKinds:
#         drunkTest((walkLengths), numTrials, dClass)
#
#
# # simAll((UsualDrunk, ColdDrunk, EWDrunk), (100, 1000), 10)
#
#
# class styleIterator(object):
#     def __init__(self, styles):
#         self.index = 0
#         self.styles = styles
#
#     def nextStyle(self):
#         result = self.styles[self.index]
#         if self.index == len(self.styles) - 1:
#             self.index = 0
#         else:
#             self.index += 1
#         return result
#
#
# def simDrunk(numTrials, dClass, walkLengths):
#     meanDistances = []
#     for numSteps in walkLengths:
#         print("Starting simulation of", numSteps, "steps")
#         trials = simWalks(numSteps, numTrials, dClass)
#         mean = sum(trials) / len(trials)
#         meanDistances.append(mean)
#     return meanDistances
#
#
# import pylab
#
#
# def simAll1(drunkKinds, walkLengths, numTrials):
#     styleChoice = styleIterator(("m-", "r:", "k-."))
#     for dClass in drunkKinds:
#         curStyle = styleChoice.nextStyle()
#         print("Starting simulation of", dClass.__name__)
#         means = simDrunk(numTrials, dClass, walkLengths)
#         pylab.plot(walkLengths, means, curStyle, label=dClass.__name__)
#         pylab.title("Mean Distance from Origin (" + str(numTrials) + " trials)")
#         pylab.xlabel("Number of Steps")
#         pylab.ylabel("Distance from Origin")
#         pylab.legend(loc="best")
#         pylab.semilogx()
#         pylab.semilogy()
#
#
# # simAll1((UsualDrunk, ColdDrunk, EWDrunk), (10, 100, 1000, 10000), 100)
# # pylab.show()
#
#
# def getFinalLocs(numSteps, numTrials, dClass):
#     locs = []
#     d = dClass()
#     for t in range(numTrials):
#         f = Field()
#         f.addDrunk(d, Location(0, 0))
#         for s in range(numSteps):
#             f.moveDrunk(d)
#         locs.append(f.getLoc(d))
#     return locs
#
#
# def plotLocs(drunkKinds, numSteps, numTrials):
#     styleChoice = styleIterator(("k+", "r^", "mo"))
#     for dClass in drunkKinds:
#         locs = getFinalLocs(numSteps, numTrials, dClass)
#         xVals, yVals = [], []
#         for loc in locs:
#             xVals.append(loc.getX())
#             yVals.append(loc.getY())
#         meanX = sum(xVals)/len(xVals)
#         meanY = sum(yVals)/len(yVals)
#         curStyle = styleChoice.nextStyle()
#         pylab.plot(xVals, yVals, curStyle, label = dClass.__name__ + " mean loc. = <" + str(meanX) + ", " + str(meanY) + ">")
#     pylab.title("Location at End of Walks (" + str(numSteps) + " steps)")
#     pylab.xlabel("Steps East/West of Origin")
#     pylab.ylabel("Steps North/South of Origin")
#     pylab.legend(loc = "lower left")
#
#
# # plotLocs((UsualDrunk, ColdDrunk, EWDrunk), 100, 200)
# # pylab.show()
#
#
# def traceWalk(drunkKinds, numSteps):
#     styleChoice = styleIterator(("k+", "r^", "mo"))
#     f = oddField(1000, 100, 200)
#     for dClass in drunkKinds:
#         d = dClass()
#         f.addDrunk(d, Location(0, 0))
#         locs = []
#         for s in range(numSteps):
#             f.moveDrunk(d)
#             locs.append(f.getLoc(d))
#         xVals, yVals = [], []
#         for loc in locs:
#             xVals.append(loc.getX())
#             yVals.append(loc.getY())
#         curStyle = styleChoice.nextStyle()
#         pylab.plot(xVals, yVals, curStyle, label = dClass.__name__)
#         pylab.title("Spots visited on Walk (" + str(numSteps) + " steps)")
#         pylab.xlabel("Steps East/West of Origin")
#         pylab.ylabel("Steps North/South of Origin")
#         pylab.legend(loc = "best")
#
#
# # traceWalk((UsualDrunk, ColdDrunk, EWDrunk), 200)
# # pylab.show()
#
#
# class oddField(Field):
#     def __init__(self, numHoles, xRange, yRange):
#         Field.__init__(self)
#         self.wormholes = {}
#         for w in range(numHoles):
#             x = random.randint(-xRange, xRange)
#             y = random.randint(-yRange, yRange)
#             newX = random.randint(-xRange, xRange)
#             newY = random.randint(-yRange, yRange)
#             newLoc = Location(newX, newY)
#             self.wormholes[(x, y)] = newLoc
#
#     def moveDrunk(self, drunk):
#         Field.moveDrunk(self, drunk)
#         x = self.drunks[drunk].getX()
#         y = self.drunks[drunk].getY()
#         if (x, y) in self.wormholes:
#             self.drunks[drunk] = self.wormholes[(x, y)]
#
# traceWalk((UsualDrunk, ColdDrunk, EWDrunk), 500)
# pylab.show()


## Inferential Statistics
# import random
# from numpy import histogram_bin_edges
# import pylab
# import time
#
#
# def flip(numFlips):
#    heads = 0
#    for i in range(numFlips):
#        if random.choice(("H", "T")) == "H":
#            heads += 1
#    return heads / numFlips
#
#
# def flipSim(numFlipsPerTrial, numTrials):
#    fracHeads = []
#    for i in range(numTrials):
#        fracHeads.append(flip(numFlipsPerTrial))
#    mean = sum(fracHeads) / len(fracHeads)
#    return mean
#
#
# def regressToMean(numFlips, numTrials):
#    fracHeads = []
#    for t in range(numTrials):
#        fracHeads.append(flip(numFlips))
#    extremes, nextTrials = [], []
#    for i in range(len(fracHeads) - 1):
#        if fracHeads[i] < 0.33 or fracHeads[i] > 0.66:
#            extremes.append(fracHeads[i])
#            nextTrials.append(fracHeads[i + 1])
#    pylab.plot(range(len(extremes)), extremes, "ko", label="Extreme")
#    pylab.plot(range(len(nextTrials)), nextTrials, "k^", label="Next Trial")
#    pylab.axhline(0.5)
#    pylab.ylim(0, 1)
#    pylab.xlim(-1, len(extremes) + 1)
#    pylab.xlabel("Extreme Example and Next Trial")
#    pylab.ylabel("Fraction Heads")
#    pylab.title("Regression to the Mean")
#    pylab.legend(loc="best")
#
#
## regressToMean(15, 50)
## pylab.show()
#
#
# def flipPlot(minExp, maxExp):
#    ratios, diffs, xAxis = [], [], []
#    for exp in range(minExp, maxExp + 1):
#        xAxis.append(2 ** exp)
#    for numFlips in xAxis:
#        numHeads = 0
#        for n in range(numFlips):
#            if random.choice(("H", "T")) == "H":
#                numHeads += 1
#        numTails = numFlips - numHeads
#        try:
#            ratios.append(numHeads / numTails)
#            diffs.append(abs(numHeads - numTails))
#        except ZeroDivisionError:
#            continue
#    pylab.title("Difference between Heads and Tails")
#    pylab.xlabel("Number of Flips")
#    pylab.ylabel("Abs(#Heads - #Tails)")
#    pylab.plot(xAxis, diffs, "ko")
#    pylab.semilogx()
#    pylab.semilogy()
#    pylab.figure()
#    pylab.title("Heads/Tails Ratios")
#    pylab.xlabel("Number of Flips")
#    pylab.ylabel("#Heads/#Tails")
#    pylab.plot(xAxis, ratios, "ko")
#    pylab.semilogx()
#
#
## random.seed(0)
## flipPlot(4, 20)
## pylab.show()
#
#
# def variance(X):
#    mean = sum(X) / len(X)
#    tot = 0.0
#    for x in X:
#        tot += (x - mean) ** 2
#    return tot / len(X)
#
#
# def stdDev(X):
#    return variance(X) ** 0.5
#
#
#
#
# def makePlot(xVals, yVals, title, xLabel, yLable, style, logX=False, logY=False):
#    pylab.figure()
#    pylab.title(title)
#    pylab.xlabel(xLabel)
#    pylab.ylabel(yLable)
#    pylab.plot(xVals, yVals, style)
#    if logX:
#        pylab.semilogx()
#    if logY:
#        pylab.semilogy()
#
#
# def runTrial(numFLips):
#    numHeads = 0
#    for n in range(numFLips):
#        if random.choice(("H", "T")) == "H":
#            numHeads += 1
#    numTails = numFLips - numHeads
#    return (numHeads, numTails)
#
#
# def flipPlot1(minExp, maxExp, numTrials):
#    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
#    xAxis = []
#    for exp in range(minExp, maxExp + 1):
#        xAxis.append(2 ** exp)
#    for numFlips in xAxis:
#        ratios, diffs = [], []
#        for t in range(numTrials):
#            numHeads, numTails = runTrial(numFlips)
#            ratios.append(numHeads / numTails)
#            diffs.append(abs(numHeads - numTails))
#        ratiosMeans.append(sum(ratios) / numTrials)
#        diffsMeans.append(sum(diffs) / numTrials)
#        ratiosSDs.append(stdDev(ratios))
#        diffsSDs.append(stdDev(diffs))
#    numTrialsString = " (" + str(numTrials) + " Trials)"
#    title = "Mean Heads/Tails Ratios" + numTrialsString
#    makePlot(
#        xAxis,
#        ratiosMeans,
#        title,
#        "Number of flips",
#        "Mean Heads/Tails",
#        "ko",
#        logX=True,
#    )
#    title = "SD Heads/Tails Ratios" + numTrialsString
#    makePlot(
#        xAxis,
#        ratiosSDs,
#        title,
#        "Number of FLips",
#        "Standard Deviation",
#        "ko",
#        logX=True,
#        logY=True,
#    )
#    title = "Mean abs(#Heads - #Tails)" + numTrialsString
#    makePlot(
#        xAxis,
#        diffsMeans,
#        title,
#        "Number of Flips",
#        "Mean abs(#Heads - #Tails)",
#        "ko",
#        logX=True,
#        logY=True,
#    )
#    title = "SD abs(#Heads - Tails)" + numTrialsString
#    makePlot(
#        xAxis,
#        diffsSDs,
#        title,
#        "Number of Flips",
#        "Standard Deviation",
#        "ko",
#        logX=True,
#        logY=True,
#    )
#
#
## # start_time = time.time()
## flipPlot1(4, 20, 20)
## # print("--- %s seconds ---" % (time.time() - start_time))
## pylab.show()
#
#
# def CV(X):
#    mean = sum(X) / len(X)
#    try:
#        return stdDev(X) / mean
#    except ZeroDivisionError:
#        return float("nan")
#
#
# def flipPlot2(minExp, maxExp, numTrials):
#    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
#    ratiosCVs, diffsCVs, xAxis = [], [], []
#    for exp in range(minExp, maxExp + 1):
#        xAxis.append(2 ** exp)
#    for numFlips in xAxis:
#        ratios, diffs = [], []
#        for t in range(numTrials):
#            numHeads, numTails = runTrial(numFlips)
#            ratios.append(numHeads / float(numTails))
#            diffs.append(abs(numHeads - numTails))
#        ratiosMeans.append(sum(ratios) / numTrials)
#        diffsMeans.append(sum(diffs) / numTrials)
#        ratiosSDs.append(stdDev(ratios))
#        diffsSDs.append(stdDev(diffs))
#        ratiosCVs.append(CV(ratios))
#        diffsCVs.append(CV(diffs))
#    numTrialsString = " (" + str(numTrials) + " Trials)"
#    title = "Mean Heads/Tails Ratios" + numTrialsString
#    makePlot(
#        xAxis,
#        ratiosMeans,
#        title,
#        "Number of flips",
#        "Mean Heads Tails",
#        "ko",
#        logX=True,
#    )
#    title = "SD Heads/Tails Ratios" + numTrialsString
#    makePlot(
#        xAxis,
#        ratiosSDs,
#        title,
#        "Number of flips",
#        "Standard Deviation",
#        "ko",
#        logX=True,
#        logY=True,
#    )
#    title = "Mean abs(#Heads - #Tails)" + numTrialsString
#    makePlot(
#        xAxis,
#        diffsMeans,
#        title,
#        "Number of Flips",
#        "Mean abs(#Heads - #Tails)",
#        "ko",
#        logX=True,
#        logY=True,
#    )
#    title = "SD abs(#Heads - #Tails)" + numTrialsString
#    makePlot(
#        xAxis,
#        diffsSDs,
#        title,
#        "Number of Flips",
#        "Standard Deviation",
#        "ko",
#        logX=True,
#        logY=True,
#    )
#    title = "Coeff. of Var. Heads/Tails Ratio" + numTrialsString
#    makePlot(
#        xAxis,
#        ratiosCVs,
#        title,
#        "Number of Flips",
#        "Coeff. of Var.",
#        "ko",
#        logX=True,
#        logY=True,
#    )
#    title = "Coeff. of Var. abs(#Heads - #Tails)" + numTrialsString
#    makePlot(
#        xAxis,
#        diffsCVs,
#        title,
#        "Number of Flips",
#        "Coeff. of Var.",
#        "ko",
#        logX=True,
#        logY=False,
#    )
#
#
## start_time = time.time()
## flipPlot2(4, 20, 20)
## print("--- %s seconds ---" % (time.time() - start_time))
## pylab.show()
#
#
# def flip(numFlips):
#    heads = 0
#    for i in range(numFlips):
#        if random.choice(("H", "T")) == "H":
#            heads += 1
#    return heads / float(numFlips)
#
#
# def flipSim(numFlipsPerTrial, numTrials):
#     fracHeads = []
#     for i in range(numTrials):
#         fracHeads.append(flip(numFlipsPerTrial))
#     mean = sum(fracHeads) / len(fracHeads)
#     sd = stdDev(fracHeads)
#     return (fracHeads, mean, sd)
#
#
#
#
# def labelPlot(numFlips, numTrials, mean, sd):
#    pylab.title(str(numTrials) + " trials of " + str(numFlips) + " flips each")
#    pylab.xlabel("Fraction of Heads")
#    pylab.ylabel("Number of Trials")
#    pylab.annotate(
#        "Mean = " + str(round(mean, 4)) + " \nSD = " + str(round(sd, 4)),
#        size="medium",
#        xycoords="axes fraction",
#        xy=(0.75, 0.5),
#    )
#
#
# def makePlots(numFlips1, numFlips2, numTrials):
#    val1, mean1, sd1 = flipSim(numFlips1, numTrials)
#    pylab.hist(val1, bins=20, edgecolor="black")
#    xmin, xmax = pylab.xlim()
#    labelPlot(numFlips1, numTrials, mean1, sd1)
#    pylab.figure()
#    val2, mean2, sd2 = flipSim(numFlips2, numTrials)
#    pylab.hist(val2, bins=20, edgecolor="black")
#    pylab.xlim(xmin, xmax)
#    labelPlot(numFlips2, numTrials, mean2, sd2)
#
#
# start_time = time.time()
# makePlots(100, 1000, 100000)
# print("--- %s seconds ---" % (time.time() - start_time))
# pylab.show()
#
#
# from numpy import flip
# import scipy.integrate
# import pylab
# import random
#
#
# def guassian(x, mu, sigma):
#     factor1 = 1.0 / (sigma * ((2 * pylab.pi) ** 0.5))
#     factor2 = pylab.e ** -(((x - mu) ** 2) / (2 * sigma ** 2))
#     return factor1 * factor2
#
#
# def checkEmperical(numTrials):
#     for t in range(numTrials):
#         mu = random.randint(-10, 10)
#         sigma = random.randint(1, 10)
#         print("For mu =", mu, "and sigma =", sigma)
#         for numStd in (1, 2, 3):
#             area = scipy.integrate.quad(
#                 guassian, mu - numStd * sigma, mu + numStd * sigma, (mu, sigma)
#             )[0]
#             print(
#                 "  Fraction within", numStd, "std = ", str(round(area * 100, 2)) + "%"
#             )
#
#
# checkEmperical(3)
#
#
# def showErrorBars(minExp, maxExp, numTrials):
#     means, sds, xVals = [], [], []
#     for exp in range(minExp, maxExp + 1):
#         xVals.append(2 ** exp)
#         fracHeads, mean, sd = flipSim(2 ** exp, numTrials)
#         means.append(mean)
#         sds.append(sd)
#     pylab.errorbar(xVals, means, yerr=1.96 * pylab.array(sds))
#     pylab.semilogx()
#     pylab.title("Mean Fraction of Heads (" + str(numTrials) + " trials)")
#     pylab.xlabel("Number of flips per trial")
#     pylab.ylabel("Fraction of heads & 95% confidence")
#
#
# showErrorBars(3, 10, 100)
# pylab.show()


## Exponential and Geometric Distributions
# import pylab
# import random
#
#
# def clear(n, p, steps):
#    numRemaning = []
#    for t in range(steps):
#        numRemaning.append(n * ((1 - p) ** t))
#    pylab.plot(numRemaning)
#    pylab.xlabel("Time")
#    pylab.ylabel("Molecules Remaining")
#    pylab.title("Clearence of Drug")
#
#
## clear(1000, 0.01, 1000)
## pylab.show()
#
#
# def successfulStarts(successProb, numTrials):
#    triesBeforeSuccess = []
#    for t in range(numTrials):
#        consecFailures = 0
#        while random.random() > successProb:
#            consecFailures += 1
#        triesBeforeSuccess.append(consecFailures)
#    return triesBeforeSuccess
#
#
## probOfSuccess = 0.5
## numTrials = 5000
## distribution = successfulStarts(probOfSuccess, numTrials)
## pylab.hist(distribution, bins = 14, edgecolor="black")
## pylab.xlabel("Tries Before Success")
## pylab.ylabel("Number of Occuerrences Out of " + str(numTrials))
## pylab.title("Probability of Starting Each Try = " + str(probOfSuccess))
## pylab.show()
#
#
# def collisionProb(n, k):
#    prob = 1.0
#    xVals, yVals = [], []
#    for i in range(1, k + 1):
#        xVals.append(i)
#        prob = prob * ((n - i) / n)
#        yVals.append(1 - prob)
#    pylab.plot(xVals, yVals, "k:")
#
#
## collisionProb(366, 100)
## pylab.show()
#
#
# def simInsertions(numIndices, numInsertions):
#    choices = range(numIndices)
#    used = []
#    for i in range(numInsertions):
#        hashVal = random.choice(choices)
#        if hashVal in used:
#            return 1
#        else:
#            used.append(hashVal)
#    return 0
#
#
# def findProb(numIndices, numInsertions, numTrials):
#    collisions = 0
#    for t in range(numTrials):
#        collisions += simInsertions(numIndices, numInsertions)
#    return collisions / numTrials
#
#
## print("Actual probability of a collision =", collisionProb(1000, 50))
## print("Est. probabilty of a collision =", findProb(1000, 50, 10000))
## print("Actual probability of a collision =", collisionProb(1000, 200))
## print("Est. probabilty of a collision =", findProb(1000, 200, 10000))
#
#
## How often does the better team win? (World Series Simulation)
# def playSeries(numGames, teamProb):
#    numWon = 0
#    for game in range(numGames):
#        if random.random() <= teamProb:
#            numWon += 1
#    return numWon > numGames // 2
#
#
# def fractionWon(teamProb, numSeries, seriesLen):
#    won = 0
#    for series in range(numSeries):
#        if playSeries(seriesLen, teamProb):
#            won += 1
#    return won / float(numSeries)
#
#
# def simSeries(numSeries):
#    prob = 0.5
#    fracsWon, probs = [], []
#    while prob <= 1.0:
#        fracsWon.append(fractionWon(prob, numSeries, 7))
#        probs.append(prob)
#        prob += 0.01
#    pylab.axhline(0.95)
#    pylab.plot(probs, fracsWon, "k", linewidth=3)
#    pylab.xlabel("Probability of Winning a Game")
#    pylab.ylabel("Probability of Winning a Series")
#    pylab.title(str(numSeries) + " Seven Game Series")
#
#
## simSeries(500)
## pylab.show()



# MONTE CARLO SIMULATION