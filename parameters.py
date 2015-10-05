from numpy import sqrt

# simulation
totalNoOfPoints = 1000  # nperiod
noOfCoordinates = 10
nPlot = 10  # number of points to plot within one period of oscillation
nPropagate = 1000  # nunber of points to propagate; same as nstep and nrkutta

# physical constants
vacuumPermittivity = 8.854*10**-12
relativePermittivity = 1.45**2


# cavity
cavityLength = 1.3*10**-2  # m
waist = 60*10**-6  # m
finesse = 0.4*10**5


# bead
density = 2198
radius = 200*10**-9

# ion trap
paulDriveFrequency = 1500  # Hz
paulScale = 10**3/sqrt(2)

# others
temperature = 300  # K
waveNo = 5.9*10**6
gravity = 0
offset = 0

# experiment
controlDetuning = -50*10**3  # Hz
probeDetuning = 0  # Hz
charge = 1  # C
voltage = 600  # V
inputPower = 1*10**3  # mW
pressure = 0*1.4*10**-2  # mbar
wellNo = 350
