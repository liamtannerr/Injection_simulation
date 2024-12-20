import gmsh
import math
import sys

gmsh.initialize()
gmsh.model.add("injectionmesh3.py")

km = 1e3
m = 1

x = 7.425 * km
y = 6.6 * km
shale_z = 3.3 * km
sandstone_z = 2.7 * km
basement_z = 2.2 * km
lc = 200
Delta = 50 * m

#------------------------------------------------------------------------------#

#Points:
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(x, 0, 0, lc, 2)
gmsh.model.geo.addPoint(0, y, 0, lc, 3)
gmsh.model.geo.addPoint(x, y, 0, lc, 4)
gmsh.model.geo.addPoint(0, 0, basement_z, lc, 5)
gmsh.model.geo.addPoint(x, 0, basement_z, lc, 6)
gmsh.model.geo.addPoint(0, y, basement_z, lc, 7)
gmsh.model.geo.addPoint(x, y, basement_z, lc, 8)
gmsh.model.geo.addPoint(0, 0, sandstone_z, lc, 9)
gmsh.model.geo.addPoint(x, 0, sandstone_z, lc, 10)
gmsh.model.geo.addPoint(0, y, sandstone_z, lc, 11)
gmsh.model.geo.addPoint(x, y, sandstone_z, lc, 12)
gmsh.model.geo.addPoint(0, 0, shale_z, lc, 13)
gmsh.model.geo.addPoint(x, 0, shale_z, lc, 14)
gmsh.model.geo.addPoint(0, y, shale_z, lc, 15)
gmsh.model.geo.addPoint(x, y, shale_z, lc, 16)


p1 = gmsh.model.geo.addPoint(0.5*x + Delta, 0.5*y + Delta, 2.45 * km + Delta, lc, 18)
p2 = gmsh.model.geo.addPoint(0.5*x + Delta, 0.5*y + Delta, 2.45 * km - Delta, lc, 19)
p3 = gmsh.model.geo.addPoint(0.5*x + Delta, 0.5*y - Delta, 2.45 * km + Delta, lc, 20)
p4 = gmsh.model.geo.addPoint(0.5*x + Delta, 0.5*y - Delta, 2.45 * km - Delta, lc, 21)
p5 = gmsh.model.geo.addPoint(0.5*x - Delta, 0.5*y + Delta, 2.45 * km + Delta, lc, 22)
p6 = gmsh.model.geo.addPoint(0.5*x - Delta, 0.5*y + Delta, 2.45 * km - Delta, lc, 23)
p7 = gmsh.model.geo.addPoint(0.5*x - Delta, 0.5*y - Delta, 2.45 * km + Delta, lc, 24)
p8 = gmsh.model.geo.addPoint(0.5*x - Delta, 0.5*y - Delta, 2.45 * km - Delta, lc, 25)

#------------------------------------------------------------------------------#

#Lines:
gmsh.model.geo.addLine(1, 2, 1) #Basement Bottom Front
gmsh.model.geo.addLine(1, 3, 2) #Basement Bottom Left
gmsh.model.geo.addLine(2, 4, 3) #Basement Bottom Right
gmsh.model.geo.addLine(3, 4, 4) #Basement Bottom Back

gmsh.model.geo.addLine(5, 6, 5) #Basement Top Front
gmsh.model.geo.addLine(5, 7, 6) #Basement Top Left
gmsh.model.geo.addLine(6, 8, 7) #Basement Top Right
gmsh.model.geo.addLine(7, 8, 8) #Basement Top Back

gmsh.model.geo.addLine(9, 10, 9) #Shale Bottom Front
gmsh.model.geo.addLine(9, 11, 10) #Shale Bottom Left
gmsh.model.geo.addLine(10, 12, 11) #Shale Bottom Right
gmsh.model.geo.addLine(11, 12, 12) #Shale Bottom Back

gmsh.model.geo.addLine(13, 14, 13) #Shale Top Front
gmsh.model.geo.addLine(13, 15, 14) #Shale Top Left
gmsh.model.geo.addLine(14, 16, 15) #Shale Top Right
gmsh.model.geo.addLine(15, 16, 16) #Shale Top Back

#Front Left Column:
gmsh.model.geo.addLine(1, 5, 17)
gmsh.model.geo.addLine(5, 9, 18)
gmsh.model.geo.addLine(9, 13, 19)

#Front Right Column:
gmsh.model.geo.addLine(2, 6, 20)
gmsh.model.geo.addLine(6, 10, 21)
gmsh.model.geo.addLine(10, 14, 22)

#Back Left Column:
gmsh.model.geo.addLine(3, 7, 23)
gmsh.model.geo.addLine(7, 11, 24)
gmsh.model.geo.addLine(11, 15, 25)

#Back Right Column:
gmsh.model.geo.addLine(4, 8, 26)
gmsh.model.geo.addLine(8, 12, 27)
gmsh.model.geo.addLine(12, 16, 28)

#Injection Source:
l1 = gmsh.model.geo.addLine(p1, p2, 29)
l2 = gmsh.model.geo.addLine(p2, p4, 30)
l3 = gmsh.model.geo.addLine(p4, p3, 31)
l4 = gmsh.model.geo.addLine(p3, p1, 32)
l5 = gmsh.model.geo.addLine(p1, p5, 33)
l6 = gmsh.model.geo.addLine(p3, p7, 34)
l7 = gmsh.model.geo.addLine(p4, p8, 35)
l8 = gmsh.model.geo.addLine(p2, p6, 36)
l9 = gmsh.model.geo.addLine(p5, p6, 37)
l10 = gmsh.model.geo.addLine(p6, p8, 38)
l11 = gmsh.model.geo.addLine(p8, p7, 39)
l12 = gmsh.model.geo.addLine(p7, p5, 40)

