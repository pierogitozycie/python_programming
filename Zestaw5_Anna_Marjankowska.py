# Zadanie 1. Utwórz klasę Car, która posiada pola brand, model, year. Dopisz metodę, która wyświetla informacje o
# obiekcie. Przykładowe użycie klasy:
# my_car = Car("Toyota", "Corolla", 2020)
# print(my_car) # Wyjście: "Toyota Corolla, 2020"

# print("\nZadanie 1")

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def __str__(self):
#         return f"{self.brand} {self.model}, {self.year}"
    
# my_car = Car("Toyota", "Corrola", 2020)
# print(my_car)

# Zadanie 2. Utwórz klasę BankAccount, która posiada pola owner_name i balance. Dopisz metody dostępowe dla
# pól i dodaj walidację, że balanse musi być liczbą nieujemną. Dodaj metody deposit(amount), która odpowiada
# wpłacie na konto oraz withdraw(amount), która odpowiada wypłacie z konta, przy czym wypłata nie może być
# większa niż stan konta. Przykładowe użycie klasy:
# account = BankAccount("Alice", 1000)
# account.deposit(500) # Stan konta 1500
# account.withdraw(2000) # Niedozwolone, wypisanie ostrzeżenia

# print("\nZadanie 2")

# class BankAccount:
#     def __init__(self, owner_name, balance = 0):
#         self.owner_name = owner_name
#         self.balance = balance if balance >= 0 else 0

#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
    
#     def withdraw(self, amount):
#         if amount <- self.balance:
#             self.balance -= amount
#         else:
#             print("Niewystarczające środki na koncie!")

# account = BankAccount("Alice", 1000)
# new_balance = account.deposit(500)
# print(f"Nowy stan konta: {new_balance}")
# account.deposit(500)
# print(f"Nowy stan konta: {account.balance}")
# account.withdraw(2000)    
# account.withdraw(500)   

# Zadanie 3. Utwórz klasę Temperature, która zwiera pole value (w stopniach Celsjusza), metody to_fahrenheit(),
# która zamienia stopnie Celsjusza na Fahrenheita i to_kelvin(), która zamienia stopnie Celsjusza na Kelvina oraz
# metodę statyczną celsius_to_fahrenheit(celsius), aby wykonać konwersję bez konieczności tworzenia obiektu.

# print("\nZadanie 3")

# class Temperature:
#     def __init__(self, value):
#         self.value = value

#     def to_fahrenheit(self):
#         return self.value * 9 / 5 + 32
    
#     def to_kelivn(self):
#         return self.value  + 273.15
    
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return celsius * 9 / 5 + 32
    

# temp = Temperature(25.5)
# print(f"Aktualna temperatura w stopanich Celsjusza: {temp.value}.")

# print(f"Temperatura w stopniach Fahrenheita: {temp.to_fahrenheit()}.")
# print(f"Temperatura w stopniach Kelvinach: {temp.to_kelivn()}.")

# print("\nMetoda statyczna:")
# temperatura = 31.7
# print(f"{temperatura} stopni Celsjusza to {Temperature.celsius_to_fahrenheit(temperatura)} stopni Fahrenheita.")

# Zadanie 4. Utwórz abstrakcyjną klasę Animal, która zawiera pole name oraz abstrakcyjną metodę make_sound().
# Utwórz dwie klasy dziedziczące Dog i Cat. Nadpisz metodę make_sound() w obu klasach. Przykładowe użycie
# klas:
# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# dog.make_sound() # "Woof!"
# cat.make_sound() # "Meow!"

# print("\nZadanie 4")

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")
    
# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")
    
# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# dog.make_sound()
# cat.make_sound()

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




