x = int(input())
for i in range (0,10):
  if (i <= 0):
       print ("N[%i] = %i" %(i, x))
  elif (1 <= i < 10):
       square = x*(2**(i))
       print("N[%i] = %i" %(i, square))