#------------------------------------------------------------------------------#

#Surfaces:
#Note that adding True as the optional 3rd argument to addCurveLoop() will
#automatically orient the closed-wire
gmsh.model.geo.addCurveLoop([3, 2, 1, 4], 1, True) #Basement Floor
gmsh.model.geo.addCurveLoop([20, 17, 1, 5], 2, True) #Basement Front
gmsh.model.geo.addCurveLoop([17, 23, 2, 6], 3, True) #Basement Left
gmsh.model.geo.addCurveLoop([26, 20, 3, 7], 4, True) #Basement Right
gmsh.model.geo.addCurveLoop([26, 23, 4, 8], 5, True) #Basement Back
gmsh.model.geo.addCurveLoop([7, 6, 5, 8], 6, True) #Basement Ceiling

gmsh.model.geo.addCurveLoop([21, 18, 5, 9], 7, True) #Sandstone Front
gmsh.model.geo.addCurveLoop([18, 24, 6, 10], 8, True) #Sandstone Left
gmsh.model.geo.addCurveLoop([27, 21, 7, 11], 9, True) #Sandstone Right
gmsh.model.geo.addCurveLoop([27, 24, 8, 12], 10, True) #Sandstone Back
gmsh.model.geo.addCurveLoop([11, 10, 9, 12], 11, True) #Sandstone Ceiling

gmsh.model.geo.addCurveLoop([22, 19, 9, 13], 12, True) #Shale Front
gmsh.model.geo.addCurveLoop([19, 25, 10, 14], 13, True) #Shale Left
gmsh.model.geo.addCurveLoop([28, 22, 11, 15], 14, True) #Shale Right
gmsh.model.geo.addCurveLoop([28, 25, 12, 16], 15, True) #Shale Back
gmsh.model.geo.addCurveLoop([15, 14, 13, 16], 16, True) #Shale Ceiling

CL1 = gmsh.model.geo.addCurveLoop([30, 32, 29, 31], 17, True)
CL2 = gmsh.model.geo.addCurveLoop([38, 40, 39, 37], 18, True)
CL3 = gmsh.model.geo.addCurveLoop([35, 34, 31, 39], 19, True)
CL4 = gmsh.model.geo.addCurveLoop([36, 33, 37, 29], 20, True)
CL5 = gmsh.model.geo.addCurveLoop([34, 33, 32, 40], 21, True)
CL6 = gmsh.model.geo.addCurveLoop([36, 35, 30, 38], 22, True)

for l in range(1, 23):
    gmsh.model.geo.addPlaneSurface([l], l)

gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(2)

dim = 2

Floor = gmsh.model.addPhysicalGroup(dim, [1])
gmsh.model.setPhysicalName(dim, Floor, "Floor")

Front = gmsh.model.addPhysicalGroup(dim, [2, 7, 12])
gmsh.model.setPhysicalName(dim, Front, "Front")

Left = gmsh.model.addPhysicalGroup(dim, [3, 8, 13])
gmsh.model.setPhysicalName(dim, Left, "Left")

Right = gmsh.model.addPhysicalGroup(dim, [4, 9, 14])
gmsh.model.setPhysicalName(dim, Right, "Right")

Back = gmsh.model.addPhysicalGroup(dim, [5, 10, 15])
gmsh.model.setPhysicalName(dim, Back, "Back")

Ceiling = gmsh.model.addPhysicalGroup(dim, [16])
gmsh.model.setPhysicalName(dim, Ceiling, "Ceiling")
#------------------------------------------------------------------------------#
#Volumes:

dim = 3
gmsh.model.geo.addSurfaceLoop([1, 2, 3, 4, 5, 6], 1)
gmsh.model.geo.addSurfaceLoop([6, 7, 8, 9, 10, 11], 2)
gmsh.model.geo.addSurfaceLoop([CL1, CL2, CL3, CL4, CL5, CL6], 3)
gmsh.model.geo.addSurfaceLoop([11, 12, 13, 14, 15, 16], 4)

gmsh.model.geo.addVolume([1], 1) 
gmsh.model.geo.addVolume([2, 3], 2) 
gmsh.model.geo.addVolume([3], 3)
gmsh.model.geo.addVolume([4], 4)


#Set materials as physical groups for OGS use
Basement = gmsh.model.addPhysicalGroup(dim, [1])
gmsh.model.setPhysicalName(dim, Basement, "Basement")
Sandstone = gmsh.model.addPhysicalGroup(dim, [2])
gmsh.model.setPhysicalName(dim, Sandstone, "Sandstone")
Injection = gmsh.model.addPhysicalGroup(dim, [3])
gmsh.model.setPhysicalName(dim, Injection, "Injection")
Shale = gmsh.model.addPhysicalGroup(dim, [4])
gmsh.model.setPhysicalName(dim, Shale, "Shale")

gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(3)


gmsh.option.setNumber("Mesh.MshFileVersion", 2.2)
gmsh.write("injectionmesh3.msh")


if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
