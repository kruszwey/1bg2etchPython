# Zad 1
# a, b, c = int(input()), int(input()),int(input())
# if c - b == b - c:
#     print("ciąg jest arytmetyczny")
# else:
#     print("ciąg nie jest arytmetyczny")
# if  c / b == b / a :
#     print("ciąg jest geometryczny")
# else:
#     print("ciąg nie jest geometryczny")
# if c > b and c > a and b > a:
#     print("Ciąg jest rosnący")
# elif c < b and c < a and b < a:
#     print("ciąg jest malejący")


# Zad 2

# suma = 0
# for i in range(100,1000):
#     if i % 8 == 0 and i % 16 != 0:
#         suma += i

# print(suma)

# Zad 3
# for i in range(10,100):
#     if i % 7 == 0:
#         wielokrotonosc = i
# ilosc = 0
# for i in range(1000,10000):
#     if i % wielokrotnosc == 0:
#         ilosc += 1
# print(ilosc)

# Zad 4
# ilosc = 0
# for i in range(10,100):
#   cd = i // 10
#   cj = i % 10
#   if cd >= 2 * cj:
#     ilosc = ilosc + 1
# print(ilosc)

# Zad 5

# print((456 // 10) % 10)


# Zad 6
# n = int(input())

# opcja 1
# n = int(input())
# licznik = 0 
# suma = 0
# i = 10
# while True:
#   if i % 19 == 0:
#     suma = suma + i 
#     licznik = licznik + 1
#   if licznik == n:
#     break
#   i = i + 1
# print(suma)

# Opcja 2
# n = int(input())
# licznik = 0 
# suma = 0
# for i in range(10,100):
#    if i % 19 == 0:
#      suma = suma + i
#      licznik = licznik + 1
#     if licznik == n:
#       brak
# print(suma)

#  opcja 3 
# n = int(input())
# suma = 0
# for i in range(19, 19 + n + 1,19):
#   suma = suma + i
# print(suma)

# Opcja 4
# n = int(input())
# for i in range(1, n+1):
#   suma = suma + 19*i
# print(suma)

# ZAD 7
# opcja 1
# n = int(input())
# suma = 0
# for i in range(999-(999 % 37), 999-(999 % 37) - (37*n), -37):
#   suma = suma + i 
# print(suma)

# Opcja 2 
# n =int(input())
# suma = 0
# licznik = 0
# for i in range(999,99,-1):
#   if i % 37 == 0:
#     suma = suma + i
#     licznik = licznik +1
#     if licznik == n:
#       break
# print(suma)
