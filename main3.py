import numpy as np
import matplotlib.pyplot as plt
import math
import fun3


def main():
    print("Interpolacja Lagrange’a (Python version)\n")
    print("[1] Wczytaj punkty z pliku\n[2] Wprowadź punkty ręcznie z funkcji")

    while True:
        try:
            wyb = int(input("Twój wybór: "))
            if wyb in [1, 2]:
                break
        except:
            pass
        print("Niepoprawny wybór.")

    if wyb == 1:
        czy = True
        nazwa = input("Podaj nazwę pliku: ")
        x_vals, y_vals = fun3.wczytaj_punkty_z_pliku(nazwa)
        f_id = fun3.wybierz_funkcje(czy, nazwa)
    else:
        czy = False
        n = int(input("Podaj liczbę węzłów: "))
        f_id = fun3.wybierz_funkcje(czy, "")
        x_vals, y_vals = fun3.wczytaj_recznie(n, f_id)

    a = float(input("Podaj początek przedziału: "))
    b = float(input("Podaj koniec przedziału: "))
    if b < a:
        a, b = b, a

    x = np.linspace(a, b, 1000)
    y_interp = [fun3.interpolacja_lagrange(xi, x_vals, y_vals) for xi in x]

    y_original = fun3.funkcja(f_id, x)


    plt.plot(x, y_interp, label="Interpolacja Lagrange’a", color='orange')
    if y_original is not None:
        plt.plot(x, y_original, label="Funkcja oryginalna", color='blue')
    plt.scatter(x_vals, y_vals, label="Węzły interpolacji", color='red')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Interpolacja wielomianowa (metoda Lagrange’a)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
