
import os
import sys
import shutil

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

"""

    Find path is the path of the files that the user would like copied
    Move path is the path of the files that the user would like to be moved
    Des Path is the final destination of the files moved with Find path

"""
 
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title='PyQt5 input Dialogs'
        self.left=10
        self.top=10
        self.width=900
        self.height=525
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.center()

        """

        Find Path to Date

        """


        #create label for find path contents
        self.dateLabel= QLabel('Select the date that you would like to collect the RAW photos from:', self)
        self.dateLabel.move(20,20)

        #create line input for user to get directory name for find path
        self.datePathLine=QLineEdit(self)
        self.datePathLine.move(20,40)
        self.datePathLine.resize(500,20)

        #create browse button for find path
        self.datebrowseButton = QPushButton('...',self)
        self.datebrowseButton.setToolTip('Submit the above information')
        self.datebrowseButton.resize(20,20)
        self.datebrowseButton.move(525,40)
        self.datebrowseButton.clicked.connect(lambda: self.get_Directory())

        #give user the number of JPGs found in location
        #self.findLabelJPG=QLabel('Number of JPGs found at path: ', self)
        #self.findLabelJPG.move()


        """
            Buttons for Submiting paths and Exiting the program

        """
        
        #create the submit button
        self.quitButton = QPushButton('Submit',self)
        self.quitButton.setToolTip('Submit the above information')
        self.quitButton.move(200,495)
        self.quitButton.clicked.connect(self.run_Command)

        #create the exit button
        self.exitButton = QPushButton('Exit',self)
        self.exitButton.setToolTip('Exit the application')
        self.exitButton.move(100,495)
        self.exitButton.clicked.connect(self.close)

        self.show()

        #function that returns the directory the user chooses
    def get_Directory(self):

        #confirmation that the function was called
        print("made it into the get_Directory function")

        print (self.dateLabel.text())

        #Have the user select the file
        self.datePath = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

        #checks to make sure the RAW, JPG, and Highlights directories exist within the selected date, they should exist if the first script was used for organization
        if( os.path.exists(self.datePath+"/RAW")==True and os.path.isdir(self.datePath+"/RAW")==True and
            os.path.exists(self.datePath+"/JPG")==True and os.path.isdir(self.datePath+"/JPG")==True and
            os.path.exists(self.datePath+"/Highlights")==True and os.path.isdir(self.datePath+"/Highlights")==True):

            #confirm the directory exists in the command line, update the DatePathLine with the selected path
            print("The RAW,JPG, and Highlight directories exsist")
            self.datePathLine.setText(self.datePath)

            #add the find files, select files, and destination files variables
            self.findPath=self.datePath+"/Highlights"
            self.movePath=self.datePath+"/RAW"
            self.desPath=self.datePath+"/Edits"

            print ( "\nFind directory: "+self.findPath+
                    "\nMove directory: "+self.movePath+
                    "\nDestination directory: "+self.desPath)

            #execution if the user selects the correct file type
        else:
            print("Selection failed")
            self.datePathLine.setText("")

    #command runs the program, outputing an error if paths do not have correct files

    """
        Catch Arritbute Error if a path name is not passed

    """

    def run_Command(self):
        
        print ("Inside the run_command function")

        print ("DatePathLine: "+self.datePathLine.text())

        if( os.path.exists(self.datePathLine.text()+"/RAW")==True and os.path.isdir(self.datePathLine.text()+"/RAW")==True and
            os.path.exists(self.datePathLine.text()+"/JPG")==True and os.path.isdir(self.datePathLine.text()+"/JPG")==True and
            os.path.exists(self.datePathLine.text()+"/Highlights")==True and os.path.isdir(self.datePathLine.text()+"/Highlights")==True):

            #print out the paths
            print ("Find Path: "+str(self.findPath))
            print ("Move Path: "+str(self.movePath))
            print ("Destination Path: "+str(self.desPath))

            #create the edits directory if it doesn't exist
            if(os.path.exists(self.desPath)==True and os.path.isdir(self.desPath)==True):
                #create an array of the file names in the find path (this also converts the file names to .ARW files when returned)
                self.findFiles()

                #go to the move path and search for the files, moving them to the final destination
                self.moveFiles()

            else:

                #create edits directory
                os.mkdir(self.desPath)

                #create an array of the file names in the find path (this also converts the file names to .ARW files when returned)
                self.findFiles()

                #go to the move path and search for the files, moving them to the final destination
                self.moveFiles()
            
        else:
            pass
            print ("Error found in the path name, try again")


    #creates a set with the find File path (should be the highlights folder)

    """
        #An error should be thrown if there are duplicate file names found, as the set function will delete them
    """

    def findFiles(self):

        #move the working directory to the path given in the find path label
        os.chdir(self.findPath)
        print ("Current Working Dictory(sound be find path):"+ os.getcwd())

        #create list of each file name found at path
        self.findItems=os.listdir(self.findPath)

        #the final list of JPGs (assuming not all files at location are JPGs)
        self.findList=[]

        #loop through the find Items List adding JPGs to the findList and converting the fine name to .ARW extention
        for names in self.findItems:
            if names.endswith(".JPG"):
                names=names[:-4]+'.ARW'
                self.findList.append(names)

        #make a set with the Find list for data operations in the moveFiles function
        self.findList=set(self.findList)

        #print the list
        print (self.findList)
    
    #this function moves all the .ARW files found at the move path to the destination path

    """
        An error should be listed if a specific file isn't found
        An error should be throw if a duplicate is found

    """

    def moveFiles(self):

        #change the working directory to the move path given by the user
        os.chdir(self.movePath)

        #create list of ARW files found at move path
        self.moveItems=set(os.listdir(self.movePath))

        #create final list with the found raw Files in the move Path
        self.moveList=[]

        #Find the intersections of the two sets
        self.moveList=self.moveItems.intersection(self.findList)

        #print out the list of found RAW files
        print (self.moveList)

        #moves the current file to from the unorganized folder to the organized folder in the JPG section
        for RAW in self.moveList:
            shutil.move(self.movePath+'/'+RAW,self.desPath)

    #centers the window when it is opened
    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp=QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

def main():
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()