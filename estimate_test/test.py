import numpy as np

def construct_double_difference(t, p):
    v, h = p
    y = v * t + h 
    return y

if __name__ == '__main__':
    t = np.array([
        -12.0, -24.0, -36.0, -48.0, -60.0, -72.0, -84.0, -96.0, -108.0, -120.0,
        12.0, 24.0, 36.0, 48.0, 60.0, 72.0, 84.0, 96.0, 108.0, 120.0
    ])
    B = np.array([
        -20.0, -40.0, -60.0, -80.0, -100.0, -120.0, -140.0, -160.0, -180.0,
        -200.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0,
        200.0
    ])

    p = np.array([6.8, 3.2])
    y = np.round(construct_double_difference(t, p))
    print(y)
    A = np.vstack([t, np.ones(len(t))]).T
    print(A)
    s = np.linalg.lstsq(A, y, rcond=None)
    print(s)
    v, h = s[0]
    print((v, h))