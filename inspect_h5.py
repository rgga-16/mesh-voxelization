import numpy as np
import pandas as pd
import json 

import pickle, h5py

from utils import show_voxels

# Inspecting a data sample from raw data. Before sampling points
datapath = 'examples/output.h5'
with h5py.File(datapath,'r') as data:
    '''
    dict key-vals
    parts_voxel_scaled64: (n_parts,64,64,64)
    scales: (n_parts,1)
    shape_voxel64: (64,64,64)
    size: (n_parts,3)
    translations: (n_parts, 3)
    '''
    items = list(data.items())
    tensor = data['tensor'][:]

    # whole = np.clip(np.sum(tensor,axis=0,keepdims=True),0,1)
    # show_voxels(np.concatenate([whole,parts],axis=0))
    show_voxels(tensor)
    print()