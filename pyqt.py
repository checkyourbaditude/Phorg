
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

            Find Path

        """

        #create label for find path contents
        self.findLabel= QLabel('Select Directory where the JPGs are Located:', self)
        self.findLabel.move(20,20)

        #create line input for user to get directory name for find path
        self.findPathLine=QLineEdit(self)
        self.findPathLine.move(20,40)
        self.findPathLine.resize(500,20)

        #create browse button for find path
        self.fbrowseButton = QPushButton('...',self)
        self.fbrowseButton.setToolTip('Submit the above information')
        self.fbrowseButton.resize(20,20)
        self.fbrowseButton.move(525,40)
        self.fbrowseButton.clicked.connect(lambda: self.get_Directory("Find"))

        #give user the number of JPGs found in location
        #self.findLabelJPG=QLabel('Number of JPGs found at path: ', self)
        #self.findLabelJPG.move()

        """

            Move Path

        """

        #create label for move lable contents
        self.moveLabel= QLabel('Select Directory where the Raw Files that need to be moved are located:', self)
        self.moveLabel.move(25,85)

        #create line input for user to get directory name for move path
        self.movePathLine=QLineEdit(self)
        self.movePathLine.move(25,100)
        self.movePathLine.resize(500,20)

        #create browse button for move path
        self.mbrowseButton = QPushButton('...',self)
        self.mbrowseButton.setToolTip('Submit the above information')
        self.mbrowseButton.resize(20,20)
        self.mbrowseButton.move(525,100)
        self.mbrowseButton.clicked.connect(lambda: self.get_Directory("Move"))

        #give user the number of RAW files found in location
        #self.findLabelJPG=QLabel('Number of Raws found at path: ', self)
        #self.findLabelJPG.move()

        """

            Destination Path

        """

        #create label for destination path
        self.desLabel= QLabel('Select Directory where the JPGs are Located:', self)
        self.desLabel.move(25,140)

        #create line input for user to get directory path for destination 
        self.desPathLine=QLineEdit(self)
        self.desPathLine.move(25,155)
        self.desPathLine.resize(500,20)

        #create browse button for destination path
        self.mbrowseButton = QPushButton('...',self)
        self.mbrowseButton.setToolTip('Submit the above information')
        self.mbrowseButton.resize(20,20)
        self.mbrowseButton.move(525,155)
        self.mbrowseButton.clicked.connect(lambda: self.get_Directory("Des"))

        #give user the number of RAW files To be moved
        #self.findLabelJPG=QLabel('Number of Raws to be moved to destination: ', self)
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
    def get_Directory(self, text):

        #confirmation that the function was called
        print("made it into the get_Directory function: "+str(text))

        print (self.findLabel.text())

        #search for the find variable and put it into the FindPath QLineEdit
        if(text=="Find"):
            #adjust the find path contents, print the directory that was found
            self.findPath = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
            print (str(text)+" directory: "+self.findPath)
            self.findPathLine.setText(self.findPath)

            return

        elif(text=="Move"):
            #adjust the find path contents, print the directory that was found
            self.movePath = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
            print (str(text)+" directory: "+self.movePath)
            self.movePathLine.setText(self.movePath)

            #send path to function to find the number of JPGs at the location

            return
        elif(text=="Des"):
            #adjust the find path contents, print the directory that was found
            self.desPath = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
            print (str(text)+" directory: "+self.desPath)
            self.desPathLine.setText(self.desPath)

            #send path to function to move files from move path to destination, first checking if the files are already there

            return
        else:
            #put in an error message box with message
            print("An error has occured")

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



    #command runs the program, outputing an error if paths do not have correct files

    """
        Catch Arritbute Error if a path name is not passed

    """

    def run_Command(self):
        
        print ("Inside the run_command function")

        #print out the paths
        print ("Find Path: "+str(self.findPath))
        print ("Move Path: "+str(self.movePath))
        print ("Destination Path: "+str(self.desPath))

        #create an array of the file names in the find path (this also converts the file names to .ARW files when returned)
        self.findFiles()

        #go to the move path and search for the files, moving them to the final destination
        self.moveFiles()

    #creates a set with the find File path (should be the highlights folder)

    """
        An error should be thrown if there are duplicate file names found, as the set function will delete them
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


def main():
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()