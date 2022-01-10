'''
File created for Assignment 1: (Other Problems) for 20 points 

Objective: 
Figure out how to plot a vector field with preferred software tool

Requirements:
1. Electric field of dipole in 2D and 3D
2. Include associated field lines of those fields
3. Plot a field with non-zero divergence (2D)
4. Plot a field with non-zero curl (2D)
5. Make the features obvious and explain how they are obvious 

Plan: 
1. Use Quiver and Streamline plot
2. Figure out the how to create array of e-field values? 
'''

import numpy as np 
import matplotlib.pyplot as plt  

# ## Sample Code example 
# #%% Plot the fields
# X,Y = np.meshgrid( np.arange(-4,4,.2), np.arange(-4,4,.2) )
# Ex = (X + 1)/((X+1)**2 + Y**2) - (X - 1)/((X-1)**2 + Y**2)
# Ey = Y/((X+1)**2 + Y**2) - Y/((X-1)**2 + Y**2)

# plt.figure()
# plt.streamplot(X,Y,Ex,Ey)
# plt.title('streamplot')

# plt.figure()
# plt.quiver(X,Y,Ex,Ey,scale=50)
# plt.title('quiver')

# plt.show()



