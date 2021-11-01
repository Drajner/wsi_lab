import matplotlib.pyplot as plt
import cec2017
import numpy as np

from cec2017.functions import f1, f2, f3
from autograd import grad


MAX_X = 200
PLOT_STEP = 0.1
UPPER_BOUND = 100
DIMENSIONALITY = 2


def booth(x):
    return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2


def steepest_descent_plot(fun, beta, steps):
    x0 = np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=DIMENSIONALITY)
    x = x0
    way = [x]
    for i in range(steps):
        fun_gradient = grad(fun)
        d = fun_gradient(x)
        x = x - (beta * d)
        way.append(x)

    x_arr = np.arange(-MAX_X, MAX_X, PLOT_STEP)
    y_arr = np.arange(-MAX_X, MAX_X, PLOT_STEP)
    X, Y = np.meshgrid(x_arr, y_arr)
    Z = np.empty(X.shape)

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = fun(np.array([X[i, j], Y[i, j]]))

    plt.contour(X, Y, Z, 20)
    for i in range(len(way)-1):
        plt.arrow(way[i][0], way[i][1], way[i+1][0] - way[i][0], way[i+1][1] - way[i][1], head_width=2, head_length=2, fc='k', ec='k')
    plt.show()


def main():
    steepest_descent_plot(booth, 0.05, 100)
    #steepest_descent_plot(f1, 0.00000001, 1000)
    #steepest_descent_plot(f2, 0.01, 1000)
    #steepest_descent_plot(f3, 0.00005, 1000)

if __name__ == "__main__":
    main()
