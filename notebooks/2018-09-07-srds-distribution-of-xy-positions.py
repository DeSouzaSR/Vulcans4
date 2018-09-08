
# coding: utf-8

# # Distribution of the planets in the xy plane.
# This notebook provides the distribution, in the xy plane, of the x and y coordinates of the planets. The orbital elements were randomly selected. The larger axles are maintained.

# ## Configurations and definitions

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from glob import glob
import yaml


# In[3]:


# Config font size
font = {'size': 18}
matplotlib.rc('font', **font)


# In[4]:


# Configurations

# Prefix simulation
prefix_simulation =  'v-00-'

# Raw data
data_path = '../data/raw_data/vulcans/'

# Number of clones
n_clones =  96


# In[9]:


get_ipython().system('ls')


# In[6]:


# Define functions 
def extract_line(line):
    """Extract coordinates x=0 and y=1 from pl.in """
    x, y = np.float(line.split()[0]), np.float(line.split()[1])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.plot(x, y, 'k.')


# In[ ]:


# Change dir
os.chdir()


# ## Inner planets

# In[10]:


plt.figure(figsize = (8,8))
plt.xlabel("x coordinate [au]")
plt.ylabel("y coordinate [au]")

# Plot positions
for i in glob(data_path + prefix_simulation + "*"):
    os.chdir(i)
    with open("pl.in") as fp:
        for cnt, line in enumerate(fp):
            if cnt == 5:
                extract_line(line)
            if cnt == 8:
                extract_line(line)
            if cnt == 11:
                extract_line(line)
            if cnt == 14:
                extract_line(line)
    os.chdir("..")

# Plot names
plt.plot(0,0,'ro') # Sun
plt.annotate("Mercury", xy=(0.4, 0.0), xytext=(2.0, 0.0), arrowprops=dict(facecolor='black', shrink=0.01))
plt.annotate("Venus", xy=(0.5, 0.5), xytext=(2.0, 0.5), arrowprops=dict(facecolor='black', shrink=0.01))
plt.annotate("Earth", xy=(0.25, 1.0), xytext=(2.0, 1.0), arrowprops=dict(facecolor='black', shrink=0.01))
plt.annotate("Mars", xy=(0.20, 1.51), xytext=(2.0, 1.5), arrowprops=dict(facecolor='black', shrink=0.01))
plt.grid()
plt.show()


# # Giant planets

# In[10]:


plt.figure(figsize = (8,8))
plt.xlabel("x coordinate [au]")
plt.ylabel("y coordinate [au]")
for i in glob(data_path + prefix_simulation + "*"):
    os.chdir(i)
    with open("pl.in") as fp:
        for cnt, line in enumerate(fp):
            if cnt == 17:
                extract_line(line)
            if cnt == 20:
                extract_line(line)
            if cnt == 23:
                extract_line(line)
            if cnt == 26:
                extract_line(line)
    os.chdir("..")
# Plot names
plt.plot(0,0,'ro') # Sun
plt.annotate("Jupiter", xy=(5, 0), xytext=(40, 0.0), arrowprops=dict(facecolor='black', shrink=0.01))
plt.annotate("Saturn", xy=(0, 10), xytext=(40.0, 10), arrowprops=dict(facecolor='black', shrink=0.01))
plt.annotate("Uranus", xy=(0, 19), xytext=(40, 19), arrowprops=dict(facecolor='black', shrink=0.01))
plt.annotate("Neptune", xy=(3, 30), xytext=(40, 30), arrowprops=dict(facecolor='black', shrink=0.01))
plt.grid()    
plt.show()


# ## Um sistema

# In[31]:


def extract_line2(line):
    """Extract coordinates x=0 and y=1 from pl.in """
    x, y = np.float(line.split()[0]), np.float(line.split()[1])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.plot(x, y, 'ko')

plt.figure(figsize = (8,8))
plt.xlabel("x coordinate [au]")
plt.ylabel("y coordinate [au]")
plt.axis('equal')
plt.axis([-1.6, 1.6, -1.6, 1.6])

os.chdir(data_path + prefix_simulation + "5")
with open("pl.in") as fp:
    for cnt, line in enumerate(fp):
        if cnt == 5:
            extract_line2(line)
            x, y = np.float(line.split()[0]), np.float(line.split()[1])
            plt.annotate("Mercury", xy=(x, y), xytext=(2.0, y), arrowprops=dict(facecolor='black', shrink=0.01))
        if cnt == 8:
            extract_line2(line)
            x, y = np.float(line.split()[0]), np.float(line.split()[1])
            plt.annotate("Venus", xy=(x, y), xytext=(2.0,y), arrowprops=dict(facecolor='black', shrink=0.01))
        if cnt == 11:
            extract_line2(line)
            x, y = np.float(line.split()[0]), np.float(line.split()[1])
            plt.annotate("Earth", xy=(x, y), xytext=(2.0,y), arrowprops=dict(facecolor='black', shrink=0.01))
        if cnt == 14:
            extract_line2(line)
            x, y = np.float(line.split()[0]), np.float(line.split()[1])
            plt.annotate("Mars", xy=(x, y), xytext=(2.0, y), arrowprops=dict(facecolor='black', shrink=0.01))


plt.plot(0,0,'ro') # Sun
#fig = plt.gcf()
mer = plt.Circle((0, 0), 3.870982252717257E-01, color='b', fill=False)
ven = plt.Circle((0, 0), 7.233268496749391E-01, color='b', fill=False)
ear = plt.Circle((0, 0), 1.000371833989169E+00, color='b', fill=False)
mar = plt.Circle((0, 0), 1.523678184302188E+00, color='b', fill=False)

ax = plt.gca()
ax.add_artist(mer)
ax.add_artist(ven)
ax.add_artist(ear)
ax.add_artist(mar)

plt.grid()    
plt.show()

