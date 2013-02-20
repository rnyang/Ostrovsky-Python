#!/bin/python

from scipy.optimize import fmin
import numpy as np
from time import sleep

# x[0] = r_{\omega}
# x[1] = r_{\psi}

def u(x):
    u1 = -16*x
    u2 = -10*x #-25*x[1] 
    u3 = -2*x -(1/100)*np.power(x,2)
    u4 = 60*x - (7/100)*np.power(x,2)
    #u5 = 32 * min(x[1], 50)
    #u5 = 32 * x[1]

    #u = -1 * (u1 + u2 + u3 + u4 + u5)
    n = -1 * (u1 + u2 + u3 + u4)
    n = -( 32*x - (8/100) * np.power(x,2))
    
    print "x: ", x
    print n
    sleep(0.5)

    #if x[0] < 0 or x[1] < 0:
    #    return 0

    return n

def main():
    x0 = [200]
    xopt = fmin(u, x0)

    print xopt

main()





