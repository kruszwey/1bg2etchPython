# Zad 1
# n = int(input())
# suma = 0
# while n > 0:
#     cyfra = n % 10
#     suma = suma + cyfra
#     n = n // 10
# print(suma)

# Zad 2

# wersja 1
# n = int(input())
# flaga = True 
# for i in range(2,n):
#   if n % i == 0:
#     flaga = False
# if flaga == True:
#   print("Tak")
# else:
#   print("Nie")

# WERSJA 2
# n = int(input())
# for i in range(2,n):
#   if n % i == 0:
#     print("NIE")
#     exit(0)
# print("TAK")

# WERSJA 3
# n = int(input())
# suma = 0
# for i in range(2, n):
#   if n % i == 0:
#     suma + suma + i
# if suma == 0:
#   print("TAK")
# else:
#   print("NIE")

# Zad 3
# n = int(input())
# suma = 0
# for i in range(1, n):
#   if n % i == 0:
#     suma + suma + i
# if suma == n:
#   print("TAK, jest doskonała")
# else:
#   print("NIE, nie jest doskonała")

# Zad 4
# a, b = int(input()), int(input())
# while b > 0:
#   a,b = b, a%b

# if a == 1:
#   print("Tak, są wzglądnie pierwsze")
# else:
#   print("Nie, są względnie pierwsze")

# Zad 5
# m = int(input())

# for i in range(10,20):
#   x, y = i, m
#   while y > 0:
#    x, y = y, x % y 
#   if x == 1:
#     print(f"Tak, {i} i {m} są wzglądnie pierwsze")
# else:
#   print(f"Nie, {i} i {m} są względnie pierwsze")


