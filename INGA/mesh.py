import gmsh
import math
import sys

gmsh.initialize()
gmsh.model.add("mesh.py")

km = 1e3
m = 1

x = 5 * km
y = 5 * km
montney_z = 0.64355 * km
debolt_z = 0.3276 * km
banff_z = 0.299 * km
lc = 100
Delta = 2 * m

#------------------------------------------------------------------------------#

#Points:
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(x, 0, 0, lc, 2)
gmsh.model.geo.addPoint(0, y, 0, lc, 3)
gmsh.model.geo.addPoint(x, y, 0, lc, 4)
gmsh.model.geo.addPoint(0, 0, banff_z, lc, 5)
gmsh.model.geo.addPoint(x, 0, banff_z, lc, 6)
gmsh.model.geo.addPoint(0, y, banff_z, lc, 7)
gmsh.model.geo.addPoint(x, y, banff_z, lc, 8)
gmsh.model.geo.addPoint(0, 0, debolt_z, lc, 9)
gmsh.model.geo.addPoint(x, 0, debolt_z, lc, 10)
gmsh.model.geo.addPoint(0, y, debolt_z, lc, 11)
gmsh.model.geo.addPoint(x, y, debolt_z, lc, 12)
gmsh.model.geo.addPoint(0, 0, montney_z, lc, 13)
gmsh.model.geo.addPoint(x, 0, montney_z, lc, 14)
gmsh.model.geo.addPoint(0, y, montney_z, lc, 15)
gmsh.model.geo.addPoint(x, y, montney_z, lc, 16)


p1 = gmsh.model.geo.addPoint(0.5*x + Delta, 0.5*y + Delta, 0.3133 * km + Delta, lc, 18)
p2 = gmsh.model.geo.addPoint(0.5*x + Delta, 0.5*y + Delta, 0.3133 * km - Delta, lc, 19)
p3 = gmsh.model.geo.addPoint(0.5*x + Delta, 0.5*y - Delta, 0.3133 * km + Delta, lc, 20)
p4 = gmsh.model.geo.addPoint(0.5*x + Delta, 0.5*y - Delta, 0.3133 * km - Delta, lc, 21)
p5 = gmsh.model.geo.addPoint(0.5*x - Delta, 0.5*y + Delta, 0.3133 * km + Delta, lc, 22)
p6 = gmsh.model.geo.addPoint(0.5*x - Delta, 0.5*y + Delta, 0.3133 * km - Delta, lc, 23)
p7 = gmsh.model.geo.addPoint(0.5*x - Delta, 0.5*y - Delta, 0.3133 * km + Delta, lc, 24)
p8 = gmsh.model.geo.addPoint(0.5*x - Delta, 0.5*y - Delta, 0.3133 * km - Delta, lc, 25)

#------------------------------------------------------------------------------#

#Lines:
gmsh.model.geo.addLine(1, 2, 1) #Banff Bottom Front
gmsh.model.geo.addLine(1, 3, 2) #Banff Bottom Left
gmsh.model.geo.addLine(2, 4, 3) #Banff Bottom Right
gmsh.model.geo.addLine(3, 4, 4) #Banff Bottom Back

gmsh.model.geo.addLine(5, 6, 5) #Banff Top Front
gmsh.model.geo.addLine(5, 7, 6) #Banff Top Left
gmsh.model.geo.addLine(6, 8, 7) #Banff Top Right
gmsh.model.geo.addLine(7, 8, 8) #Banff Top Back

gmsh.model.geo.addLine(9, 10, 9) #Debolt Bottom Front
gmsh.model.geo.addLine(9, 11, 10) #Debolt Bottom Left
gmsh.model.geo.addLine(10, 12, 11) #Debolt Bottom Right
gmsh.model.geo.addLine(11, 12, 12) #Debolt Bottom Back

gmsh.model.geo.addLine(13, 14, 13) #Debolt Top Front
gmsh.model.geo.addLine(13, 15, 14) #Debolt Top Left
gmsh.model.geo.addLine(14, 16, 15) #Debolt Top Right
gmsh.model.geo.addLine(15, 16, 16) #Debolt Top Back

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
gmsh.model.geo.addCurveLoop([3, 2, 1, 4], 1, True) #Banff Floor
gmsh.model.geo.addCurveLoop([20, 17, 1, 5], 2, True) #Banff Front
gmsh.model.geo.addCurveLoop([17, 23, 2, 6], 3, True) #Banff Left
gmsh.model.geo.addCurveLoop([26, 20, 3, 7], 4, True) #Banff Right
gmsh.model.geo.addCurveLoop([26, 23, 4, 8], 5, True) #Banff Back
gmsh.model.geo.addCurveLoop([7, 6, 5, 8], 6, True) #Banff Ceiling

gmsh.model.geo.addCurveLoop([21, 18, 5, 9], 7, True) #Debolt Front
gmsh.model.geo.addCurveLoop([18, 24, 6, 10], 8, True) #Debolt Left
gmsh.model.geo.addCurveLoop([27, 21, 7, 11], 9, True) #Debolt Right
gmsh.model.geo.addCurveLoop([27, 24, 8, 12], 10, True) #Debolt Back
gmsh.model.geo.addCurveLoop([11, 10, 9, 12], 11, True) #Debolt Ceiling

gmsh.model.geo.addCurveLoop([22, 19, 9, 13], 12, True) #Montney Front
gmsh.model.geo.addCurveLoop([19, 25, 10, 14], 13, True) #Montney Left
gmsh.model.geo.addCurveLoop([28, 22, 11, 15], 14, True) #Montney Right
gmsh.model.geo.addCurveLoop([28, 25, 12, 16], 15, True) #Montney Back
gmsh.model.geo.addCurveLoop([15, 14, 13, 16], 16, True) #Montney Ceiling

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
Banff = gmsh.model.addPhysicalGroup(dim, [1])
gmsh.model.setPhysicalName(dim, Banff, "Banff")
Debolt = gmsh.model.addPhysicalGroup(dim, [2])
gmsh.model.setPhysicalName(dim, Debolt, "Debolt")
Injection = gmsh.model.addPhysicalGroup(dim, [3])
gmsh.model.setPhysicalName(dim, Injection, "Injection")
Montney = gmsh.model.addPhysicalGroup(dim, [4])
gmsh.model.setPhysicalName(dim, Montney, "Montney")

gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(3)


gmsh.option.setNumber("Mesh.MshFileVersion", 2.2)
gmsh.write("mesh.msh")


if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
