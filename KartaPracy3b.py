from os import system
from math import sqrt, floor
# Zad 1

# wszystkie dni tygodnia - lista

# dniTygodnia = [
#     'Poniedziałek',
#     'Wtorek',
#     'Środa',
#     'Czwartek',
#     'Piątek',
#     'Sobota',
#     'Niedziela'
# ]

# print('Wszystkie dni listopada 2022 roku:\n')

# for i in range(1, 31, 1):
#     print(f'{i}.11.2022 - {dniTygodnia[i%7]}')

# -- Zad 1

# print()

# Zad 2
# print('Kwadraty liczb nieparzystych:\n')

# for i in range(1,11,1):
#     if i % 2 > 0:
#         print(f'{i}^2 = {i*i}')

 # -- Zad 2

# print()

# Zad 3
# print('Wszytkie liczby czterocyfrowe podzielne przez 379:\n')

# for i in range(1000,10000,1):
#     if i % 379 == 0:
#         print(f'{i} % 379 == 0')

# -- Zad 3

# print()

# Zad 4
# print('Wszytkie liczby trzycyfrowe podzielne przez 5,6 lub 11:\n')
# for i in range(100, 1000, 1):
#     if i%5==0:
#         print(f'{i} % 5 == 0')
#     if i%6 == 0:
#         print(f'{i} % 6 == 0')
#     if i%11 == 0:
#         print(f'{i} % 11 == 0')
# -- Zad 4

# print()

# Zad 5
# n = int(input('podaj n: '))
# suma = 0

# for i in range(n):
#     suma += int(input(f'podaj liczbę nr {i+1}: '))
# print(f'suma: {suma}')
# # -- Zad 5

# print()

# Zad 6
# k = int(input('podaj k: '))
# suma = 0

# for i in range(1,k,1):
#     if i % 2 == 0:
#         suma += i
# print(f'suma: {suma}')
# -- Zad 6

# print()

# Zad 7
# m = int(input('podaj m: '))
# suma = 0

# for i in range(1,m,1):
#     if i % 2 > 0:
#         suma += i
# print(f'suma: {suma}')
# -- Zad 7

# print()

#Zad 8
# W0 = int(input("Podaj początkową wartość inwestycji:"))
# L = int(input("Podaj lata inwestycji:"))
# Wk = 0
# suma = Wk
# for i in range(0,L * 12):
#   Wk = suma * 0.06 * (1/12)
#   suma = suma+Wk
# print("Końcowa wartość inweestycji wynosi:")
# print(suma)

# Zad 9
# n = int(input('podaj n: '))
# suma = 0

# for i in range(1,n,1):
#     if i % 100 == 21:
#         suma += i
# print(f'suma: {suma}')


# -- Zad 9

# print()

# Zad 10

# for i in range(1,1001):
#     pierwiastek = floor(sqrt(i))
#     if i % 10 == pierwiastek:
#         print(i)


 # -- Zad 10





# Zad 8
# procent = 6 
# L = float(input("Podaj długość trwania inwestycji: "))
# W0 = int(input("Podaj ile kasy wrzucasz na inwestycje: "))
# W = W0

# for i in range(int(L*12)):
#   W = W*(1+(procent/12)/100)
# print(W)




