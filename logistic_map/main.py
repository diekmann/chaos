#!/usr/bin/env python3
"""Implmenetation of https://en.wikipedia.org/wiki/Logistic_map."""

import math
import numpy as np
import matplotlib.pyplot as plt

def x_next(r, x):
    assert 0 <= x <= 1
    return r*x*(1-x)


def converge(r):
    x = 0.5
    x_p = [x]  # previous values
    msg = ""
    convergence_count = 0
    for i in range(100000):
        x_p.append(x)
        x = x_next(r, x)
        if math.isclose(x, x_p[-1], rel_tol=1e-15):
            msg = f"converged on {x}"
            convergence_count += 1
            if convergence_count > 100:
                break
        else:
            convergence_count = 0
        #if x < 0 or x > 1:
        #    return f"diverged with {x}"
        #if i % 10000 == 0:
        #    print(f"still running, ... {x:.6f}", end='\n')
    else:
        msg = f"fail: after {i} iterations, we are at " + str([f"{xp:.3f}" for xp in x_p[-10:]])
    return x_p[-100:], msg

xs = []
ys = []
for r in np.arange(0, 4, 0.001):
    cys, msg = converge(r)
    print(f"{r=:.3f}: {msg}")
    xs.extend([r]*len(cys))
    ys.extend(cys)

plt.scatter(xs, ys)
plt.show()
