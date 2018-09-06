# Extract data of the planets
# 
# The output of Swift program is a binary file. This program extract \
# the planets' data and convert it in a text file, separated each planet.

import os
import subprocess
import shutil
from glob import glob
import yaml
import platform

# Definitons for follow program
if platform.system() == 'Darwin': 
    # Mac
    follow_path = '/Users/sandro/Programas/swift/tools'
else:
    # Linux
    follow_path = '/home/sandro/Programas/swift/tools'

path_vulcan_data = '../data/raw_data/vulcans'
prefix_simulation = 'v'


with open('../parameters.yaml', "r") as f:
    parameters = yaml.load(f)
    
n_clones = parameters["n_clones"]
n_vulcans = parameters["n_vulcans"]

# Code planets used by follow_swift program
planets = {"Mercury":-2, "Venus":-3, "Earth":-4, "Mars":-5,\
           "Jupiter":-6, "Saturn":-7, "Uranus":-8, "Neptune":-9, "Vulcan":-10}


os.chdir(path_vulcan_data)
for vulcan in range(n_vulcans):
    for clone in range(n_clones):
        os.chdir('{}-{:02d}-{:03d}'.format(prefix_simulation, vulcan, clone))
        shutil.copy(follow_path + "/follow_swift.x", ".")
        for planet in planets:
            with open("input_follow.txt", "w") as f:
                f.write(str(planets[planet]) + "\n1")
            with open(os.devnull, 'w') as devnull:
                subprocess.run("./follow_swift.x < input_follow.txt", shell = True, \
                            stdout=devnull, stderr=devnull)
            os.rename("follow.out", planet + ".txt")
            os.remove("input_follow.txt")
        os.remove("follow_swift.x")
        os.chdir("..")
    print("Finish vulcan{}".format(vulcan))