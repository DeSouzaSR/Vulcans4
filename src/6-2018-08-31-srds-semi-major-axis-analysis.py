# Semi-major axis
# This program analyse the time evolution of the semi-major axis for each
# planet. 

import os
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import platform

# Matplotlib configure
plt.style.use('ggplot')
font = {'size'   :  12}
matplotlib.rc('font', **font)


def create_columns(simulations):
    """Create a list of columns for dataframe"""
    return ['time'] + \
           ['ss_{}'.format(simulation) for simulation in simulations]


def init_df(planet, simulations):
    """Initialize an empty dataframe"""
    columns = create_columns(simulations)
    df = pd.DataFrame(columns=columns)
    df['time']= np.genfromtxt(
                '{}0/{}.txt'.format(prefix_simulation,planet))[:,0]
    return df


def read_orbital_element(planet, orbital_element, simulations):
    """Read the orbital elements for each planet for all simulations"""
    df = init_df(planet, simulations)
    for simulation in simulations:
        os.chdir('{}{}'.format(prefix_simulation, simulation))
        df['ss_{}'.format(simulation)] = np.genfromtxt('{}.txt'.format(\
                                         planet))[:,orbital_element]
        os.chdir('..')
    return df


def create_data_planet(planet, orbital_element, simulations):
    """Create data frame for all planets together by each orbital element"""
    oe = {'time':0, 'a':1, 'e':2, 'inc':3, 'capom':4, 'omega':5, 'capm':6, \
          'peri':7, 'apo':8, 'obar':9}
    list_df_planets =[read_orbital_element(planet, oe[orbital_element], simulations) for planet in planets]
    data_planets = pd.concat(list_df_planets, keys=planets)
    return data_planets

path_ss_data = '../data/raw_data/ss'
prefix_simulation = 'ss-'
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

os.chdir(path_ss_data)
planet = 'Mercury' # for time reference
orbital_element = 'a'
n_lines = 96 # Number of simulations
simulations = np.arange(n_lines)

data_planet = create_data_planet('Mercury', 'a', simulations)

time = data_planet.loc['Mercury']['time']
mercury = data_planet.loc['Mercury']

# Plot Mercury's semi-major axis
mercury.set_index('time').plot(legend=False, figsize=(10,7))
font = {size: 12}
plt.title("Semi-major axis for all Mercury's simulations", fontdict=font)
plt.xlabel("Time [a]")
plt.ylabel("Semi-major axis [au]")
plt.show()

# Plot Inner's semi-major axis
ax = plt.gca()
for planet in  planets[0:4]:
    data_planet.loc[planet].set_index('time').plot(ax = ax, legend=False, figsize=(10,7))
plt.title("Semi-major axis evolution of the inner planets")
plt.xlabel("Time [a]")
plt.ylabel("Semi-major axis [au]")
plt.text(8e6, 0.41, "Mercury")
plt.text(8e6, 0.74, "Venus")
plt.text(8e6, 1.02, "Earth")
plt.text(8e6, 1.54, "Mars")
plt.show()

# Plot giant's semi-major axis
ax = plt.gca()
for planet in planets[4:8]:
    data_planet.loc[planet].set_index('time').plot(ax = ax, legend=False, figsize=(10,7))
plt.title("Semi-major axis evolution of the giant planets")
plt.xlabel("Time [a]")
plt.ylabel("Semi-major axis [au]")
plt.text(8e6, 5.22, "Jupiter")
plt.text(8e6, 9.60, "Saturn")
plt.text(8e6, 19.25, "Uranus")
plt.text(8e6, 30.12, "Neptune")
plt.show()
