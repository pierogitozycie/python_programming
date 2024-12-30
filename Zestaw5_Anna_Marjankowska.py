# Zadanie 1. Utwórz klasę Car, która posiada pola brand, model, year. Dopisz metodę, która wyświetla informacje o
# obiekcie. Przykładowe użycie klasy:
# my_car = Car("Toyota", "Corolla", 2020)
# print(my_car) # Wyjście: "Toyota Corolla, 2020"

print("\nZadanie 1")

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model}, {self.year}"
    
my_car = Car("Toyota", "Corrola", 2020)
print(my_car)

# Zadanie 2. Utwórz klasę BankAccount, która posiada pola owner_name i balance. Dopisz metody dostępowe dla
# pól i dodaj walidację, że balanse musi być liczbą nieujemną. Dodaj metody deposit(amount), która odpowiada
# wpłacie na konto oraz withdraw(amount), która odpowiada wypłacie z konta, przy czym wypłata nie może być
# większa niż stan konta. Przykładowe użycie klasy:
# account = BankAccount("Alice", 1000)
# account.deposit(500) # Stan konta 1500
# account.withdraw(2000) # Niedozwolone, wypisanie ostrzeżenia

print("\nZadanie 2")

class BankAccount:
    def __init__(self, owner_name, balance = 0):
        self.owner_name = owner_name
        self.balance = balance if balance >= 0 else 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <- self.balance:
            self.balance -= amount
        else:
            print("Niewystarczające środki na koncie!")

account = BankAccount("Alice", 1000)
new_balance = account.deposit(500)
print(f"Nowy stan konta: {new_balance}")
account.deposit(500)
print(f"Nowy stan konta: {account.balance}")
account.withdraw(2000)    
account.withdraw(500)   

# Zadanie 3. Utwórz klasę Temperature, która zwiera pole value (w stopniach Celsjusza), metody to_fahrenheit(),
# która zamienia stopnie Celsjusza na Fahrenheita i to_kelvin(), która zamienia stopnie Celsjusza na Kelvina oraz
# metodę statyczną celsius_to_fahrenheit(celsius), aby wykonać konwersję bez konieczności tworzenia obiektu.

print("\nZadanie 3")

class Temperature:
    def __init__(self, value):
        self.value = value

    def to_fahrenheit(self):
        return self.value * 9 / 5 + 32
    
    def to_kelivn(self):
        return self.value  + 273.15
    
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32
    

temp = Temperature(25.5)
print(f"Aktualna temperatura w stopanich Celsjusza: {temp.value}.")

print(f"Temperatura w stopniach Fahrenheita: {temp.to_fahrenheit()}.")
print(f"Temperatura w stopniach Kelvinach: {temp.to_kelivn()}.")

print("\nMetoda statyczna:")
temperatura = 31.7
print(f"{temperatura} stopni Celsjusza to {Temperature.celsius_to_fahrenheit(temperatura)} stopni Fahrenheita.")

# Zadanie 4. Utwórz abstrakcyjną klasę Animal, która zawiera pole name oraz abstrakcyjną metodę make_sound().
# Utwórz dwie klasy dziedziczące Dog i Cat. Nadpisz metodę make_sound() w obu klasach. Przykładowe użycie
# klas:
# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# dog.make_sound() # "Woof!"
# cat.make_sound() # "Meow!"

print("\nZadanie 4")

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")
    
class Cat(Animal):
    def make_sound(self):
        print("Meow!")
    
dog = Dog("Buddy")
cat = Cat("Whiskers")
dog.make_sound()
cat.make_sound()

# Zadanie 5. Napisz decorator dla funkcji make_sound(), który powiela wykonanie funkcji tejże funkcji losową liczbę
# razy (od 1 do 5).

print("\nZadanie 5")


import random as rnd
from abc import ABC, abstractmethod
from functools import wraps

def repeat_random(func):
    @wraps(func)
    def wrapper(*args):
        n = rnd.randint(1, 5)
        for _ in range(n):
            func(*args)
    return wrapper

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")
    
class Cat(Animal):
    @repeat_random
    def make_sound(self):
        print("Meow!")
    
cat = Cat("Whiskers")
cat.make_sound()

