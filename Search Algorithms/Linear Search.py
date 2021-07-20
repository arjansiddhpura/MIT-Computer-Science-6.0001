# Linear Search of a Sorted List
def search(L, e):
   for i in range(len(L)):
       if L[i] == e:
           return True
       if L[i] > e:
           return False
   return False

L=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(search(L, 12))