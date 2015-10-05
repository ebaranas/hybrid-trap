import numpy as np
from numpy import pi
from rungeKutta import rungeKutta
from parameters import noOfCoordinates, controlDetuning, nPlot, nPropagate, pressure, totalNoOfPoints
from equilibriumValues import omegaMechanical
from parameters import wellNo, waveNo
from outputSignal import outputSignal
# # from parameters import inputPower, probeDetuning
# from equilibriumValues import omegaMechanical
# # from putBackToWell import putBackToWell
# from outputSignal import outputSignal

# for inputPower in range(1, 1):
# for probeDetuning in range(1, 1):


dx = dxUpdate = state = stateOut = stateIn = np.array([0]*noOfCoordinates)
output = np.array([0]*totalNoOfPoints)
initialPosition = wellNo/waveNo*pi
stateIn[5] = initialPosition
stateIn[7] = initialPosition/100
stateIn[9] = initialPosition/100


maximumFrequencyScale = max(omegaMechanical, abs(controlDetuning))
tPeriod = 2*pi/maximumFrequencyScale  # time scale for each period
tPlot = tPeriod/nPlot  # time scale for plotting; =tdel
dt = tPlot/nPropagate  # time scale for each propagation
tInitial = 0

# high damping to force the particle on wellNo
'''for ii in range(0, 20):
    time = 0
    for jj in range(1, nPropagate):
        state = stateIn
        my_pressure = pressure*10**6
        rungeKutta(pressure, state, stateOut, tInitial, dt, time)
        stateIn = stateOut
        time = time + dt
    tInitial = tInitial+tPlot  # update time for each RK propagation'''
# regular regularDamping
for ii in range(0, totalNoOfPoints):
    time = 0
    for jj in range(0, nPropagate):
        rungeKutta(pressure, state, stateOut, tInitial, dt, time)
        stateIn = stateOut
        time = time + dt
    output[ii] = outputSignal(tInitial, stateOut)
    tInitial = tInitial+tPlot  # update time for each RK propagation
# insert resetting function if bead comes out
