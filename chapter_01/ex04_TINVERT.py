import numpy as np

def TINVERT(frame):
    R = np.array([[frame[0][0], frame[0][1]],
                  [frame[1][0], frame[1][1]]])

    R_inv = np.transpose(R)
    p = -R_inv @ np.array([frame[0][2], frame[1][2]])

    return np.array([[R_inv[0][0], R_inv[0][1], p[0]],
                     [R_inv[1][0], R_inv[1][1], p[1]],
                     [0          , 0          , 1]])

def main():
    frame = np.array([[0, 1, 1],
                      [1, 0, 1],
                      [0, 0, 1]])

    print(TINVERT(frame))

if __name__ == '__main__':
    main()