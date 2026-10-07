from ex02_UTOI import UTOI
from ex03_TMULT import TMULT
from ex04_TINVERT import TINVERT
import numpy as np

def main():
    u1 = (11.0, -1.0, np.deg2rad(30.0))
    u2 = (0.0, 7.0, np.deg2rad(45.0))
    u3 = (-3.0, -3.0, np.deg2rad(-30.0))

    frame1 = UTOI(u1)
    frame2 = UTOI(u2)
    frame3 = UTOI(u3)

    frame = TMULT(TMULT(frame2, TINVERT(frame1)), TINVERT(frame3))

    print(frame)

if __name__ == '__main__':
    main()