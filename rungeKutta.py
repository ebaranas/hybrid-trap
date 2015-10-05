'''from differentialEquations import differentialEquations
from parameters import noOfCoordinates
# from outputSignal import outputSignal


def rungeKutta(pressure, state, stateOut, tInitial, dt, time):

    node = 0
    dxUpdate = differentialEquations(pressure, state, node, tInitial, dt, time)

    for ll in range(0, noOfCoordinates-1):
        stateOut[ll] = stateOut[ll]+dxUpdate[ll]/6
        # state[ll] = stateIn[ll] + dxUpdate[ll]/2  # FOR WHAT ARE THIESE LINES????

    # xk2=f(tt+dt/2,state(tt)+xk1/2)*dt
    node = 0.5
    differentialEquations(pressure, state, node, tInitial, dt, time)
    for ll in range(0, noOfCoordinates):
        stateOut[ll] = stateOut[ll] + dxUpdate[ll]/3
        # state[ll] = stateIn[ll] + dxUpdate[ll]/2

    # xk3=f(tt+dt/2), state(tt) +xk2/2)*dt
    node = 0.5
    differentialEquations(pressure, state, node, tInitial, dt, time)
    for ll in range(0, noOfCoordinates):
        stateOut[ll] = stateOut[ll] + dxUpdate[ll]/3
        # state[ll] = stateIn[ll] + dxUpdate[ll]

    # xk4=f(tt+dt, state(tt)+xk3)*dt
    node = 1
    differentialEquations(pressure, state, node, tInitial, dt, time)
    for ll in range(0, noOfCoordinates):
        stateOut[ll] = stateOut[ll] + dxUpdate[ll]/6

    return stateOut'''

from differentialEquations import differentialEquations
# from outputSignal import outputSignal


def rungeKutta(pressure, state, stateOut, tInitial, dt, time):

    node = 0
    dxUpdate = differentialEquations(pressure, state, node, tInitial, dt, time)

    stateOut = stateOut+dxUpdate/6
    # state[ll] = stateIn[ll] + dxUpdate[ll]/2  # FOR WHAT ARE THIESE LINES????

    # xk2=f(tt+dt/2,state(tt)+xk1/2)*dt
    node = 0.5
    differentialEquations(pressure, state, node, tInitial, dt, time)
    stateOut = stateOut + dxUpdate/3
    # state[ll] = stateIn[ll] + dxUpdate[ll]/2

    # xk3=f(tt+dt/2), state(tt) +xk2/2)*dt
    node = 0.5
    differentialEquations(pressure, state, node, tInitial, dt, time)
    stateOut = stateOut + dxUpdate/3
    # state[ll] = stateIn[ll] + dxUpdate[ll]

    # xk4=f(tt+dt, state(tt)+xk3)*dt
    node = 1
    differentialEquations(pressure, state, node, tInitial, dt, time)
    stateOut = stateOut + dxUpdate/6

    return stateOut
