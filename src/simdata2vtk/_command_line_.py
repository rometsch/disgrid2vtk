from argparse import ArgumentParser
from os.path import exists

from simdata2vtk.convert import simdata2vtk


def main():

    parser = ArgumentParser()
    parser.add_argument("resource", type=str,
                        help="Path or id of the simulation.")
    parser.add_argument("Noutput", type=int, help="Output number to process.")
    parser.add_argument("-o", "--output", type=str,
                        help="Output file, can include '{}' to use as a template.")
    parser.add_argument("-u", "--update", action="store_true",
                        help="Set flag to force update the data from the server.")
    opts = parser.parse_args()

    if exists(opts.resource):
        from simdata import Data
        d = Data(opts.resource)
        name = "data"
    else:
        from simdata import NData
        d = NData(opts.resource)
        name = opts.resource

    if opts.output is None:
        filename = f"{name}_{opts.Noutput}"
    else:
        filename = opts.output.format(opts.Noutput)

    simdata2vtk(d, opts.Noutput, filename)
