"""
	The Purpose of this script is to update the database with the new file statistics
	I would also like the script to eventually be used to update the database in case some things have changed with the past dates stored in the database
"""

import os
import mysql.connector
from mysql.connector import errorcode
from PIL import Image
from PIL.ExifTags import TAGS
from collections import Counter

def updateDatabase():

	print "Made it to the updateDatabase function!"

	#make a connection to the database
	connectDatabase()

	"""
		Organize data by date, make list of objects per date
	"""

	#The top of the photo directory, this is going to have to be dynamically passed into the program through a box in the user UI
	photoDirectory='C:/Users/Chris/Desktop/wrk/'
	directoryDates=os.listdir(photoDirectory)

	"""
	#create a list of objects to be added to database

	insertList={}

	#create the years list
	yearsList=os.listDir(photoDirectory)

	for year in yearsList:

		print "Entering year: "+str(year)

		#create the sub month list
		monthsList=os.listDir(photoDirectory+'/'+year)

		for month in monthsList:

			print "Entering month: "+str(month)

			#create the day list
			dayList=os.listDir(photoDirectory+'/'+year+'/'+month)

			for day in dayList:
	
				print "Entering Day: "+str(day)

				# loop through the photos in Highlights, and JPGS accessing exif data
				# check if edits file exists after testing
				if(	os.path.exists(photoDirectory+'/'+year+'/'+month+'/'+day)==True and
					os.path.exists(photoDirectory+'/'+year+'/'+month+'/'+day+'/Highlights')==True and
					os.path.exists(photoDirectory+'/'+year+'/'+month+'/'+day+'/JPG')==True and
				   	os.path.isdir(photoDirectory+'/'+year+'/'+month+'/'+day)==True and
				   	os.path.isdir(photoDirectory+'/'+year+'/'+month+'/'+day+'/Highlights')==True and
					os.path.isdir(photoDirectory+'/'+year+'/'+month+'/'+day+'/JPG')==True and):
				   	#do something if the directories exist
					
					insertList

				else:
					print "The file structure is incorrect, please make sure the Phorg application is being used correctly"
					sys.exit()

	"""

	print "The Directory list is: "+str(directoryDates)

	
	#begin working with the images here
	data1=photoData('DSC07943','C:/Users/Chris/Desktop/wrk/2019/01 Jan/04 Jan 2019/Highlights/DSC07943.JPG')
	data2=photoData('DSC08252','C:/Users/Chris/Desktop/wrk/2019/01 Jan/19 Jan 2019/Highlights/DSC08252.JPG')

	#print getattr(data1,'Year')

	#for attr, value in data1.__dict__.items():
		#print attr+": "+value


#function that opens the database
def connectDatabase():

	print "Made it into the connect database function"

	#connect to database
	try:
		dataBase = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="password",
			database="PhotoData"
		)
	except mysql.connector.Error as err:
		if (err.errno == errorcode.ER_ACCESS_DENIED_ERROR):
			print "Your username or password is incorrect"
		elif (err.errno == errorcode.ER_BAD_DB_ERROR):
			print "Database does not exist"
		else:
			print "Error: "+str(err)
	else:
		dataBase.close()

#this class creates a photo object with all of the data collected from the photo's EXIF data
class photoData:
	def __init__(self,imageName,imagePath):

		#initialize the image name and path as an attbribute of the object
		self.imageName=imageName
		self.imagePath=imagePath

		self.getExifData(imagePath)

	def getExifData(self,image):

		#self.ret = {}
		i = Image.open(image)
		info = i._getexif()

		print "Photo EXIF data: "

		#insert the file name and path in the object file
		#self.ret['File Name']=self.imageName
		#self.ret['File Path']=self.imagePath

		#loop through the exif data of the image, keeping the information then formatting it properly
		for tag, value in info.items():

			decoded=str(TAGS.get(tag, tag))

			#inclusions of EXIF data, and reformating of the data
			if(	decoded=='ISOSpeedRatings'): self.ISOSpeedRatings=str(newValue)
			elif(decoded=='LensModel'): self.LensModel=str(newValue)
			elif(decoded=='Make'): self.Make=str(newValue)
			elif(decoded=='Model'): self.Model=str(newValue)
			elif(decoded=='ExposureTime'):

				value=str(value)
				newValue=value[value.find("(")+1:value.find(",")]+"/"+value[value.find(",")+2:value.find(")")]
				self.ExposureTime=str(newValue)

			elif(decoded=="FNumber"):

				value=str(value)
				newValue=value[value.find("(")+1:value.find(",")]

				if(len(newValue)==2):
					newValue=newValue[0]+"."+newValue[1]
				else:
					newValue=newValue[0:(len(newValue)-1)]+"."+newValue[len(newValue)-1]
 
				self.FNumber=str(newValue)

			elif(decoded=='FocalLength'):

				value=str(value)
				newValue=value[value.find("(")+1:(value.find(",")-1)]
				self.FocalLength=str(newValue)

			elif(decoded=='BrightnessValue'):

				value=str(value)
				newValue=float(value[value.find("(")+1:(value.find(","))])/float(value[value.find(",")+2:value.find(")")])
				self.BrightnessValue=str(newValue)

			elif(decoded=='DateTime'):

				self.Year=		''.join(value[0:4])
				self.Month=		''.join(value[5:7])
				self.Day=		''.join(value[8:10])



#run after imported
if __name__=="__main__":
	updateDatabase()