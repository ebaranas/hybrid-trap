from numpy import pi
from parameter import waveNo, wellNo

def putBackToWell():
    position = state[6]*waveNo/pi-wellNo
    if abs(position) > 0.45:
        initialPosition = wellNo/waveNo*pi
        print "jumped out, well = "position
        state[6] = initialPosition
        state[5] = 0
putBackToWell()
