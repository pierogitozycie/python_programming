import numpy as np
import random as rnd
from PIL import Image
from scipy.ndimage import convolve

# Zadanie 1. Utwórz tablicę numpy nxn zawierającą liczby losowe o rozkładzie normalnym o średniej 3
# i odchyleniu standardowym 2. Następnie oblicz:
# a) Wyznacznik macierzy
# b) Macierz odwrotną / pseudo-odwrotną
# c) Macierz transponowaną
# d) Wypisz wartości własne i wektory własne macierzy

# print("Zadanie 1 \n")
# n = 4
# matrix = np.random.normal(loc=3, scale=2, size=(n,n))
# print(f"Macierz {n}x{n}:\n{matrix}")

# # a) Wyznacznik macierzy

# determinant = np.linalg.det(matrix)
# print(f"\nWyznacznik macierzy: {determinant:0.2f}")

# # b) Macierz odwrotną / pseudo-odwrotną

# try:
#     inversematrix = np.linalg.inv(matrix)
# except np.linalg.LinAlgError:
#     print("Macierz nie jest osobliwa! Obliczymy macierz pseudo-odwrotną")
#     inversematrix = np.linalg.pinv(matrix)


# print("\n", inversematrix)

# # c) Macierz transponowaną

# transposematrix = matrix.T
# print(f"Macierz transponowana to:\n {transposematrix}")

# # d) Wypisz wartości własne i wektory własne macierzy

# eigenvalues, eigenvectors = np.linalg.eig(matrix)

# print(f"\nWartości właśne to:\n {eigenvalues} \nwektory własne:\n{eigenvectors}")

# Zadanie 2. Napisz funkcję, która zlicza częstotliwość występowania poszczególnych wartości w tablicy
# numpy.

# print("\nZadanie 2")

# matrix = np.array([[1,1,1,4], [0,1,5,1], [5,4,6,5]])

# def count_frequencies(matrix):
#     unique, counts = np.unique(matrix, return_counts=True)
#     return dict(zip(unique, counts))

# print(matrix)
# print(count_frequencies(matrix))

# Zadanie 3. Napisz funkcję, która zamienia wszystkie wartości ujemne na zero w tablicy numpy oraz
# wszystkie wartości NaN na średnią z kolumn w tablicy numpy.

# print("\nZadanie 3")

# matrix = np.array([[1,-1,np.nan,4], [np.nan,1,5,1], [5,-4,6,np.nan]])
# print(f"\nMacierz początkowa:\n{matrix}")

# def matrix_conventer(matrix):
#     # zamiana wartosci ujemnych na 0
#     matrix[matrix < 0] = 0

#     # zamiana wartości NA na średnią
#     columns_mean = np.nanmean(matrix, axis=0)
#     nan_index = np.where(np.isnan(matrix))
#     # np.where zwraca krotkę dwóch tablic, pirwsza zwiera indkesy wierszy, druga kolumn
#     matrix[nan_index] = columns_mean[nan_index[1]]

#     return matrix

# print(f"Macierz po zamianie wartości:\n{matrix_conventer(matrix)}")

# Zadanie 4. Wczytaj lub utwórz przykładową tablicę numpy o rozmiarze (100, 5), a następnie:
# • Znormalizuj (na podstawie minimum i maksimum w każdej kolumnie) dane w każdej kolumnie
# w taki sposób, aby wartości były w zakresie [0, 1].
# • Zwróć znormalizowaną tablicę oraz średnią wartość każdej kolumny po normalizacji.

# print("\nZadanie 4")

# matrix = np.random.randint(-10, 20, size=(100,50))

# print(f"Macierz początkowa: {matrix}")

# # normalizowanie macierzy 

# def normalize_matrix(matrix):
#     min_col = np.min(matrix, axis=0)
#     max_col = np.max(matrix, axis=0)

#     normalized_matrix = (matrix - min_col) / (max_col - min_col)
#     # dzieki broadcastingowi mozemy odejmowac macierze roznych wymiarow
#     return normalized_matrix, np.mean(normalized_matrix, axis=0)

# normalize_matrix, columns_mean = normalize_matrix(matrix)

# print(f"Macierz znormalizowana:\n{normalize_matrix}")
# print(f"\nŚrednie wartości z kolumn:\n{columns_mean}")

