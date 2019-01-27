import os
import sys
import shutil

def SelectPhotos(datePath):
        
    print ("Inside the SelectPhotos function")
    print ("Date Path Chosen: "+datePath)
    os.chdir(datePath)

    if( os.path.exists(datePath+"/RAW")==True and os.path.isdir(datePath+"/RAW")==True and
        os.path.exists(datePath+"/JPG")==True and os.path.isdir(datePath+"/JPG")==True and
        os.path.exists(datePath+"/Highlights")==True and os.path.isdir(datePath+"/Highlights")==True):

    	#declare the findPath, movePath, and desPath variables once the directories are confirmed again
    	findPath=datePath+"/Highlights"
    	movePath=datePath+"/RAW"
    	desPath=datePath+"/Edits"

        #print out the paths
        print ("Find Path: \t\t\t"+findPath)
        print ("Move Path: \t\t\t"+movePath)
        print ("Destination Path: \t\t\t"+desPath)

        #create the edits directory if it doesn't exist
        if(os.path.exists(desPath)==True and os.path.isdir(desPath)==True):

			print ("The destination path has already been created, proceeding to find RAW files")

			#create an array of the file names in the find path (this also converts the file names to .ARW files when returned)
			findList=findFiles(findPath)

			#go to the move path and search for the files, moving them to the final destination
			moveFiles(movePath,desPath,findList)

        else:

			#create edits directory since it was not found
			os.mkdir(desPath)

			#create an array of the file names in the find path (this also converts the file names to .ARW files when returned)
			findList=findFiles(findPath)

			#go to the move path and search for the files, moving them to the final destination
			moveFiles(movePath,desPath,findList)
        
    else:
        print ("Error found in the path name, try again")
        pass


    #creates a set with the find File path (should be the highlights folder)

    """
        #An error should be thrown if there are duplicate file names found, as the set function will delete them
    """

def findFiles(findPath):

    #move the working directory to the path given in the find path label
    os.chdir(findPath)
    print ("Current Working Dictory(sound be find path):"+ os.getcwd())

    #create list of each file name found at path
    findItems=os.listdir(findPath)

    #the final list of JPGs (assuming not all files at location are JPGs)
    findList=[]

    #loop through the find Items List adding JPGs to the findList and converting the fine name to .ARW extention
    for names in findItems:
        if names.endswith(".JPG"):
            names=names[:-4]+'.ARW'
            findList.append(names)

    #make a set with the Find list for data operations in the moveFiles function
    findList=set(findList)

    #print the list
    print (findList)

    return findList

#this function moves all the .ARW files found at the move path to the destination path

"""
    An error should be listed if a specific file isn't found
    An error should be throw if a duplicate is found

"""

def moveFiles(movePath,desPath,findList):

    #change the working directory to the move path given by the user
    os.chdir(movePath)

    #create list of ARW files found at move path
    moveItems=set(os.listdir(movePath))

    #create final list with the found raw Files in the move Path
    moveList=[]

    #Find the intersections of the two sets
    moveList=moveItems.intersection(findList)

    #print out the list of found RAW files
    print (moveList)

    #moves the current file to from the unorganized folder to the organized folder in the JPG section
    for RAW in moveList:
        shutil.move(movePath+'/'+RAW,desPath)

#run after imported
if __name__=="__main__":
	SelectPhotos(datePath)