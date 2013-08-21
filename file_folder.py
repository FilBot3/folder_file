#!/usr/bin/python

import os, sys
import shutil

class FolderFiles(object) :

	def welcome(self) :
		"""
		This will go through and make folders named 
		after files and place them in those folders
		"""
		print """
Please input the absolute path of the directory you 
wish to list the files
EXAMPLE: /Users/test/Doctuments
		"""
		path = raw_input("> ")
		dirs = os.listdir(path)
		os.chdir(path)

		for file in dirs :
			print file
			newfolder = os.path.splitext(file) [0]
			os.makedirs(newfolder, 0755);
			print newfolder
			shutil.move(file, newfolder)

runProgram = FolderFiles()
runProgram.welcome()
