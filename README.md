# Injection_simulation
The necessary files for the preprocessing, solving and postprocessing steps of a simple CO2 injection.

When run, Injectionmesh1.py generates the injectionmesh1.msh file which can then be converted to .vtu format for OpenGeoSys use using the in house OGS shell commands.
In order to complete the simulation, run the 'ogs' command with injection.prj as the input file. Injection.prj references both the injectiongeo.gml file and the injectionmesh1.vtu file.
Once the OGS solver terminates, the output files can be analyzed using paraview.

ogs.py has been written to simplify the shell commands required to run OpenGeoSys and Paraview. In order to run OGS this way, the file must be modified for each machine. This is a simple
case of changing the path to the ogs executable and project file. ogs.py has two functionalities; "python ogs.py --tool ogs" runs OpenGeoSys and then immediately opens Paraview for
post processing and "python ogs.py --tool para" simply opens Paraview.