# Zadanie 6. Utwórz klasę Library, która zawiera listę obiektów klasy Book. Dopisz metody add_book(book), która
# dodaje książkę do listy, remove_book(title), która usuwa książkę z listy oraz list_books(), która wyświetla wszystkie
# książki na liście. Przykładowe użycie klasy:
# library = Library()
# book1 = Book("1984", "George Orwell")
# library.add_book(book1)
# library.list_books()

print("\nZadanie 6")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title}, {self.author}"


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_to_remove):
        self.books = [book for book in self.books if not (book.title == book_to_remove.title and book.author == book_to_remove.author)]

    def list_books(self):
        for book in self.books:
            print(book)


library = Library()

book1 = Book("Lalka", "Bolesław Prus")
book2 = Book("Dziady", "Adam Mickiewicz")
book3 = Book("Dziady 3", "Adam Mickiewicz")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("Stan biblioteczki:")
library.list_books()

library.remove_book(book2)
print(f"\nStan biblioteczki po usunięciu {book2}:")
library.list_books()


# Zadanie 7. Utwórz klasę DataTimeSeries, która zawiera pola filepath, time_col_name, data_csv,
# windowLength. W konstruktorze klasy wczytaj dane z podanego pliku (filepath). Kolumnę z datami zamień na typ
# DataTime. Napisz metody: get_stats(self) - która wyznaczy statystyki opisowe Szeregu Czasowego z danych oraz
# get_rolling(self) – która policzy średnie ruchome o podanym oknie (windowLength). Dodaj metodę
# plot_time_series(self) rysującą wykresy szeregów z wyrównaniem średnią ruchomą. Napisz klasę
# SeasonalDataTimeSeries , która dziedziczy po klasie DataTimeSeries. Klasa ta ma mieć dodatkowe pole no_diff,
# określające ilość różnic. Na przykład dla no_diff = 1 wyznaczane są pierwsze różnice, dla no_diff = 2 wyznaczane są
# pierwsze różnice oraz drugie różnice itd. Każde różnice należy dodać do ramki danych jako kolumnę name_i (gdzie
# name jest nazwą szeregu a i kolejna różnicą). Wykorzystaj wyrażenie listowe / wyrażenie generatorowe.

print("\nZadanie 7")

import pandas as pd
import matplotlib.pyplot as plt

class DataTimeSeries:
    def __init__(self, filepath, time_col_name, windowLength):
        self.filepath = filepath
        self.time_col_name = time_col_name
        self.windowLength = windowLength
        self.data_csv = pd.read_csv(filepath, sep=',')
        self.data_csv[time_col_name] = pd.to_datetime(self.data_csv[time_col_name])

    def get_stats(self):
        return self.data_csv.describe()

    def get_rolling(self):
        column_to_roll = 'value'
        self.data_csv[f"{column_to_roll}_rolling_mean"] = self.data_csv[column_to_roll].rolling(window=self.windowLength).mean()
        return self.data_csv[[self.time_col_name, column_to_roll, f"{column_to_roll}_rolling_mean"]]

    def plot_time_series(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.data_csv[self.time_col_name], self.data_csv.iloc[:, 1], label="Original Data")
        rolling_mean = self.get_rolling()
        plt.plot(self.data_csv[self.time_col_name], rolling_mean.iloc[:, 1], label=f"{self.windowLength}-Point Rolling Mean")
        plt.legend()
        plt.show()


class SeasonalDataTimeSeries(DataTimeSeries):
    def __init__(self, filepath, time_col_name, windowLength, no_diff):
        super().__init__(filepath, time_col_name, windowLength)
        self.no_diff = no_diff

    def add_differences(self):
        for i in range(1, self.no_diff + 1):
            self.data_csv[f"diff_{i}"] = self.data_csv.iloc[:, 1].diff(periods=i)



filepath = "/Users/aniamarjankowska/Documents/GitHub/python_programming/data.csv"
time_col_name = "time"
windowLength = 3
no_diff = 2

seasonal_series = SeasonalDataTimeSeries(filepath, time_col_name, windowLength, no_diff)
print(seasonal_series.get_stats())
seasonal_series.add_differences()
print(seasonal_series.data_csv.head())
seasonal_series.plot_time_series()


