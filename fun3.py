import numpy as np

def liniowa(x):
    return 3 * x + 2

def wielomian(x):
    return x**3 - 2 * x + 7

def zlozona1(x):
    return np.cos(x)**2 + 3 * x

def zlozona2(x):
    return np.abs(-5 * x + 10)

def wybierz_funkcje(czy, nazwa):
    if czy:
        return int(nazwa[8])
    print("""
Wybierz funkcję:
[1] y = 3x + 2
[2] |x|
[3] x^3 - 2x + 7
[4] sin(x)
[5] cos^2(x) + 3x
[6] |-5x + 10|
    """)
    while True:
        try:
            wyb = int(input("Podaj numer funkcji: "))
            if wyb in range(1, 7):
                break
        except:
            pass
        print("Niepoprawna wartość, spróbuj ponownie.")

    return wyb

def funkcja(f_id, x):
    if f_id == 1:
        return liniowa(x)
    elif f_id == 2:
        return np.abs(x)
    elif f_id == 3:
        return wielomian(x)
    elif f_id == 4:
        return np.sin(x)
    elif f_id == 5:
        return zlozona1(x)
    elif f_id == 6:
        return zlozona2(x)
    return None




def interpolacja_lagrange(x, x_vals, y_vals):
    wynik = 0.0
    n = len(x_vals)
    for i in range(n):
        iloczyn = 1.0
        for j in range(n):
            if i != j:
                iloczyn *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        wynik += iloczyn * y_vals[i]
    return wynik

def wczytaj_punkty_z_pliku(nazwa_pliku):
    x_vals, y_vals = [], []
    with open(nazwa_pliku) as f:
        n = int(f.readline())
        for _ in range(n):
            x, y = map(float, f.readline().split())
            x_vals.append(x)
            y_vals.append(y)
    return np.array(x_vals), np.array(y_vals)

def wczytaj_recznie(n, f_id):
    x_vals = []
    for i in range(n):
        x = float(input(f"x[{i}]: "))
        x_vals.append(x)
    y_vals = funkcja(f_id, np.array(x_vals))
    return np.array(x_vals), np.array(y_vals)