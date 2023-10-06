# import os
# import random

# skrzynka = [
#     {"nazwa": "M4A4 | Neo-Noir (StatTrak™)", "szansa": 0.10, "cena": 500},
#     {"nazwa": "AK-47 | Asiimov", "szansa": 0.05, "cena": 800},
#     {"nazwa": "AWP | Dragon Lore", "szansa": 0.02, "cena": 1500},
#     {"nazwa": "Glock-18 | Fade", "szansa": 0.15, "cena": 300},
#     {"nazwa": "USP-S | Kill Confirmed (Factory New)", "szansa": 0.08, "cena": 400}
# ]

# portfel = 1000
# koszt_skrzynki = 250
# ekwipunek = []

# def czysc_ekran():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def otworz_skrzynke():
#     global portfel, ekwipunek
    
#     if portfel < koszt_skrzynki:
#         print("Nie masz wystarczająco pieniędzy, aby otworzyć skrzynkę.")
#         return
    
#     print("Otwieranie skrzynki...")
#     portfel -= koszt_skrzynki
    
#     losowa_liczba = random.uniform(0, 1)
#     suma_szans = 0
#     wylosowany_przedmiot = None
    
#     for przedmiot in skrzynka:
#         suma_szans += przedmiot["szansa"]
#         if losowa_liczba <= suma_szans:
#             wylosowany_przedmiot = przedmiot
#             break
    
#     if wylosowany_przedmiot is not None:
#         print("Znalazłeś:", wylosowany_przedmiot["nazwa"])
#         ekwipunek.append(wylosowany_przedmiot)
#     else:
#         print("Nie udało się znaleźć żadnego przedmiotu.")
    
#     print("Stan portfela:", portfel)

# def sprzedaj_skin():
#     global portfel, ekwipunek
    
#     if len(ekwipunek) == 0:
#         print("Twój ekwipunek jest pusty.")
#         return
    
#     print("Twój ekwipunek:")
#     for i, przedmiot in enumerate(ekwipunek):
#         print(i+1, ".", przedmiot["nazwa"], "| Cena:", przedmiot["cena"])
    
#     numer_przedmiotu = int(input("Wybierz numer przedmiotu do sprzedaży (0 - sprzedaj wszystko): "))
    
#     if numer_przedmiotu < 0 or numer_przedmiotu > len(ekwipunek):
#         print("Nieprawidłowy numer przedmiotu.")
#         return
    
#     if numer_przedmiotu == 0:
#         sprzedaj_wszystko()
#         return
    
#     sprzedany_przedmiot = ekwipunek[numer_przedmiotu-1]
#     cena_sprzedanego = sprzedany_przedmiot["cena"]
    
#     portfel += cena_sprzedanego
#     print("Sprzedałeś", sprzedany_przedmiot["nazwa"], "za", cena_sprzedanego)
#     del ekwipunek[numer_przedmiotu-1]

# def sprzedaj_wszystko():
#     global portfel, ekwipunek
    
#     if len(ekwipunek) == 0:
#         print("Twój ekwipunek jest pusty.")
#         return
    
#     suma_cen = sum(przedmiot["cena"] for przedmiot in ekwipunek)
#     portfel += suma_cen
#     print("Sprzedałeś wszystkie przedmioty za łączną sumę", suma_cen)
#     ekwipunek.clear()

# def ulepsz_przedmiot():
#     global portfel, ekwipunek
    
#     if len(ekwipunek) == 0:
#         print("Twój ekwipunek jest pusty.")
#         return
    
#     print("Twój ekwipunek:")
#     for i, przedmiot in enumerate(ekwipunek):
#         print(i+1, ".", przedmiot["nazwa"], "| Cena:", przedmiot["cena"])
    
#     numer_przedmiotu = int(input("Wybierz numer przedmiotu do ulepszenia: "))
    
#     if numer_przedmiotu < 1 or numer_przedmiotu > len(ekwipunek):
#         print("Nieprawidłowy numer przedmiotu.")
#         return
    
#     przedmiot_do_ulepszenia = ekwipunek[numer_przedmiotu-1]
    
