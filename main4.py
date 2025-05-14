import matplotlib.pyplot as pyplot
import numpy as np
import fun4
from math import cos, pi, sin, sqrt




def main():
    functions = [
        ("1", fun4.Function(lambda x: 1)),
        ("x^2 + 2", fun4.Function(lambda x: x ** 2 + 2)),
        ("sin(x)", fun4.Function(lambda x: sin(x))),
        ("x^5 + 3x^4 + x^2 + 1", fun4.Function(lambda x: x ** 5 + 3 * x ** 4 + x ** 2 + 1)),
        ("1 +  1 / (1 + 25x^2)", fun4.Function(lambda x: 1 + 1 / (1 + 25 * x**2))),
        ("|1 / x|", fun4.Function(lambda x: abs(1 / x))),
        ("1 / sqrt(1 - x^2)", fun4.Function(lambda x: 1 / sqrt(1 - x**2))),
        ("|sin(x * 10 pi)|", fun4.Function(lambda x: abs(sin(x * 10 * pi))))
    ]

    function_choice = None
    method_choice = None
    e = 0
    calc_limit = None
    nodes = []

    while function_choice is None:
        print("Wybierz funkcje")
        for i in range(len(functions)):
            print(f"\t{i + 1}. {functions[i][0]}")
        function_choice = input("\t>>>>")
        if int(function_choice) not in range(1, len(functions) + 1):
            print("Nie ma takiej opcji w menu")
            function_choice = None
    chosen_function = functions[int(function_choice) - 1][1]
    while method_choice is None:
        print("Wybierz metode")
        print("\t1. Newton-Cotes")
        print("\t2. Gauss-Czebyszew")
        method_choice = input("\t>>>>")
        if int(method_choice) not in range(1, 3):
            print("Nie ma takiej opcji w menu")
            method_choice = None
    if int(method_choice) == 1:
        wage_function = lambda x: (1/((1-x**2)**(1/2)))
        a = -1
        b = 1
        while float(e) <= 0:
            print("Podaj dokladnosc")
            e = input("\t>>>>")
        result, nodes = fun4.simpson_limit(chosen_function, float(e), wage_function)
        print(result)
        fun4.draw_function2(chosen_function, -1, 1, nodes)
    else:
        a, b = -0.99, 0.99
        for n in range(2, 6):
            result = fun4.gauss_czebyszew(chosen_function, n)
            print(f"Wynik dla {n} węzłów: {round(result[0],5)}")
            nodes = result[1]
            fun4.draw_function(fun4.Function(lambda x: chosen_function(x) / (1/sqrt(1 - x ** 2))), float(a), float(b), nodes)


if __name__ == '__main__':
    main()