#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
#
# Lese aktuelle Farevarsler fra TED databasen og lage Produkt som kan vises i DIANA.
#
# Author:
#  Bård Fjukstad.  Mar. 2015

import sys
import MySQLdb
import time
import os
import xml.etree.ElementTree as ET

from fare_utilities import *
from generatecap import *

KML_HEADING = """<?xml version="1.0" encoding="iso-8859-1"?>

<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
	<ExtendedData>
	  <Data name="met:layer:0:name">
		<value>%s</value>
	  </Data>
	  <Data name="met:layer:0:visible">
		<value>true</value>
	  </Data>
	</ExtendedData>
"""

KML_END = """  </Document>
</kml>
"""

KML_VALIDLABEL = """	<Placemark>
	  <name>Valid warnings at:</name>
	  <ExtendedData>
		<Data name="met:objectType">
		  <value>Text</value>
		</Data>
		<Data name="met:style:type">
		  <value>Label</value>
		</Data>
		<Data name="met:layerId">
		  <value>0</value>
		</Data>
		<Data name="met:text">
		  <value>GYLDIGE ADVARSLER PR
%s</value>
		</Data>
		<Data name="met:spacing">
		  <value>0.5</value>
		</Data>
		<Data name="met:margin">
		  <value>4</value>
		</Data>
	  </ExtendedData>
	  <Polygon>
		<tessellate>1</tessellate>
		<outerBoundaryIs>
		  <LinearRing>
			<coordinates>-3.16288,75.7207,0
15.9619,74.349,0
</coordinates>
		  </LinearRing>
		</outerBoundaryIs>
	  </Polygon>
	</Placemark>
"""

KML_AREA_END = """			</coordinates>		 
		  </LinearRing>
		</outerBoundaryIs>
	  </Polygon>
	</Placemark>
"""

KML_AREA_NEW = """	<Placemark>
	  <name>%s</name>
	  <description>
	  %s
	  </description>
	  <TimeSpan>
		<begin>%s</begin>
		<end>%s</end>
	  </TimeSpan>
	  <ExtendedData>
		<Data name="met:objectType">
		  <value>PolyLine</value>
		</Data>
		<Data name="met:info:type">
		  <value>%s</value>
		</Data>
		<Data name="met:info:severity">
		  <value>%s</value>
		</Data>	
		<Data name="met:info:comment">
		  <value>%s</value>
		</Data>
	  </ExtendedData>
	  <Polygon>
		<tessellate>1</tessellate>
		<outerBoundaryIs>
		  <LinearRing>
		   <coordinates>"""


KML_TEXT_OL = """	<Placemark>
	 <name>%s</name>
	 <Point>
	 	<coordinates>%f,%f,0</coordinates>
	 </Point>
	</Placemark>
"""

def get_locations(db, select_string ):
	"""Retrieve all currently valid GALE forecasts from the TED db"""

	try:
		cur = db.cursor()
		cur.execute(select_string)
		result = cur.fetchall()

	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		return None
	
	return result

def get_xml_doc( db, dateto):
	"""Retrieve a full document from the data base."""
	
	# print db, dateto
	
	select_string="select value from document where name = \"X_test_Farevarsel_B\" and vto > \"%s \" " %	dateto

	# print select_string
	
	try:
		cur = db.cursor()
		cur.execute(select_string)
		result = cur.fetchall()

	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		return None
	
	return result
	
