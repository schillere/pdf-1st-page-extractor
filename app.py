# -*- coding: utf-8 -*-
"""
2020-08-27

Extract first page from all PDF's in input directory
Place results in the output directory
Move the files from input to archive

ES

0.2 commented out debugging statements
0.1 first working
"""

#relative to current directory
strInputDirectory = r".\input"
strOutputDirectory = r".\output"
strArchiveDirectory = r".\archive"


#for running JAR file
import subprocess


#for creating archive folder
from datetime import date
today = date.today()
strDate = today.strftime("%Y%m%d") #YYYYMMDD format
#print("strDate =", strDate) #debugging


#for file handling
import os


strPathArchive = os.path.join(strArchiveDirectory, strDate) 
#print('strPathArchive =' + strPathArchive) #debugging    



#list files in a directory with a certain extension
for file in os.listdir(strInputDirectory):
    if file.endswith(".pdf"):
        
        #filepath of PDF file in input directory
        strFilepathIn = os.path.join(strInputDirectory, file)
        #print('strFilepathIn =' + strFilepathIn) #debugging

        #filepath of PDF file in output directory
        strFilepathOut = os.path.join(strOutputDirectory, file)
        #print('strFilepathOut =' + strFilepathOut) #debugging

        #filepath for PDF file in archive directory
        strFilepathArchive = os.path.join(strPathArchive, file)
        #print('strFilepathArchive =' + strFilepathArchive) #debugging     


        #PDFBox command string: "java -jar pdfbox-app-1.8.13.jar PDFSplit -endPage 1 ./test.pdf"
        strOutput = subprocess.run(["java", "-jar", "pdfbox-app-1.8.13.jar", \
                                   'PDFSplit', '-endPage', '1', \
                                   '-outputPrefix', \
                                   strFilepathOut, \
                                   strFilepathIn], \
                                   capture_output=True,)
        #print(strOutput) #debugging
        #print(strOutput.stdout.decode()) #debugging
        #print(strOutput.stderr.decode()) #debugging
        
        
        #make directory if not already there
        if not os.path.exists(strPathArchive):
            os.makedirs(strPathArchive)        
        
        #move input file to archive
        os.replace(strFilepathIn, strFilepathArchive)
        