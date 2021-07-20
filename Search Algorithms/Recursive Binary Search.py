# Recursive Binary Search
def search(L, e):
   """Assumes L is a sorted list in ascending order"""

   def bSearch(L, e, low, high):
       #Decrements high - low
       if high == low:
           return L[low] == e
       mid = (low + high)//2
       if L[mid] == e:
           return True
       elif L[mid] > e:
           if low == mid: #Nothing left to search
               return False
           else:
               return bSearch(L, e, mid + 1, high)

   if len(L) == 0:
       return False
   else:
       return bSearch(L, e, 0, len(L) - 1)