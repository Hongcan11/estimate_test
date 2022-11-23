import numpy as np
from scipy import optimize

def construct_double_difference(t, B, p):
    #N = np.random.normal(loc=0.0, scale=np.pi / 2, size=(1, 5))
    v, h = p
    #pha = (v * t * 86400 + B * h + N) % (2 * np.pi)
    pha = v * t + B * h 
    return pha

def error(p, t, B, pha): 
    return construct_double_difference(t, B, p) -pha

if __name__ == '__main__':   
    t = np.array([
        -12.0, -24.0, -36.0, -48.0, -60.0
    ])
    B = np.array([
        -20.0, -40.0, -60.0, -80.0, -100.0
    ])
    pha = np.array([
        4.15, 5.39, 3.40, 1.19, 0.18
    ])
    '''
    t = np.array([
        -12.0, -24.0, -36.0, -48.0, -60.0, -72.0, -84.0, -96.0, -108.0, -120.0,
        12.0, 24.0, 36.0, 48.0, 60.0, 72.0, 84.0, 96.0, 108.0, 120.0
    ])
    B = np.array([
        -20.0, -40.0, -60.0, -80.0, -100.0, -120.0, -140.0, -160.0, -180.0,
        -200.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0,
        200.0
    ])
    pha = np.array([
        4.15, 5.39, 3.40, 1.19, 0.18, 2.64,
        5.24, 2.57, 3.36, 0.72, 1.52, 4.79,
        1.82, 5.09, 3.23, 1.23, 1.53, 1.38,
        3.22, 1.95
    ])
    '''
    r = optimize.leastsq(error, np.array([0, 0]), args=(t, B, pha))
    v, h = r[0]
    print(v, h)