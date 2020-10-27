import numpy as np

import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt

import h5py

# --- plot the specific star formation rate versus stellar masss relationship for the test simulation


# --- this specifies a single simulation and snapshot (redshift)
sim = '00' # the first FLARES simulation
snap = '008_z007p000' # z=7

f = h5py.File(f'../../data/flares_{sim}_{snap}.hdf5', 'r') # open the file

sfr = np.log10(f[f'{snap}/Galaxy/SFR/SFR_10'][:]) # the SFR averaged over the last 10 million years M_sol/yr
stellar_mass = np.log10(f[f'{snap}/Galaxy/Mstar_30'][:]) + 10 # the stellar mass

ssfr = sfr - stellar_mass # specific star formation rate is the amount of star formation per unit stellar mass
ssfr += 9 # convert to Gyr^-1


# --- make a plot

fig = plt.figure(figsize=(4,4))

left  = 0.2
bottom = 0.2
width = 0.75
height = 0.75

ax = fig.add_axes((left, bottom, width, height))



ax.scatter(stellar_mass, ssfr, s=1) # scatter plot


# --- TASKS

# 1 - colour code the scatter plot points by SFR
# 2 - add a median line - you'll need to bin the points and calculate the median in each bin. There are various ways of doing this.


ax.set_xlabel(r'$\rm log_{10}(M^{\star}/M_{\odot})$')
ax.set_ylabel(r'$\rm log_{10}(sSFR/Gyr^{-1})$')

fig.savefig(f'figs/sSFR.pdf')
fig.clf()
