import math
a = int(input("Podaj a "))
g = int(input("Podaj g "))
if (a+g) / 2 > math.sqrt(a*g):
  print("Tak")
else:
  print("Nie")