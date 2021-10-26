import matplotlib.pyplot as plt
import cec2017
import numpy as np

from cec2017.functions import f1, f2, f3
from autograd import grad

UPPER_BOUND = 100
DIMENSIONALITY = 2
#wylosuj punkt x:
x = np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=DIMENSIONALITY)

#wyznacz ocenę x
q = f1(x)
print('q(x) = %.6f' %q)


