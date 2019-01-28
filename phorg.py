# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Phorg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import os
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog

from OrganizeScript import OrganizePhotos
from SelectScript import SelectPhotos
from StatisticsScript import updateDatabase

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.resize(391, 258)
        self.OrganizeTab = QtGui.QWidget()
        self.OrganizeTab.setObjectName(_fromUtf8("OrganizeTab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.OrganizeTab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.organizeLabel_1 = QtGui.QLabel(self.OrganizeTab)
        self.organizeLabel_1.setWordWrap(True)
        self.organizeLabel_1.setObjectName(_fromUtf8("organizeLabel_1"))
        self.verticalLayout.addWidget(self.organizeLabel_1)
        self.organizeButton = QtGui.QPushButton(self.OrganizeTab)
        self.organizeButton.setObjectName(_fromUtf8("organizeButton"))
        self.verticalLayout.addWidget(self.organizeButton)
        TabWidget.addTab(self.OrganizeTab, _fromUtf8(""))
        self.SelectionTab = QtGui.QWidget()
        self.SelectionTab.setObjectName(_fromUtf8("SelectionTab"))
        self.gridLayout = QtGui.QGridLayout(self.SelectionTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.selectLabel_1 = QtGui.QLabel(self.SelectionTab)
        self.selectLabel_1.setWordWrap(True)
        self.selectLabel_1.setObjectName(_fromUtf8("selectLabel_1"))
        self.gridLayout.addWidget(self.selectLabel_1, 1, 0, 1, 3)
        self.selectButton = QtGui.QPushButton(self.SelectionTab)
        self.selectButton.setObjectName(_fromUtf8("selectButton"))
        self.gridLayout.addWidget(self.selectButton, 6, 0, 1, 3)
        self.selectLabel_2 = QtGui.QLabel(self.SelectionTab)
        self.selectLabel_2.setObjectName(_fromUtf8("selectLabel_2"))
        self.gridLayout.addWidget(self.selectLabel_2, 2, 0, 1, 3)
        self.selectLineEdit = QtGui.QLineEdit(self.SelectionTab)
        self.selectLineEdit.setObjectName(_fromUtf8("selectLineEdit"))
        self.gridLayout.addWidget(self.selectLineEdit, 5, 0, 1, 2)
        self.findDateButton = QtGui.QPushButton(self.SelectionTab)
        self.findDateButton.setObjectName(_fromUtf8("findDateButton"))
        self.gridLayout.addWidget(self.findDateButton, 5, 2, 1, 1)
        TabWidget.addTab(self.SelectionTab, _fromUtf8(""))
        self.statTab = QtGui.QWidget()
        self.statTab.setObjectName(_fromUtf8("statTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.statTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.statButton = QtGui.QPushButton(self.statTab)
        self.statButton.setObjectName(_fromUtf8("statButton"))
        self.verticalLayout_2.addWidget(self.statButton)
        TabWidget.addTab(self.statTab, _fromUtf8(""))

        """
            Organize Script
        """

        self.organizeButton.clicked.connect(self.organizePhotos)

        """
            Select Script
        """

        #Find the correct date directory
        self.findDateButton.clicked.connect(lambda: self.get_Directory())

        #run the Select Script
        self.selectButton.clicked.connect(lambda: self.selectPhotos())

        """
            Statistics Script
        """

        self.statButton.clicked.connect(lambda: self.statPhotos())

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "Phorg", None))
        self.organizeLabel_1.setText(_translate("TabWidget", "The button below takes all of the photos in the \"Unorganized\" photo folder and organizes them by date and file type", None))
        self.organizeButton.setText(_translate("TabWidget", "Organize Photos", None))
        TabWidget.setTabText(TabWidget.indexOf(self.OrganizeTab), _translate("TabWidget", "Organize", None))
        self.selectLabel_1.setText(_translate("TabWidget", "The section is meat to be used after a set of photos has already been organized by the Organize tab. Take the JPG versions you like and put them into the highlights folder. This script will take the RAW versions of the JPGs in the Highlights folder and put them in a new folder called Edits.", None))
        self.selectButton.setText(_translate("TabWidget", "Collect RAW Photos", None))
        self.selectLabel_2.setText(_translate("TabWidget", "Use the button on the right to select the file path, or enter it manually below", None))
        self.findDateButton.setText(_translate("TabWidget", "...", None))
        TabWidget.setTabText(TabWidget.indexOf(self.SelectionTab), _translate("TabWidget", "Select", None))
        self.statButton.setText(_translate("TabWidget", "UpdateDatabase", None))
        TabWidget.setTabText(TabWidget.indexOf(self.statTab), _translate("TabWidget", "Statistics", None))

    def organizePhotos(self):

        """
            Put a window asking if you are sure
        """

        OrganizePhotos()


    def selectPhotos(self):

        """
            Put a window asking if you are sure
        """

        SelectPhotos(self.datePath)

    def statPhotos(self):

        """
            Put a window asking if you are sure
        """

        updateDatabase()

    def get_Directory(self):

        #confirmation that the function was called
        print("made it into the get_Directory function")

        #not sure why this is here
        #print (self.dateLabel.text())

        #Have the user select the file
        self.datePath = str(QFileDialog.getExistingDirectory())

        print "The directory chosen is: "+str(self.datePath)

        #checks to make sure the RAW, JPG, and Highlights directories exist within the selected date, they should exist if the first script was used for organization
        if( os.path.exists(self.datePath+"/RAW")==True and os.path.isdir(self.datePath+"/RAW")==True and
            os.path.exists(self.datePath+"/JPG")==True and os.path.isdir(self.datePath+"/JPG")==True and
            os.path.exists(self.datePath+"/Highlights")==True and os.path.isdir(self.datePath+"/Highlights")==True):

            #confirm the directory exists in the command line, update the DatePathLine with the selected path
            print("The RAW, JPG, and Highlight directories exsist")
            self.selectLineEdit.setText(self.datePath)

        #execution if the user selects the incorrect file type
        else:

            """
                Put error message here
            """

            print("Selection failed, must choose folder organized by ORGANIZE SCRIPT")
            self.selectLineEdit.setText("")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    TabWidget = QtGui.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())

