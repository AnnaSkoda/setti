def printMax(x, y):

   x = int(x) #конвертируем в целые,если воможно
   y = int(y)

   if x > y:
       print(x, 'наибольшее')
   else:
       print(y, 'наибольшее')

printMax(3, 5)
print(printMax.__doc__)