import pandas as pd
import ssl
import certifi
ssl._create_default_https_context = ssl._create_unverified_context


# Zadanie 8. Wczytaj za pomocą biblioteki pandas dane z pliku market.csv. Dane dotyczą transakcji sesji
# w ciągu jednego dnia. Następnie oblicz:
# 1. Ilość transakcji w ciągu tego dnia.
# 2. Sumę wartości wszystkich transakcji.
# 3. Trzy najczęściej handlowane spółki.
# 4. Trzy spółki, na których sumaryczny obrót transakcji był najwyższy


print("/nZadanie 8")

# wczytanie danych
data = pd.read_csv('/Users/aniamarjankowska/Documents/GitHub/python_programming/market.csv', sep = "," )

# podejrzenie danych
print(data.head())

# 1. Ilość transakcji w ciągu tego dnia.
print(f"Liczba transakcji zakładajac, że jedna transkacja odpowiada jednemu wierszowi: {data.shape[0]}.")

# 2. Sumę wartości wszystkich transakcji.
data['suma'] = data['cena']*data['ilosc']
print(f"Suma wartości wszytskich transakcji: {data['suma'].sum():0.2f}")

# 3. Trzy najczęściej handlowane spółki.
print(f"Trzy najczęściej handlowane spółki to: {", ".join(data['nazwa'].value_counts()[:3].index)}")

# 4. Trzy spółki, na których sumaryczny obrót transakcji był najwyższy
top3 = pd.DataFrame(data.groupby('nazwa')['suma'].sum().nlargest(3))
print(f"Trzy spółki o najwyżsyzm sumaryczynm obrocie to: \n{'\n'.join(f"{index}: {row['suma']:.2f}" for index, row in top3.iterrows())}")

# Zadanie 9. Wczytaj za pomocą biblioteki pandas dane o notowaniach giełdowych wybranych trzech
# spółki w formacie CSV (stooq.pl). Następnie:
# 1. Połącz dane w data frame ze względu na daty i uzupełnij braki danych
# 2. Przeprowadź analizę danych, tworząc kolumny z informacjami o procentowej zmianie ceny
# zamknięcia oraz o średniej ruchomej (np. 5-dniowej, miesięcznej) dla ceny zamknięcia.
# 3. Wyznaczyć dni, w których zmiana procentowa była większa niż określony próg (np. 2%) i wyświetl
# te rekordy.
# 4. Wyznacz stopy zwrotu i znajdź okresy, w których stopy zwrotu były najniższe lub najwyższe.

print("\nZadanie 9")

# parse_dates - zmienia kolumne na obiekt dataframe
pko_df = pd.read_csv("pko_d.csv", parse_dates=['Data'], index_col='Data')
pkn_df = pd.read_csv("pkn_d.csv", parse_dates=['Data'], index_col='Data')
lpp_df = pd.read_csv("lpp_d.csv", parse_dates=['Data'], index_col='Data')

# opuszczamy kolumny które nie są nam potrzebne, oraz zmieniamy nazwy aby identyfikować każdą firmę:
pko_df = pko_df[['Zamkniecie']].rename(columns={'Zamkniecie': 'PKO_Zamkniecie'})
pkn_df = pkn_df[['Zamkniecie']].rename(columns={'Zamkniecie': 'PKN_Zamkniecie'})
lpp_df = lpp_df[['Zamkniecie']].rename(columns={'Zamkniecie': 'LPP_Zamkniecie'})

# 1. Połącz dane w data frame ze względu na daty i uzupełnij braki danych
# join outher = nie pomijamy wartosci N/A po połączeniu dwóch df
data = pd.concat([pko_df, pkn_df, lpp_df], axis=1, join='outer')
data = data.ffill().bfill()
print(data.head())

# 2. Przeprowadź analizę danych, tworząc kolumny z informacjami o procentowej zmianie ceny
# zamknięcia oraz o średniej ruchomej (np. 5-dniowej, miesięcznej) dla ceny zamknięcia.

data['PKO_Zmiana'] = data['PKO_Zamkniecie'].pct_change() * 100
data['PKN_Zmiana'] = data['PKN_Zamkniecie'].pct_change() * 100
data['LPP_Zmiana'] = data['LPP_Zamkniecie'].pct_change() * 100

data['PKO_SR5'] = data['PKO_Zamkniecie'].rolling(window=5).mean()
data['PKO_SR30'] = data['PKO_Zamkniecie'].rolling(window=30).mean()

data['PKN_SR5'] = data['PKN_Zamkniecie'].rolling(window=5).mean()
data['PKN_SR30'] = data['PKN_Zamkniecie'].rolling(window=30).mean()

data['LPP_SR5'] = data['LPP_Zamkniecie'].rolling(window=5).mean()
data['LPP_SR30'] = data['LPP_Zamkniecie'].rolling(window=30).mean()

print(data.head())

# 3. Wyznaczyć dni, w których zmiana procentowa była większa niż określony próg (np. 2%) i wyświetl
# te rekordy.

PKO_powyzej_progu = data[data['PKO_Zmiana'] > 2]
PKN_powyzej_progu = data[data['PKN_Zmiana'] > 2]
LPP_powyzej_progu = data[data['PKN_Zmiana'] > 2]

