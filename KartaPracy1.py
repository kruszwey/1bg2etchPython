#zad 1

# a = int(input())
# b = int(input())
# print(a**2 +b**2)

#zad 2 
# a = int(input())
# b = int(input())
# print((a+b)**2)

# a = int(input())
# b = int(input())
# print((a-b)**3)

#zad 4
# a = int(input())
# b = int(input())
# c = int(input())
# print(a*b*c)

#zad 5
# a = int(input())
# b = int(input())
# print(2*(a+b)/5)
# print((a+b)*0,4)

#zad 6

# brutto = int(input())
# print(brutto/ 1.23)

#zad 7
# a = int(input())
# b = int(input())
# print(a % b)

słowo = input("Podaj słowo: ")

podsłowa = [słowo[i: j] for i in range(len(słowo))
          for j in range(i + 1, len(słowo) + 1)]

wynik = [podsłowo for podsłowo in podsłowa if podsłowo[0] == 'p']

print("Podsłowa z literą początkową:")
print(wynik)
