import numpy as np

def TMULT(frame1, frame2):
    frame = frame1 @ frame2
    return frame

def main():
    frame1 = np.array([[0, 1, 2], 
                       [1,  0, 2], 
                       [0,  0, 1]])

    frame2 = np.array([[0, 1, 3], 
                       [1,  0, 3], 
                       [0,  0, 1]])

    print(TMULT(frame1, frame2))

if __name__ == '__main__':
    main()