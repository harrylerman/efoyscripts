# -*- coding: utf-8 -*-
"""
Created on Sat May  7 12:37:17 2022

@author: larry
"""
from os import listdir
from os.path import isfile, join, exists
import re
import csv

def getfiles(filepath,startdate,stopdate):
    '''
    Returns a list of efoy logfiles between startdate and stopdate
    Argument filepath is the directory of the efoy logfiles (should only be 
    efoy logfiles in filename format 'yyyymmdd.txt' in that directory or this 
    script will break)
    Arguments startdate, stopdate are in yyyymmdd format
    '''
    files = []
    filenames = [f for f in listdir(filepath) if isfile(join(filepath, f))]
    for file in filenames:
        date = int(file.rsplit(".",1)[0]) #get just the filename without '.txt', this should be the date
        if date >= startdate and date <= stopdate:
            files.append(file) #get files between startdate and stopdate
    return files

def splitfile2csv(file,outfile):
    '''
    Goes through an efoy logfile line by line
    Splits each line and outputs to a csv file
    Arguments are the full path of the efoy logfile to read, and the full path 
    output csv file to write to.
    '''
    logfile = open(file, 'r')
    csvfile = open(outfile, 'a+')
    writer = csv.writer(csvfile) #using python csv module for simplicity
    for line in logfile:
        out = []
        split = line.split(', ') #start off splitting the line by commas and spaces
        dateinfo = split.pop(0) #the first few elements need some more splitting because of how the logfile is structured
        dateinfo = dateinfo.split(' ')
        split[:0] = dateinfo
        for item in split:
            out.append(re.sub(r'[^A-Za-z0-9 .:-]', '', item)) #strip out unwanted characters
        writer.writerow(out) #use the csv python module to write to the csv file  
    logfile.close() #done reading logfile
    csvfile.close() #done writing as well
    return True

if __name__ == "__main__":
    '''
    This script reads in all efoy logfiles in the 'filepath' directory between
    'startdate' and 'stopdate', and outputs a csv file named
    startdate_stopdate.csv in the outpath directory (this directory probably
    has to be created)
    '''
    startdate = 20220504
    stopdate = 20220508
    filepath = "/home/pi/logs/efoy/"
    outpath = "/home/pi/logs/efoy_csv/"

    outname = str(startdate)+"_"+str(stopdate)+".csv"
    outfile = outpath+outname
    
    if exists(outfile): #give a warning if the output file already exists
        print("output file ", outfile, " already exists and will be appended to, press enter to continue or ctrl-c to interrupt")
        input()
    
    files = getfiles(filepath, startdate, stopdate)
    
    for file in files:
        print("reading: ", file)
        fullpath = filepath+file
        splitfile2csv(fullpath, outfile)
    
        
        
            
