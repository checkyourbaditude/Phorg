"""
	The Purpose of this script is to update the database with the new file statistics
	I would also like the script to eventually be used to update the database in case some things have changed with the past dates stored in the database
"""

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
	
	#begin working with the images here
	photoData('DSC00225','C:/Users/Chris/Desktop/wrk/test/DSC00225.JPG')


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

		ret = {}
		i = Image.open(image)
		info = i._getexif()

		print "Photo EXIF data: "

		for tag, value in info.items():

			decoded=str(TAGS.get(tag, tag))

			#exclusions on exif data
			if(	decoded=='ISOSpeedRatings' or
			    decoded=='ExposureTime' or
			    decoded=='FNumber'or
				decoded=='FocalLength'or
				decoded=='BrightnessValue'or
				decoded=='LensModel'or
				decoded=='Make'or
				decoded=='Model'or
				decoded=='LensModel'or
				decoded=='DateTime'):

				ret[decoded]=str(value)

		for data in ret:
			print "\t"+str(data)+": "+str(ret[data])+"\n"

		#return ret


#run after imported
if __name__=="__main__":
	updateDatabase()