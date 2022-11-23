import numpy as np

def construct_double_difference(v, h):
    t = np.array([
        -12.0, -24.0, -36.0, -48.0, -60.0, -72.0, -84.0, -96.0, -108.0, -120.0,
        12.0, 24.0, 36.0, 48.0, 60.0, 72.0, 84.0, 96.0, 108.0, 120.0
    ])
    B = np.array([
        -20.0, -40.0, -60.0, -80.0, -100.0, -120.0, -140.0, -160.0, -180.0,
        -200.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0,
        200.0
    ])
    N = np.random.normal(loc=0.0, scale=np.pi / 2, size=(1, 20))
    print(N)
    pha = (v * t * 86400 + B * h + N) % (2 * np.pi)
    pha = pha[0, :]
    print(pha)

if __name__ == '__main__':
    construct_double_difference(5.2, 20.6)