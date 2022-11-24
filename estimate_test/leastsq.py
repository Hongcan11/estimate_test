import numpy as np
from scipy.optimize import leastsq

def construct_double_difference(t, B, p):
    v, h = p
    pha = v * t + B * h 
    return pha

def error(p, t, B, pha): 
    return construct_double_difference(t, B, p) -pha

if __name__ == '__main__':
    t = np.array([
        -12.0, -24.0, -36.0, -48.0, -60.0, -72.0, -84.0, -96.0, -108.0, -120.0,
        12.0, 24.0, 36.0, 48.0, 60.0, 72.0, 84.0, 96.0, 108.0, 120.0
    ])
    B = np.array([
        -20.0, -40.0, -60.0, -83.0, -100.0, -112.0, -140.0, -160.0, -180.0,
        -200.0, 20.0, 40.0, 60.0, 80.0, 103.0, 120.0, 140.0, 160.0, 180.0,
        200.0
    ])

    p = np.array([26.0, 5.4])
    pha0 = np.round(construct_double_difference(t, B, p))
    print(pha0)
    N = np.random.normal(loc=0.0, scale=1, size=20)
    print(N)
    pha1 = np.round((pha0 + N), 2)
    print(pha1)
    r1 = leastsq(error, np.array([0, 0]), args=(t, B, pha0))
    v, h = r1[0]
    print(v, h)
    r2 = leastsq(error, np.array([0, 0]), args=(t, B, pha1))
    v1, h1 = r2[0]
    print(v1, h1)