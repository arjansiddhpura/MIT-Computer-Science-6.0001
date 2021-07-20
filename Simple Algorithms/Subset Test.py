# Implementation of a Subset Test
def isSubset(L1, L2):
   for e1 in L1:
       matched = False
       for e2 in L2:
           if e1 == e2:
               matched = True
               break
       if not matched:
           return False
   return True

print(isSubset(L1=[5, 3], L2=[1, 2, 3, 4, 5]))