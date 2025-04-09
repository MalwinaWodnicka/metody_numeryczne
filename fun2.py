# Julia Dobroszek, Malwina Wodnicka 4
import os
import numpy as np
from numpy.matlib import empty

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

def dane_z_pliku(nazwa_pliku):
    sciezka = os.path.join("UkladyRownan", nazwa_pliku)
    try:
        with open(sciezka, "r", encoding="utf-8") as f:
            linie = f.readlines()
# dane z linii są ładowane do macierzy numpy
        dane = np.loadtxt(linie)
        macierz = dane[:, :-1]
        wektor = dane[:, -1]
        return macierz, wektor
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku {nazwa_pliku}: {e}")
        return None, None


def wybor():
    dostepne_przyklady = set(przyklady.values())
    wybory = []
    kontynuuj = True

    while kontynuuj:
        wybor = input("Wybierz przykład (q aby zakończyć): ").upper()
        if wybor == "Q" and len(wybory) > 0:
            kontynuuj = False
        elif wybor == "Q":
            print("Wybierz przynajmniej jeden przykład.")
        elif wybor in dostepne_przyklady and wybor not in wybory:
            wybory.append(wybor)
        elif wybor in wybory:
            print("Ten przykład został już wybrany.")
        else:
            print("Wybierz istniejący przykład.")

    return wybory


def czy_oznaczona(przyklad, macierz, wektor):
    try:
        A = np.array(macierz, dtype=np.float64)
        b = np.array(wektor, dtype=np.float64).flatten()

        if A.ndim != 2 or b.ndim != 1 or A.shape[0] != b.shape[0]:
            return f"\nNieprawidłowe wymiary macierzy/wektora dla przykładu: {przyklad}\n"

        macierz_rozszerzona = np.column_stack((A, b))

        rzad_A = np.linalg.matrix_rank(A)
        rzad_rozszerzona = np.linalg.matrix_rank(macierz_rozszerzona)
        n = A.shape[1]

        if rzad_A < rzad_rozszerzona:
            return f"\nUkład jest sprzeczny (brak rozwiązań) dla przykładu: {przyklad}\n"
        elif rzad_A == rzad_rozszerzona:
            if rzad_A < n:
                return f"\nUkład jest nieoznaczony (nieskończenie wiele rozwiązań) dla przykładu: {przyklad}\n"
            else:
                return True
        else:
            return True

    except Exception as e:
        return f"\nBłąd podczas analizy układu {przyklad}: {str(e)}\n"

def stop():
    print("Podaj kryterium zatrzymania algorytmu:")
    print("1 - Dokładność ε (|xi−xi−1| < ε)")
    print("2 - Liczba iteracji")

    while True:
        try:
            stop = int(input("Wybierz kryterium (1/2): "))
            if stop == 1:
                e = float(input("Podaj ε: "))
                return e, None
            elif stop == 2:
                i = int(input("Podaj maksymalną liczbę iteracji: "))
                return None, i
            else:
                print("Błędna wartość. Wybierz 1 lub 2.")
        except ValueError:
            print("Podano niepoprawny format. Spróbuj ponownie.")

def dominacja_diagonalna(A):
    for i in range(len(A)):
        suma = sum(abs(A[i][j]) for j in range(len(A)) if j != i)
        if abs(A[i][i]) <= suma:
            return False
    return True

def gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=100):
    n = len(A)
    x = np.zeros(n) if x0 is None else x0.copy()

    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            suma = sum(A[i][j] * x_new[j] if j < i else A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - suma) / A[i][i]

        if float(np.linalg.norm(x_new - x, ord=np.inf)) < tol:
            return x_new, k + 1
        x = x_new

    return x, max_iter

def rozwiaz_uklad(przyklad, macierz, wektor, tol, max_iter):
    if macierz is None or wektor is None:
        print(f"\nBłąd: Brak danych dla przykładu {przyklad}.")
        return
    print(f"\nRozwiązanie dla przykładu {przyklad}:")
    if not dominacja_diagonalna(macierz):
        print("Macierz nie spełnia warunku dominacji diagonalnej. Nie można rozwiązać metodą Gaussa-Seidla.")
    else:
        x, iteracje = gauss_seidel(macierz, wektor, tol=tol, max_iter=max_iter)

        print(f"Rozwiązanie: {x}")
        print(f"Liczba iteracji: {iteracje}")