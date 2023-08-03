# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:36:39 2019

@author: SAM
"""

string1='modeler -nq -meter -state covzonal.pmdl Union '
string2='"__PATH TO YOUR SHAPE FILE___" integer '
string3='"__PATH TO YOUR RASTER IMAGE__" \'float table meant '
string4='attribute incov :: "R{}";\' \'meant = zonal mean (incov, inrast ({}), useall 0);\' '
string5='"None" ____YOUR SHAPE FILE EXTENT____ Polygon\n\n'
string=string1+string2+string3+string4+string5

nof=366 # number of files
file = open("bas_rf_2001.txt", "w")
for i in range(1,nof):
    file.write(string.format(i,i))
file.close()

#********************** EXAMPLE- 1 *****************************

#string2_1='modeler -nq -meter -state covzonal.pmdl Union '
#string2_2='"e:/rainfall_projected/rainfall_shapefiles/bas_rf_2002.shp" integer'
#string2_3='"e:/rainfall_projected/rainfall_shapefiles/rain_2002.img" \'float table meant'
#string2_4='attribute incov :: "R{}";\' \'meant = zonal mean (incov, inrast ({}), useall 0);\''
#string2_5='"None" 27410.75713511272 27410.75713511272 meters Polygon'
#string2=string2_1+string2_2+string2_3+string2_4+string2_5

#file = open("bas_rf_2002.txt", "w")
#for i in range(1,366):
#    file.write(string2.format(i,i))
#file.close()

#********************** EXAMPLE- 2 *****************************
#For rainfall 2010
#string2_1='modeler -nq -meter -state covzonal.pmdl Union'
#string2_2='"e:/rainfall_projected/rainfall_shapefiles/rain_2010.shp" integer'
#string2_3='"e:/rainfall_projected/rainfall_shapefiles/rain_2010.img" \'float table meant'
#string2_4='attribute incov :: "R{}";\' \'meant = zonal mean (incov, inrast ({}), useall 0);\''
#string2_5='"None" 27410.75713511272 27410.75713511272 meters Polygon'
#string2=string2_1+string2_2+string2_3+string2_4+string2_5

#file = open("bas_rf_2010.txt", "w")
#for i in range(1,366):
#    file.write(string2.format(i,i))
#file.close()
