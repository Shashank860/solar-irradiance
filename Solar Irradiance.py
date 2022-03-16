# Copyright  by B Shashank Yadav
# All rights reserved.


import datetime

import matplotlib.pyplot as plt
import numpy as np
Lsc = 1.37 #kW m-2
latitude=12.97*(np.pi/180)
def k(n):
    return (1+(0.033*np.cos((360*n/365)*(np.pi/180))))


days=np.arange(1,366,1)

def B(n):
    return 23.5*(np.pi/180)*np.sin(((2*np.pi*(n-84))/365))

X=(24*Lsc)/np.pi #24 * Lsc / Pi
def W(n):
    return (np.arccos(-1*np.tan(latitude)*np.tan(B(n))))
def Ho(n):
    
    return X*k(n)*((np.cos(latitude)*np.cos(B(n))*np.sin(W(n)))+( W(n) * np.sin(B(n)) * np.sin(latitude)))
print("This is copy right file ")

plt.plot(days, Ho(days),'b')
plt.xlabel('Day # in Year')
plt.ylabel('Ho KW m-2')
plt.show()#needed to display plot

