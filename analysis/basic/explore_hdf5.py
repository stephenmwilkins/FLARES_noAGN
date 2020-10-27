


# This code simply prints all the datasets in the HDF5 file

import h5py

def printname(name):
    print(name)

sim = '00'
snap = '008_z007p000'

f = h5py.File(f'../../data/flares_{sim}_{snap}.hdf5', 'r')

f.visit(printname)
