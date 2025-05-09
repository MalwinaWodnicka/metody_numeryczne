import matplotlib.pyplot as pyplot
import numpy as np

from math import cos, pi, sin, sqrt

class Function:
    def __init__(self, calc):
        self.__calc = calc

    def __call__(self, x):
        return self.__calc(x)


def draw_function(function, a, b, nodes=[]):
    x = np.linspace(a, b, 100)

    figure = pyplot.figure()
    axis = figure.add_subplot(1, 1, 1)
    axis.spines['right'].set_color('none')
    axis.spines['top'].set_color('none')
    axis.xaxis.set_ticks_position('bottom')
    axis.spines['bottom'].set_position(('data', 0))
    axis.yaxis.set_ticks_position('left')
    axis.spines['left'].set_position(('data', 0))

    axis.plot(1, 0, ls="", marker=">", ms=10, color="k",
              transform=axis.get_yaxis_transform(), clip_on=False)
    axis.plot(0, 1, ls="", marker="^", ms=10, color="k",
              transform=axis.get_xaxis_transform(), clip_on=False)

    y_vals = x.copy()
    for i in range(len(y_vals)):
        y_vals[i] = function(x[i])
    pyplot.plot(x, y_vals, 'r', label="f(x)")

    section = np.arange(a, b, 0.0001)
    y_vals = section.copy()
    for i, val in enumerate(y_vals):
        y_vals[i] = function(val)
    pyplot.fill_between(section, y_vals, color='b', alpha=.2)

    for i, node_x in enumerate(nodes):
        node_y = function(node_x)
        pyplot.plot(node_x, node_y, 'rx')

    pyplot.axvline(x=a)
    pyplot.axvline(x=b)

    pyplot.xticks(np.arange(min(x), max(x) + 1, 1.0))
    pyplot.legend()
    pyplot.show()



# Dzieli przedział na coraz więcej podprzedziałów (zaczynając od 3)
# Oblicza wartość całki dla każdego podziału
# Powtarza, aż różnica między kolejnymi przybliżeniami będzie mniejsza niż e

def simpson(f, a, b, e, wage_function):
    prev_val = None
    curr_val = None
    nodes = 3  # musi być >= 2 i nieparzysta

    while prev_val is None or abs(prev_val - curr_val) >= e:
        prev_val = curr_val
        h = (b - a) / nodes #szerokość podprzedziału
        sum = f(a) * wage_function(a)
        sum += f(b) * wage_function(b)

        for i in range(1, nodes + 1):
            if i % 2 == 1: #węzły środkowe
                sum += 4 * f(a + i * h) * wage_function(a + i * h)
            else: #węzły pośrednie
                sum += 2 * f(a + i * h) * wage_function(a + i * h)

        sum *= h
        sum /= 3

        curr_val = sum
        nodes += 2
    return curr_val, nodes

# Wykorzystuje n węzłów będących pierwiastkami wielomianów Czebyszewa
# Oblicza przybliżenie całki z funkcji ważonej 1/√(1-x²)
def gauss_czebyszew(f, n):
    sum = 0
    A = pi / (n + 1) #waga kwadratury (stała dla wszystkich węzłów w tej metodzie)
    nodes = []
    for i in range(0, n + 1):
        x = cos(((2 * i + 1) * pi) / (2 * n + 2)) #pierwiastek wielomianu czybyszewa: węzeł
        nodes.append(x)
        sum += A * f(x)
    return sum, nodes

# Oblicza całkę w przedziale [-1, 1] metodą adaptacyjną
# Dzieli przedział na mniejsze fragmenty aż do osiągnięcia żądanej dokładności
def simpson_limit(func, epsilon: float, wage_function) -> float:
    a = 0
    b = 0.5
    result = 0
    # granica do +1
    while True:
        integral = simpson(func, a, b, epsilon, wage_function)[0]
        result += integral
        a = b
        b = b + (1 - b) / 2
        if abs(integral) < epsilon:
            break
    # granica do -1
    a = -0.5
    b = 0
    while True:
        integral = simpson(func, a, b, epsilon, wage_function)[0]
        result += integral
        b = a
        a = a - (1 - abs(a)) / 2
        if abs(integral) < epsilon:
            break
    return round(result, 5)