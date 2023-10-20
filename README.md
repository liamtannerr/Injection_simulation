# Injection_simulation
The necessary files for the preprocessing, solving and postprocessing steps of a simple CO2 injection.

When run, Injectionmesh1.py generates the injectionmesh1.msh file which can then be converted to .vtu format for OpenGeoSys use using the in house OGS shell commands.
In order to complete the simulation, run the 'ogs' command with injection.prj as the input file. Injection.prj references both the injectiongeo.gml file and the injectionmesh1.vtu file.
Once the OGS solver terminates, the output files can be analyzed using paraview.
