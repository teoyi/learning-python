'''
As Stated in Assignment 3: 
- Use a grid of 20 points in both x- and y- directions, for a total of 400 grid points
- Set a = 1 
References: Jin Kiatvon, Zachary Scroggy, Ryan Wong 
'''
import numpy as np 
import matplotlib.pyplot as plt 

## Creation of constants and array ##
V0 = 4
a = 1
gridL = np.zeros((20,20))

## Implementing Initial Conditions ##
gridL[:,0] = V0
gridL[0,:] = 0
gridL[-1,:] = V0
y = np.linspace(0, 1, 20)
gridL[:,-1] = V0*y/a

## Logic per Iteration ##
gridN = []
iteration = 0 
gridN = gridL
while True:
    if (iteration != 50):
        for rows in np.arange(0,20,1):
            for cols in np.arange(0,20,1):
                print(rows,cols)
                if (rows == 19) or (cols == 19):
                    gridN[rows, cols] = gridL[rows, cols]
                elif (rows == 0) or (cols == 0):
                    gridN[rows, cols] = gridL[rows, cols]
                else: 
                    gridN[rows, cols] = (
                                        (gridL[rows-1,cols] 
                                        + gridL[rows, cols-1] 
                                        + gridL[rows, cols+1] 
                                        + gridL[rows+1, cols])/4
                                        )
        gridN = gridL 
        iteration += 1
        print(f"Iteration: {iteration}")
    else: 
        break

print(gridN)

plt.figure()
plt.imshow(gridN, origin = "lower", cmap = "twilight", extent = [0, 1, 0, 1])
plt.title('Method of Relaxation')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(label = 'V(x,y)')
plt.savefig('Method-of-Relaxation-Numerical')
plt.show()
    









