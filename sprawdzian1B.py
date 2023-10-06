# 1 Wypisz ilosc różnych liter w podanym przez usera słowie . Np dla wyrazu szkoła wynikiem jest 6, a dla wyrazu anna wynikiem jest 2

word = input("Podaj słowo: ")
unique_letters = set(word)
count = len(unique_letters)
print("Liczba różnych liter w słowie", word, "to", count)

# 2 Przeformatuj słowo do słowa wariackiego. śłowo wariackie to takie słowo, w którym łączą się skrajne pary literek dając nowe słowo, czyli pierwsza łączy się z ostatnią druga z poprzednią i tak do wyczeprpania liter

word = input("Podaj słowo: ")
length = len(word)
if length < 2:
    print("Słowo jest zbyt krótkie, aby stać się słowem wariackim.")
else:
    wariackie = word[0] + word[length - 1]
    for i in range(1, length // 2):
        wariackie += word[i] + word[length - i - 1]
    if length % 2 == 1:
        wariackie += word[length // 2]
print("Słowo wariackie to:", wariackie)