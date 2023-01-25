# PRE

# from math import gcd
# print(gcd(15,20))

# 1. wybór 2 dużych liczb pierwszch

p = 11
g = 13

# 2 . liczym n = p * g oraz funkcje fulera F = (p - 1) * (g- 1)
n = p*g
F = (p - 1) * (g - 1)
print(n)
print(F)

# 3 . Generujemy klucz publiczny e  taki, że NWD(F,e) = 1
from math import gcd
for i in range(2, F):
  if gcd(i,F) == 1:
    e = i
    break
print(e, n)

# 4. generujemy klucz prywatny  d taki, że d * e mod F == 1 
for j in range(2,F):
  if ((j*e) % F) == 1:
    d = j
    break
print(d,n)

#  Jak szyfrować?
# mamy  m - wiadomość
# c = m**e % n (c- cipher - szyfrogram, tekst zaszyfrowany)
# t = c**d % n (t - text - tekst jawny - znów wiadomość m)

m = input()
cipher = ""
for i in m:
  cipher  += chr((ord(i)**e) % n)
print(m)
print(cipher)

tekst = ""
for i in cipher:
  tekst += chr((ord(i)**d)%n)
print(tekst)

# napisz w pseudo kodzie
