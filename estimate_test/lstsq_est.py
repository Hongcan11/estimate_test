import numpy as np


def construct_double_difference(t, B, p):
    v, h = p
    y = v * t + B * h
    return y


if __name__ == '__main__':
    t = np.array([
        -12.0, -24.0, -36.0, -48.0, -60.0, -72.0, -84.0, -96.0, -108.0, -120.0,
        12.0, 24.0, 36.0, 48.0, 60.0, 72.0, 84.0, 96.0, 108.0, 120.0
    ])
    B = np.array([
        -24, -40, -56.0, -80.0, -104.0, -120.0, -142.0, -160.0, -180.0,
        -200.0, 20.0, 40.0, 60.0, 80.0, 106.0, 120.0, 140.0, 160.0, 180.0,
        200.0
    ])

    p = np.array([5.0, 4.0])
    y = np.mat(construct_double_difference(t, B, p)).T
    print(y)

    A = np.vstack([t, B]).T
    print(A)
    s1 = np.linalg.inv(np.dot(A.T, A))
    # print(s1, np.linalg.det(s1))
    s = np.dot(np.dot(s1, A.T), y)
    v1 = s[0]
    h1 = s[1]
    print(v1, h1)
    s2 = np.linalg.lstsq(A, y, rcond=None)
    v2, h2 = s2[0]
    print(v2, h2)
