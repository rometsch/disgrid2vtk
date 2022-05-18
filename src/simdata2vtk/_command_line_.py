import logging
from argparse import ArgumentParser
from os.path import exists

from disgrid2vtk.convert import disgrid2vtk


def main():

    parser = ArgumentParser()
    parser.add_argument("resource", type=str,
                        help="Path or id of the simulation.")
    parser.add_argument("Noutput", type=int, help="Output number to process.")
    parser.add_argument("-o", "--output", type=str,
                        help="Output file, can include '{}' to use as a template.")
    parser.add_argument("-u", "--update", action="store_true",
                        help="Set flag to force update the data from the server.")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Verbose output.")
    opts = parser.parse_args()

    configure_logging(opts.verbose)

    if exists(opts.resource):
        from disgrid import Data
        d = Data(opts.resource)
        name = "data"
    else:
        from disgrid import NData
        d = NData(opts.resource)
        name = opts.resource

    if opts.output is None:
        filename = f"{name}_{opts.Noutput}"
    else:
        filename = opts.output.format(opts.Noutput)

    disgrid2vtk(d, opts.Noutput, filename)

def configure_logging(verbose):
    if verbose:
        level=logging.DEBUG
    else:
        level=logging.INFO
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')