#     print("Ulepszanie przedmiotu:", przedmiot_do_ulepszenia["nazwa"])
#     print("Cena ulepszenia:", przedmiot_do_ulepszenia["cena"])
#     print("Wybierz mnożnik:")
#     print("1. x2 (50%)")
#     print("2. x5 (20%)")
#     print("3. x10 (8%)")
    
#     numer_mnoznika = int(input("Wybierz numer mnożnika: "))
    
#     if numer_mnoznika == 1:
#         mnoznik = 2
#         procent = 50
#     elif numer_mnoznika == 2:
#         mnoznik = 5
#         procent = 20
#     elif numer_mnoznika == 3:
#         mnoznik = 10
#         procent = 8
#     else:
#         print("Nieprawidłowy numer mnożnika.")
#         return
    
#     print(f"Ulepszanie przedmiotu: {przedmiot_do_ulepszenia['nazwa']}")
#     print(f"Cena ulepszenia: {przedmiot_do_ulepszenia['cena']}")
#     print(f"Szansa na ulepszenie x{mnoznik} ({procent}%):")
    
#     if random.randint(1, 100) <= procent:
#         przedmiot_do_ulepszenia['cena'] *= mnoznik
#         print(f"Ulepszenie udane! Cena przedmiotu została pomnożona przez {mnoznik}.")
#     else:
#         print("Ulepszenie nieudane! Przedmiot zostaje usunięty.")
#         del ekwipunek[numer_przedmiotu-1]
    
#     print("Stan portfela:", portfel)

# def wyswietl_stan():
#     global portfel, ekwipunek
    
#     print("Stan portfela:", portfel)
    
#     if len(ekwipunek) > 0:
#         print("Twój ekwipunek:")
#         for przedmiot in ekwipunek:
#             print("-", przedmiot["nazwa"])
#     else:
#         print("Twój ekwipunek jest pusty.")

# def czysc_czat():
#     czysc_ekran()
#     print("1. Otwórz skrzynkę")
#     print("2. Sprzedaj skin")
#     print("3. Ulepsz przedmiot")
#     print("4. Wyświetl stan")
#     print("5. Wyjdź z programu")

# def main():
#     while True:
#         czysc_czat()
#         wybor = input("Wybierz opcję: ")
        
#         if wybor == "1":
#             otworz_skrzynke()
#         elif wybor == "2":
#             sprzedaj_skin()
#         elif wybor == "3":
#             ulepsz_przedmiot()
#         elif wybor == "4":
#             wyswietl_stan()
#         elif wybor == "5":
#             break
#         else:
#             print("Nieprawidłowa opcja.")

# if __name__ == "__main__":
#     main()




# import openai

# # Konfiguracja klucza API
# openai.api_key = 'TU_WPROWADŹ_SWÓJ_KLUCZ_API'

# # Funkcja udzielająca odpowiedzi na pytania za pomocą OpenAI
# def udziel_odpowiedzi(pytanie):
#     response = openai.Completion.create(
#         engine="davinci-codex",
#         prompt=pytanie,
#         max_tokens=50,
#         n=1,
#         stop=None,
#         temperature=0.7
#     )
#     odpowiedz = response.choices[0].text.strip()
#     return odpowiedz

# # Główna pętla programu
# while True:
#     pytanie = input("Zadaj pytanie (lub wpisz 'q' aby zakończyć): ")
#     if pytanie.lower() == "q":
#         break
#     odpowiedz = udziel_odpowiedzi(pytanie)
#     print(odpowiedz)







# import random

# Dreams_Nightmares_Case = [
#     {"nazwa": "M4A4 | Neo-Noir (StatTrak™)", "szansa": 0.10, "cena": 500},
#     {"nazwa": "AK-47 | Asiimov", "szansa": 0.05, "cena": 800},
#     {"nazwa": "AWP | Dragon Lore", "szansa": 0.02, "cena": 1500},
#     {"nazwa": "Glock-18 | Fade", "szansa": 0.15, "cena": 300},
#     {"nazwa": "USP-S | Kill Confirmed (Factory New)", "szansa": 0.08, "cena": 400}
# ]

