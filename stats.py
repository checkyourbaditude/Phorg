import Tkinter
import tkMessageBox
import os
from tkFileDialog import askdirectory
from Tkinter import *

class ARWFinder(window):

		#initializes program with the window
		def initialize():

			#create labels for text box
			lbl=Label(window, text="Path")
			lbl.grid(column=0, row=0)
			lb2=Label(window, text="Explore")
			lb2.grid(column=1,row=0)
			lb3=Label(window, text="Destination")
			lb3.grid(column=0, row=1)

			#variables to hold the inputs from the user
			Path=Entry(window,width=40,)
			Path.insert(0,'C:\Users\Chris\Desktop\example')
			Path.grid(column=1, row=0)
			Destination=Entry(window,width=40)
			Destination.grid(column=1, row=1)

			#explore buttons
			ExploreButton=Button(window, text="...", command= lambda: get_dirname())
			ExploreButton.grid(column=2, row=0)

			#button to run the program
			RunButton = Button(window, text="Run", command= lambda: run(Path.get(),Destination.get()))
			RunButton.grid(column=1, row=2)

			#Button to exit the program
			ExitButton = Button(window, text="Exit", command= lambda: exit())
			ExitButton.grid(column=0, row=2)

		#function that runs program when clicked
		def run (Path,Destination):
		 
		    #lbl.configure(text="Button was clicked !!")

		    tkMessageBox.showinfo("Congradulations!", "You ran the program")

		    print "This is the path: " + Path
		    print "\nThis is the destination: " + Destination

		    #creates new variable holding the variable names
		    photoNames=getPhotoNames(Path)

		    #search for .ARW file names in the destination folder

		#returns the directory name
		def get_dirname():
			name= askdirectory() 
			print "Name in the get_dirname: " + name
			return name

		#this function is going to return an array of the photo names
		def getPhotoNames(Path):

			#gets the file name and arranges them in the array
			dirList=os.listdir(Path)

			#print the directory list
			for x in dirList:
				if(x.endswith('.JPG')):
					print "found JPG! Adjusting name...."
					x=x[:-4]+'.ARW'
					print "New Name: "+ x
				else:
					print "Found non-JPG image, exiting!"
					exit()

			#return the directory list
			return dirList



#converts the array names from .jpg to .arw 
#def convARW():


#run the program
def main():
	#initalize the window
	window = Tk()
	window.title("Welcome to Phorg")
	window.geometry('350x100')
	app = ARWFinder(window)
	window.mainloop()

if __name__ == '__main__':
	main()


"""
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x100')
lbl = Label(window, text="Path") 
lbl.grid(column=0, row=0)
lb2 = Label(window, text="Destination")
lb2.grid(column=0, row=1) 
Path = Entry(window,width=40) 
Path.grid(column=1, row=0)
Destination = Entry(window,width=40)
Destination.grid(column=1, row=1) 
def clicked():
 
    #lbl.configure(text="Button was clicked !!")

    tkMessageBox.showinfo("Title", "a Tk MessageBox")

btn = Button(window, text="Run", command=clicked)
btn.grid(column=1, row=2)
window.mainloop()
"""
 
initialize()