# WSTĘP


# 1.Oblicz sumę liczb 3-cyfrowych

# suma = 0
# for liczba in range(100, 1000):
#     suma += liczba
# print("Suma liczb 3-cyfrowych: ", suma)

# 2.Oblicz sumę  i ilość  dwucyfrowych wielokrotności liczby 6.

# suma = 0
# ilosc = 0
# for liczba in range(10, 100):
#     if liczba % 6 == 0:
#         suma += liczba
#         ilosc += 1
# print("Suma dwucyfrowych wielokrotności liczby 6: ", suma)
# print("Ilość dwucyfrowych wielokrotności liczby 6: ", ilosc)

# 3. znajdź największą liczbę wśród  5 wylosowanych przez program liczb 4 - cyfrowych

# import random
# liczby = [random.randint(1000, 10000) for _ in range(5)]
# najwieksza = max(liczby)
# print("Wylosowane liczby: ", liczby)
# print("Największa liczba: ", najwieksza)

# 4 Podaj  sumę cyfr  w dowolnej liczbie

# liczba = input("Podaj liczbę: ")
# suma = 0
# for cyfra in liczba:
#     suma += int(cyfra)
# print("Suma cyfr w liczbie:", suma)

# 5 Znajdz najmniejszą cyfrę we wpisanej przez usera liczbie 3-cyfrowej

# a = input("Podaj liczbe 3 cyfrową: ")
# n = min(a)
# print(n)



# ALGORYTMY

# 1 Sprawdz czy wpisana przez usera liczba jest pierwsza

# liczba = int(input("Podaj liczbę: "))
# if liczba < 2:
#     print("Liczba jest złożona")
# else:
#     for i in range(2, int(liczba ** 0.5) + 1):
#         if liczba % i == 0:
#             print("Liczba jest złożona")
#             break
#     else:
#         print("Liczba jest pierwsza ")

# 2 Sprawdz czy wpisana przez usera liczba jest złożona

# liczba = int(input("Podaj liczbę: "))

# if liczba < 2:
#     print("Liczba jest złożona")
# else:
#     for i in range(2, int(liczba ** 0.5) + 1):
#         if liczba % i == 0:
#             print("Liczba jest złożona")
#             break
#         else:
#              print("Liczba jest pierwsza")
# 3 Sprawdz czy wpisana przez usera liczba jest względnie pierwsza z 24

# liczba = int(input("Podaj liczbę: "))
# def nwd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
# if nwd(liczba, 24) == 1:
#     print("Liczba jest względnie pierwsza z 24")
# else:
#     print("Liczba nie jest względnie pierwsza z 24")


# 4 Zakoduj szyfrem cezara i kluczem k słowo s
# def cezar(tekst, alfabet, klucz):
#     wynik = ""
#     DLT = len(tekst)
#     DLA = len(alfabet)
#     for i in range(DLT):
#         for j in range(DLA):
#             if tekst[i] == alfabet[j]:
#                 wynik += alfabet[(j + klucz) % DLA]
#     return wynik
# print(cezar("S", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3))

# 5 Dodaj dwa ułamki a/b + c/d. Zapisz sumę jako ułamek nieskracalny i liczbe mieszaną 

# def znajdz_najwiekszy_wspolny_dzielnik(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# def dodaj_ulamki(a, b, c, d):
#     wspolny_mianownik = b * d
#     licznik = a * d + c * b

#     najwiekszy_wspolny_dzielnik = znajdz_najwiekszy_wspolny_dzielnik(licznik, wspolny_mianownik)

#     skrocony_licznik = licznik // najwiekszy_wspolny_dzielnik
#     skrocony_mianownik = wspolny_mianownik // najwiekszy_wspolny_dzielnik

#     liczba_mieszana = skrocony_licznik // skrocony_mianownik
#     reszta = skrocony_licznik % skrocony_mianownik

#     return skrocony_licznik, skrocony_mianownik, liczba_mieszana, reszta

# a = int(input("Podaj a: "))
# b = int(input("Podaj b: "))
# c = int(input("Podaj c: "))
# d = int(input("Podaj d: "))

# skrocony_licznik, skrocony_mianownik, liczba_mieszana, reszta = dodaj_ulamki(a, b, c, d)

# if liczba_mieszana == 0:
#     print("Suma ułamków:", skrocony_licznik, "/", skrocony_mianownik)
# else:
#     print("Suma ułamków:", liczba_mieszana, "i", reszta, "/", skrocony_mianownik)

# 6 Znajdź NWW dwóch wpisanych przez usera liczb 

# def nwd(a, b):
#     if b == 0:
#         return a
#     return nwd(b, a % b)
# def nww(a, b):
#     return (a * b) // nwd(a, b)
# print("NWW:", nww(int(input()), int(input())))

# Na kartce
# ONP 8822+/234*---


# NAPISY
# 1 Znajdź ilość liter C we wpisanym napisie

# napis = input("Wpisz napis: ")
# ilosc_c = napis.count("c")
# ilosc_C = napis.count("C")
# print("Ilość liter C: ", ilosc_c + ilosc_C)

# 2 Sprawdź czy literki w napisie są w porządku nierosnącym: np ZOO, WOK, WODA itp 

# def ros(a):
#     X = list(a)
#     Y = list(a)
#     X.sort()
#     if X == Y:
#         return False
#     else:
#         return True

# print(ros(input()))


# 3 Podaj najdłuższy z 3 wpisanych przez usera wyrazow

# wyrazy = [input() for _ in range(3)]
# najdluzszy_wyraz = max(wyrazy, key=len)
# print(najdluzszy_wyraz)


# Dodatkowe nie potrzebne koniecznie 



# def znwd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# def dodaj_ulamki(a, b, c, d):
#     wm = b * d
#     licznik = a * d + c * b

#     nwd = znwd(licznik, wm)

#     sl = licznik // nwd
#     sm = wm // wm

#     lm = sl // sm
#     reszta = sl % sm

#     return sl, sm, lm, reszta

# a = int(input("Podaj a: "))
# b = int(input("Podaj b: "))
# c = int(input("Podaj c: "))
# d = int(input("Podaj d: "))

# sl, sm, lm, reszta = dodaj_ulamki(a, b, c, d)

# if lm == 0:
#     print("Suma ułamków:", sl , "/", sm)
# else:
#     print("Suma ułamków:", lm, "i", reszta, "/", sm)