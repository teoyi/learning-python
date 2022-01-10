import numpy as np 
import matplotlib.pyplot as plt 
'''
PH 403 Assignment 4
Plots for Griffith's Question 7.2
'''
# Declaring constants and derived values 
V0 = 120 # Initial voltage of the battery 
R = 110*10**3 # Resistance of the resistor  
C = 27*10**-6 # Capacitance of the capacitor 

Q0 = V0*C # Initial charge used for discharge situation 
tc = R*C # Time constant for the circuit (tau)

## For part a) 
def q_a(t): 
    return Q0 * np.exp(-t/tc)

def i_a(t): 
    return (V0/R) * np.exp(-t/tc)

## For part c) 
def q_c(t): 
    return C * V0 * (1 - np.exp(-t/tc))

def i_c(t): 
    return (V0/R) * np.exp(-t/tc)


t = np.arange(0,25,0.001)
fig = plt.figure(figsize=(8,4))
plot1 = fig.add_subplot(1,2,1) 
plot1.plot(t, q_a(t), label = "Q(t) for a)", zorder = 2)
plot1.plot(t, q_c(t), label = "Q(t) for c)", zorder = 2)
plot1.axvline(tc, linestyle = '--', color = 'black', label = "Time Constant", zorder = 1)
plot1.set_xlabel("Time (s)")
plot1.set_ylabel("Charge (C)")
plot1.legend(fontsize=8, loc = 'center right')

plot2 = fig.add_subplot(1,2,2)
plot2.plot(t, i_a(t), label = "I(t) for a)", zorder = 2)
plot2.plot(t, i_c(t), label = "I(t) for c)", zorder = 2)
plot2.axvline(tc, linestyle = '--', color = 'black', label = "Time Constant", zorder = 1)
plot2.set_xlabel("Time (s)")
plot2.set_ylabel("Current (A)")
plot2.legend(fontsize=8, loc = 'center right')

fig.tight_layout()
plt.savefig("/Users/luke/Desktop/Python/GitClone/scientific-computing-archive/electrodynamics/A4/CI_plot.png")
plt.show()
