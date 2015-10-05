from numpy import sqrt, cos, sin
from parameters import probeDetuning
from equilibriumValues import probeDrive, cavityDecayRate


def outputSignal(tInitial, stateOut):
    transmittedRe = -(probeDrive*cos(probeDetuning*tInitial))/sqrt(2*cavityDecayRate)*10
    transmittedRe = transmittedRe+sqrt(2*cavityDecayRate)*(stateOut[1]+stateOut[3])
    transmittedIm = -(probeDrive*sin(probeDetuning*tInitial))/sqrt(2*cavityDecayRate)*10
    transmittedIm = transmittedIm+sqrt(2*cavityDecayRate)*(stateOut[2]+stateOut[4])
    # meanIntraCavityField = sqrt(transmittedRe**2+transmittedIm**2)
    transmittedLight = sqrt(transmittedRe**2+transmittedIm**2)
    # outputs are time, photon number, X, Y, and Z
    return tInitial, transmittedLight, stateOut[5], stateOut[4]
