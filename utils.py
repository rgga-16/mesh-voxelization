import numpy as np
import pyvista as pv
from pyvistaqt import BackgroundPlotter, MultiPlotter

def show_voxels(voxels,true_threshold=0.5,title='',n_rows=1):
    '''
    Args:
    voxel (numpy.ndarray(l,w,h)): A voxel grid of dimension l x w x h
    '''
    n_voxels = voxels.shape[0]
    n_cols = int(np.ceil(n_voxels/n_rows))

    # voxels = np.transpose(voxels, (0,1,3,2))
    
    plotter = pv.Plotter(shape=(n_rows,n_cols),title=title)
    r = 0; c = 0
    for i in range(n_voxels):
        voxel = voxels[i]
        grid = pv.UniformGrid()
        grid.dimensions = voxel.shape
        grid.spacing = (1, 1, 1)  
        grid.point_data["values"] = voxel.flatten(order="F")  # Flatten the array!
        grid = grid.threshold(true_threshold, invert=False)
        plotter.subplot(r,c)
        plotter.add_mesh(grid,name=f'{r}_{c}',show_edges=True)
        c+=1
        if c==n_cols:
            r+=1
            c=0
        if r==n_rows:
            break
    plotter.show()
    return 


def show_voxel(voxel,true_threshold=0.5):

    # Create the spatial reference
    grid = pv.UniformGrid()
    grid.dimensions = voxel.shape
    grid.spacing = (1, 1, 1)  # These are the cell sizes along each axis

    # Add the data values to the cell data
    grid.point_data["values"] = voxel.flatten(order="F")  # Flatten the array!
    grid = grid.threshold(true_threshold, invert=False)

    # Now plot the grid!
    # grid.plot(show_edges=True)
    plotter = pv.Plotter()
    plotter.add_mesh(grid)
    return 

def synsets2categories(path='./synsetoffset2category.txt'):
    synsets2categories = {}
    with open(path) as f:
        for line in f:
            stuff = line.split()
            synsets2categories[stuff[0]]= stuff[1]
    return synsets2categories