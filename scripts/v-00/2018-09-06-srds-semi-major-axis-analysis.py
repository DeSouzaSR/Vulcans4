"""
Analysis of the Semi-major axis
"""

# Imports
import os
import numpy as np
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import platform

# Matplotlib configure
plt.style.use('ggplot')
font = {'size'   :  12}
matplotlib.rc('font', **font)

# Define functions
def create_columns(simulations):
    """Create a list of columns for dataframe"""
    return ['time'] + \
           ['v_{:02d}'.format(simulation) for simulation in simulations]


def init_df(planet, simulations):
    """Initialize an empty dataframe"""
    columns = create_columns(simulations)
    df = pd.DataFrame(columns=columns)
    df['time']= np.genfromtxt(
                '{}-00-000/{}.txt'.format(prefix_simulation,planet))[:,0]
    return df


def read_orbital_element(planet, orbital_element, simulations, vulcan):
    """Read the orbital elements for each planet for all simulations"""
    df = init_df(planet, simulations)
    for simulation in simulations:
        os.chdir('{}-{}-{:-03d}'.format(prefix_simulation, vulcan, simulation))
        df['v_{:02d}'.format(simulation)] = np.genfromtxt('{}.txt'.format(\
                                         planet))[:,orbital_element]
        os.chdir('..')
    return df


def create_data_planet(planet, orbital_element, simulations):
    """Create data frame for all planets together by each orbital element"""
    oe = {'time':0, 'a':1, 'e':2, 'inc':3, 'capom':4, 'omega':5, 'capm':6, \
          'peri':7, 'apo':8, 'obar':9}
    list_df_planets =[read_orbital_element(planet, oe[orbital_element], simulations, vulcan) for planet in planets]
    data_planets = pd.concat(list_df_planets, keys=planets)
    return data_planets


# Definitions
path_ss_data = '../data/raw_data/vulcans'
prefix_simulation = 'v'
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Vulcan']
planet = 'Mercury' # for time reference
orbital_element = 'a'
n_lines = 96 # Number of simulations
simulations = np.arange(n_lines)

# Create a empty dataframe
os.chdir(path_ss_data)
data_planet = create_data_planet(planet, 'a', simulations)
time = data_planet.loc['Mercury']['time']
mercury = data_planet.loc['Mercury']