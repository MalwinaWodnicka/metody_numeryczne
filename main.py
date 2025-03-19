# Julia Dobroszek, Malwina Wodnicka
import numpy as np
import matplotlib.pyplot as plt
import fun

wybrana_funkcja = fun.wybor_funkcji()
poczatek_przedzialu, koniec_przedzialu = fun.okreslenie_przedzialu(wybrana_funkcja)

# Domyślne wartości
e = 1e-10
max_iteracje = 1000

e, max_iteracje = fun.stop(e, max_iteracje)

# Program wykonuje obliczenia metodami 03, wyświetla wyniki
x_bisekcja, i_bisekcja = fun.bisekcja(wybrana_funkcja, poczatek_przedzialu, koniec_przedzialu, e, max_iteracje)
print("Metoda bisekcji: ")
print(f"Znalezione miejsce zerowe: {x_bisekcja}, liczba iteracji: {i_bisekcja}")
x_regula_falsi, i_regula_falsi = fun.regula_falsi(wybrana_funkcja, poczatek_przedzialu, koniec_przedzialu, e,
                                                  max_iteracje)
print("Metoda Regula Falsi: ")
print(f"Znalezione miejsce zerowe: {x_regula_falsi}, liczba iteracji: {i_regula_falsi}")

# Rysunek wykresu funkcji na zadanym przedziale z rozwiązaniami na wykresie

x = np.linspace(poczatek_przedzialu, koniec_przedzialu, 1000)
y = wybrana_funkcja(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Funkcja', color='blue')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')

# Oznaczenie znalezionych miejsc zerowych
plt.scatter(x_bisekcja, wybrana_funkcja(x_bisekcja), color='red', marker='x', label='Bisekcja', zorder=3)
plt.scatter(x_regula_falsi, wybrana_funkcja(x_regula_falsi), color='green', marker='+', label='Regula Falsi', zorder=3)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji z miejscami zerowymi')
plt.legend()
plt.grid()
plt.show()
