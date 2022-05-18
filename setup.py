#!/usr/bin/env python3
from setuptools import setup, find_namespace_packages

setup(  name="disgrid2vtk"
        ,version="0.1"
        ,description="Create vtk files from simulation data readable by disgrid."
        ,author="Thomas Rometsch"
        ,package_dir={'': 'src'}
        ,packages=find_namespace_packages(where="src")
        ,install_requires=["numpy", "disgrid", "pyevtk"]
        ,entry_points = {
                'console_scripts': ['disgrid2vtk=disgrid2vtk._command_line_:main']
        }
        )
