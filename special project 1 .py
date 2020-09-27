#!/usr/bin/env python
# coding: utf-8

# In[19]:


import matplotlib.pyplot as plt 
import numpy as np 
x = np.arange(-.5, 5.01, 0.1) 
y = np.sin(x) 
plt.plot(x, y) 
 

plt.show() 


# In[ ]:


#here we can see there are two root for the graph sin(x) in the domain [-.5,5]


# In[ ]:


import math
from math import sin
def f(x):
    return sin(x)
def sgn(x):
    if x<-.5:
        return -5
    elif x==-.5:
        return -.5
    else:
        return 5
def bisection (a,b):
    if sgn((f(a)*f(b))>=0):
        print('f(a) and f(b) have the same sign therefore the bisection method cannot be used')
    c=a
    while ((b-a)>=.0001):
        c=(a+b)/2
    if (f(c)*f(a)<0):
        b=c
    else:
        a=c
    print('value:')

a=-.5
b=5
bisection(a,b)
        
        


# In[ ]:


#bisection theorem does not work here due to the fact that f(a) and f(b) are the same sign this was double checked using desmos
#both f(a) and f(b) are negative therefore the algorthm does not take into account the rest of the code


# In[6]:


def newton(f,df,x0,epsilon,max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        dfxn = df(xn)
        if dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None
    


# In[11]:


import math
from math import sin
from math import cos
p = lambda x: sin(x)
dp = lambda x: cos(x)
approx = newton(p,dp,-.5,1.e-14,1000)
print(approx)


# In[18]:


import math
from math import sin
from math import cos
p = lambda x: sin(x)
dp = lambda x: cos(x)
approx = newton(p,dp,2,1.e-14,1000)
print(approx)


# In[ ]:





# In[ ]:




