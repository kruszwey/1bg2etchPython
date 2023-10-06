T = [50,20,10,5,2,1]
T.sort(reverse=True)
x = int(input("reszta: "))
for i in T:
  ilosc = x // i
  if ilosc > 0:
    x = x - ilosc * i
    print(f"{ilosc}razy{i}")