# disgrid2vtk
Create vtk files from grid based fluid dynamics simulations which can be read using disgrid.

## Datasource

Data is loaded using the [disgrid](https://github.com/rometsch/disgrid) tool.
You can either specify a directory, in which case the `Data` class is used; or a simulation id, in which case the `NData` class based on smurfnet is used.

## Supported geometries

- 2d polar grid