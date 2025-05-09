import sys
from cmath import cos
import matplotlib.pyplot as plt
import numpy as np
from fun5 import *


def check_int(value):
    try:
        value = int(value)
        return value
    except ValueError:
        print("\nWprowadzono nieprawidlowy znak!")


def check_float(value):
    try:
        value = float(value)
        return value
    except ValueError:
        print("\nWprowadzono nieprawidlowy znak!")


if __name__ == '__main__':

    while True:
        # WYBOR FUNKCJI
        print()
        choice = 'str'
        test = {0, 1, 2, 3, 4}
        while choice not in test:
            print('__WYBÓR FUNKCJI__')
            print('0. WYJŚCIE Z PROGRAMU')
            print('1. x + 2')
            print('2. x^2 - 2x + 2')
            print('3. |x|')
            print('4. cos(2x)')
            # print('5. -x^5 + 3x^3 + x + 2')

            choice = input('\nWybierz funkcję z listy: ')
            choice = check_int(choice)

            if choice not in test:
                print("\nWybierz funkcję z zakresu 1-4!")
            print()

        # PRZYPISANIE FUNKCJI
        def fun(x):
            return x

        if choice == 0:
            sys.exit()
        if choice == 1:
            def fun(x): return H([1, 2], x)
        if choice == 2:
            def fun(x): return H([1, -2, 2], x)
        if choice == 3:
            def fun(x): return abs(x)
        if choice == 4:
            def fun(x): return cos(2 * x)
        # if choice == 5:
        #     def fun(x): return H([-1, -1, 0, 3, 0, 1, 3, 0, 0], x)

        # WYBÓR TRYBU
        c = 'str'
        test = {1, 2}
        while c not in test:
            print("Wybór trybu:")
            print("1. Wybór stopnia wielomianu aproksymującego")
            print("2. Wprowadzenie oczekiwanego błędu aproksymacji")

            c = input('\nWybierz tryb z listy: ')
            c = check_int(c)

            if c not in test:
                print("\nWybierz tryb 1 lub 2")
            print()
        if c == 1:
            n = check_int(input("Podaj stopień wielomianu aproksymującego: "))
        else:
            n = 1
            eps = check_float(input("Podaj oczekiwaną wartość błędu aproksymacji: "))

        # WYBÓR PRZEDZIAŁU
        a, b = 0, 0
        while a >= b:
            a = check_float(input("\nPodaj lewy kraniec przedziału: "))
            b = check_float(input("Podaj prawy kraniec przedziału: "))

        # WYBRANIE DOKŁADNOŚCI CAŁKOWANIA
        nodes = 1
        while nodes < 2 or nodes > 5:
            nodes = check_int(input("\nPodaj ilość węzłów( 2-5 ): "))
            print()

        x, w = np.polynomial.laguerre.laggauss(nodes)
        factors = []
        err = 0
        if c == 1:
            for i in range(n + 1):
                print(f'Wspolczynnik {i}')
                factors.append(calculate(fun, w, x, nodes, i))
                print(f'a{i} = {factors[i]}\n')
            err = error(fun, w, x, factors, nodes, n)
            print(f'Błąd aproksymacji = {err}')
        else:
            while True:
                factors = []
                for i in range(n+1):
                    factors.append(calculate(fun, w, x, nodes, i))
                err = round(error(fun, w, x, factors, nodes, n), 6)
                if err <= eps:
                    print(f'Błąd aproksymacji {err} <= {eps} osiągnięto dla wielomianu aproksymującego stopnia {n}')
                    break
                else:
                    n += 1

        plt_x, plt_y, plt_yo = [], [], []
        x_s = np.linspace(a, b, 100)
        for x in x_s:
            res = 0
            for j in range(n + 1):
                res += factors[j] * L(x, j)
            plt_x.append(x)
            plt_y.append(fun(x))
            plt_yo.append(res)
            # print(f'x={plt_x}, y={plt_y}, yo={plt_yo}')
        plt.plot(plt_x, plt_y, 'g')    # funkcja pierwotna (zielona)
        plt.plot(plt_x, plt_yo, 'r--')     # funkcja aproksymująca (czerwona)
        plt.legend(['funkcja pierwotna', 'funkcja aproksymująca'])
        plt.show()