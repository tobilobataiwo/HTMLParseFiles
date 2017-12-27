import fileinput
import os
import re

#opens the file with the required header for each html file
openheader = open("20170222-130955-CST.html", "r", encoding="utf-8")

#creates list to append the lines of the header into 
headerlines = []

#creates list to append the employee's email address' into 
emails = []
headercount = 0 
count = 0
whilecount =0



#defines filename so that each file with be named after a number in an ascending action
filename = str(count) + ".html"

#places each line of the header file into the header list
for line in openheader:
        #checks to see if where the header ends
        if line[10:12] != "32":
                headerlines.append(line)
                headercount +=1
        #if the header is done it stops the loop
        else:
                break
                

#opens the html file with the employees' information
openhtml = open("20170222-130955-CST.html", "r", encoding="utf-8")

#skips through the header part of the file
for line in openhtml:
        while (whilecount < headercount):
                line = openhtml.readline()
                whilecount +=1
        #uses regex to find the employees' full email address and place into the email list
        match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
        for i in match:
                emails.append(i)
                
        #uses substring to find the "32" line indicating whether or not to create a new file 
        if line[10:12] == "32":
                
                #creates a new file with the count as the name
                f = open(filename,'w')
                print("New File Created")
                
                #writes the required header into the new html file
                for i in range(0, len(headerlines)):
                        f.write(str(headerlines[i]))
                        
                #writes the line containing "<p class="s32"> into the new html file"
                f.write("\n"+line)

                #checks line again to see if a new html page needs to begin 
                if line[10:12] == "32":

                        #increases count and names a new html page named after it
                        count += 1
                        filename = str(count) + ".html"
                        
        #if line[10:12] isn't "32" then it writes line to whatever html file is still open
        else:
                f.write(line)
                
for i in range (0, len(emails)):
        #closes file
        f.close()
        
        #sets variable for easy indexing of the full email address
        fullemail = (str(emails[i]))
        
        #takes the full email address and sets ulid to whatever is before the "@" symbol 
        ulid = (fullemail.rsplit('@', 1)[0])

        #set file to be renamed as the i since all files were previously named after the count(Ex: 12.html)
        oldfilename = str(i) + ".html"

        #sets newfilename as employees ulid
        newfilename = ulid + ".html"

        #renames the file from count or "i" to the ulid
        os.rename(oldfilename, newfilename)
print("done")
##        
