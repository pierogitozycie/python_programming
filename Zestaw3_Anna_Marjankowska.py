import itertools
import random as rnd

# Zadanie 1. Niech będzie dana lista lst = ['a','b','c','d','e','f']. Wykorzystując metody z modułu itertools
# utwórz listę lst_res = ['a', 'ab', 'abc', 'abcd', 'abcdef'].

print("\nZadanie 1")
lst = ['a','b','c','d','e','f']
lst_rest = itertools.accumulate(lst)
print(list(lst_rest))


# Zadanie 2. Wykorzystując metody z modułu itertools utwórz listę złożoną z maksymalnych
# elementów wybranych z kolejnych 1, 2, 3, 4, … elementów listy. Na przykład, dla listy [5, 3, 6, 2, 1, 9,
# 1] wynikiem będzie lista [5, 5, 6, 6, 6, 9, 9] (5 = max(5), 5 = max(5, 3), 6 = max(5, 3 ,6), 6 = max(5, 3, 6,
# 2), itd.).

print("\nZadanie 2")

numbers = [5, 3, 6, 2, 1, 9, 1]
max_number = list(itertools.accumulate(numbers, max))
print(max_number)

# Zadanie 3. Napisz generator, który generuje kolejne potęgi dwójki od 1 do n (n ma być parametrem
# generatora). Do potęgowania wykorzystaj przesunięcie bitowe.

print("\nZadanie 3")

def potega(n):
    for i in range(1, n+1):
        yield 1 << i

number = 5

print(f"Kolejne potęgi liczby 2 od 1 do {number}")
for gen in potega(number):
    print(gen)

# Zadanie 4. Wykorzystaj łączenie generatorów do wygenerowania kwadratów n (n ma być
# parametrem generatora) kolejnych liczb ciągu Fibonacciego.

print("\nZadanie 4")

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def squareoffibbonaci(n):
    for fib in fibonacci(n):
        yield fib**2

n = 10

print(f"Kwadraty {n} kolejnych liczb ciągu Fibonacciego:")

for gen in squareoffibbonaci(n):
    print(gen)


# Zadanie 5. Napisz generator, który przyjmuje inny generator i zwraca tylko liczby parzyste z jego
# wyników.

print("\nZadanie 5")

def numbers(n):
    lst_res = []
    for _ in range(n):
        rand = rnd.randint(0,100)
        lst_res.append(rand)
        yield rand
    print("\nLista początkowa:", lst_res)
    

def evennumber(gen):
    print("Liczby parzyste z liczby początkowej:")
    for num in gen:
        if num % 2 == 0:
            yield num
    
for gen in evennumber(numbers(6)):
    print(gen)

# Zadanie 6. Napisz program, który korzystając z funkcji filter(), wyświetli tylko liczby parzyste z
# listy zagnieżdżonych list.

print("\nZadanie 6")

# Stwórzmy funckję, która stworzy nam listę zagnieżdżonych list 
# n liczba list w liscie, k - liczba elementow w podliscie

def numbers(n, k):
    lst = []
    for _ in range (n):
        lstin = []
        for _ in range(k):
            random = rnd.randint(0,100)
            lstin.append(random)
        lst.append(lstin)
    return lst

nested_list = numbers(3, 4)
print(f"Początkowa lista: {nested_list}")

filtered_list = [list(filter(lambda x: x % 2 == 0, sublist)) for sublist in nested_list]
print(f"Liczby parzyste: {filtered_list}")