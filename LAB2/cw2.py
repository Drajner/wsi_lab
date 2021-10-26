import matplotlib.pyplot as plt
import cec2017
import numpy as np

from cec2017.functions import f1, f2, f3
from autograd import grad


MAX_X = 100
PLOT_STEP = 0.1
UPPER_BOUND = 100
DIMENSIONALITY = 2


def booth(x1, x2):
    term1 = (x1 + 2*x2 - 7)**2
    term2 = (2*x1 + x2 - 5)**2
    y = term1 + term2
    return y


#wylosuj punkt x:
x = np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=DIMENSIONALITY)

#wyznacz ocenę x
q = f1(x)
print('q(x) = %.6f' %q)

def gradient(x, q):
    grad_fct = grad(q)
    gradinet = grad_fct(x)


x_arr = np.arange(-MAX_X, MAX_X, PLOT_STEP)
y_arr = np.arange(-MAX_X, MAX_X, PLOT_STEP)
X, Y = np.meshgrid(x_arr, y_arr)
Z = np.empty(X.shape)

q=f1

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i, j] = q(np.array([X[i, j], Y[i, j]]))
        
plt.contour(X, Y, Z, 20)
plt.arrow(0, 0, 50, 50, head_width=3, head_length=6, fc='k', ec='k')
plt.show()
  