print("Dni kiedy zmiana procentowa dla PKO była wyższa niż 2%:\n")
print(pd.DataFrame(PKO_powyzej_progu.index))

print("Dni kiedy zmiana procentowa dla PKN była wyższa niż 2%\n")
print(pd.DataFrame(PKN_powyzej_progu.index))

print("Dni kiedy zmiana procentowa dla LPP była wyższa niż 2%\n")
print(pd.DataFrame(LPP_powyzej_progu.index))

# 4. Wyznacz stopy zwrotu i znajdź okresy, w których stopy zwrotu były najniższe lub najwyższe.

data['PKO_Stopy'] = data["PKO_Zamkniecie"] /  data["PKO_Zamkniecie"].iloc[0] - 1
data['PKN_Stopy'] = data["PKN_Zamkniecie"] /  data["PKN_Zamkniecie"].iloc[0] - 1
data['LPP_Stopy'] = data["LPP_Zamkniecie"] /  data["LPP_Zamkniecie"].iloc[0] - 1

PKO_max_stopa = data[data['PKO_Stopy'] == data['PKO_Stopy'].max()]
PKO_min_stopa = data[data['PKO_Stopy'] == data['PKO_Stopy'].min()]

PKN_max_stopa = data[data['PKN_Stopy'] == data['PKN_Stopy'].max()]
PKN_min_stopa = data[data['PKN_Stopy'] == data['PKN_Stopy'].min()]

LPP_max_stopa = data[data['LPP_Stopy'] == data['LPP_Stopy'].max()]
LPP_min_stopa = data[data['LPP_Stopy'] == data['LPP_Stopy'].min()]


print(f"\nMaksymalna stopa dla PKO była równa:\n{PKO_max_stopa}\n najniższa:\n{PKO_min_stopa} ")
print(f"\nMaksymalna stopa dla PKN była równa:\n{PKN_max_stopa}\n najniższa:\n{PKN_min_stopa} ")
print(f"\nMaksymalna stopa dla LPP była równa\n{LPP_max_stopa}\n  najniższa:\n{LPP_min_stopa} ")

# Zadanie 10. Masz zbiór danych dotyczący sprzedaży produktów na przykład na stronie
# https://archive.ics.uci.edu/ml/machine-learningdatabases/00292/Wholesale%20customers%20data.csv. Następnie:
# 1. Wykonaj preprocessing danych (np. usunięcie brakujących wartości, wyznacz statystyki opisowe).
# 2. Wyznacz średnie sprzedaży w określonych regionach.
# 3. Oblicz współczynniki korelacji między sprzedażą różnych produktów.

print('\nZadanie 10')

data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00292/Wholesale%20customers%20data.csv")
print(data.head())

# 1. Wykonaj preprocessing danych (np. usunięcie brakujących wartości, wyznacz statystyki opisowe).
print(f"\nBrakujące wartości w danych:\n{data.isnull().sum()}")
print(f"\nStatystki opisowe:\n{data.describe()}")

# 2. Wyznacz średnie sprzedaży w określonych regionach.
average_per_region = data.groupby("Region").mean()
print(f"\nŚrednia sprzedaży w rejonach:\n{average_per_region}")

# 3. Oblicz współczynniki korelacji między sprzedażą różnych produktów.
correlationmatrix = data.corr()
print(f"Macierz korealcji:\n {correlationmatrix}")

# Zadanie 11. Analiza danych z sensorów IoT
# Poszukaj danych z kilku sensorów (temperatura, wilgotność, ciśnienie) zapisanych w pliku CSV. Każdy
# wiersz niech zawiera wartości z danego momentu czasowego.
# • Wczytaj dane z pliku CSV.
# • Zbadaj rozkład wartości z każdego sensora (średnia, mediana, odchylenie standardowe, wartości
# minimalne i maksymalne).
# • Wyznacz dni, w których wartości sensora przekroczyły określone progi (np. temperatura > 30°C)

print("\nZadanie 11")

# • Wczytaj dane z pliku CSV.
data = pd.read_csv("AirQualityUCI.csv", sep=';', decimal=',', engine='python')
print(data.head())

# Usunięcie kolumn pustych
data = data.drop(columns=["Unnamed: 15", "Unnamed: 16"], errors='ignore')

# Konwersja kolumny daty i czasu na format datetime
data['DateTime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], format='%d/%m/%Y %H.%M.%S', errors='coerce')

# Usunięcie wierszy z brakującymi wartościami
print(f"Print brakujące dane: {data.isnull().sum()}")
data = data.dropna()

# • Zbadaj rozkład wartości z każdego sensora (średnia, mediana, odchylenie standardowe, wartości
# minimalne i maksymalne).
print(f"\nStatystyki opisowe:\n{data.describe()}")

# • Wyznacz dni, w których wartości sensora przekroczyły określone progi (np. temperatura > 30°C)
high_temp = data[data['T'] > 30]
print(f"\nDni z temperaturą powyżej 30°C:\n{high_temp[['DateTime', 'T']]}")