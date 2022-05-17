#!/usr/bin/env python3
from setuptools import setup, find_namespace_packages

setup(  name="simdata2vtk"
        ,version="0.1"
        ,description="Create vtk files from simulation data readable by simdata."
        ,author="Thomas Rometsch"
        ,package_dir={'': 'src'}
        ,packages=find_namespace_packages(where="src")
        ,install_requires=["numpy", "simdata", "pyevtk"]
        ,entry_points = {
                'console_scripts': ['simdata2vtk=simdata2vtk._command_line_:main']
        }
        )
