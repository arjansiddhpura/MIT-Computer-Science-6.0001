def cube(x):
   x=x**3
   return x

def applyToEach(L, f):
   for i in range(len(L)):
       L[i]=f(L[i])

L=[1, 2, 3, 4, 5]
print('L= ', L)
print('Apply cube to each element of L.')
applyToEach(L, cube)
print('L= ', L)