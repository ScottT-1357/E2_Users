# #########################################################################
# E2_Users: Python script to list currently logged in users in E2
#
# Scott Thompson 3/30/18 : Created
#
# #########################################################################
import os
import datetime
import sys
import tkinter as tk
from tkinter import ttk

# #########################################################################
# Define Constants and global variables
# #########################################################################
E2_DataDir = r'\\cms-Shoptech\Data\Blswin32\Dat'
os.chdir(E2_DataDir)
files=[]
MaxUsers=17

def getUserList():
    for file in os.listdir('.'):
        if file.endswith(".USR"):
            files.append(file)

class HelloApp:

	def __init__(self, master):

		self.label = ttk.Label(master, text = 'CustomCrimp E2 Active Users')
		self.label.grid(row = 0, column = 0, columnspan = 2)
		self.labels = []

		ttk.Button(master, text = 'Update', command = self.UpdateE2Users).grid(row = 1, column = 0, columnspan = 2)

		# Create lables for all the possible E2 users (based on licenses avaialble)
		i = 0
		while i < MaxUsers:
			defaultText = 'E2 User - ' + str(i+1)
			self.labels.append(ttk.Label(master, text = defaultText).grid(row=i+2,column = 0))
			i += 1

		# User the current users to update the list of items
		# count = 0
		# for file in files:
		# 	f = open(file, 'r')
		# 	userinfo = f.read()
		# 	myLabel = self.labels[count]
		# 	myLabel.config(text = userinfo)

		# 	#print ('\t', file, '\tE2 User(' +  str(count) + "): \t"+ userinfo[:37] + "  " + userinfo[37:])
		# 	count += 1
		# 	f.close()

	def UpdateE2Users(self):
		self.label.config(text = 'Updated E2 Users')

def main():
	win = tk.Tk()
	getUserList()
	app = HelloApp(win)
	win.mainloop()

if __name__ == "__main__": main()
