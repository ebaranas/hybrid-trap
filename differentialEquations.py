'''from numpy import cos, sin, pi, exp
from parameters import noOfCoordinates, radius
from parameters import waist, density, waveNo, charge
from parameters import voltage, paulScale, gravity, controlDetuning, probeDetuning, offset
from equilibriumValues import mass, A, omegaDrive, cavityDecayRate
from equilibriumValues import controlDrive, probeDrive
from scipy import constants
hbar = constants.h
c = constants.c
# from numba import jit


# @jit
waistSquared = (0.5*waist)**2
coefficient = A*hbar*waveNo/mass


def differentialEquations(pressure, state, node, tInitial, dt, time):
    dx = [0]*noOfCoordinates
    dxUpdate = [0]*noOfCoordinates
    tt = tInitial+dt*node+time
    dprobe = probeDetuning*tt

    # mechanical damping coefficient
    mechanicalDamping = 1600/pi*pressure
    mechanicalDamping = mechanicalDamping/500/density/radius

    aRe1 = state[0]
    aIm1 = state[1]
    aRe2 = state[2]
    aIm2 = state[3]
    vX = state[4]
    X = state[5]
    kX = waveNo*X
    vY = state[6]
    Y = state[7]
    vZ = state[8]
    Z = state[9]

    photonNo = aRe1**2+aIm1**2
    expYZ = exp(-2*(Y**2+Z**2)*waistSquared)
    coskxSquared = cos(kX)*cos(kX)
    opticalFieldX = coefficient*expYZ*photonNo
    opticalFieldYZ = 4*coefficient*photonNo*coskxSquared*expYZ/waistSquared
    omegaTrapSq = 2*charge*voltage/paulScale**2/mass
    trapField = omegaTrapSq*sin(omegaDrive*tt)
    correction = A*coskxSquared*expYZ
    effectiveDetuning = controlDetuning+correction

    # photon coordinates
    dx[0] = -effectiveDetuning*aIm1-cavityDecayRate*aRe1-controlDrive
    dx[1] = effectiveDetuning*aRe1-cavityDecayRate*aIm1
    dx[2] = -effectiveDetuning*aIm2-cavityDecayRate*aRe2-probeDrive*sin(dprobe)
    dx[3] = effectiveDetuning*aRe2-cavityDecayRate*aIm2-probeDrive*cos(dprobe)

    # x,y,z coordinates
    dx[4] = -mechanicalDamping*vX-trapField*X-opticalFieldX*sin(2*kX)
    dx[5] = vX
    # with gravity and offset
    dx[6] = -mechanicalDamping*vY-trapField*(Y+offset)-opticalFieldYZ*Y-gravity
    dx[7] = vY
    # modify for peter trap coefficient=1.7 not 2
    dx[8] = -mechanicalDamping*vZ+1.7*trapField*Z-opticalFieldYZ*Z
    dx[9] = vZ

    # dx[4] = -(2*pi*400000)**2*X
    # dx[5] = vX
    # now multiply by *dt
    for ll in range(0, noOfCoordinates):
        dxUpdate[ll] = dx[ll]*dt

    return dxUpdate
# differentialEquations()
# dt is h (increment)'''

import numpy as np
from numpy import cos, sin, pi, exp
from parameters import noOfCoordinates, radius
from parameters import waist, density, waveNo, charge
from parameters import voltage, paulScale, gravity, controlDetuning, probeDetuning, offset
from equilibriumValues import mass, A, omegaDrive, cavityDecayRate
from equilibriumValues import controlDrive, probeDrive
from scipy import constants
hbar = constants.h
c = constants.c
# from numba import jit


# @jit
waistSquared = (0.5*waist)**2
coefficient = A*hbar*waveNo/mass


def differentialEquations(pressure, state, node, tInitial, dt, time):
    dx = dxUpdate = np.array([0]*noOfCoordinates)
    tt = tInitial+dt*node+time
    dprobe = probeDetuning*tt

    # mechanical damping coefficient
    mechanicalDamping = 1600/pi*pressure
    mechanicalDamping = mechanicalDamping/500/density/radius

    aRe1 = state[0]
    aIm1 = state[1]
    aRe2 = state[2]
    aIm2 = state[3]
    vX = state[4]
    X = state[5]
    kX = waveNo*X
    vY = state[6]
    Y = state[7]
    vZ = state[8]
    Z = state[9]

    photonNo = aRe1**2+aIm1**2
    expYZ = exp(-2*(Y**2+Z**2)*waistSquared)
    coskxSquared = cos(kX)*cos(kX)
    opticalFieldX = coefficient*expYZ*photonNo
    opticalFieldYZ = 4*coefficient*photonNo*coskxSquared*expYZ/waistSquared
    omegaTrapSq = 2*charge*voltage/paulScale**2/mass
    trapField = omegaTrapSq*sin(omegaDrive*tt)
    correction = A*coskxSquared*expYZ
    effectiveDetuning = controlDetuning+correction

    # photon coordinates
    dx[0] = -effectiveDetuning*aIm1-cavityDecayRate*aRe1-controlDrive
    dx[1] = effectiveDetuning*aRe1-cavityDecayRate*aIm1
    dx[2] = -effectiveDetuning*aIm2-cavityDecayRate*aRe2-probeDrive*sin(dprobe)
    dx[3] = effectiveDetuning*aRe2-cavityDecayRate*aIm2-probeDrive*cos(dprobe)

    # x,y,z coordinates
    dx[4] = -mechanicalDamping*vX-trapField*X-opticalFieldX*sin(2*kX)
    dx[5] = vX
    # with gravity and offset
    dx[6] = -mechanicalDamping*vY-trapField*(Y+offset)-opticalFieldYZ*Y-gravity
    dx[7] = vY
    # modify for peter trap coefficient=1.7 not 2
    dx[8] = -mechanicalDamping*vZ+1.7*trapField*Z-opticalFieldYZ*Z
    dx[9] = vZ

    # dx[4] = -(2*pi*400000)**2*X
    # dx[5] = vX
    # now multiply by *dt

    dxUpdate = dx*dt

    return dxUpdate
# differentialEquations()
# dt is h (increment)
