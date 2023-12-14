import numpy as np


def gauss_method(a, b):
    n = len(a)

    for k in range(n - 1):
        for i in range(k + 1, n):
            if a[i, k] != 0.0:
                factor = a[i, k] / a[k, k]
                a[i, k + 1:n] = a[i, k + 1:n] - np.multiply(factor, a[k, k + 1:n])
                b[i] = b[i] - np.multiply(factor, b[k])
    print(a)

    for k in range(n - 1, -1, -1):
        if a[k, k] != 0:
            b[k] = (b[k] - np.dot(a[k, k + 1:n], b[k + 1:n])) / a[k, k]

    return b


s = np.array([[1, 2, 0, 0], [0, 1, 1, 0], [0, -3, 1, -1], [0, -4, 0, 2]], dtype=float)

g = np.array([5, 1, -5, 0], dtype=float)

x = gauss_method(s, g)

print(x)
