# Zad 1

# for i in range(1, 31):
#   print(f"{i} listopada 2022")

# Zad 2
# a = 1
# while True:
#   print(a ** 2)
#   a += 2

# Zad 3 
# for i in range(1000, 10000):
#   if i % 379 == 0:
#     print(i)

# Zad 4
# for i in range(100, 1000):
#   if i % 5 == 0 or i % 6 == 0 or i % 11 == 0:
#     print(i)

# Zad 5
# n = int(input())
# g = 0
# for i in range(n):
#   k = int(input())
#   g += k
# print(g)


# WAŻNE


# ZAD 6

# k = int(input())
# a = 0
# for i in range(0,2 * k,2):
#   a += i
# print(a)

# ZAD 7
# m = int(input())
# a = 0 
# for i in range(11,m * 2 + 10,2):
#   if i < 100:
#     a += i
# print(a)

# ZAD 8 (BARDZO TRUDNE)n

# procent = 6 
# L = float(input("Podaj długość trwania inwestycji: "))
# W0 = int(input("Podaj ile kasy wrzucasz na inwestycje: "))
# W = W0

# for i in range(int(L*12)):
#   W = W*(1+(procent/12)/100)
# print(W)

# ZAD 9 
# n = int(input())
# a = 0
# for i in range(21,n * 100 + 21,100):
#   a += i
# print(a)

# ZAD 10
# for i in range(1,1000):
#   if i % 10 == i ** (1/2):
#     print(i)
#   elif i % 100 == i ** (1/2):
#     print(i)