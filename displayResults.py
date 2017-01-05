#!/usr/bin/env python

import cgi, cgitb
import sqlite3
import sys

print "Content-type: text/html\r\n\r\n"

con = sqlite3.connect('student-grade.db')
cur = con.cursor()

cur.execute('select student.fName, student.lName, course.courseName, workType.TypeName, mark.letter FROM student INNER JOIN course ON course.courseId = student.courseID INNER JOIN workType ON workType.workTypeId = student.workType INNER JOIN mark ON mark.markId = student.mark ORDER BY student.fName')
data = cur.fetchall()
                     
print '<!DOCTYPE html>'
print '<html lang="en">'
print '<head>'
print '<meta charset="UTF-8">'
print '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
print '<meta http-equiv="X-UA-Compatible" content="ie=edge">'
print '<link rel="stylesheet" href="./css/style.css">'
print '<title>Display Results of Student Grades</title>'
print '</head>'
print '<body>'
print '<main>'
print '<table id="results">'
print '<thead>'
print '<tr>'
print '<th>First Name</th>'
print '<th>Last Name</th>'
print '<th>Course Name</th>'
print '<th>Work Type</th>'
print '<th>Grade</th>'
print '</tr>'
print '</thead>'
print '<tbody>'
for row in data:
    print '<tr>'
    for i in range(0, len(row)): 
        print '<td>'+str(row[i])+'</td>'
    print '</tr>'
print '</tbody>'
print '</table>'
print '<a href="./get-data.py" class="button" id="returnlink">Add Another Student</a>'
print '</main>'
print '</body>'
print '</html>'

con.close()

    
    





