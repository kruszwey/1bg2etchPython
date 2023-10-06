# Liczby pierwsze
# n = int(input("Podaj liczbę: "))
# if n<=2:
#   print("NIE")
# else:
#   for i in range(2, n):
#     if n % i == 0:
#       print("NIE")
#       break
#   else:
#     print("TAK") 
# liczby pierwsze zakres od N do E
# n = int(input()) 
# e = int(input()) 
# for i in range(n,e+1):
#   flaga = True;
#   for j in range(2,i):
#     if i%j==0:
#       flaga = False
#       break
#   if flaga:
#     print(i, end=" ")

# NWD

# a = int(input("podaj liczbe "))
# b = int(input("podaj liczbe "))
# from math import gcd
# print(gcd(a,b))

# NWW
# a=int(input())
# b=int(input())
# from math import gcd
# iloczyn=a*b
# NWD=gcd(a,b)
# NWW=iloczyn//NWD
# print(NWW)

# Ułamki
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# from math import gcd
# x, y = b, d
# iloczyn = x*y
# nwd=gcd(x,y)
# nww=iloczyn//nwd
# e=(nww//b)*a
# f=(nww//d)*c
# g=e+f
# print(f"{g}/{nww}")



# n = int(input("do ilu mam znaleść liczby pierwsze? "))
# for i in range(2,n+1):
#   flaga = True;
#   for j in range(2,i):
#     if i%j==0:
#       flaga = False
#       break
#   if flaga:
#     print(i, end=" ")
