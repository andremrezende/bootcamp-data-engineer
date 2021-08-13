a = [float(x) for x in input().split()]
if a[0] + a[1] > a[2] and a[1] + a[2] > a[0] and a[0] + a[2] > a[1]:
  p = sum(a)
  print("Perimetro = {}".format(p))
else:
  area = ((a[0] + a[1])*a[2])/2.0
  print("Area = {}".format(area))