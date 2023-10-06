#1 wczytaj dowolny napis i wypisz z niego pierwszą i ostatnią 

# napis = input("Wpisz dowolny napis: ")
# print("Pierwszy znak:", napis[0])
# print("Ostatni znak:", napis[-1])


#2 wczytaj dowolny napis i wypisz  z niego literki bez pierwszej i ostatniej  

# napis = input("Wpisz dowolny napis: ")
# litery = napis[1:-1]
# print("Litery bez pierwszej i ostatniej:", litery)


#3 wypisz 4 ostatnie literki z wpisanego napisy w kolejnosci od końca 

# napis = input("Wpisz dowolny napis: ")
# ostatnie_litery = napis[-1:-5:-1]
# print("4 ostatnie litery w kolejności od końca:", ostatnie_litery)


#4 Waga napisu to suma kofów ascii jego liter. znajdz wpisany napis

# napis = input("Wpisz dowolny napis: ")
# waga = 0
# for litera in napis:
#     waga += ord(litera)
# print("Waga napisu to :", waga)



#5 Policz ile we wpisanym napisie jest liter A

# napis = input("Wpisz dowolny napis: ")
# liczba_a = 0
# for litera in napis:
#     if litera == "A" or litera == "a":
#         liczba_a += 1
# print("Liczba liter A w napisie to:", liczba_a)


#6 podaj dominującą literkę we wpisanym napisie, Niech to będzie tylko jedna

# napis = input("Wpisz dowolny napis: ")
# czestotliwosci = {}
# for litera in napis:
#     if litera in czestotliwosci:
#         czestotliwosci[litera] += 1
#     else:
#         czestotliwosci[litera] = 1
# dominujaca_litera = max(czestotliwosci, key=czestotliwosci.get)
# print("Dominująca litera w napisie to:", dominujaca_litera)

# 7 znajdz literkę- dominantę w napisie (może być ich kilka, a może nie być żadniej )

# 8 sprawdz czy w napisie występują trzy pociągi "LA"
# h =input()
# ilosc = 0
# for i in range(len(h)):
#   if h[i:i+2] == "LA":
#     ilosc += 1
# if ilosc == 3:
#   print("Tak")
# else:
#   print("Nie")

# 1 Anagramy

# def czy_anagram(fraza1, fraza2):
#     fraza1 = sorted(fraza1.lower())
#     fraza2 = sorted(fraza2.lower())
#     if fraza1 == fraza2:
#         return True
#     else:
#         return False
# fraza1 = input("Podaj pierwszą frazę: ")
# fraza2 = input("Podaj drugą frazę: ")
# if czy_anagram(fraza1, fraza2):
#     print("Podane frazy są anagramami.")
# else:
#     print("Podane frazy nie są anagramami.")



# 2 Palindromy
# wyraz = input("Podaj wyraz: ")
# def czy_palindrom(wyraz):
#     wyraz = wyraz.lower().replace(" ", "")
#     if wyraz == wyraz[::-1]:
#         return True
#     else:
#         return False
# if czy_palindrom(wyraz):
#     print("Podany wyraz jest palindromem.")
# else:
#     print("Podany wyraz nie jest palindromem.")


# 3 Boyer-Moore 
# def boyer_moore(text, pattern):
#     n = len(text)
#     m = len(pattern)

#     # tworzymy tablice przesunieć
#     shifts = [m] * 256
#     for i in range(m - 1):
#         shifts[ord(pattern[i])] = m - i - 1

#     # przeszukujemy tekst zgodnie z algorytmem Boyer-Moore
#     i = m - 1
#     while i < n:
#         j = m - 1
#         while text[i] == pattern[j]:
#             if j == 0:
#                 return i
#             i -= 1
#             j -= 1
#         i += max(shifts[ord(text[i])], m - j)

#     return -1

# # przykładowe użycie
# text = "Ala ma kota, a kot ma Ale"
# pattern = "kot"
# result = boyer_moore(text, pattern)

# if result != -1:
#     print(f"Wzorzec znaleziony na pozycji {result}.")
# else:
#     print("Wzorzec nie znaleziony.")


# 4 reszta 
# T = [200,100,50,20,10,5,2,1]
# T.sort(reverse=True)
# W = []
# x = int(input("Reszta: "))
# for i in T:
#     ilość = x // i
#     if ilość > 0:
#         x = x - ilość * i
#         for j in range(ilość):
#             W.append(i)
# print(W)
