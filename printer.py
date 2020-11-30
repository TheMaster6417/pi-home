import time
import PiPython
from PiPython import pi


isrunning = "false"
pimove = 1000
isrunning = "true"


while isrunning == "true":
    pimove = pimove + pimove
    pi(pimove)
    time.sleep(3)
