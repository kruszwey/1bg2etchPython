# Napis jest prawie "listą"
# s = input()
# print(s)

# for i in s:
#   print(i)
# for i in range(len(s)):
#   print(s[i])

# L = [5,7,2,4]
# print(L)
# L.sort()
# print(L)
# s= input()
# print(s)
# s.sort() - to jest błąd, napis to nie normalna lista
# print(s)

# przechodzenie: napis <-> lista (list() ( join())

# s = input()
# L = list(s)
# print(s,L)
# L.sort()
# print(s,L)
# s = "".join(L)
# print(s,L)

# Napisz algorytm czy czy wyraz jest palindromem(czyli że od wtyłu będzie to samo)

# s = input()
# L =list(s)
# R = L.copy()
# print(s,L)
# L.reverse()
# print(s,L)
# if L == R:
#   print("Tak")
# else:
#   print("Nie")

# palindrom ver 2
# s = input()
# for i in range(len(s)//2):
#   if s[i] != s[len(s)-1-i]:
#     exit"(")

from ramdom import randint

n = 10
L = [randint(1, 30) for i in range(n)]
print(L)

for i in range(n):
  for j in range(i, n):
    mi = i
    if L[j] < L[mi]:
      mi = j
    L[i], L[mi] = L[mi], L[i]
print(L)
