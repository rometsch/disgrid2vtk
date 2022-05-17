#!/usr/bin/env python3
import numpy as np

from pyevtk.hl import gridToVTK


def get_grid(f):
    r = f.grid.get_interfaces("r").to_value("au")
    p = f.grid.get_interfaces("phi").to_value("rad")

    P, R, Z = np.meshgrid(p, r, [0])

    X = R*np.cos(P)
    Y = R*np.sin(P)
    return X, Y, Z


def get_celldata(f):
    g = f.grid
    values = f.data.cgs.value

    if "r" in g.active_interfaces:
        values = 0.5*(values[:-1, :] + values[1:, :])
    if "phi" in g.active_interfaces:
        if values.shape[1] == len(g.get_interfaces("phi")):
            values = 0.5*(values[:, 1:] + values[:, :-1])
        else:
            values = 0.5*(values + np.roll(values, 1, axis=1))
    values = np.expand_dims(values, 2)
    return values


def simdata2vtk(d, N, filename):
    f = d.get(dim="2d", var="mass density", N=N)

    X, Y, Z = get_grid(f)

    cellData = {}
    for key in ["mass density", "energy", "velocity radial", "velocity azimuthal"]:
        name = key.replace(" ", "_")
        f = d.get(dim="2d", var=key, N=N)
        cellData[name] = get_celldata(f)
    gridToVTK(filename, X, Y, Z, cellData=cellData)
