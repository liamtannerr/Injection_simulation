# Injection_simulation
This repository contains 3 CO2 injection simulation cases that increase in complexity and a simulation involving the waste water disposal well: SECURE INGA C- 088-J/094-A-12. All of the cases make use of the gmsh Python tool for meshing and the OpenGeoSys finite element solver to run the simulation. Results can easily by viewed in paraview.

OneLayer: Very simple injection into a homogenous medium. The injection occurs evenly over one face of the cube.
TwoLayers: Slightly more complex injection simulation involving two layers of material with a specified injection point in the top layer.
ThreeLayers: Essentially the same as Injection with a third layer added in addition to more realistic physical properties of the materials and depth of the layers.

INGA: This simulation uses all the paramters of the SECURE INGA C- 088-J/094-A-12 waste water disposal well. These parameters can be found in the INGA _Parameters.xlsx file which is the work of Malakai Jobin.This is another 3 layer case but adheres to depth values and material properties of the aforementioned well.
