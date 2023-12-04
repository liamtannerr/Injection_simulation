# ------------------------------------------------------------------------------
#   Mesh for OGS C02 injection #2.
#   This mesh is an 18x16x7 rectangular prism which is partitioned into 3 parts.
#   These parts being Bedrock, Sediment and an Injection source.
#   The source of the injection lies in the middle of the bedrock but is its own material (there is no overlap).
# ------------------------------------------------------------------------------

# The Python API is entirely defined in the `gmsh.py' module (which contains the
# full documentation of all the functions in the API):
import gmsh
import math
import sys

# Before using any functions in the Python API, Gmsh must be initialized:
gmsh.initialize()

# Next we add a new model named "injectionmesh1" (if gmsh.model.add() is not called a new
# unnamed model will be created on the fly, if necessary):
gmsh.model.add("injectionmesh2.py")

# Units: meter
km = 1e3  # km in m
m = 1

lc = 500    #Represents the density/ precision of the mesh.

x = 18 * km
y = 16 * km
z = 3.5 * km

Delta = 100 * m

#Add all the vertices of the prism.
dim = 2

gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(x, 0, 0, lc, 2)
gmsh.model.geo.addPoint(0, y, 0, lc, 3)
gmsh.model.geo.addPoint(0, 0, z, lc, 4)
gmsh.model.geo.addPoint(x, y, 0, lc, 5)
gmsh.model.geo.addPoint(0, y, z, lc, 6)
gmsh.model.geo.addPoint(x, 0, z, lc, 7)
gmsh.model.geo.addPoint(x, y, z, lc, 8)
gmsh.model.geo.addPoint(0, 0, 2*z, lc, 9)
gmsh.model.geo.addPoint(x, 0, 2*z, lc, 10)
gmsh.model.geo.addPoint(0, y, 2*z, lc, 11)
gmsh.model.geo.addPoint(x, y, 2*z, lc, 12)

#Connect all the vertices with the 'addline()' function.
#First two arguments are the vertices to connect.
#Last argument is the line tag.
gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(1, 3, 2)
gmsh.model.geo.addLine(2, 5, 3)
gmsh.model.geo.addLine(3, 5, 4)
gmsh.model.geo.addLine(1, 4, 5)
gmsh.model.geo.addLine(2, 7, 6)
gmsh.model.geo.addLine(3, 6, 7)
gmsh.model.geo.addLine(5, 8, 8)

gmsh.model.geo.addLine(4, 6, 9)
gmsh.model.geo.addLine(4, 7, 10)
gmsh.model.geo.addLine(6, 8, 11)
gmsh.model.geo.addLine(7, 8, 12)

gmsh.model.geo.addLine(4, 9, 13)
gmsh.model.geo.addLine(7, 10, 14)
gmsh.model.geo.addLine(6, 11, 15)
gmsh.model.geo.addLine(8, 12, 16)
gmsh.model.geo.addLine(9, 11, 17)
gmsh.model.geo.addLine(9, 10, 18)
gmsh.model.geo.addLine(11, 12, 19)
gmsh.model.geo.addLine(10, 12, 20)

gmsh.model.geo.addLine(3, 11, 21)
gmsh.model.geo.addLine(5, 12, 22)
gmsh.model.geo.addLine(2, 10, 23)
gmsh.model.geo.addLine(1, 9, 24)



#Now in order to mesh the faces we must first create a curve loop that defines the face.
#Always be sure to close the loop by listing the line tags in an order that makes sense and use negatives to reverse the curve as needed.
#'addCurveLoop()' takes in a list of lines (boundaries) as the first argument.
#The last element is the loop tag which is then referenced in the next step to create the surface.

gmsh.model.geo.addCurveLoop([3, -2, 1, -4], 1) #Ceiling panel
gmsh.model.geo.addCurveLoop([12, -9, 10, -11], 2) #Middle panel
gmsh.model.geo.addCurveLoop([12, -3, 6, -8], 3) #Top right panel
gmsh.model.geo.addCurveLoop([9, -2, 5, -7], 4) #Top left panel
gmsh.model.geo.addCurveLoop([8, -7, 4, -11], 5) #Top front panel
gmsh.model.geo.addCurveLoop([6, -5, 1, -10], 6) #Top back panel

gmsh.model.geo.addCurveLoop([20, -17, 18, -19], 7) #Floor Panel
gmsh.model.geo.addCurveLoop([20, -12, 14, -16], 8) #Bottom right panel
gmsh.model.geo.addCurveLoop([17, -9, 13, -15], 9) #Bottom left panel
gmsh.model.geo.addCurveLoop([16, -15, 11, -19], 10) #Bottom front panel
gmsh.model.geo.addCurveLoop([14, -13, 10, -18], 11) #Bottom back panel

gmsh.model.geo.addCurveLoop([20, -3, 23, -22], 12) #Full right panel
gmsh.model.geo.addCurveLoop([17, -2, 24, -21], 13) #Full left panel
gmsh.model.geo.addCurveLoop([19, -4, 21, -22], 14) #Full front panel
gmsh.model.geo.addCurveLoop([18, -1, 24, -23], 15) #Full back panel

#Now create a cubic mesh to represent the injection point 

