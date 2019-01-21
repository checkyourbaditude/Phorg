import sys
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


        '''
        #set up the view for the path folder below

        hlay = QHBoxLayout(self)
        self.treeview = QTreeView()
        self.listview = QListView()
        hlay.addWidget(self.treeview)
        hlay.addWidget(self.listview)

        path = QDir.rootPath()

        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.rootPath())
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)

        self.fileModel = QFileSystemModel()
        self.fileModel.setFilter(QDir.NoDotAndDotDot |  QDir.Files)

        self.treeview.setModel(self.dirModel)
        self.listview.setModel(self.fileModel)

        self.treeview.setRootIndex(self.dirModel.index(path))
        self.listview.setRootIndex(self.fileModel.index(path))

        self.treeview.clicked.connect(self.on_clicked)

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

        #create label for destination path
        self.desLabel= QLabel('Select Directory where the JPGs are Located:', self)
        self.desLabel.move(25,140)

        #create line input for user to get directory path for destination 
        self.desPathLine=QLineEdit(self)
        self.desPathLine.move(25,155)
        self.desPathLine.resize(500,20)

        #create browse button for move path
        self.mbrowseButton = QPushButton('...',self)
        self.mbrowseButton.setToolTip('Submit the above information')
        self.mbrowseButton.resize(20,20)
        self.mbrowseButton.move(525,155)
        self.mbrowseButton.clicked.connect(lambda: self.get_Directory("Des"))

        '''

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

        #path=self.getText()

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

            #send path to function to find the number of JPGs at the location
            self.findLabel.setText(str(self.findLabel.text()+" THIS WORKED"))

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


    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp=QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    def run_Command(self):
        
        print ("Inside quit application")

    """def getText(self):

        text=QLineEdit()

        text, okPressed = QInputDialog.getText(self, "GetText", "YourName:", QLineEdit.Normal, "")
        
        if okPressed and text != '':
            print (text)
            return text
            """

    def on_clicked(self, index):
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        self.listview.setRootIndex(self.fileModel.setRootPath(path))


def main():
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()