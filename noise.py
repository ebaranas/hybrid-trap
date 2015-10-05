from randomNumberGenerator import erika_function

STATE0 = []
STATE = []
STATEOUT = []
sta
r = erika_function(1000)
# print a

# os.system("randomNumberGenerator.py")
sigma = 0
factor = sqrt(-2*sigma*sigma*log(r)/r)
opticalNoiseRe = x*factor/sqrt(2)
opticalNoiseIm = y*factor/sqrt(2)

coefficient = A*hbar*waveNo/mass
gravity = 0
offset = 0
waistSquared = (0.5*waist)**2
photonNo = STATEOUT(1)**2+STATEOUT(2)**2
instantaneousMechanicalFrequency = sqrt(2*hbar*A*photonNo*waveNo**2/mass)

XnoiseScale = sqrt(hbar*instantaneousMechanicalFrequency/mass)
phononNo = k*temperature/hbar/instantaneousMechanicalFrequency
XnoiseScale = XnoiseScale*sqrt(2*phononNo+1)

signalNoiseRatio = sqrt(2*cavityDecayRate)
Xnoise = sqrt(mechanicalDamping*2)*XnoiseScale*2

dt = tPlot/nstep
# what is nstep? number of divisions (for propagation) per plotting interval?
variance = sqrt(dt)

for ll in range(1, noOfCoordinates):
    STATE0(ll) = STATE(ll)
    STATEOUT(ll) = STATE(ll)

tt = time  # ?????????????

# EXECUTE RK HERE TO GET STATEOUT FOR EACH PLOTTING INTERVAL

# add noise to optical field
r = erika_function(1000)
STATEOUT(1) = STATEOUT(1)+randomNo1*signalNoiseRatio
STATEOUT(3) = STATEOUT(3)+randomNo2*signalNoiseRatio
STATEOUT(5) = STATEOUT(5)+randomNo1*Xnoise

# reset STATE0
for ll in range(1, noOfCoordinates):
    STATE0(ll) = STATEOUT(ll)

# update time
TT = TT+DT