# skrzynka_revolution = [
#     {"nazwa": "SCAR-20 | Fragments", "szansa": 0.10},
#     {"nazwa": "Tec-9 | Rebel", "szansa": 0.10},
#     {"nazwa": "P250 | Re.built", "szansa": 0.10},
#     {"nazwa": "MAG-7 | Insomnia", "szansa": 0.10},
#     {"nazwa": "SG 553 | Cyberforce", "szansa": 0.10},
#     {"nazwa": "MP9 | Featherweight", "szansa": 0.10},
#     {"nazwa": "MP5-SD | Liquidation", "szansa": 0.10},
#     {"nazwa": "MAC-10 | Sakkaku", "szansa": 0.10},
#     {"nazwa": "R8 Revolver | Banana Cannon", "szansa": 0.10},
#     {"nazwa": "Glock-18 | Umbral Rabbit", "szansa": 0.10},
#     {"nazwa": "P90 | Neoqueen", "szansa": 0.10},
#     {"nazwa": "M4A1-S | Emphorosaur-S", "szansa": 0.10},
#     {"nazwa": "UMP-45 | Wild Child", "szansa": 0.10},
#     {"nazwa": "P2000 | Wicked Sick", "szansa": 0.10},
#     {"nazwa": "AWP | Duality", "szansa": 0.10},
#     {"nazwa": "AK-47 | Head Shot", "szansa": 0.10},
#     {"nazwa": "M4A4 | Temukau", "szansa": 0.10}
# ]

# portfel = 1000
# koszt_skrzynki = 250
# ekwipunek = []

# def otworz_skrzynke(Dreams_Nightmares_Case):
#     global portfel, ekwipunek
    
#     if portfel < koszt_skrzynki:
#         print("Nie masz wystarczająco pieniędzy, aby otworzyć skrzynkę.")
#         return
    
#     print("Otwieranie skrzynki...")
#     portfel -= koszt_skrzynki
    
#     losowa_liczba = random.uniform(0, 1)
#     suma_szans = 0
#     wylosowany_przedmiot = None
    
#     for przedmiot in Dreams_Nightmares_Case:
#         suma_szans += przedmiot["szansa"]
#         if losowa_liczba <= suma_szans:
#             wylosowany_przedmiot = przedmiot
#             break
    
#     if wylosowany_przedmiot is not None:
#         print("Znalazłeś:", wylosowany_przedmiot["nazwa"])
#         ekwipunek.append(wylosowany_przedmiot)
#     else:
#         print("Nie udało się znaleźć żadnego przedmiotu.")
    
#     print("Stan portfela:", portfel)


# def sprzedaj_skin():
#     global portfel, ekwipunek
    
#     if len(ekwipunek) == 0:
#         print("Twój ekwipunek jest pusty.")
#         return
    
#     print("Twój ekwipunek:")
#     for i, przedmiot in enumerate(ekwipunek):
#         print(i+1, ".", przedmiot["nazwa"], "| Cena:", przedmiot["cena"])
    
#     numer_przedmiotu = int(input("Wybierz numer przedmiotu do sprzedaży (0 - sprzedaj wszystko): "))
    
#     if numer_przedmiotu < 0 or numer_przedmiotu > len(ekwipunek):
#         print("Nieprawidłowy numer przedmiotu.")
#         return
    
#     if numer_przedmiotu == 0:
#         sprzedaj_wszystko()
#         return
    
#     sprzedany_przedmiot = ekwipunek[numer_przedmiotu-1]
#     cena_sprzedanego = sprzedany_przedmiot["cena"]
    
#     portfel += cena_sprzedanego
#     print("Sprzedałeś", sprzedany_przedmiot["nazwa"], "za", cena_sprzedanego)
#     del ekwipunek[numer_przedmiotu-1]

# def sprzedaj_wszystko():
#     global portfel, ekwipunek
    
#     if len(ekwipunek) == 0:
#         print("Twój ekwipunek jest pusty.")
#         return
    
