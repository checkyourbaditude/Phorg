"""
	The Purpose of this script is to update the database with the new file statistics
	I would also like the script to eventually be used to update the database in case some things have changed with the past dates stored in the database
"""

import os
import datetime
import mysql.connector
from mysql.connector import errorcode

from PIL import Image
from PIL.ExifTags import TAGS
from collections import Counter

def updateDatabase():

	"""
		Organize data by date, make list of objects per date
	"""

	#The top of the photo directory, this is going to have to be dynamically passed into the program through a box in the user UI
	photoDirectory='C:/Users/Chris/Desktop/Phorg/Organized'

	#create a list of objects to be added to database
	insertList=[]
	
	#insertList.append(photoData('DSC06287','C:/Users/Chris/Desktop/Phorg/organized/2018/11 November/17 Nov 2018/Highlights/DSC06287.JPG'))
	#for attr, value in data1.__dict__.items():
			#print str(attr)+": "+str(value)

	#create the years list
	yearsList=os.listdir(photoDirectory)

	for year in yearsList:

		print "Entering year: "+str(year)

		#create the sub month list
		monthsList=os.listdir(photoDirectory+'/'+year)

		for month in monthsList:

			print "Entering month: "+str(month)

			#create the day list
			dayList=os.listdir(photoDirectory+'/'+year+'/'+month)

			for day in dayList:
	
				print "Entering Day: "+str(day)

				# loop through the photos in Highlights, and JPGS accessing exif data
				# check if edits file exists after testing
				if(	os.path.exists(photoDirectory+'/'+year+'/'+month+'/'+day)==True and
					os.path.exists(photoDirectory+'/'+year+'/'+month+'/'+day+'/Highlights')==True and
					os.path.exists(photoDirectory+'/'+year+'/'+month+'/'+day+'/JPG')==True and
				   	os.path.isdir(photoDirectory+'/'+year+'/'+month+'/'+day)==True and
				   	os.path.isdir(photoDirectory+'/'+year+'/'+month+'/'+day+'/Highlights')==True and
					os.path.isdir(photoDirectory+'/'+year+'/'+month+'/'+day+'/JPG')==True):

				   	#do something if the directories exist
					print "The highlights, JPG, and date have been found!"

					#navigate to the highlights folder and get the data from the photos inside
					os.chdir(photoDirectory+'/'+year+'/'+month+'/'+day+'/Highlights')
					photoDirList=os.listdir(photoDirectory+'/'+year+'/'+month+'/'+day+'/Highlights')

					for photo in photoDirList:
						#do I need to pass the path every time?
						#print str(photo)
						#print str(photo[:-4])

						insertList.append(photoData(photo[:-4],photoDirectory+'/'+year+'/'+month+'/'+day+'/Highlights/'+photo))

					#move to the JPG folder and do the same thing as above
					os.chdir(photoDirectory+'/'+year+'/'+month+'/'+day+'/JPG')
					photoDirList=os.listdir(photoDirectory+'/'+year+'/'+month+'/'+day+'/JPG')

					for photo in photoDirList:

						#don't pas duplicate data
						if(os.path.exists(photoDirectory+'/'+year+'/'+month+'/'+day+'/Highlights/'+photo)==True): pass
						else: insertList.append(photoData(photo[:-4],photoDirectory+'/'+year+'/'+month+'/'+day+'/JPG/'+photo))


				#else:
					#print "The file structure is incorrect, please make sure the Phorg application is being used correctly"
					#sys.exit()
	
	"""
	#loop through the objects and insert them into the database, update the data in the database, or skip
	for object in insertList:
		print "\n"
		for attr, value in object.__dict__.items():
			print str(attr)+": "+str(value)
	
	"""

	#send the list to the insertDatabasefunction
	insertDatabase(insertList)	



