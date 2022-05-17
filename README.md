# simdata2vtk
Create vtk files from grid based fluid dynamics simulations which can be read using simdata.

## Datasource

Data is loaded using the [simdata](https://github.com/rometsch/simdata) tool.
You can either specify a directory, in which case the `Data` class is used; or a simulation id, in which case the `NData` class based on smurfnet is used.

## Supported geometries

- 2d polar grid