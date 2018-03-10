"""
Avenue to Learn Discussion Participation Autograder
Last edited: January 26, 2018
Version: 1.2
"""

#Before running:
#1) Retrieve .csv from Avenue gradebook":
"""
When exporting .csv from Avenue:
1) Under Key Field, select only Org Defined ID
2) Under Grade Values, select only Points grade
3) Under User Details, select only Last Name and First Name
4) Uncheck all graded items with the exception of the item being graded
5) Export
"""
#2) Retrieve all .html source code from discussion pages
#   and copy it all into a single text file

#3) Make sure both files are in the same directory as the script. You may now run it.

#Example usage:

#gradebook
#newgradebook
#source

"""
The participants() function takes the input file holding all the Avenue to Learn
discussion page source.html code and returns a set containing the names of all
students that commented in the discussion.

It is recommended that page sources for all pages of possible discussion are
included within the same .txt file in order to include every student. Duplicate
posts from the same student are not taken into consideration.
"""
def participants(filename: "File name to open (not including .txt extension"):
    
    doc = open(filename+".txt", 'r')
    lines = doc.readlines()
    doc.close()
    
    names = set()
    incompleteNames = []
    
    #appends line with suffix of -posted... + .json information
    for line in lines:
        if "posted" in line:
            temp = []
            index = 0
            while index < len(line):
                index+= 1
                if line[index] == ">":
                    index+=1
                    break
            while index < len(line):
                temp.append(line[index])
                index+= 1
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

"""
The processCSV() function takes in three arguments:
1) name of the .csv file to read from
2) name of the .csv file to write to (can overwrite, or create new file)
3) name of text file holding all discussion page .html source codes

Process is as follows:
1) Retrieves set of student names from the participants function
2) Retrieve student name per line in the gradebook
3) Looks up student name in the set of student names
4) Assigns a student grade of 0.5 (CHANGE ACCORDING TO GRADE BEING ASSIGNED!) or
   0 if a grade does not currently exist for the student, depending on whether
   their name was in the set or not
5) Stores student grade in a temporary array that is identical to the original
   .csv file to be eventually all be copied at the same time to the file to
   write to
6) Writes temporary array to a .csv file with the specified second input name
"""
import csv
def processCSV(toReadCSV: "CSV file to read",
               toWriteCSV: "Name of CSV file being written to",
               sourceCode: "name of .txt with all .html source codes"):
    names = participants(sourceCode)
    with open(toReadCSV+'.csv', newline='') as toRead:
        with open(toWriteCSV+'.csv', 'w', newline = '') as toWrite:
            reader = csv.reader(toRead)
            writer = csv.writer(toWrite)
            newContents = []
            i = 0
            for row in reader:
                if row[3] == "":
                    name = row[2]+" "+row[1]
                    if name in names:
                        print(name+ " | Assigned grade = 0.5")
## NOTE:
#  Please change the below value that row[3] is being assigned to in the case
#  that the discussion participation grade is not 0.5/0.5! Change to the assignment
#  value according to the grade being used!
                        row[3] = 0.5
                    else:
                        print(name+ " | Assigned grade = 0")
                        row[3] = 0
                    newContents.append(row)
                elif i == 0:
                    i = 1
                    newContents.append(row)
                else:
                    name = row[2]+" "+row[1]
                    print(name+ "'s grade was unchanged! Current grade: "+row[3])
                    
            writer.writerows(newContents)
            z = csv.reader(reader, delimiter='\t')
            z = csv.reader(writer, delimiter='\t')
            print('\nNew CSV created; grading complete!')

def main():
    print("Note: Please exempt all file extensions when entering file names.")
    print("Name of .csv file to read from:")
    readCSV = input()
    print("Name of .csv file to write to:")
    writeCSV = input()
    print("Name of source code text file:")
    sourceTxt = input()
    processCSV(readCSV, writeCSV, sourceTxt)
    
main()
