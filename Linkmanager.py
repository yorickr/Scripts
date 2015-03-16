#!/usr/bin/python2.7
import os
from email.Utils import formatdate

debug = False
dir = "/home/imegumii/.linkmanager/"
try:
    if os.path.exists(dir) == False:
        os.mkdir(dir)
except:
    os.system("echo \"Was unable to create a new path for linkmanager, reason unknown.\nPlease contact.\"")
recentlog = open(dir + "log.log",'a')

def makeNewLink():
    assistance = raw_input("Would you like path assistance?\ny/n?\n")
    if assistance == "y":
        sourcedir = pathAssistance()
        print sourcedir
    elif assistance == "n":
        sourcedir = raw_input("Please input the path of the file you're making a link to.\n").replace(' ', '\ ')
        print sourcedir
    else:
        os.system("echo \"Not a valid option, try again.\"")
        makeNewLink()
    linkname = raw_input("Please input the name of the new link.\n")
    check = raw_input("Are you sure you want to apply this change?\ny/n?\n")
    if check == "y":
        os.system("sudo ln " + sourcedir + " /usr/bin/" + linkname + " -s")
        writelog("Made symlink " + linkname + " from path " + sourcedir + ".")
    else: 
        os.system("echo \"Action terminated by user\"")

def renameLink():
    programname = raw_input("Please input the name of the program you would like to change.\n")
    renamedname = raw_input("Please input what you'd like to rename " + programname + " to.\n")
    check = raw_input("Are you sure you want to apply this change?\ny/n?\n")
    if check == "y":
        os.system("sudo ln /usr/bin/"+ programname + " /usr/bin/"+ renamedname + " -s")
        writelog("Renamed symlink "+ programname + " to " + renamedname + ".")
    elif check == "n":
        os.system("echo \"Action terminated by user\"")
    else:
        os.system("echo \"Input not correct.\"")

def removeLink():
    linktoremove = raw_input("Please input the name of the link you'd like to remove.\n")
    check = raw_input("Are you sure you want remove " + linktoremove + "?\ny/n?\n")
    if check == "y":
        os.system("sudo unlink /usr/bin/" + linktoremove)
        writelog("Unlinked " + linktoremove + ".")
    elif check == "n":
        os.system("echo \"Action terminated by user\"")
    else:
        os.system("echo \"Input not correct.\"")

def listLink():
    prompt = raw_input("Would you like to filter the list?\ny/n?\n")
    if prompt == "y":
        filterword = raw_input("Input the word you'd like to filter for.\n")
        os.system("echo \"LIST:\"")
        os.system("echo \"------------------------------\"")
        os.system("sudo ls /usr/bin/ | grep " + filterword)
        os.system("echo \"------------------------------\"")
        writelog("Listed using filter " + filterword + ".")
    elif prompt == "n":
        os.system("echo \"LIST:\"")
        os.system("echo \"------------------------------\"")
        os.system("sudo ls /usr/bin/")
        os.system("echo \"------------------------------\"")
        writelog("Listed without filter.")
    else: 
        os.system("echo \"Not a valid answer, try again.\"")
        listLink()
    
def pathAssistance():
    os.system("echo \"Press CTRL + C at any moment to indicate that you're done.\"")
    pathstring = ""
    try:
        startofpath = raw_input("Enter the start of your path.\n")
        pathstring += "/" + startofpath
        os.system("echo \"------------------------------\"")
        os.system("ls " + pathstring)
        os.system("echo \"------------------------------\"")
        while True:
            restofpath = raw_input("Enter the next part of your path.\n")
            pathstring += "/" + restofpath.replace(' ', '\ ')
            os.system("echo \"------------------------------\"")
            os.system("ls " + pathstring)
            os.system("echo \"------------------------------\"")
    except KeyboardInterrupt:
        print("")
        writelog("PathAssistance gave " + pathstring + "")
        return pathstring

def promptDecision():
    decision = raw_input("Would you like to perform another action?\ny/n?\n")
    if decision == "y":
        main()
    elif decision == "n":
        quitPrompt()
    else:
        os.system("echo \"Not a valid input, try again.\"")
        promptDecision()

def displayPrompt():
    display = raw_input("Would you like to display a list of symlinks?\ny/n?\n")
    if display == "y":
        return True
    elif display == "n":
        return False
    else:
        os.system("echo \"Not a valid input, try again.\"")

def quitPrompt():
    quit = raw_input("Press enter to quit.")
    kill()

def writelog(msg):
    stamp = formatdate(localtime=True)
    full="["+stamp+"] " + msg
    recentlog.write(full+"\n")
    recentlog.flush()

def kill():
    writelog("Stopping application.")
    writelog("------------------------------")
    recentlog.close()

def main():
    if os.getuid() == 0:
        decision = raw_input("What action would you like to perform?\nnew/add/remove/list?\n")
        if decision == "new":
            makeNewLink()
            promptDecision()
        elif decision == "add":
            if displayPrompt() == True:
                listLink()
            renameLink()
            promptDecision()
        elif decision == "remove":
            if displayPrompt() == True:
                listLink()
            removeLink()
            promptDecision()
        elif decision == "list":
            listLink()
            promptDecision()
        else:
            os.system("echo \"No valid option selected, try again.\"")
            promptDecision()
    else:
        writelog("User is not root, quitting application.")
        print("Run this application as root.")
        kill()
     
os.system("echo \"------------------------------\"")
os.system("echo \"Linkmanager\"")
os.system("echo \"Press ctrl + c at any time to quit this application.\"")       
os.system("echo \"------------------------------\"")
writelog("------------------------------")
writelog("Starting application.")
if debug == False:
    try:
        main()
    except KeyboardInterrupt:
        writelog("User exit application using CTRL C.")
        print("")
        print("Quit application")
        kill()
else:
    pathAssistance()
