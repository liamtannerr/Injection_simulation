# Injection_simulation
This repository contains 3 CO2 Injection simulation cases that increase in complexity. All of the cases make use of the gmsh Python API for meshing and the OpenGeoSys finite element solver to run the simulation. Results can easily by viewed in paraview.

Injection1: Very simple injection into a homogenous medium. The injection occurs evenly over one face of the cube.
Injection2: Slightly more complex injection simulation involving two layers of material with a specified injection point in the top layer.
Injection3: Essentially the same as Injection with a third layer added in addition to more realistic physical properties of the materials and dimensions of the layers.

ogs.py has been written to simplify the shell commands required to run OpenGeoSys and Paraview. In order to run OGS this way, the file must be modified for each machine. This is a simple
case of changing the path to the ogs executable and project file. ogs.py has two functionalities; "python ogs.py --tool ogs" runs OpenGeoSys and then immediately opens Paraview for
post processing and "python ogs.py --tool para" simply opens Paraview.
