# This file contains all the functions for the script to run properly


# imports
import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS
from collections import Counter

#checks to see if the file is still present in the Photoconsolidater folder
def checkDirectoryExists(dirName,absFilePath):

	if(checkPathExists(absFilePath)==True): 

		#checks to see if the path is going to the specified directory
		#if(os.path.isdir(dirName)==False):
		if(os.path.isdir(absFilePath+"/"+dirName)==False):
			print "No Directory was found with that name"
			return False
		else:
			print "Directory was found at the path: "+absFilePath
			return True

	else:
		print "Could not Execute, path not found"
		return True

def checkPathExists(absFilePath):
	#checks to see if the path still exists
	if (os.path.exists(absFilePath)):
		print "Path Exists"
		return True
	
	else:
		print "No Path Found"
		return False

"""
		A try catch block needs to be added to this section

		Also, add a text file with some information on the photos that can be later edited

"""
#this function creates a directory with a date that is passed to the function
def createDatedDirectories(date, absFilePath):

	#Makes a directory at the path with the name as the date
	newDirName=absFilePath+'/'+date

	#attempt to make the directory, throw exception if it has been made already
	#try:
	os.mkdir(newDirName)
	os.mkdir(newDirName+'/RAW')
	os.mkdir(newDirName+'/JPG')
	print "Directory" , newDirName , " created along with JPG and RAW directories"



	#except FileExistsError:
		#print "Directory" , newDirName , " already exists"


#creates an object for the data in the image, then returns that object
def getExifData(image):
    ret = {}
    i = Image.open(image)
    info = i._getexif()
    for tag, value in info.items():
    	decoded=str(TAGS.get(tag, tag))
    	if(decoded=='50341' or decoded=='UserComment' or decoded=='MakerNote'):
    		pass
    	else:
    		ret[decoded]=str(value)

    return ret

#returns the image date in [Day Month Year] format
def getImageDate(image):
	#get the date Date, convert to string, then char array for operations
	i=getExifData(image)
	dateValue=list(i['DateTime'])
	
	#parse the list to add the proper date values as strings in each variable
	Year=	''.join(dateValue[0:4])
	Month=	getMonth(''.join(dateValue[5:7]))
	Day=	''.join(dateValue[8:10])

	#create the final date
	finalDate=Day+" "+Month+" "+Year

	return 	finalDate

def getMonth(value):
	if(value=="01"): 		return 'Jan'
	elif(value=="02"):	 	return 'Feb'
	elif(value=="03"):	 	return 'Mar'
	elif(value=="04"):	 	return 'Aprl'
	elif(value=="05"):	 	return 'May'
	elif(value=="06"):	 	return 'June'
	elif(value=="07"):	 	return 'July'
	elif(value=="08"):		return 'Agst'
	elif(value=="09"):	 	return 'Sept'
	elif(value=="10"):	 	return 'Oct'
	elif(value=="11"):	 	return 'Nov'
	elif(value=="12"):	 	return 'Dec'

	#throw exception if value is outsides the bounds of the function
	else:				return


#returns the focal length
def getFocalLength(image):

	i=getExifData(image)

	#turns the focal length into a string
	info=list(i['FocalLength'])
	focalLength=''.join(info[1:3])

	return focalLength

def fileIsRaw(image):

	if(image.endswith('.ARW')):
		return True
	else:
		return False



		"""	
def checkFileExists(fileName,absFilePath):

	#checks to see if the path still exists
	if (os.path.exists(absFilePath)):
		print "Found file"
		return True
	
	else:
		print "failed to find file"
		return Talse
		"""

# Simple function that counts the number of photos in the file name
#def countPhoto(dirList):

	#local variables to run the function
	#countJPG = 0;
	#countRAW = 0;
	#number_files = len(dirList)

	#print "The total number of photos is: ", number_files

	#continue by counting the raw and jpg files seperately
	#for file in dirList:
		#print file
		#if (file.endswith('.JPG')):
			#countJPG += 1
		#if (file.endswith('.ARW')):
			#countRAW += 1

	#print "Number of JPG files: ", countJPG
	#print "Number of RAW files: ", countRAW	

	#return number_files;	