def retrieve_from_xml( value ):
	"""Retrieves some parameters from the XML text and returns as list."""

	results = {}
	i = 0

	for doc in value:
	
		vto = None
		vfrom = None
		locations = {}
		res = {}
	
		n = 0
	
		xmldoc =  doc[0]
	
		# print xmldoc
	
		root		 = ET.fromstring(xmldoc)
	
		for location in root.iter('location'):
		
			name = None
			varsel = None
			nam = None
			severity = None
			type = None
			kommentar = None
			id = None
			loc = {}
		
		
			id = location.get('id')
			name = location.find('header').text
			varsel = location.find('in').text
		
			for keyword in location.iter('keyword'):
		
				nam = keyword.get('name')
		
				if nam == "severity":
					severity = keyword.find('in').text
				elif nam =="type":
					type = keyword.find('in').text
				elif nam =="kommentar":
					kommentar = keyword.find('in').text

			# print "---------------------"
			# if id:		print id
			if name:	  name = name.encode('Latin-1')
			if varsel:	varsel = varsel.encode('Latin-1')
			if severity:  severity = severity.encode('Latin-1')
			if type:	  type = type.encode('Latin-1')
			if kommentar: kommentar = kommentar.encode('Latin-1')
			# print "---------------------"

			loc['id'] = id
			loc['name'] = name
			loc['varsel'] = varsel
			loc['severity'] = severity
			loc['type'] = type
			loc['kommentar'] = kommentar
	
			n = n + 1

			locations[n] = loc

		for t in root.iter('time'):
			# print "Tag: ",t.tag, " Attrib: ", t.attrib
	
			vto = t.get('vto')
			vfrom = t.get('vfrom')
	
			# print vfrom
			# print vto


		res['locations']= locations
		res['vfrom']= vfrom
		res['vto']=vto
	
		results[i] = res
		i = i + 1
	
	
	return results

def generate_file( db, filename, type, labelType, dateto ):
	"""Writes the given locations to a file. First as AREAS then as LABELs"""
		
	fil = open(filename,'w')
	
	fil.write(KML_HEADING % type)
	
	doc = get_xml_doc( db, dateto)
	
	# print doc
	
	results = retrieve_from_xml( doc )
	
	# print results
	
	# print results
	
	for i in results:
	
		res = results[i]
	
		dt = time.strptime(res['vto'],"%Y-%m-%d %H:%M:00")
		dt = time.strftime("%Y-%m-%dT%H:%M:00Z",dt)
		
		df = time.strptime(res['vfrom'],"%Y-%m-%d %H:%M:00")
		df = time.strftime("%Y-%m-%dT%H:%M:00Z",df)
	
		for p in res['locations']:
		
		  #print p
	  
		  locs = res['locations'][p]
	  
		  # print locs
	  
		  for n in locs['id'].split(":"):
		  
			# print n
		
			latlon = get_latlon(n,db)
			first = 0
			value = locs['varsel']
			comm =  locs['kommentar']
			sev  =  locs['severity']
	
			type  =  locs['type']
			
			# print latlon
				
			for name,lon,lat in latlon:
				
				if first == 0:
					fil.write(KML_AREA_NEW % (name,value,df,dt,type,sev,comm)) #name, description, vfrom,vto
					first_lat = lat
					first_lon = lon
					
				fil.write("%f,%f,0\n"%(lon,lat))
				first= first + 1
		
			fil.write("%f,%f,0\n"%(first_lon,first_lat))
			fil.write(KML_AREA_END)

	fil.write(KML_END)
	
	fil.close()
	
	return 0

#
# MAIN
#
if __name__ == "__main__":

	if len(sys.argv) < 6:
		print "Wrong number of arguments\nUsage faremeldinger.py <TED db username> <passwd> <TEDDBhost> <TEDDB port> <directory for files> <Optional: OpenLayerDir>"
		exit(1)

	db = MySQLdb.connect(user=sys.argv[1],
						passwd=sys.argv[2],
						host=sys.argv[3],
						port=int(sys.argv[4]),
						db="ted",
						)

	dirname = sys.argv[5]
	OpenLayer = False
	
	
	if len(sys.argv) >6:
		ol_dirname = sys.argv[6]
		OpenLayer = True

	now = time.strftime("%Y-%m-%d %H:%M:00")

### Farevarsler

	filename = "%s/Current_fare.kml" %  dirname

	generate_file( db, filename, "Dangerous weather warning", "Label Faremelding", now )


## Close

	if db:
		db.close()