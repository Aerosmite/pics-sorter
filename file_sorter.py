#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
from math import *
import time
from datetime import datetime
import json
import googlemaps
import subprocess
import LatLon

# Init
images = []
# Your googlemaps API key
gmaps_key = 'YOUR_API_KEY'
# The folder path to sort
dir_path = '/Volumes/Mathieu/_Photos a Trier (copier coller)/Auto/Test2'
# The temporary folder path
temp_path = os.path.join(dir_path,"temp")
# Mounths name
Month = ['January','February','March','April','May','June','July','August','September','October','November','December']
# Split conditions
distance_max = 75 # in kilometers
duration_max = 7*(24*60*60) # in seconds

# function by https://github.com/girasquid/Exiftool
def parse_exif(file):
	proc = subprocess.Popen(['exiftool', '-S', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	if hasattr(file, 'read'):
		# file-like object
		ret = proc.communicate(file.read())[0]
	else:
		# buffer
		ret = proc.communicate(file)[0]
	exif = {}
	for line in ret.splitlines():
		try:
			(tag, value) = line.split(': ')
		except:
			continue
		exif[tag] = value
	return exif

# function by https://stackoverflow.com/users/188595/michael-dunn
def haversine(lon1, lat1, lon2, lat2):
	"""
	Calculate the great circle distance between two points 
	on the earth (specified in decimal degrees)
	"""
	# convert decimal degrees to radians 
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
	# haversine formula 
	dlon = lon2 - lon1 
	dlat = lat2 - lat1 
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a)) 
	km = 6367 * c
	return km

def return_creation_date(tags):
	creation_date = datetime.strptime(str(tags['CreateDate']), '%Y:%m:%d %H:%M:%S')
	return creation_date

def return_lat_lon(tags):
	(lat_exif,lon_exif) = (tags['GPSLatitude'],tags['GPSLongitude'])
	# convert to degress (float)
	(lat_str,lon_str) = str(LatLon.string2latlon(lat_exif,lon_exif, 'd% deg %m%\' %S%\" %H')).split(', ')
	(lat,lon) = (float(lat_str),float(lon_str))
	return (lat,lon)

def add_exif_to_list(filename_path):
	f = name = tags = creation_date = ts = lat = lon = lat_str = lon_str = lat_exif = lon_exif = None

	filename = os.path.basename(filename_path)
	f = open(filename_path,'rb')
	tags = parse_exif(f)

	if 'CreateDate' in tags:
		creation_date = return_creation_date(tags)
		# convert date to timestamp 
		ts = time.mktime(creation_date.timetuple())

		if 'GPSLatitude' and 'GPSLongitude' in tags:
			(lat,lon) = return_lat_lon(tags)
			# stored
			images.append({'filename':filename,'ts':ts,'date':creation_date, 'lat':lat, 'lon':lon})
			print "Exif data stored:", filename
		else:
			print "No GPS:",filename
	else:
		print "No creation date:",filename

# create a new "event" folder
def new_event():
	# get date of first temp_path file
	f = open(os.path.join(temp_path, os.listdir(temp_path)[0]))
	tags = parse_exif(f)
	firstfile_date = return_creation_date(tags)
	# get name of "at the middle" temp_path file
	temp_files_num = len(next(os.walk(temp_path))[2])
	m = temp_files_num / 2 + (temp_files_num % 2 > 0) - 1
	middlefile_name = os.listdir(temp_path)[m]
	# get GPS coords of it
	f = open(os.path.join(temp_path, middlefile_name))
	tags = parse_exif(f)
	(middlefile_lat,middlefile_lon) = return_lat_lon(tags)
	# get the town of it
	gmaps = googlemaps.Client(key=gmaps_key)
	reverse_geocode_result = gmaps.reverse_geocode((middlefile_lat,middlefile_lon))
	middlefile_town = 'unknown'
	if reverse_geocode_result:
		for item in reverse_geocode_result:
	   		if 'types' in item['address_components'][0]:
				if item['address_components'][0]['types'][0] == 'locality':
					middlefile_town = item['address_components'][0]['long_name']
	if middlefile_town == 'unknown':
		print "No town found:",middlefile_name

	# test if the first and the last file of temp_path have the same month
	if previous_object['date'].month == firstfile_date.month:
		new_event_name = middlefile_town + ", " + Month[firstfile_date.month-1]
	else:
		new_event_name = middlefile_town + ", " + Month[firstfile_date.month-1] + " - " + Month[previous_object['date'].month-1]
	
	# creation of the event
	new_event_path = os.path.join(dir_path,str(firstfile_date.year),new_event_name)
	if os.path.isdir(new_event_path) == False:
		os.makedirs(new_event_path)
		print "Event created:",os.path.join(str(firstfile_date.year),new_event_name)
	else:
		print "Merged duplicates:",os.path.join(str(firstfile_date.year),new_event_name)

	# moving files
	for f in os.listdir(temp_path):
		os.rename(os.path.join(temp_path,f),os.path.join(new_event_path,f))

# creation/clearing of temp_path
if os.path.isdir(temp_path) == False:
	os.makedirs(temp_path)
else:
	for f in os.listdir(temp_path):
		os.rename(os.path.join(temp_path,f),os.path.join(dir_path,f))

# get files data
for f in os.listdir(dir_path):
	# only images/videos (other supported file types here: http://owl.phy.queensu.ca/~phil/exiftool/)
	if os.path.isfile(os.path.join(dir_path,f)):
		add_exif_to_list(os.path.join(dir_path,f))

# sort files by TimeStamp (DateCreation)
images_chrono = sorted(images, key=lambda k: k['ts'])

# ignore first file
previous_object = images_chrono[0]

# program
for x in images_chrono:
	# split test
	split = False
	# distance
	if haversine(x['lon'],x['lat'],previous_object['lon'],previous_object['lat']) >= distance_max:
		split = True
	# duration
	elif x['ts'] - previous_object['ts'] >= duration_max:
		split = True
	if split == True:
		new_event()
	os.rename(os.path.join(dir_path,x['filename']),os.path.join(temp_path,x['filename']))
	# save previous object data for the next comparison
	previous_object = x

# new event with last files in temp_path
if os.path.isdir(temp_path) == True:
    if os.listdir(temp_path) != []:
    	new_event()
    os.rmdir(temp_path)