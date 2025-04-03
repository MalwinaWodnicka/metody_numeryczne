import numpy as np
from tabulate import tabulate
import fun2

# Julia Dobroszek, Malwina Wodnicka 4

# Metoda iteracyjna Gaussa-Seidla

# Użytkownik wybiera ilość równań (maksymalna ilość może być ograniczona z gówy, ale algorytm uniwersalny)

# Użytkownik podaje warunek stopu (ilość iteracji albo uzyskanie dokładności)

# Wczytywanie współczynników układów równań z plików

# Sprawdzenie, czy podana macierz spełnia warunki zbieżności
def main():
    przyklady = {
        "ukladA.txt": "A",
        "ukladB.txt": "B",
        "ukladC.txt": "C",
        "ukladD.txt": "D",
        "ukladE.txt": "E",
        "ukladF.txt": "F",
        "ukladG.txt": "G",
        "ukladH.txt": "H",
        "ukladI.txt": "I",
        "ukladJ.txt": "J",
    }

    pliki = list(przyklady.keys())
    wszystkie_macierze = {}

    for plik in pliki:
        macierz, wektor = fun2.dane_z_pliku(plik)
        print(
            f"Typ macierzy: {type(macierz)}, Typ elementów: {macierz.dtype if isinstance(macierz, np.ndarray) else 'nie NumPy'}")
        print(
            f"Typ wektora: {type(wektor)}, Typ elementów: {wektor.dtype if isinstance(wektor, np.ndarray) else 'nie NumPy'}")

        if macierz is not None and wektor is not None:
            rozszerzona_macierz = np.hstack((macierz, wektor.reshape(-1, 1)))
            naglowki = [f"x{i + 1}" for i in range(macierz.shape[1])] + ["b"]
            nazwa_przykladu = przyklady.get(plik, f"Macierz równań z pliku: {plik}")

            print(f"\nPrzykład {nazwa_przykladu}")
            print(tabulate(rozszerzona_macierz, headers=naglowki, tablefmt="grid"))

            wszystkie_macierze[nazwa_przykladu] = (macierz, wektor)

    wybrane_przyklady = fun2.wybor()
    print("Wybrane przykłady:", wybrane_przyklady)

    for przyklad in list(wybrane_przyklady):
        macierz, wektor = wszystkie_macierze.get(przyklad, (None, None))
        ozn = fun2.czy_oznaczona(przyklad, macierz, wektor)
        if ozn != True:
            print(ozn)
            wybrane_przyklady.remove(przyklad)
    e, max_iteracje = fun2.stop()
    if e is None:
        e = 1e-10
    if max_iteracje is None:
        max_iteracje = 1000

    for przyklad in wybrane_przyklady:
        fun2.rozwiaz_uklad(przyklad, *wszystkie_macierze.get(przyklad, (None, None)), e, max_iteracje)

if __name__ == "__main__":
    main()
