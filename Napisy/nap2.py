# anagramy np adam dama mada amda aamd

# a = input()
# b = input()
# x, y = list(a), list(b)
# x.sort()
# y.sort()
# a = "".join(x)
# b = "".join(y)
# if a == b:
#   print("TAK")
# else:
#   print("NIE")

# anagramy przez tablice

a = input()
b = input()
X = [0] * 200
Y = [0] * 200
print(X)
for i in range(len(a)):
  X[ord(a[i])] +=1
for j in range(len(b)):
  Y[ord(a[i])] +=1
  print(X)
  if X == Y:
    print("Tak")
  else:
    print("Nie")