import math
import random as rnd
import statistics as stat
import math
import string
from datetime import datetime
from functools import reduce
import os

# GENERATORY

# a) Napisz generator, który będzie zwracał kolejne cyfry liczby podanej od użytkownika.
# Wyznacz kilka pierwszych elementów generatora. Wyznacz sumę wszystkich cyfr.

# Definiowanie generatora:
def digit_gen(number):
    for digit in str(number):
        yield int(digit)

number = int(input("Podaj liczbę, która składa się z minimum trzech cyfr: "))
gen = digit_gen(number)
# Kilka pierwszych elementow generatora:
print("Trzy pierwsze cyfry liczby to: ")
for _ in range(3):
    print(next(gen))

# Suma cyfr: 
print("Suma wszystkich cyfr liczby:", sum(digit_gen(number)))

# b) Napisz generator, który znajdzie pierwsze 10 (lub dowolne n) trójek pitagorejskich, czyli
# takich (x, y, z) dla których zachodzi x*x + y*y == z*z.

def generator(n):
    count = 0
    z = 1
    while count < n:
        for x in range(1, z):
            for y in range(x, z):
                if x * x + y * y == z * z:
                    yield (x, y, z)
                    count += 1
                    if count == n:
                        return
        z += 1

# Dla n = 5
n = 5
print(f"Pierwszych {n} trójek pitagorajskich:")
for sets in generator(n):
    print(sets)


# c) Napisz program, który przyjmuje jedną lub więcej nazw plików jako argumenty i wypisuje
# wszystkie linie, które są dłuższe niż 40 znaków.

def print_long_lines(*filenames):
    for filename in filenames:
        try:
            with open(filename, 'r') as file:       # otwieramy plik w celu odczytania wartosci
                for line in file:
                    if len(line) > 40:
                        print(line.strip())         # funkcja strip() usuwamy biale znaki 
        except FileNotFoundError:
            print(f"Plik {filename} nieistnieje.")


# d) Napisz funkcję findfiles, która rekurencyjnie zejdzie do drzewa katalogów dla podanego
# katalogu i wygeneruje ścieżki do wszystkich plików w drzewie.

def findfiles(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)


# e) Wbudowana funkcja enumerate pobiera iteratable i zwraca iterator po parach (indeks,
# wartość) dla każdej wartości w źródle. Napisz funkcję, która wczytuje od użytkownika
# listę imion, a następnie wypisuje je w podanym formacie:
def listaimion():
    # funkcja strip usuwa nam niepotrzebne białe znaki, a split rozdziela między przecinkami 
    imiona = [imie.strip() for imie in list(input("Podaj listę imion odzielając je przecinkami: ").split(","))]
    for index, value in enumerate(imiona):
        print(f"{index}: {value}")

# Wywołanie funkcji: 
listaimion()

# FUNKCJE

# a) Napisz funkcję mySrednia( ?? ), która przyjmuje dowolną liczbę argumentów
# (w tym argumenty liczbowe i tekstowe).
# Skonwertuj argumenty nie liczbowe na liczby (jeśli się nie da to pomiń) i policz średnią
# z podanych danych liczbowych.

def mySrednia(*args):           # *args -> "*" pozwala wprowadzic dowolna liczbe argumentow
    numbers = []
    for arg in args:
        try:                    # probujemy przekonwertowac na liczbe
            number = float(arg)
            numbers.append(number)
        except ValueError:      # jesli pojawia się blad, to pomijamy
            continue
    if not numbers:             # sprawdzamy czy lista jest pusta, if not sprawdza czy wyrazenie po not jest falszywe, a pusta lista zwraca False
        return (0.0, 0)
    else:
        return (sum(numbers), len(numbers), sum(numbers) / len(numbers)) # gdy uzyjemy funkcji mean z biblioteki stat, to zwracana wartosc jest do 2 miejsc po przecinku

# Przetestujemy funckje: 
print(mySrednia(1, 2, 3, '2.0', 'a', 1.2))
print(mySrednia('a', 'b', 'c', '2.0', '1', 1.2))
print(mySrednia('a', 'b', 'c', '2.a'))


