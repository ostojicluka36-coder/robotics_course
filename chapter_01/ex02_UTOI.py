import numpy as np
import sys

def UTOI(uform):
    x = uform[0]
    y = uform[1]
    theta = uform[2]
    iform = np.array([[np.cos(theta), -np.sin(theta), x], 
                      [np.sin(theta),  np.cos(theta), y], 
                      [0,              0,             1]])

    return iform

def ITOU(iform):
    x = iform[0][2]
    y = iform[1][2]

    theta = np.atan2(iform[1][0], iform[0][0])

    return (x, y, theta)

def main(args=None):
    if args is not None:
        args = sys.argv[1:]
        args = [float(x) for x in args]
        args = tuple(args)

    input = args

    frame = UTOI(input)

    print(frame)



    

if __name__ == '__main__':
    main(sys.argv)
