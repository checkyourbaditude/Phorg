"""workflow for downloading photos from camera
 * first step is to download all the photos on the desktop
 * next step is to run the seperate.py script on the file that was just downloaded
 *		this will in turn create two seperate folders, one with the jpg files and one with the RAW files
 * Look through the folder of jpgs, deleting the ones that are unappealing/overexposed/etc
 * Run colsolidatebackup.py script on the folder
 *		Firstly, the script will search for the remaining jpg's corresponding RAW files
 *			The RAW files that are to have the same file name as a kept JPG will be kept (just with a different file extension), while the others will all be deleted
 *		Secondly, new folder will be created with the remaining photos
 """