injectionmid = gmsh.model.geo.addPoint(0.5*x, 0.5*y, 0.5*z, lc, 13)
#Note that by multiplying lc by 0.5, we double the precision of the mesh at the injection point
p1 = gmsh.model.geo.addPoint(0.5*x + Delta, 0.5*y + Delta, 0.5*z + Delta, lc * 0.5, 14)
p2 = gmsh.model.geo.addPoint(0.5*x + Delta, 0.5*y + Delta, 0.5*z - Delta, lc * 0.5, 15)
p3 = gmsh.model.geo.addPoint(0.5*x + Delta, 0.5*y - Delta, 0.5*z + Delta, lc * 0.5, 16)
p4 = gmsh.model.geo.addPoint(0.5*x + Delta, 0.5*y - Delta, 0.5*z - Delta, lc * 0.5, 17)
p5 = gmsh.model.geo.addPoint(0.5*x - Delta, 0.5*y + Delta, 0.5*z + Delta, lc * 0.5, 18)
p6 = gmsh.model.geo.addPoint(0.5*x - Delta, 0.5*y + Delta, 0.5*z - Delta, lc * 0.5, 19)
p7 = gmsh.model.geo.addPoint(0.5*x - Delta, 0.5*y - Delta, 0.5*z + Delta, lc * 0.5, 20)
p8 = gmsh.model.geo.addPoint(0.5*x - Delta, 0.5*y - Delta, 0.5*z - Delta, lc * 0.5, 21)

l1 = gmsh.model.geo.addLine(p1, p2, 25)
l2 = gmsh.model.geo.addLine(p2, p4, 26)
l3 = gmsh.model.geo.addLine(p4, p3, 27)
l4 = gmsh.model.geo.addLine(p3, p1, 28)
l5 = gmsh.model.geo.addLine(p1, p5, 29)
l6 = gmsh.model.geo.addLine(p3, p7, 30)
l7 = gmsh.model.geo.addLine(p4, p8, 31)
l8 = gmsh.model.geo.addLine(p2, p6, 32)
l9 = gmsh.model.geo.addLine(p5, p6, 33)
l10 = gmsh.model.geo.addLine(p6, p8, 34)
l11 = gmsh.model.geo.addLine(p8, p7, 35)
l12 = gmsh.model.geo.addLine(p7, p5, 36)

CL1 = gmsh.model.geo.addCurveLoop([26, 28, 25, 27], 16)
CL2 = gmsh.model.geo.addCurveLoop([34, 36, 35, 33], 17)
CL3 = gmsh.model.geo.addCurveLoop([-31, 30, 27, -35], 18)
CL4 = gmsh.model.geo.addCurveLoop([-32, 29, 33, -25], 19)
CL5 = gmsh.model.geo.addCurveLoop([-30, 29, 28, -36], 20)
CL6 = gmsh.model.geo.addCurveLoop([-32, 31, 26, -34], 21)

#Loop through all the curve loops we just made and create a surface for each one
for l in range(1, 22):
    gmsh.model.geo.addPlaneSurface([l], l)


#Set the boundaries as physical groups for OGS use
Top = gmsh.model.addPhysicalGroup(dim, [1])
gmsh.model.setPhysicalName(dim, Top, "Top")

Right = gmsh.model.addPhysicalGroup(dim, [12])
gmsh.model.setPhysicalName(dim, Right, "Right")

Left = gmsh.model.addPhysicalGroup(dim, [13])
gmsh.model.setPhysicalName(dim, Left, "Left")

Bottom = gmsh.model.addPhysicalGroup(dim, [7])
gmsh.model.setPhysicalName(dim, Bottom, "Bottom")

Front = gmsh.model.addPhysicalGroup(dim, [14])
gmsh.model.setPhysicalName(dim, Front, "Front")

Back = gmsh.model.addPhysicalGroup(dim, [7])
gmsh.model.setPhysicalName(dim, Back, "Back")


gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(2)

dim = 3

gmsh.model.geo.addSurfaceLoop([1, 2, 3, 4, 5, 6], 1) #Bedrock
gmsh.model.geo.addSurfaceLoop([2, 11, 7, 8, 9, 10], 2) #Sediment
gmsh.model.geo.addSurfaceLoop([CL1, CL2, CL3, CL4, CL5, CL6], 3) #Injection

gmsh.model.geo.addVolume([1, 3], 1) # The Bedrock must not overlap with the injection point
gmsh.model.geo.addVolume([2], 2)
gmsh.model.geo.addVolume([3], 3)


#Set materials as physical groups for OGS use
Bedrock = gmsh.model.addPhysicalGroup(dim, [1])
gmsh.model.setPhysicalName(dim, Bedrock, "Bedrock")
Sediment = gmsh.model.addPhysicalGroup(dim, [2])
gmsh.model.setPhysicalName(dim, Sediment, "Sediment")
Injection = gmsh.model.addPhysicalGroup(dim, [3])
gmsh.model.setPhysicalName(dim, Injection, "Injection")

gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(3)

# ... and save it to disk
gmsh.option.setNumber("Mesh.MshFileVersion", 2.2)
gmsh.write("injectionmesh2.msh")

# Launch the GUI to see the results:
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

# This should be called when you are done using the Gmsh Python API:
gmsh.finalize()
