#import of the functions file
import os
from functions import checkDirectoryExists
#from functions import checkFileExists
from functions import createDatedDirectories
from functions import getExifData
from functions import getImageDate
from functions import getFocalLength
from functions import fileIsRaw


#variables for the program to work properly
fileName='unorganized_photos'
absFilePath='/home/chris/Documents/Phorg/unorganized_photos'
absFilePathOrg='/home/chris/Documents/Phorg/organized_photos'
dirList=os.listdir(fileName)
numPhotos=len(dirList)
counter=0

#check to see if the organized folder has been created
if(os.path.exists(absFilePathOrg)==True and os.path.isdir(absFilePathOrg)==True):

	#print checkDirectoryExists(absFilePath,fileName)

	os.chdir(absFilePath)

	#print "File Name\t\t"+"Date"

	while(numPhotos>counter):

		#check if the file is RAW of JPG
		if(fileIsRaw(dirList[counter])==False):
			
			#get the date of the file being processed in the loop
			currentFileDate=getImageDate(dirList[counter])
			print "\n\n"+dirList[counter]+":\t\t "+currentFileDate

			#check if a directory exists with the date
			if(checkDirectoryExists(currentFileDate, absFilePathOrg)==False):
				print "Directory has not yet been made!"

				#create new directory
				createDatedDirectories(currentFileDate, absFilePathOrg)

			else:
				print"Directory has already been made"

		counter+=1

		#fail safe
		if(counter>numPhotos):
			break
else:
	print "Error in initialing program"