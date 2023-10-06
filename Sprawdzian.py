# Zad 1 # 4G3E2T6W3H
# W = " GGGGEEETTWWWWWWHHH"
# W = W + "."
# ilosc = 1
# H =" "
# for i in range(len(W)-1):
#   if W[i] == W[i+1]:
#     ilosc += 1
#   else:
#     if ilosc > 1:
#       H +=str(ilosc)
#     H += W[i]
#     ilosc = 1
# print("Wersja w Huffmanie:",H)


# Zad 2
# a,b,c,d,e,f = int(input("Podaj pierwszą liczbe: ")),int(input("Podaj drugą liczbe: ")),int(input("Podaj trzecią liczbe: ")),int(input("Podaj czwartą liczbe: ")),int(input("Podaj piątą liczbe: ")),int(input("Podaj szóstą liczbe: "))
# from math import gcd
# y,x = b,d
# iloczyn = x * y 
# NWD = gcd(x,y)
# NWW = iloczyn // NWD
# g = (NWW//b) * a
# h = (NWW//d) * c
# l = (NWW//f) * e
# m = (NWW//d) * g
# j = g+h
# k = l+m
# print(f"{j},{k}/{NWW}")