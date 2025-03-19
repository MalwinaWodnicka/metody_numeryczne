# Julia Dobroszek, Malwina Wodnicka
import numpy as np
import matplotlib.pyplot as plt


def funkcja_wielomianowa(x):
    return -2 * x ** 3 + 12 * x ** 2 + 16 * x


def funkcja_trygonometryczna(x):
    return 4 * np.sin(2 * x)


def funkcja_wykladnicza(x):
    return 4 ** x - 16


def funkcja_zlozona(x):
    z = 4 * np.sin(2 * x)
    return -2 * z ** 3 + 12 * z ** 2 + 16 * z


# Użytkownik wybiera funkcję (funkcje, które muszą być wbudowane: wielomian, f. tryg., f. wykładnicza, złożenie z poprzednich 3)
def wybor_funkcji():
    funkcja = 0
    while funkcja not in [1, 2, 3, 4]:
        print("Wybierz funkcję.")
        print("1 - wielomian (-2x^3 + 12x^2 + 16x)")
        print("2 - funkcja trygonometryczna (4sin(2x))")
        print("3 - funkcja wykładnicza (4^x - 16)")
        print("4 - złożenie funkcji (-2(4sin(2x))^3 + 12(4sin(2x))^2 + 16(4sin(2x)))")
        funkcja = int(input("Wybierz funkcję: "))

        if funkcja == 1:
            return funkcja_wielomianowa
        elif funkcja == 2:
            return funkcja_trygonometryczna
        elif funkcja == 3:
            return funkcja_wykladnicza
        elif funkcja == 4:
            return funkcja_zlozona
        else:
            print("Niepoprawny wybór funkcji.")
    return None


# Użytkownik określa przedział, na którym poszukiwane jest miejsce zerowe.
def okreslenie_przedzialu(f):
    print("Podaj początek i koniec przedziału, na którym poszukiwane jest miejsce zerowe.")
    while True:
        a = float(input("Podaj początek przedziału: "))
        b = float(input("Podaj koniec przedziału: "))
        # Sprawdzenie, czy przedział jest unimodalny
        if f(a) * f(b) < 0:
            return a, b
        print("Przedział musi być unimodalny. Podaj wartości ponownie.")


# Użytkownik wybiera kryterium zatrzymania algorytmu:
def stop(e, i):
    print("Podaj kryterium zatrzymania algorytmu.")
    print("1 - Dokładność ε ((|xi−xi−1| < ε)")
    print("2 - Liczba iteracji")
    while True:
        stop = int(input("Wybierz kryterium: "))
        if stop == 1:
            e = float(input("Podaj ε: "))
            return e, i
        elif stop == 2:
            max_iteracje = int(input("Podaj maksymalną liczbę iteracji: "))
            i = max_iteracje
            return e, i
        else:
            print("Została podana zła wartość. Podaj wartość ponownie.")


# 0: Metoda bisekcji
def bisekcja(f, a, b, e, i):
    n = 0
    while (b - a) / 2 > e and n < i:
        c = (a + b) / 2
        if f(c) == 0:
            return c, n
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        n += 1
    return (a + b) / 2, n


# 3: Metoda Regula Falsi
def regula_falsi(f, a, b, e, i):
    n = 0
    c = a
    while n < i:
        c_poprzednie = c
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if abs(c - c_poprzednie) < e:
            return c, n

        if f(c) == 0:
            return c, n
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        n += 1
    return c, n