# Zadanie 5. Utwórz dwie macierze numpy o wymiarach (100, 100) z wartościami losowymi, a następnie:
# • Wykonaj iloczyn macierzy (mnożenie macierzy).
# • Oblicz iloczyn Kroneckera.
# • Przeprowadź dekompozycję macierzy przy użyciu SVD (Singular Value Decomposition).

# print("\nZadanie 5")

# matrix1 = np.random.randint(-10, 11, size=(100, 100))
# matrix2 = np.random.randint(-10, 11, size=(100, 100))

# # iloczyn: macierzy
# matrix_product = np.dot(matrix1, matrix2)
# print(f"Iloczyn macierzy:\n {matrix_product}")

# # iloraz Kroneckera
# kronecker = np.kron(matrix1, matrix2)
# print(f"\nIloczyn Kroneckera wymiaru {kronecker.shape}:\n {kronecker}")

# # dekompozycja macierzy
# U, S, Vh = np.linalg.svd(matrix1)
# print(f"\nDekompozycja została przeprowadzona. Rozmiar macierzy U: {U.shape}, S: {S.shape} i Vh: {Vh.shape}.")


# Zadanie 6. Utwórz tablicę numpy o wymiarach (50, 10), w której każda kolumna reprezentuje różne cechy,
# a następnie
# • Oblicz macierz korelacji pomiędzy kolumnami danych.
# • Znajdź parę kolumn, która ma najwyższą wartość korelacji dodatniej i parę z najwyższą korelacją
# ujemną

# print("\nZadanie 6")

# matrix = np.random.randint(-10, 11, size=(50, 10))
# print(f"Macierz początkowa:\n {matrix}")

# # obliczenie korelacji pomiędzy kolumnami danych:
# corr_matrix = np.corrcoef(matrix, rowvar=False)
# print(f"Macierz korelacji:\n {np.round(corr_matrix, decimals=2)}")

# # wyłączanie diagonalnych wartości (które zawsze wynoszą 1)
# np.fill_diagonal(corr_matrix, 0)

# # najwyższa korelacja dodatnia
# max_corr_value = np.max(corr_matrix)
# max_corr_indices = np.where(corr_matrix == max_corr_value)
# print(f"\nNajwyższa korelacja dodatnia jest między parą kolumn: {max_corr_indices[0][0]} i {max_corr_indices[1][0]}.")

# # najwyższa korelacja ujemna
# min_corr_value = np.min(corr_matrix)
# min_corr_indices = np.where(corr_matrix == min_corr_value)
# print(f"\nNajwyższa korelacja ujemna jest między parą kolumn: {min_corr_indices[0][0]} i {min_corr_indices[1][0]}.")

# Zadanie 7. Obraz może być przedstawiony jako tablica numpy, w której piksele są wartościami
# numerycznymi. Napisz operacje przetwarzania obrazu, takie jak konwersja do odcieni szarości, rozmycie i
# wykrywanie krawędzi:
# • Wczytaj obraz i przekształć go w tablicę numpy (każdy piksel ma trzy wartości: R, G, B).
# • Przekształć obraz do odcieni szarości (wykorzystując odpowiednie wagi dla kanałów R, G, B).
# • Zastosuj rozmycie obrazu przy użyciu splotu macierzy (np. użyj macierzy Gaussa do rozmycia).
# • Zastosuj wykrywanie krawędzi przy użyciu operatora Sobela.

print("\nZadanie 7")

# wczytanie obrazu i przekształcnie w tablicę numpy:
image = Image.open("/Users/aniamarjankowska/Downloads/305464337-760x500.jpg")  # Replace with your image path
image_np = np.array(image)

# przekształcenie do odcieni szarości:
weights = np.array([0.2989, 0.5870, 0.1140])  
gray_image = np.dot(image_np[..., :3], weights)

# rozmycie obrazu:
gaussian_kernel = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
]) / 16

blurred_image = convolve(gray_image, gaussian_kernel)

# wykrywanie krawędzi: 
sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])
sobel_y = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])


edges_x = convolve(blurred_image, sobel_x)
edges_y = convolve(blurred_image, sobel_y)

edges = np.hypot(edges_x, edges_y)  
edges = (edges / edges.max() * 255).astype(np.uint8)  

# wyświetlanie obrazu:
edges_image = Image.fromarray(edges)
edges_image.show() 
