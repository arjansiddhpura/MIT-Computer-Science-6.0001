def copy(L1, L2):
   """Assumes L1, L2 are lists
   Mutates L2 to be a copy of L1"""
   if L1 != L2:
       while len(L2) > 0: #remove all elements from L2
           L2.pop() #remove last element of L2
       for e in L1: #append L1's elements to initially empty L2
           L2.append(e)
   else:
       print("given lists are the same, no copying necessary")

Ly=[1, 3, 5, 7, 9, 11, 13, 15]
Lz=[2, 4, 6, 8, 10, 12, 14, 16]

print(Lz)
copy(Ly, Lz)
print(Lz)