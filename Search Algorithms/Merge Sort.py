# Taking an input from digits.txt of 10,000 values, 
# ranging from - Billion to + Billion,
# sorted using the Merge Sort Algorithm
import time

#List Converter
with open('digits.txt') as f:
    content = f.readlines()
content = [x.strip() and int(x) for x in content]


#Merge Sorting Algorithm
def merge(left, right, compare):
    
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result
    
def mergeSort(L, compare = lambda x, y: x < y):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)

start_time = time.time()
sortedL = mergeSort(content)
print(sortedL)
print('--- %s seconds ---' % (time.time()-start_time))