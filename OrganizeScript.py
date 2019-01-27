"""
	This Script takes all of the JPGs and .ARW files in the unorganized file and organizes them by month, date, and file type
"""

import os
import shutil

from functions import organizeDirListJPG
from functions import organizeDirListRAW
from functions import checkDirectoryExists
from functions import createDatedDirectories
from functions import getExifData
from functions import getImageDate
from functions import getFocalLength
from functions import fileIsRaw
from functions import countRAW
from functions import getFileType

def OrganizePhotos():

	#variables for the program to work properly
	fileName='unorganized'
	absFilePath='C:/Users/Chris/Desktop/Phorg/unorganized'
	absFilePathOrg='C:/Users/Chris/Desktop/Phorg/organized'
	dirListJPG=organizeDirListJPG(os.listdir(absFilePath), absFilePath, absFilePathOrg)
	dirListRAW=organizeDirListRAW(os.listdir(absFilePath))
	numPhotos=len(dirListJPG)
	counter=0

	#check to see if the organized folder has been created
	if(os.path.exists(absFilePathOrg)==True and os.path.isdir(absFilePathOrg)==True):

		#change the working directory to the file path
		os.chdir(absFilePath)

		#while loop to organize all of the JPG Files, create all relevant directories, and files
		while(numPhotos>counter):

			#store the current file date
			currentFileDate=getImageDate(dirListJPG[counter])

			#create function to return file type, branching
			print "\n\n"+dirListJPG[counter]+":\t\t "+currentFileDate
			print "The file type of "+dirListJPG[counter]+" is "+getFileType(dirListJPG[counter])

			"""
				Moves the file to the correct location
			"""

			#moves the current file to from the unorganized folder to the organized folder in the JPG section
			shutil.move(absFilePath+'/'+dirListJPG[counter],absFilePathOrg+'/'+currentFileDate+'/JPG')
			print "file "+dirListJPG[counter]+" has been moved"

			#check to see if the raw file exists
			#if it exists, find the RAW file with the same name and move it to the new folder in the same location
			fileNameRAW=dirListJPG[counter]
			fileNameRAW=fileNameRAW[:-4]+'.ARW'

			if(os.path.isfile(absFilePath+'/'+fileNameRAW)==True):
				print "A corresponding raw file was found for "+str(dirListJPG[counter])

				#moves the current file to from the unorganized folder to the organized folder in the RAW section
				shutil.move(absFilePath+'/'+fileNameRAW,absFilePathOrg+'/'+currentFileDate+'/RAW')
				print str(fileNameRAW)+ "has been moved"

			else:

				print "No corresponding file name found for "+str(dirListJPG)



			"""
				Iterate the counter, make a fail check the failsafe
			"""

			counter+=1

			#fail safe
			if(counter>numPhotos):
				break

	else:

		"""
			Put Error Message here
		"""

		print "Error in initialing program"

#run after imported
if __name__=="__main__":
	OrganizePhotos()