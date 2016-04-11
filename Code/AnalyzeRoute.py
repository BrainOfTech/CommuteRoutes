#This file last edited by (S)am on 4-10-16
#This file contains utilities for parsing input from the encrypted email,
#analyzing coordinate streams,
#maintaining a list of known locations and paths,
#generating encrypted receipt pages for use by the mobile application,
#and entering data into the relevant databases.

from Regression import *

#The main method is actually invoked at the end of this file.
#The primary purpose of the main method is to call the appropriate subfunctions in sequence.
#The main method has no return value. Data is assumed to be piped through standard input.
#Input consists of an encrypted sequence of GPS coordinates and a list of locations to exclude tracking.
#The main method should decrypt the data, parse the stream, identify locations and paths, and update the relevant databases.
#TODO
def main():
	#Read Input through standard input
	#Decrypt Sequence
	#Parse Sequence into latitude coords, longitude coords, and timestamps
	#Identify centers of locations
	#Partition into locations and paths
	#Load Partition/Paths Record
	#Classify locations and paths
	#Filter locations and paths to ignore
	#Remove records from database of newly added "to ignore" locations and paths.
	#Pass abstracted data to the database via SendMail
	print "in main" #TODO: remove
	####DEBUGGING
	#tempData = [[1,4.01],[3,4.1],[4,4]]#DEBUGGING
	#print(computeCorrelationIsSignificant(tempData))#DEBUGGING

#Call the main method if this file is not simply being imported.
if __name__ = "__main__":
	main()
