import Tkinter
import tkMessageBox
import os
from tkFileDialog import askdirectory
from Tkinter import *
import Tkinter as tk

"""
	Find path is the path of the files that the user would like copied
	Move path is the path of the files that the user would like to be moved
	Des Path is the final destination of the files moved with Find path
"""

class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):

    	#initalize
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        #create the view for the user
        self.create_View(parent)

    def create_View(self,parent):
    	#add title to window and dims
      	parent.title("Phorg")
      	parent.geometry('500x300')
      	
        #create lables and field for the find Path, plus explore button at the end
        self.lbFindPath=Label(parent, text="Path of files Files you would like to find the RAW files of: ")
        self.lbFindPath.grid(sticky="W",column=0, row=0)

        self.FindPath=Entry(parent,width=50)
        self.FindPath.grid(sticky="W",column=0, row=1)

        self.ExFindButton=Button(parent, text="...", command=lambda: self.update_View("Find"))
        self.ExFindButton.grid(sticky="W",column=1,row=1)

        #create Lables and field for the find path
        self.lbMovePath=Label(parent, text="Path of the files that the user would like to be moved: ")
        self.lbMovePath.grid(sticky="W",column=0,row=2)

        self.MovePath=Entry(parent,width=50)
        self.MovePath.grid(sticky="W",column=0, row=3)

        self.ExMoveButton=Button(parent, text="...", command=lambda: self.update_View("Move"))
        self.ExMoveButton.grid(sticky="W",column=1,row=3)

        #label and fields for the destination path
        self.lbDesPath=Label(parent, text="Final Destination of found files: ")
        self.lbDesPath.grid(sticky="W",column=0,row=4)

        self.DesPath=Entry(parent,width=50)
        self.DesPath.grid(sticky="W",column=0, row=5)

        self.ExDesButton=Button(parent, text="...", command=lambda: self.update_View("Des"))
        self.ExDesButton.grid(sticky="W",column=1,row=5)

        #run the program button
        self.RunButton=Button(parent, text="Run", command=parent.quit)
        self.RunButton.grid(sticky="NW",column=0,row=7)

        #exit Button
        self.ExitButton=Button(parent, text="Exit", command=parent.quit)
        self.ExitButton.grid(sticky="N",column=0,row=7)

    

    def update_View(self, Path):
    	if(Path=="Find"):
    		print "Entering the askdirectory section for Find Path"
    		self.FindPath.insert(0, askdirectory())
    	elif(Path=="Move"):
    		print "Entering the askdirectory section for Move Path"
    		self.MovePath.insert(0, askdirectory())
    	elif(Path=="Des"):
    		print "Entering the askdirectory section for Des Path"
    		self.DesPath.insert(0, askdirectory())
    	else:
    		tkMessageBox.showinfo("Error", "Correct Exploration Path not provided")




if __name__ == "__main__":
    root = tk.Tk()
    #MainApplication(root).pack(side="top", fill="both", expand=True)
    MainApplication(root)
    root.mainloop()