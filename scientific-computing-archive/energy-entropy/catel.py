import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 


# Reading .csv file containing cat elevator data 
path = "/Users/luke/Desktop/catel-analysis.csv"
df = pd.read_csv(path)
print(df)

# Plot of data 
fig = plt.figure(figsize = (15,4))
grid = plt.GridSpec(1, 3, hspace = 0.2, wspace = 0.2)
ax1 = fig.add_subplot(grid[0,0])
ax2 = fig.add_subplot(grid[0,1])
ax3 = fig.add_subplot(grid[0,2])

ax1.scatter(df["XL"], df["FL"], color = "black")
ax1.set_xlabel("XL (cm)")
ax1.set_ylabel("FL (# of Small Ball)")
ax1.set_title("FL vs XL")

ax2.scatter(df["XR"], df["FR"], color = "black")
ax2.set_xlabel("XR (cm)")
ax2.set_ylabel("FR (# of Small Ball)")
ax2.set_title("FR vs XR")

ax3.scatter(df["XR"], df["XL"], color = "black")
ax3.set_xlabel("XR (cm)")
ax3.set_ylabel("XL (cm)")
ax3.set_title("XL vs XR")
plt.savefig("/Users/luke/Desktop/catel-plot.png")
plt.show()

# Calculating work 
# Processes will be denoted as 1,2,3, or 4
# 1 = loading, 2 = raising, 3 = unloading, 4 = descending 

workLTotal = round(np.trapz(df["FL"], x = df["XL"]), 2)
workL1 = round(np.trapz(df["FL"][1:5], x = df["XL"][1:5]), 2) 
workL2 = round(np.trapz(df["FL"][5:17], x = df["XL"][5:17]), 2) 
workL3 = round(np.trapz(df["FL"][17:21], x = df["XL"][17:21]), 2) 
workL4 = round(np.trapz(df["FL"][21:31], x = df["XL"][21:31]), 2) 
workRTotal = round(np.trapz(df["FR"], x = df["XR"]), 2) 
workR1 = round(np.trapz(df["FR"][1:5], x = df["XR"][1:5]), 2) 
workR2 = round(np.trapz(df["FR"][5:17], x = df["XR"][5:17]), 2)
workR3 = round(np.trapz(df["FR"][17:21], x = df["XR"][17:21]), 2)
workR4 = round(np.trapz(df["FR"][21:31], x = df["XR"][21:31]), 2)

print("\nFor the left side:")
print(f"Work done on process 1 (left side) = {workL1}")
print(f"Work done on process 2 (left side) = {workL2}")
print(f"Work done on process 3 (left side) = {workL3}")
print(f"Work done on process 4 (left side) = {workL4}")
print(f"Total work done on the left side = {workLTotal}")

print("\nFor the right side:")
print(f"Work done on process 1 (right side) = {workR1}")
print(f"Work done on process 2 (right side) = {workR2}")
print(f"Work done on process 3 (right side) = {workR3}")
print(f"Work done on process 4 (right side) = {workR4}")
print(f"Total work done on the right side = {workRTotal}")
