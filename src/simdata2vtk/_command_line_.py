from argparse import ArgumentParser

from simdata import NData

from simdata2vtk.convert import simdata2vtk


def main():

    parser = ArgumentParser()
    parser.add_argument("simid", type=str, help="Id of the simulation.")
    parser.add_argument("Noutput", type=int, help="Output number to process.")
    parser.add_argument("-o", "--output", type=str,
                        help="Output file, can include '{}' to use as a template.")
    parser.add_argument("-u", "--update", action="store_true",
                        help="Set flag to force update the data from the server.")
    opts = parser.parse_args()

    if opts.output is None:
        filename = f"{opts.simid}_{opts.Noutput}"
    else:
        filename = opts.output.format(opts.Noutput)

    d = NData(opts.simid)

    simdata2vtk(d, opts.Noutput, filename)