# b) Napisz funkcję mySredniaTup(), która policzy średnie: harmoniczną, geometryczną i
# arytmetyczną z liczb zawartych w tupli. Zwróć tuple zawierającą wyniki (w powyżej
# podanej kolejności).

def mySredniaTup(tupla):

    srednia_harmoniczna = len(tupla) / sum(1 / digit for digit in tupla)
    srednia_geometryczna = math.prod(tupla) ** (1 / len(tupla))
    srednia_arytmetyczna = sum(tupla) / len(tupla)

    return (srednia_harmoniczna, srednia_geometryczna, srednia_arytmetyczna)


# Przetestujmy działanie dla przykładowej krotki:
print(mySredniaTup((1, 2, 3, 2.0, 1.2)))


# c) Napisz funkcję wykladnik(), która zwraca pierwszą potęgę (wykładnik), dla którego 2^n
# jest większe od zadanej wartości k.
def wykladnik(k):
    
    #zakładamy ze k >= 2. 
    n = 1
    while 2 ** n <= k:
        n += 1
    return n

# Przetestujemy działanie dla k = 9
print(wykladnik(9))

# FUNKCJE LAMBDA / ANONIMOWE

# a) Posortuj listę tupli:
# przedmiot_ocena = [('Matma', 6.0), ('Polski', 3.5), ('Angielski', 4.5), ('Informatyka', 6.0)]
# według pierwszego elementu tupli z wykorzystaniem funkcji lambda (wykorzystaj funkcję
# sorted() oraz metodę .sort() dla listy). Posortuj listę tupli według drugiego elementu tupli.
przedmiot_ocena = [('Matma', 6.0), ('Polski', 3.5), ('Angielski', 4.5), ('Informatyka', 6.0)]

# Sortujemy listę według pierwszego elementu za pomocą funkcji sorted():
sorted1 = sorted(przedmiot_ocena, key = lambda x: x[0])
print(sorted1)

# Sortujemy listę według pierwszego elementu za pomocą metody .sort():
przedmiot_ocena.sort(key = lambda x: x[0])
print(przedmiot_ocena)

# Sortujemy listę według drugiego elementu za pomocą funkcji sorted():
sorted2 = sorted(przedmiot_ocena, key = lambda x: x[1])
print(sorted2)

# Sortujemy listę według drugiego elementu za pomocą funkcji metody .sort()
przedmiot_ocena.sort(key = lambda x: x[1])
print(przedmiot_ocena)

# b) Posortuj listę słowników:
# lista_slownikow =[{'producent': 'Nokia', 'model': 216, 'kolor': 'Czarny'},
# {'producent': 'Mi Max', 'model': 2, 'kolor': 'Złoty'},
# {'producent': 'Samsung', 'model': 7, 'kolor': 'Niebieski'}]
# Według numeru modelu, a następnie według koloru.

lista_slownikow =[{'producent': 'Nokia', 'model': 216, 'kolor': 'Czarny'},
 {'producent': 'Mi Max', 'model': 2, 'kolor': 'Złoty'},
 {'producent': 'Samsung', 'model': 7, 'kolor': 'Niebieski'}]

# wartosc slownika wywolujemy odwolujac sie do jego klucza

# Sortujemy wedlug numeru modelu: 
sorted1= sorted(lista_slownikow, key = lambda x: x['model'])
print(sorted)

# Sortujemy wedlug koloru:
lista_slownikow.sort(key = lambda x: x['kolor'])
print(lista_slownikow)

# c) Napisz funkcję lambda sprawdzającą czy podany ciąg znaków zaczyna się od podanej
# litery.

# dzieki zastosowaniu funkcji .lower() funkcja lambda nie jest wrazliwa na wielkosc liter:
firstletter = lambda str, letter: str[0].lower() == letter.lower()

# Przetestujmy kod: 
print(firstletter("Storczyk", "s"))
print(firstletter("Monstera", "O"))

# d) Napisz funkcję lambda, która z podanej daty systemowej wypisze rok, miesiąc i dzień.
data = lambda date: (date.year, date.month, date.day)

