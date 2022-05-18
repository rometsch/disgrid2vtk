#!/usr/bin/env python3
import numpy as np
import logging
from pyevtk.hl import gridToVTK


def get_grid(f):
    g = f.grid

    if g.dim == 2:
        if set(g.names) != set(["r", "phi"]):
            raise AttributeError(f"Can't handle 2d grid with directions {g.names}")
        logging.info("Detected 2d polar grid.")
        return coords_polar_2d(g)
    elif g.dim == 3:
        if set(g.names) != set(["r", "phi", "theta"]):
            raise AttributeError(f"Can't handle 3d grid with directions {g.names}")
        logging.info("Detected 3d spherical grid.")
        return coords_spherical_3d(g)
    else:
        raise AttributeError(f"grid with dim={g.dim} is not supported.")

def coords_polar_2d(g):

    r = g.get_interfaces("r").to_value("au")
    p = g.get_interfaces("phi").to_value("rad")

    P, R, Z = np.meshgrid(p, r, [0])

    X = R*np.cos(P)
    Y = R*np.sin(P)
    return X, Y, Z


def coords_spherical_3d(g):
    r = g.get_interfaces("r").to_value("au")
    p = g.get_interfaces("phi").to_value("rad")
    theta = g.get_interfaces("theta").to_value("rad")

    P, R, T = np.meshgrid(p, r, theta)

    logging.info(f"coord sizes are {R.shape}, {P.shape}, {T.shape}")

    X = R*np.cos(P)*np.sin(T)
    Y = R*np.sin(P)*np.sin(T)
    Z = R*np.cos(T)
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
    if g.dim == 2:
        values = np.expand_dims(values, 2)
    return values


def simdata2vtk(d, N, filename):
    f = d.get(var="mass density", N=N)

    X, Y, Z = get_grid(f)

    cellData = {}
    for key in ["mass density"]:#, "energy", "velocity radial", "velocity azimuthal"]:
        name = key.replace(" ", "_")
        g = f.grid
        f = d.get(dim=f"{g.dim}d", var=key, N=N)
        cellData[name] = get_celldata(f)

    for key, val in cellData.items():
        logging.info(f"Cell data {key} has shape {val.shape}")
    gridToVTK(filename, X, Y, Z, cellData=cellData)
