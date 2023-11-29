# ------------------------------------------------------------------------------
#   Mesh for OGS C02 injection #1.
#   Mesh is an 18x16x7 rectangular prism.
#   Each face of the prism is a mesh surface.
#   The inside of the prism is a mesh volume that can represent any material specified in the OGS .prj file.
#   Note that when 'tag' is mentioned below, it refers to naming a particular element such as a point, line, surface or volume in our case.
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


lc = 0.5    #Represents the density/ precision of the mesh.

x = 18
y = 16
z = 3.5

#Add all the vertices of the prism.
#First three arguments are the xyz coordinates.
#The next is the density of the surrounding mesh.
#Finally the point tag is represented by a strictly positive integer.
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

dim = 2

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

#Loop through all the curve loops we just made and create a surface for each one
for l in range(1, 16):
    gmsh.model.geo.addPlaneSurface([l], l)



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


# Before they can be meshed (and, more generally, before they can be used by API
# functions outside of the built-in CAD kernel functions), the CAD entities must
# be synchronized with the Gmsh model, which will create the relevant Gmsh data
# structures. This is achieved by the gmsh.model.geo.synchronize() API call for
# the built-in CAD kernel. Synchronizations can be called at any time, but they
# involve a non trivial amount of processing; so while you could synchronize the
# internal CAD data after every CAD command, it is usually better to minimize
# the number of synchronization points.

gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(2)

gmsh.model.geo.addSurfaceLoop([1, 2, 3, 4, 5, 6], 1)
gmsh.model.geo.addVolume([1], 1)
gmsh.model.geo.addSurfaceLoop([2, 11, 7, 8, 9, 10], 2)
gmsh.model.geo.addVolume([2], 2)

dim = 3
TopLayer = gmsh.model.addPhysicalGroup(dim, [1])
gmsh.model.setPhysicalName(dim, TopLayer, "TopLayer")
BottomLayer = gmsh.model.addPhysicalGroup(dim, [2])
gmsh.model.setPhysicalName(dim, BottomLayer, "BottomLayer")

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
