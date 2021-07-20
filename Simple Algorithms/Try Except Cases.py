def getGrades(fname):
   try:
       gradesFile = open(fname, 'r') #open file for reading
   except IOError:
       raise ValueError('getGrades could not open ' + fname)
   grades = []
   for line in gradesFile:
       try:
           grades.append(float(line))
       except:
           raise ValueError('Unable to convert line to float')
   return grades

try:
   grades = getGrades('quiz1grades.txt')
   grades.sort()
   median = grades[len(grades)//2]
   print('Median grade is', median)
   assert median == 49.0, "Are you sure it is not 49.0?"
except ValueError as errorMsg:
   print('Whoops.', errorMsg)
except AssertionError as error:
   print(error)