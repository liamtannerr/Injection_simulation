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
gmsh.model.add("injectionmesh1.py")


lc = 0.3    #Represents the density/ precision of the mesh.

#Add all the vertices of the prism.
#First three arguments are the xyz coordinates.
#The next is the density of the surrounding mesh.
#Finally the point tag is represented by a strictly positive integer.
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(18, 0, 0, lc, 2)
gmsh.model.geo.addPoint(0, 16, 0, lc, 3)
gmsh.model.geo.addPoint(0, 0, 7, lc, 4)
gmsh.model.geo.addPoint(18, 16, 0, lc, 5)
gmsh.model.geo.addPoint(0, 16, 7, lc, 6)
gmsh.model.geo.addPoint(18, 0, 7, lc, 7)
gmsh.model.geo.addPoint(18, 16, 7, lc, 8)

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

#Now in order to mesh the faces we must first create a curve loop that defines the face.
#Always be sure to close the loop by listing the line tags in an order that makes sense and use negatives to reverse the curve as needed.
#'addCurveLoop()' takes in a list of lines (boundaries) as the first argument.
#The last element is the loop tag which is then referenced in the next line to create the surface.
gmsh.model.geo.addCurveLoop([3, -2, 1, -4], 1)
gmsh.model.geo.addCurveLoop([12, -9, 10, -11], 2)
gmsh.model.geo.addCurveLoop([12, -3, 6, -8], 3)
gmsh.model.geo.addCurveLoop([9, -2, 5, -7], 4)
gmsh.model.geo.addCurveLoop([8, -7, 4, -11], 5)
gmsh.model.geo.addCurveLoop([6, -5, 1, -10], 6)

#Loop through all the curve loops we just made and create a surface for each one
for l in range(1, 7):
    gmsh.model.geo.addPlaneSurface([l], l)


dim = 2
Top = gmsh.model.addPhysicalGroup(dim, [1])
gmsh.model.setPhysicalName(dim, Top, "Top")

Bottom = gmsh.model.addPhysicalGroup(dim, [2])
gmsh.model.setPhysicalName(dim, Bottom, "Bottom")

Right = gmsh.model.addPhysicalGroup(dim, [3])
gmsh.model.setPhysicalName(dim, Right, "Right")

Left = gmsh.model.addPhysicalGroup(dim, [4])
gmsh.model.setPhysicalName(dim, Left, "Left")

Front = gmsh.model.addPhysicalGroup(dim, [5])
gmsh.model.setPhysicalName(dim, Front, "Front")

Back = gmsh.model.addPhysicalGroup(dim, [6])
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

# We can then generate a 2D mesh...
gmsh.model.mesh.generate(2)

#To create our inner volume we essentially repeat the surfacing step but with 1 more dimension.
#This uses the 'addSurfaceLoop()' function which references the surfaces that encompass the loop.
#Finally we tag this surface loop as '1' and reference it in making the volume.
gmsh.model.geo.addSurfaceLoop([1, 2, 3, 4, 5, 6], 1)
gmsh.model.geo.addVolume([1], 1)

dim = 3
Interior = gmsh.model.addPhysicalGroup(dim, [1])
gmsh.model.setPhysicalName(dim, Interior, "Interior")

gmsh.model.geo.synchronize()


gmsh.model.mesh.generate(3)

# ... and save it to disk
gmsh.write("injectionmesh1.msh")

# Launch the GUI to see the results:
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

# This should be called when you are done using the Gmsh Python API:
gmsh.finalize()