year, month, day = data(datetime.now())
print(f"Rok: {year}, miesiac: {month} i dzien {day}")

# Drugim sposobem mozemy nie podawac argumentu do lambdy:
data = lambda: (datetime.now().year, datetime.now().month, datetime.now().day)

year, month, day = data()
print(f"Rok: {year}, miesiac: {month} i dzien {day}")

# e) Napisz funkcję lambda, która dla podanego ciągu znaków sprawdzi, czy jest to liczba (
# użyj funkcji isdigit() 
is_digit = lambda str: str.isdigit()

print(is_digit("Kwiat"))
print(is_digit("567"))

# FUNKCJE MAP, FILTER, REDUCE

# a) Za pomocą funkcji map() sprawdź, które wyrazy na liście są palindromami.
terms = ["hello", "radar", "sos", "slonce", "kajak"]
ispalindron =  map(lambda word: word == word[::-1], terms)

# Wypiszmy wyniki dla listy terms:
print(list(ispalindron))

# b) pomocą funkcji map() i filter() wypisz dużymi literami wszystkie palindromy na
# liście.
terms = ["hello", "radar", "sos", "slonce", "kajak"]

# Najpierw chcemy zwrocic te slowa ktore faktycznie sa palindromami, za pomoca funkcji filter()
palindrons = filter(lambda word: word == word[::-1], terms)

# Nastepnie za pomoca funkcji map() wypiszemy je duzymi literami
print(list(map(lambda word: word.upper(), palindrons)))

# c) Za pomocą funkcji map() oblicz sumę elementów listy, krotki oraz elementów
# słownika. Dodaj weryfikację, że wszystkie dodawane elementy są liczbami.

# Stowrzmy testowa liste, krotke oraz slownik: 
lista = [1, 2, 3, 4, "Zupa", 5]
krotka = ("Kwiat", 5, 11, "Zupa")
slownik = {"Ocena1": 1, "Ocena2": 2, "Ocena3": 'A'}

# Aby dodac elementy tych trzech struktur mozemy polaczyc je w liste

allelements = lista + list(krotka) + list(slownik.values())

# Filtrujemy listę, tak aby otrzymać tylko listę liczb (int or float):
listaliczb = list(filter(lambda x: isinstance(x, (int, float)), allelements))

# Sumujemy elementy listy:
print(listaliczb)
print(sum(map(lambda x: x, listaliczb)))


# d) d) Niech będzie dana lista [("Klasa A",11),("Klasa A",12),("Klasa A",5), ("Klasa B",3),("Klasa
# B",15),("Klasa B",10),("Klasa B",2)]. Bez użycia pętli oblicz, ile jest sumarycznie
# elementów w każdej klasie. 
lista = [("Klasa A",11),("Klasa A",12),("Klasa A",5), ("Klasa B",3),("Klasa B",15),("Klasa B",10),("Klasa B",2)]

# Przefilturjmy liste, tak aby otrzymac dwie listy: jedna dla Klasy A i druga dla Klasy B:
klasaA = list(filter(lambda x: x[0] == "Klasa A", lista))
klasaB = list(filter(lambda x: x[0] == "Klasa B", lista))

# Teraz sumujemy elementy na drugim indeksie kazdej tupli poszczegolnych klas:
sumaelementowA = sum(map(lambda x: x[1], klasaA))
sumaelementowB = sum(map(lambda x: x[1], klasaB))

print(f"Suma elementow Klasy A to: {sumaelementowA}, a klasy B: {sumaelementowB}")

# e) Wypisz pary elementów z dwóch list
# Przykład:
# numbers = [1, 2, 3, 4, 5, 6]
# letters = ['a', 'b', 'c', 'd', 'e', 'f']
# Wynik: 1 : 'a', 2 : 'b', …
numbers = [1, 2, 3, 4, 5, 6]
letters = ['a', 'b', 'c', 'd', 'e', 'f']

pary = map(lambda x, y: f"{x}: '{y}'", numbers, letters)

# Poprzez "*" przekazujemy kazdy element.
print("Wynik to: ", *pary)