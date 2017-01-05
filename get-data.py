#!/usr/bin/env python

import cgi, cgitb
import sqlite3
import sys

form = cgi.FieldStorage()


#get data from fields
if form.getvalue('firstName') and form.getvalue('lastName') and form.getvalue('course') and form.getvalue('workType') and form.getvalue('enterGrades'):
    firstName = form.getvalue('firstName')
    lastName = form.getvalue('lastName')
    course = form.getvalue('course')
    workType = form.getvalue('workType')
    mark = form.getvalue('enterGrades')

# open index.html to load form             
print "Content-type: text/html\r\n\r\n"
fr = open('index.html', 'r')
html_doc = fr.read()
print html_doc

#initialize 
letterGrade = 0

#convert list of grades to a letter: 1=A, 2=B, 3=C, 4=D, 5=C
def getLetterGrade (mark):
    grade = 0
    # sum of entered grades divided to find percentage
    for i in mark.split(','):
        n = int(len(mark.split()))
        i = float(i)
        grade += i/n

    #convert percentage stored in 'grade' to numerical reference of letter grade     
    if grade >= 80: 
         letterGrade = 1
    elif grade >= 70: 
        letterGrade = 2
    elif grade >= 60: 
        letterGrade = 3
    elif grade >= 50: 
        letterGrade = 4
    else:  
        letterGrade = 5
    return letterGrade
# convert list of grades to letter and assign the variable
letterResult = getLetterGrade(mark)
    
try:
    con = sqlite3.connect('student-grade.db')
    cur = con.cursor()
    cur.execute('INSERT INTO Student VALUES(NULL, ?, ?, ?, ?, ?)', (firstName, lastName, course, workType, letterResult))
    con.commit()
    
except sqlite3.Error, e:
    print "Error %s:" % e.args[0]
    con.rollback()
    
finally:
    if con: con.close()
    
            
