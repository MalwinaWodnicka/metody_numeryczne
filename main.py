#Użytkownik wybiera funkcję (funkcje, które muszą być wbudowane: wielomian, f. tryg., f. wykładnicza)
funkcja = input("Wybierz funkcję. (1 - wielomian, 2 - funkcja trygonometryczna, 3 - funkcja wykładnicza): ")

#Użytkownik określa przedział, na którym poszukiwane jest miejsce zerowe. UWAGA: sprawdzenie, czy przedział jest unimodalny
a = input("Podaj początek przedziału: ")
b = input("Podaj koniec przedziału: ")
#Użytkownik wybiera kryterium zatrzymania algorytmu:
stop = input("Podaj kryterium zatrzymania algorytmu. (1 - osiągnięcie zadanej dokładności obliczeń, 2 - wykonanie określonej liczby iteracji): ")
# (1 - osiągnięcie zadanej dokładności obliczeń A: (|xi−xi−1| < ε)
if stop == 1:
    e = input("Podaj ε: ")
        #Jeśli 1: Użytkownik wprowadza ε.
    # (2 - wykonanie określonej liczby iteracji)
        #Jeśli 2: Użytkownik podaje liczbę iteracji.

#Program wykonuje obliczenia metodami 03
    #0: Metoda bisekcji
    #3: Metoda Regula Falsi

#Wyświetlenie wyników

#Rysunek wykresu funkcji na zadanym przedziale z rozwiązaniami na wykresie