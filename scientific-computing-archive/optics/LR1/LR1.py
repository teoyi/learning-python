import pandas as pd 
import numpy as np 
import os 
import matplotlib.pyplot as plt 

os.chdir('./optics/LR1')
df_p = pd.read_csv('p-half.csv')
df_s = pd.read_csv('s-half.csv')

plt.figure()
plt.plot(df_p[df_p.columns[0]], df_p[df_p.columns[1]], color = 'black')

plt.figure()
plt.plot(df_s[df_s.columns[0]], df_s[df_s.columns[1]], color = 'black')

plt.show()
