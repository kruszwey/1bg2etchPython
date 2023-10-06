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
h =input()
ilosc = 0
for i in range(len(h)):
  if h[i:i+2] == "LA":
    ilosc += 1
if ilosc == 3:
  print("Tak")
else:
  print("Nie")