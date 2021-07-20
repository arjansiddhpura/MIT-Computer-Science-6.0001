# Integer to String Convertor
def intToStr(i):
   digits = '0123456789'
   result = ''
   if i == 0:
       return '0'
   while i > 0:
       result = digits[i%10] + result
       i //= 10
   return result

def addDigits(n):
   stringRep = intToStr(n)
   val = 0
   for c in stringRep:
       val += int(c)
   return val

print(addDigits(123))