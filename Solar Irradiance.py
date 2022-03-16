"""MIT License

Copyright (c) 2022 Shashank860

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
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

