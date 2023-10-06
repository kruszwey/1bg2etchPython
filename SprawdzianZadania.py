# Grupa 2 

# Zadanie 1
# Użytkownik wprowadza dwa słowa.Sprawdź czy pierwsze z nich jest zawarte w drugim

# pierwsze_słowo = input("Wprowadź pierwsze słowo: ")
# drugie_słowo = input("Wprowadź drugie słowo: ")

# if pierwsze_słowo in drugie_słowo:
#     print(f"{pierwsze_słowo} jest zawarte w {drugie_słowo}")
# else:
#     print(f"{pierwsze_słowo} nie jest zawarte w {drugie_słowo}")


# Zadanie 2
# Sprawdz czy z podzbioru liter wpisanego przez usera słowa da się utworzyć słowo "baza"

# litery = input("Podaj litery: ")
# if all(litera in litery for litera in "baza"):
#     print("Można utworzyć słowo 'baza' z podanych liter.")
# else:
#     print("Nie można utworzyć słowa 'baza' z podanych liter.")
    

# Zadanie 3
# Wypisz wszystkie wyrazy które powstają z podanego przez usera słowa przez usunięcie duplikatów liter

# from itertools import permutations

# slowo = input("Podaj słowo: ")
# bez_duplikatow = ''.join(set(slowo))
# for permutacja in permutations(bez_duplikatow):
#     print(''.join (permutacja))


# Grupa 1  

#zadanie 1
# import re

# slowo = input("Wprowadź słowo: ")
# match = re.search(r"(.)(.*)(\1)", slowo)
# znaki = match.group(2) if match else ""

# print(f"Znaki między parą takich samych znaków: {znaki}")

#zadanie 2

# slowo = input("Wprowadź słowo: ")
# nowe_slowo = ""

# for i in range(len(slowo)-2, -1, -2):
#     para = slowo[i:i+2][::-1]
#     nowe_slowo += para

# print(nowe_slowo)

#zadanie 3
# a = input()
# X = list(a)
# Y = list(a)
# Y.sort(key=lambda y: y.lowe3r())
# if X == Y:
#     print("TAK")
# else:
#     print("NIE")

word = input("Podaj słowo: ")
subwords = [word[i:j] for i in range(len(word)) for j in range(i+1, len(word)+1) if word[i] == word[j-1]]
print("Pod słowa z literą początkową w słowie", word, "to:", subwords)


word = input("Podaj słowo: ")
count = 0
for i in range(len(word)-1):
    if word[i] == word[i+1]:
        count += 1
print("Liczba sytuacji, gdy w słowie", word, "występują koło siebie dwie takie same literki:", count)1


