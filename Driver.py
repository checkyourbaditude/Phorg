#import
import os
import shutil

from functions import checkDirectoryExists
#from functions import checkFileExists
from functions import createDatedDirectories
from functions import getExifData
from functions import getImageDate
from functions import getFocalLength
from functions import fileIsRaw
from functions import countRAW

import mysql.connector


#variables for the program to work properly
fileName='unorganized'
absFilePath='C:/Users/Chris/Desktop/Phorg/unorganized'
absFilePathOrg='C:/Users/Chris/Desktop/Phorg/organized'
dirList=os.listdir(fileName)
numPhotos=len(dirList)
numPhotosRAW=countRAW(dirList)
counter=0
counterRAW=0

#check to see if the organized folder has been created
if(os.path.exists(absFilePathOrg)==True and os.path.isdir(absFilePathOrg)==True):

	#print checkDirectoryExists(absFilePath,fileName)

	os.chdir(absFilePath)

	#print "File Name\t\t"+"Date"

	#while loop to organize all of the JPG Files, create all relevant directories, and files
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

				#move JPG file to the new directory
				print "file "+dirList[counter]+" has been moved"

				#moves the current file to from the unorganized folder to the organized folder in the JPG section
				shutil.move(absFilePath+'/'+dirList[counter],absFilePathOrg+'/'+currentFileDate+'/JPG')

				#find the RAW file with the same name and move it to the new folder in the same location
				fileNameRAW=dirList[counter]
				fileNameRAW=fileNameRAW[:-4]+'.ARW'

				#moves the current file to from the unorganized folder to the organized folder in the RAW section
				shutil.move(absFilePath+'/'+fileNameRAW,absFilePathOrg+'/'+currentFileDate+'/RAW')

				#move JPG file to the new directory
				print "file "+fileNameRAW+" has been moved"

			else:
				print"Directory has already been made"

				#Move JPG to the already created folder
				shutil.move(absFilePath+'/'+dirList[counter],absFilePathOrg+'/'+currentFileDate+'/JPG')

				#find the RAW file with the same name and move it to the new folder in the same location
				fileNameRAW=dirList[counter]
				fileNameRAW=fileNameRAW[:-4]+'.ARW'

				#moves the current file to from the unorganized folder to the organized folder in the RAW section
				shutil.move(absFilePath+'/'+fileNameRAW,absFilePathOrg+'/'+currentFileDate+'/RAW')

		counter+=1

		#fail safe
		if(counter>numPhotos):
			break

else:
	print "Error in initialing program"