#function that opens the database
def insertDatabase(insertList):

	print "Made it into the insertDatabase function"

	#connect to database
	try:
		dataBase = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="password",
			database="PhotoData"
		)

		#loop through the insert objects, iterating through each one and inserting their data into the database
		for photo in insertList:

			#open the cursor
			dbCursor = dataBase.cursor()

			print "checking to see if photo "+str(photo.imageName)+" has been entered into the Database yet..."

			#add exception if the photo is already in the database, check information and do appropriate action
			photoDataDB = "SELECT * FROM photoMetaData WHERE photoName=%s"
			dbCursor.execute(photoDataDB, (photo.imageName,))

			photoData=dbCursor.fetchall()

			#if the data doesn't yet exist in the database
			if not dbCursor.rowcount:

				print "Image data not found in Database, entering data in to Database"

				"""
					Insert data into Database here
				"""

				#find the Camera Model and Lens model, then put them into the proper variables
				lensDataDB = "SELECT lensIndex FROM lensData WHERE fullLensName=%s"
				cameraDataDB = "SELECT cameraIndex FROM cameraData WHERE cameraModel=%s"

				#run query for the lens index
				dbCursor.execute(cameraDataDB, (photo.Model,))
				cameraIndex=str(dbCursor.fetchall())
				cameraIndex=cameraIndex[cameraIndex.find("(")+1:cameraIndex.find(",")]

				#run query for the camera index
				dbCursor.execute(lensDataDB, (photo.LensModel,))
				lensIndex=str(dbCursor.fetchall())
				lensIndex=lensIndex[lensIndex.find("(")+1:lensIndex.find(",")]

				#insert into the photoMetaData Table
				v=(photo.imageName, photo.Date, photo.FocalLength,photo.FNumber,photo.ExposureTime,photo.ISOSpeedRatings,photo.BrightnessValue,cameraIndex,lensIndex)
				sqlPhotoMetaData = "INSERT INTO photoMetaData (photoName,photoDate,focalLength,aperture,shutterSpeed,ISO,BrightnessValue,cameraIndex,lensIndex) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
				dbCursor.execute(sqlPhotoMetaData, v)

				#Insert data into highlights table

				#commit the changes to the database
				dataBase.commit()

			#if the database already has an entry, check to make sure the values haven't changed, if they have update the values to the correct ones
			else:

				print "Image data found in database, checking to see if location has changed"

				#check to see if the date data matches, if so, check if location changed


				#if date data does not match, add it to the database

				dataBase.commit()

				pass

				"""
					Perhaps I should allow multiple entries, just check to make sure the exif data (in particular the date data) is different?
				"""

				#run a query for the gallery/highlights and see if it has changed



			dataBase.commit()

		dataBase.close()	



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
		self.isHighlight=0
		self.isGallery=0

		self.getExifData(imagePath)

	def getExifData(self,image):

		#self.ret = {}
		i = Image.open(image)
		info = i._getexif()

		"""
			Exceptions need to be made if the file doesn't have exif data
		"""

		#loop through the exif data of the image, keeping the information then formatting it properly
		for tag, value in info.items():

			decoded=str(TAGS.get(tag, tag))

			#inclusions of EXIF data, and reformating of the data
			if(	decoded=='ISOSpeedRatings'): self.ISOSpeedRatings=str(value)
			elif(decoded=='LensModel'):self.LensModel=str(value)
			elif(decoded=='Make'): self.Make=str(value)
			elif(decoded=='Model'): self.Model=str(value)
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
				self.BrightnessValue=newValue

			elif(decoded=='DateTime'):

				Year=		''.join(value[0:4])
				Month=		''.join(value[5:7])
				Day=		''.join(value[8:10])

				self.Date=str(datetime.date(int(Year), int(Month), int(Day)))

		#figure out if the photo is a highlight and in the gallery
		self.Highlight()
		#self.Gallery()

	def Highlight(self):

		if(os.path.exists(self.imagePath)==True and ('Hightlights' in self.imagePath)):
			self.isHighlight=1
		else:
			self.isHightlight=0


#run after imported
if __name__=="__main__":
	updateDatabase()