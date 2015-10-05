# include probe2.h
from numpy import pi, sqrt, cos
from scipy import constants
from parameters import noOfCoordinates, radius, vacuumPermittivity, relativePermittivity
from parameters import waist, cavityLength, density, waveNo, finesse, wellNo
from parameters import pressure, charge
from parameters import voltage, paulScale, paulDriveFrequency, temperature
from parameters import inputPower, controlDetuning
c = constants.c
hbar = constants.h
k = constants.k


# initial values
stateeq = [0]*noOfCoordinates

# compute mass and polarisability
mass = density*4/3*pi*radius**3
polarisability = vacuumPermittivity*(relativePermittivity-1)/(relativePermittivity + 2)
polarisability = 4*pi*radius**3*polarisability

# laser angular frequency, wavenumber
omegaLaser = c * waveNo
waistSquared = (0.5*waist)**2
modeVolume = pi*cavityLength*waistSquared

# depth of standing wave potential
A = omegaLaser*polarisability/2/modeVolume/vacuumPermittivity
# /2 factor
cavityDecayRate = pi*c/finesse/cavityLength/2
# trap beam equilibrium
controlDrive = sqrt(cavityDecayRate*inputPower/2./omegaLaser/hbar)
# probe beam equilibrium
probeDrive = sqrt(cavityDecayRate*0.01*inputPower/2./omegaLaser/hbar)

'''
peter 1.d-4 mbar => 0.125hz
now take usual expression eg levitated review by li geraci etc
1 bar= 10^ 5 pascal; press is in mbar = 10^ 2 pascal
gamma=16 p/(pi*v*rho*r)
v=speed of air=500
'''
correction = A
effectiveDetuning = controlDetuning+correction

# mechanical damping coefficient
mechanicalDamping = 1600/pi*pressure
mechanicalDamping = mechanicalDamping/500/density/radius


omegaTrapSquared = 2*charge*voltage/paulScale**2/mass
omegaDrive = 2*pi*paulDriveFrequency

energy = 3/2*k*temperature

amplitude = sqrt(2*energy/mass/omegaTrapSquared)
velocity = sqrt(2*energy/mass)

equilibriumPosition = 0
kX0 = waveNo*equilibriumPosition

'''
we calculate equilibrium photon fields and x_0
real part of photon field for trap
this version uses 2*phas=pi/2 for equilibria
'''
c1 = cavityDecayRate**2 + effectiveDetuning**2
stateeq[1] = controlDrive * effectiveDetuning**2/c1
# imaginary part of photon field 1
stateeq[2] = -controlDrive * cavityDecayRate/c1
# |alpha1|^2
photonNo = controlDrive**2/c1

# set ke to a fraction of the optical trap depth.
# energy = hbar*a*asq1
# vamp = sqrt(2.*energy/xm)

aStabilityParameter = 4*hbar*A*photonNo*waistSquared/mass/omegaLaser**2
qStabilityParameter = omegaTrapSquared/omegaDrive**2


class seculars:
    alpha = 0
    qoppa = 0

    def secularFrequency(self, alpha, qoppa):
        return 0.5*omegaDrive*sqrt(alpha*aStabilityParameter+0.5*(qoppa*qStabilityParameter)**2)

yTrapped = yUntrapped = zTrapped = zUntrapped = seculars()
print yTrapped.secularFrequency(2, 1)
print yUntrapped.secularFrequency(1, 1)
print zTrapped.secularFrequency(2, 2)
print zUntrapped.secularFrequency(1, 2)

omegaMechanical = sqrt(2*hbar*A*photonNo*cos(2*kX0)*waveNo**2/mass)
mechanicalFrequency = omegaMechanical/2/pi

'''analytical optomechanical cooling rate using only trap beam
formula given by linear response theory or perturbation theory
given in 2012 pra rapid'''

optomechanicalCouplingSquared = hbar*photonNo*waveNo**2*A**2/omegaMechanical/mass  # sin(2kX0) factor averaged?

'''use the time averaged rate - average over 2pi/omega
gammopt=2*kappa2*a**2*hbar/omega/xm [k x_eq]**2
xeq= damped micromotion=omtrap**2/omegam**2 *asq1*x_well
x_well= position of well at which particle localises
ere assume it is well number welln; then rescale
! eg well 1000 gives (1000/welln)^2 times the cooling'''

driveAmplitude = omegaTrapSquared/omegaMechanical**2*pi*wellNo
sPlus = (effectiveDetuning+omegaMechanical)**2+cavityDecayRate**2
sPlus = 1/sPlus
sMinus = (effectiveDetuning-omegaMechanical)**2+cavityDecayRate**2
sMinus = 1/sMinus

coolingRate = -cavityDecayRate*optomechanicalCouplingSquared*(sPlus-sMinus)
# halve the cooling rate because of the period average, factor of 4 to offset 0.5 in kappa
coolingRate = coolingRate*0.5*4

values = mass
with open("equilibriumValues.txt", "a") as myfile:
    myfile.write("values")
