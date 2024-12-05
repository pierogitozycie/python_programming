import math
import random as rnd
import statistics as stat
import string
import itertools

# Zadanie 1
# Napisz program proszący użytkownika o podanie dwóch liczb a i b. Wypisz w konsoli ich sumę,
# różnicę, iloczyn, iloraz oraz √𝑎 + 𝑏

print("Podaj dwie liczby całkowite:")
a = int(input("a: "))
b = int(input("b: "))

print(f"Suma: {a + b:.2f}")
print(f"Rónica: {a - b:.2f}")
print(f"Iloczyn: {a * b:.2f}")

if b != 0:
    print(f"Iloraz: {a / b:.2f}")
else:
    print("Nie dziel przez zero!")

print(f"Pierwiastek: {math.sqrt(a + b):.2f}")

# Zadanie 2
# Napisz program zgadywanka, który polega na wylosowaniu przez komputer liczby od 1 do 5,
# a użytkownik zgaduje jaka to liczba

# Losujmey liczbę od [1, 5] 
liczba = rnd.randint(1,5)

traf = int(input("\nPodaj liczbę od 1 do 5: "))
if liczba == traf:
    print("\nBrawo! Zgadłeś poprawnie.")
else:
    print("Niestety, nie udało się. Poprawna liczba to: ", liczba)

# Zadanie 3
# Wygeneruj 10 elementową listę (nums) zawierającą całkowite liczby losowe z przedziału [2,8]. Napisz
# program

# Generujemy 10 elementowa liste z przedzialu [2, 8]
nums = [rnd.randint(2, 8) for _ in range(10)]
print("\nLista początkowa:", nums)

# a) wypisujący wszystkie elementy listy nums wraz z indeksami
print("Indeksy i wartości w liście :")
for index, value in enumerate(nums):
    print(f"Indeks {index}: {value}")

# b) usuwający z listy nums liczby nieparzyste
nums_without_odds = [num for num in nums if num % 2 == 0]
print("\nLista po usunięciu liczb nieparzystych:", nums_without_odds)

# c) zamieniający wartości elementów nieparzystych w nums na ich indeksy 
nums_replaced_odds = [index if num % 2 != 0 else num for index, num in enumerate(nums)]
print("Lista po zastąpieniu liczb nieparzystych na ich indeksy:", nums_replaced_odds)

# d) usunie z listy nums wszystkie wystąpienia liczb 2 i 3,
nums_without2and3 = [num for num in nums if num != 2 and num != 3]
print("Lista po usunięcniu powtórzeń 2 i 3: ", nums_without2and3)

# e) po każdej liczbie podzielnej przez 3 w liście nums wstawi nowy dodatkowy element o wartości 15
nums_extended = []

for i in range(len(nums)):
    if nums[i] % 3 == 0:
        nums_extended.append(nums[i])
        nums_extended.append(15)
    else:
        nums_extended.append(nums[i])

print("Lista rozszerzna o wartosc 15 po kazdym wystawieniu liczby podzielnej przez 3:\n", nums_extended)

# Zadanie 4
# Wygeneruj 10 elementową tuplę (tnums) zawierającą całkowite liczby losowe z przedziału [2,15].
# Napisz program:

tnums = tuple(rnd.randint(2, 15) for _ in range(10))
print("\nTupla poczatkowa: ", tnums)

# a) wypisujący wszystkie elementy tupli tnums wraz z indeksami
print("Indeksy i wartości tupli: ")
for index, value in enumerate(tnums):
    print(index, value)

# b) wyznaczający średnie: harmoniczną, geometryczną i arytmetyczną z liczb zawartych w tupli tnums
print(f"\nSrednia harmoniczna: {stat.harmonic_mean(tnums):.2f}")
print(f"Srednia geometryczna: {stat.geometric_mean(tnums):.2f}")
print(f"Srednia arytemtyczna: {stat.mean(tnums):.2f}")

# c) zliczy wszystkie wystąpienia liczby 3 i 5 w tupli tnums
print(f"Liczba wystąpień liczby 2: {tnums.count(2)}, a liczby 3: {tnums.count(3)}")

# Zadanie 5

# Tworzymy liste przedmiotow, studentow oraz ID:
sub = ['math', 'python', 'ang', 'algebra', 'analysis', 'statistic']
names = ['Ania', 'Zosia', 'Piotr', 'Kamil', 'Wojtek', 'Julia']
ids = [23222 + i for i in range(len(names))]

group = []

for i in range(len(names)):
    subjects = rnd.sample(sub, rnd.randint(1, len(sub))) # tworzymy liste przedmiotow zawierajaca sie minimum z jendego przedmiotu, maksymalnie ze wszytskich 
    student = (ids[i], names[i], subjects)
    group.append(student)

print("\nStudenci zaliczyli ponizsze przedmioty: ")
for student in group:
    print(student)


# Zadanie 6

