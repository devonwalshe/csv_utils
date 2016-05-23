# /usr/bin/python
## Converts Shapefiles to GeoJson 
## Required GDAL library installed on system

import os
import sys

if len(sys.argv) < 2:
  sys.exit("\n\nExiting - pass shapefile location in as first script argument to run \n\n")

shapefile = sys.argv[1]


def convert_shapefile(shapefile_location):
  filename = os.path.splitext(shapefile_location)[0]
  
  conversion_string = "ogr2ogr -f GeoJSON -t_srs crs:84 {0}.geojson {0}.shp".format(filename)
  os.system(conversion_string)
  print "\nSuccessfully converted:"
  print "+++++++++++++++++++++++\n"
  print "{0}.shp --> {0}.geojson".format(filename)
  print "\n"

convert_shapefile(shapefile)
  

  
  