#     suma_cen = sum(przedmiot["cena"] for przedmiot in ekwipunek)
#     portfel += suma_cen
#     print("Sprzedałeś wszystkie przedmioty za łączną sumę", suma_cen)
#     ekwipunek.clear()

# def ulepsz_przedmiot():
#     global portfel, ekwipunek
    
#     if len(ekwipunek) == 0:
#         print("Twój ekwipunek jest pusty.")
#         return
    
#     print("Twój ekwipunek:")
#     for i, przedmiot in enumerate(ekwipunek):
#         print(i+1, ".", przedmiot["nazwa"], "| Cena:", przedmiot["cena"])
    
#     numer_przedmiotu = int(input("Wybierz numer przedmiotu do ulepszenia: "))
    
#     if numer_przedmiotu < 1 or numer_przedmiotu > len(ekwipunek):
#         print("Nieprawidłowy numer przedmiotu.")
#         return
    
#     wybrany_przedmiot = ekwipunek[numer_przedmiotu-1]
#     cena_ulepszenia = wybrany_przedmiot["cena"]
    
#     print("Ulepszanie przedmiotu:", wybrany_przedmiot["nazwa"])
#     print("Cena ulepszenia:", cena_ulepszenia)
    
#     print("Wybierz mnożnik:")
#     print("1. x2 (50%)")
#     print("2. x5 (20%)")
#     print("3. x10 (8%)")
    
#     wybrany_mnoznik = input("Wybierz numer mnożnika: ")
    
#     if wybrany_mnoznik == "1":
#         if random.random() <= 0.5:
#             wybrany_przedmiot["cena"] *= 2
#             print("Ulepszenie udane! Cena przedmiotu została pomnożona przez 2.")
#         else:
#             print("Ulepszenie nieudane! Przedmiot został usunięty.")
#             del ekwipunek[numer_przedmiotu-1]
#     elif wybrany_mnoznik == "2":
#         if random.random() <= 0.2:
#             wybrany_przedmiot["cena"] *= 5
#             print("Ulepszenie udane! Cena przedmiotu została pomnożona przez 5.")
#         else:
#             print("Ulepszenie nieudane! Przedmiot został usunięty.")
#             del ekwipunek[numer_przedmiotu-1]
#     elif wybrany_mnoznik == "3":
#         if random.random() <= 0.08:
#             wybrany_przedmiot["cena"] *= 10
#             print("Ulepszenie udane! Cena przedmiotu została pomnożona przez 10.")
#         else:
#             print("Ulepszenie nieudane! Przedmiot został usunięty.")
#             del ekwipunek[numer_przedmiotu-1]
#     else:
#         print("Nieprawidłowy numer mnożnika.")

# while True:
#     print("Stan portfela:", portfel)
#     print("Twój ekwipunek:", [przedmiot["nazwa"] for przedmiot in ekwipunek])
#     print("1. Otwórz skrzynkę (koszt:", koszt_skrzynki, "zł)")
#     print("2. Sprzedaj skin")
#     print("3. Sprzedaj wszystko")
#     print("4. Ulepsz przedmiot")
#     print("5. Zakończ")
    
#     wybor = input("Wybierz opcję: ")
    
#     if wybor == "1":
#         print("1. Skrzynka Dreams & Nightmares Case")
#         print("2. Skrzynka Revolution Case")
#         rodzaj_skrzynki = input("Wybierz rodzaj skrzynki: ")
#         if rodzaj_skrzynki == "1":
#             otworz_skrzynke(Dreams_Nightmares_Case)
#         elif rodzaj_skrzynki == "2":
#             otworz_skrzynke(skrzynka_revolution)
#         else:
#             print("Nieprawidłowy wybór.")
#     elif wybor == "2":
#         sprzedaj_skin()
#     elif wybor == "3":
#         sprzedaj_wszystko()
#     elif wybor == "4":
#         ulepsz_przedmiot()
#     elif wybor == "5":
#         break
#     else:
#         print("Nieprawidłowy wybór.")