# a) Podaj wyrażenie listowe, które wypisze duże litery alfabetu w kolejności rosnącej
# (alfabetycznej) grupami po 5 liter w każdej podliście.
letters = [[string.ascii_uppercase[i:i+5]] for i in range(0, len(string.ascii_uppercase), 5)]
print("\nDuze litery alfabetu pogrupowane po 5 liter w kazdej podliscie: ", letters)

# b) Podaj wyrażenie listowe, które wypisze duże litery alfabetu w kolejności rosnącej
# (alfabetycznej) grupami o liczności liter w każdej podliście podanej jako lista_liczności.

lista_licznosci = []
suma = 0
# tworzymy losowa liste lista_licznosci, ktorej suma elementow da nam 26, tak aby podzielic caly alfabet
while suma < len(string.ascii_uppercase):
    # tutaj losujemy liczbe z przedzialu (1, 26 - suma)
    # dzieki czemu napewno bedziemy miec wszytskie elementy alfabetu w listach
    # randint losuje z przedzialu domkniętego [a, b]
     liczba = rnd.randint(1, len(string.ascii_uppercase) - suma)
     lista_licznosci.append(liczba)
     suma += liczba

letters = [string.ascii_uppercase[sum(lista_licznosci[:i]):sum(lista_licznosci[:i+1])] for i in range(len(lista_licznosci))]
print(f"Duze litery alfabetu {letters}, \nporupowane wedlug licznosci {lista_licznosci}")

# c) Podaj wyrażenie listowe, które wypisze wszystkie tuple postaci (x, y), utworzone z liczb
# naturalnych z przedziału (1, 10), zawierające jako x liczby parzyste, a jako y liczby nieparzyste.
pairs = [(x, y) for x in range(1, 10) if x%2 == 0 for y in range(1, 10) if y%2 != 0]
print("\nTuple postaci (x, y): ")
for pair in pairs: 
    print(pair)

# d) Użyj zagnieżdżonego wyrażenia listowego do transponowania macierzy (zamiany wierszy z
# kolumnami). 
matrix = [
    [1,2,4],
    [0,0,0],
    [4,6,8]]

# towrzymy losową macierz wymiaru 3x4 o losowych wartościach z przedziału [0, 10)
# uzywamy "_" w petlach gdy chcemy wykonac petle, ale bez odniesienia sie do zmiennej licznikowej.

matrix = [[rnd.randint(0,10) for _ in range(4)] for _ in range(3) ]

print("\nMacierz A: ")
for row in matrix: print(row)

transponse_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("\nMacierz A transponowana: ")
for row in transponse_matrix: print(row)

# e) Używając wyrażenia listowego, wygeneruj listę liczb pierwszych w zakresie od 2 do 100. 
liczby_pierwsze = [n for n in range(2, 101) if all(n % i != 0 for i in range(2, int(n**0.5) + 1))]

print(f"\nLiczby pierwsze w zakresie od 2 do 100: {liczby_pierwsze}")

# f) Stwórz szyfr Cezara, który przesuwa litery w podanym słowie o 3 miejsca w alfabecie,
# używając wyrażenia listowego.
print("\nAlfabet:", string.ascii_uppercase)
word = 'EXAMPLE'

# dzielimy modulo przez 26 i wtedy mamy pewnosc ze nie wyjdziemy poza indeksy alfabetu
zaszyfrowane = "".join([string.ascii_uppercase[(string.ascii_uppercase.index(char) + 3) % 26] for char in word])
print("Slowo zaszyfrowane szyfrem Cezara:", zaszyfrowane)


# Zadanie 7

# a) Napisz program, który na podstawie listy:
# student_grades = [("Alice", 5), ("Bob", 4), ("Eve", 3), ("AAA", "BBB")]
# utworzy słownik z listy par student – ocena tak, aby usunąć wszystkie oceny, które nie są
# liczbami.

student_grades = [("Alice", 5), ("Bob", 4), ("Eve", 3), ("AAA", "BBB")]
slownik = {student: grade for student, grade in student_grades if isinstance(grade, int)}

print(slownik)

# b) Utwórz słownik, który mapuje małe litery na ich wartości ASCII

slownik = {letter: ord(letter) for letter in string.ascii_lowercase}

print(slownik)

# c) Utwórz zagnieżdżony słownik, w którym zewnętrzny słownik mapuje liczbę do innego
# słownika zawierającego kwadraty i sześciany.


numbers = [rnd.randint(0, 10) for _ in range(5)]
slownik = {num: {'square': num ** 2, 'cube': num ** 3} for num in numbers}
print(slownik)


# Zadanie 8

smak = ["smietankowe", "pistacjowe", "truskawkowe", "jagodowe", "cytrynowe"]
rozmiar = ["duze", "male"]
dodatek = ["polewa czekoladowa", "polewa karmelowa", "posypka czekoladowa", "posypka kolorowa"]

zbior = set(itertools.product(rozmiar, smak, dodatek))

print(zbior)



