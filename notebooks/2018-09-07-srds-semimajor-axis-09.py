
# coding: utf-8

# # Vulcan 09
# ## Semimajor axis
# This notebook provides the graphics of the time evolution of the semi-major axis.
# 
# $a = 0.50\,au$

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from glob import glob


# In[3]:


# Config matplotlib
font = {'size'   : 22}
matplotlib.rc('font', **font)


# In[4]:


# Raw data
data_path = "../data/raw_data/vulcans"

# Number of clones
n_clones = 96


# In[5]:


# Define variables
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Vulcan"]


# In[6]:


# Prefix simulation
prefix_simulation = "v-09-"
os.chdir(data_path)


# ### Inner planets

# In[7]:


inner = planets[0:4]
inner.append(planets[8])
print(inner)


# In[8]:


plt.figure(figsize=(16,10))

for clone in [sim.split("-")[2] for sim in glob(prefix_simulation + '*')]:
    os.chdir(prefix_simulation + clone)
    for planet in inner[0:5]:
        data = np.genfromtxt(planet + ".txt")
        plt.plot(data[:,0], data[:,1])
    os.chdir("..")

plt.xlim([0,1e7])
plt.ylim([0.3, 1.67])
plt.xlabel("Time [a]")
plt.ylabel("Semimajor axis [au]")
plt.text(0.2e7, 0.4, "Mercury")
plt.text(0.2e7, 0.74, "Venus")
plt.text(0.2e7, 1.023, "Earth")
plt.text(0.2e7, 1.55, "Mars")

plt.show()


# ## Giant planets

# In[9]:


plt.figure(figsize=(16,10))

for clone in [sim.split("-")[2] for sim in glob(prefix_simulation + '*')]:
    os.chdir(prefix_simulation + clone)
    for planet in planets[4:8]:
        data = np.genfromtxt(planet + ".txt")
        plt.plot(data[:,0], data[:,1])
    os.chdir("..")

plt.xlim([0, 1e7])
plt.ylim([4, 33])
plt.xlabel("Time [a]")
plt.ylabel("Semimajor axis [au]")
plt.text(0.2e7, 5.8, "Jupiter")
plt.text(0.2e7, 10, "Saturn")
plt.text(0.2e7, 20, "Uranus")
plt.text(0.2e7, 30.8, "Neptune")

plt.show()


# ## Verifying each simulation

# In[10]:


inner = planets[0:4]
inner.append(planets[8])
print(inner)


# 
# ## Inner planets

# In[11]:


for clone in range(n_clones):
    plt.figure(figsize=(16,4))

    #os.chdir(data_path)
    os.chdir(prefix_simulation + "{:03d}".format(clone))
    for planet in inner[0:5]:
        data = np.genfromtxt(planet + ".txt")
        plt.plot(data[:,0], data[:,1], label=planet)
    os.chdir('..')

    plt.xlim([0,1e7])
    plt.ylim([0.0, 1.67])
    plt.xlabel("Time [a]")
    plt.ylabel("Semimajor axis [au]")
    plt.title("Vulcan {:03d}".format(clone))
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()


# ## Giants planets

# In[12]:


for clone in range(n_clones):
    plt.figure(figsize=(16,4))

    #os.chdir(data_path)
    os.chdir(prefix_simulation + "{:03d}".format(clone))
    for planet in planets[4:8]:
        data = np.genfromtxt(planet + ".txt")
        plt.plot(data[:,0], data[:,1], label=planet)
    os.chdir('..')

    plt.xlim([0,1e7])
    plt.ylim([4, 32])
    plt.xlabel("Time [a]")
    plt.ylabel("Semimajor axis")
    plt.title("Vulcan {:03d}".format(clone))
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()


# In[13]:


# Print all planets
for clone in range(1,n_clones + 1):
    plt.figure(figsize=(16,10))

    os.chdir(prefix_simulation + "{:03d}".format(clone))
    for planet in planets[0:9]:
        data = np.genfromtxt(planet + ".txt")
        plt.plot(data[:,0], data[:,1], label=planet)
    os.chdir('..')

    plt.xlim([0,1e7])
    plt.ylim([0, 32])
    plt.xlabel("Time [a]")
    plt.ylabel("Semimajor axis")
    plt.title("Vulcan " + "{:03d}".format(clone))
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()


# In[ ]:


# Plot specifc system with apo and peri astro

plt.figure(figsize=(16,10))

os.chdir(prefix_simulation + "009")
for planet in inner[0:5]:
    data = np.genfromtxt(planet + ".txt")
    #plt.plot(data[:,0], data[:,1], data[:,0], data[:,7], data[:,0], data[:,8], label=planet)
    plt.plot(data[:,0], data[:,1],label=planet)
    plt.plot(data[:,0], data[:,7], color='#B2B2B2' )
    plt.plot(data[:,0], data[:,8], color='#B2B2B2' )
os.chdir('..')

plt.xlim([0.0, 1e7])
plt.ylim([0.0, 1.6])
plt.xlabel("Time [a]")
plt.ylabel("Semimajor axis")
plt.title("v-00-000")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()

