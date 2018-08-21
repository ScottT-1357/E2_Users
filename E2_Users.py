# #########################################################################
# E2_Users: Python script to list currently logged in users in E2
#
# Scott Thompson 3/30/18 : Created
#
# #########################################################################
import os
import datetime
import sys
import tkinter
from tkinter import *

# #########################################################################
# Define Constants and global variables
# #########################################################################
E2_DataDir = r'\\cms-Shoptech\Data\Blswin32\Dat'
os.chdir(E2_DataDir)
files=[]
    
def getUserList():
    for file in os.listdir('.'):
        if file.endswith(".USR"):
            files.append(file)

def printUserList():
    print("E2 users logged in now:")
    count = 0
    for file in files:
        f = open(file, 'r')
        userinfo = f.read()
        print ('\t', file, '\tE2 User(' +  str(count) + "): \t"+ userinfo[:37] + "  " + userinfo[37:])

        count += 1
        f.close()
    print("E2 User Count: ", count)
    return count

def promptUserInput(currentcount):
    print('Select the user number to logout (', cnt, ') to quit ', sep='', end='')
    option = input("")
    if option == "":
        opt = currentcount
    else:
        opt = int(option)
    print (opt)
    return opt

#
# Main Program
#
getUserList()
cnt = printUserList()
opt = promptUserInput(cnt)

# Loop until the user decides to quite (enter the cnt)
while opt < cnt:
    print('\nDeleting user file:', files[opt])
    os.remove(files[opt])

    files=[]
    getUserList()
    cnt = printUserList()
    opt = promptUserInput(cnt)

 