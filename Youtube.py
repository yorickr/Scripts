#!/usr/bin/python2.7

import os
import praw
import urllib
import time
import datetime
import ConfigParser
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from random import randint

from datetime import timedelta
# from datetime import datetime
from threading import Timer



# homedir = "/home/imegumii/Projects/LiClipse Workspace/Testproject/"
homedir = "/media/HDD/shares/Python/Youtube/"
databasefileURL = homedir + "ytdb.txt"
historyfileURL = homedir + "yth.txt"
dbf = open(databasefileURL, 'r+')
hsf = open(historyfileURL, 'a+')
hs = []
db = []
ident = ";-----;"

def decrypt(passwd):
    passwdstring = ""
    passwdlist = passwd.split(',')
    for char in passwdlist:
        char = int(char)
        char = (char ** 127) % 4087
        passwdstring = passwdstring + str(chr(char))
    return passwdstring

def init():
    for line in hsf:
        hs.append(line.rstrip("\n"))
    loadDB()

def writeToDB(string):
    dbf.write(string)
    dbf.flush()
    
def hsCheck(string):
    if string in hs:
        return True        
    else:
        hs.append(string)
        hsf.write(string + "\n")
        hsf.flush()
        return False
    
def loadDB():
    for line in dbf:
        db.append(line.rstrip("\n"))
        
def pickRandomFromDB():
    chosen = db[randint(0,len(db)-1)]
    entry = chosen.split(ident)
    return entry
        
def mail(entry):
    print "Mail"
    sender = config.get("Email", "mail")
    passwd = config.get("Email", "password")
    passwd = decrypt(passwd)
    
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = "yorick-rommers@hotmail.com"
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "A new song."
    string = "Title: " + entry[0] + "\nURL: " + entry[1] + "\nDate of post: " + entry[2] + "\n" 

    html = "<iframe width=\"560\" height=\"315\" src=\""+ entry[1] +"\" frameborder=\"0\" allowfullscreen></iframe>"
    msg.attach( MIMEText("" + string))
    part = MIMEText(html, 'html')
    msg.attach(part)
    for part in msg.walk():
        print part
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, passwd)
    text = str(msg)
    server.sendmail(sender, msg['To'], text)
    server.close()
        
def sendEveryDay():
    x=datetime.datetime.today()
    y = (x + timedelta(days=1)).replace(hour=2, minute=0, second=0)
    delta_t=y-x

    secs=delta_t.seconds+1

    t = Timer(secs, mail(pickRandomFromDB()))
    #t.start()
        
def fetchAndWriteToDB():
    submissions = reddit.get_subreddit('japanesemusic').get_hot()
    for sub in submissions:
        if "youtube.com" in sub.url:
            writestring = sub.title + ident + sub.url + ident + str(datetime.datetime.fromtimestamp(sub.created_utc)) + "\n"
            if(hsCheck(sub.url) == True):
                print("Error, duplicate")
            else:
                writeToDB(writestring.encode('utf-8', 'ignore'))

config = ConfigParser.ConfigParser()
config.read(homedir + "cfg.cfg")
USER_AGENT = 'Image downloader by /u/yorickr'
REDDIT_ID = 'Moe-bot'
REDDIT_PASS = decrypt(config.get('Email', 'password'))
reddit = praw.Reddit(USER_AGENT)
print "logging in"
reddit.login(REDDIT_ID, REDDIT_PASS)
print "logged in"

def main():
    init()
    loadDB()
    sendEveryDay()
    try:
        while True:
            fetchAndWriteToDB()
            time.sleep(60)
    except KeyboardInterrupt:
        print("Woooosh")


main()
