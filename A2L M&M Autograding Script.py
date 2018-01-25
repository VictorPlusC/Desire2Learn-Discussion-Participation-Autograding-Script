"""
Avenue to Learn Discussion Participation Autograder
Last edited: January 23, 2018
Version: 1.0
"""

import csv

def script(filename: "File name to open (not including .txt extension"):
    
    doc = open(filename+".txt", 'r')
    lines = doc.readlines()
    doc.close()
    names = set()
    incompleteNames = []

    #appends line with suffix of -posted... + .json information
    for i in lines:
        if "posted" in i:
            temp = []
            j = 0
            while j < len(i):
                j+= 1
                if i[j] == ">":
                    j+=1
                    break
            while j < len(i):
                temp.append(i[j])
                j+= 1
            incompleteNames.append("".join(temp))
    
    #removing the suffix of -posted... + .json information
    for name in incompleteNames:
        split = name.split(" ")
        temp = []
        for element in split:
            if element != "posted":
                temp.append(element)
                temp.append(" ")
            else:
                tempName = "".join(temp)
                names.add(tempName[0:len(tempName)-1])
                break
    return names

def processCSV(toReadCSV, toWriteCSV, sourceCode):
    names = script(sourceCode)
    with open(toReadCSV+'.csv', newline='') as toRead:
        with open(toWriteCSV+'.csv', 'w', newline = '') as toWrite:
            reader = csv.reader(toRead)
            writer = csv.writer(toWrite)
            newContents = []
            i = 0
            for row in reader:
                if row[4] == "":
                    name = row[2]+" "+row[1]
                    if name in names:
                        print(name+ " | Assigned grade = 0.5")
                        row[4] = 0.5
                    else:
                        print(name+ " | Assigned grade = 0")
                        row[4] = 0
                    newContents.append(row)
                elif i == 0:
                    i = 1
                    newContents.append(row)
                    
            writer.writerows(newContents)
            print('\nNew CSV created; grading complete!')
