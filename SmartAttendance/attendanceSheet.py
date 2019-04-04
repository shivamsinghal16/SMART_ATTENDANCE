import os
import sqlite3
import xlwt
from xlwt import Workbook


def createAttendanceSheet(rollno):
    wb = Workbook()
    sheet1 = wb.add_sheet('sheet1')
    sheet = "attendance.xls"

    first_col = sheet1.col(0)
    second_col = sheet1.col(1)
    third_col = sheet1.col(2)
    first_col.width = 256 * 16
    second_col.width = 256 * 17
    third_col.width = 256 * 18

    style = xlwt.easyxf('font: bold 1; align: horiz center')
    style2 = xlwt.easyxf('align: horiz center')
    
    sheet1.write(0,0,"Section Roll No.",style)
    sheet1.write(0,1,"Student Name",style)
    sheet1.write(0,2,"University Roll No.",style)

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    for i in range(len(rollno)):
        cursor.execute('SELECT Section_RollNumber,Student_Name from students where Roll_Number={}'.format(rollno[i]))
        data = cursor.fetchone()
        sheet1.write(i+1,0,data[0],style2)
        sheet1.write(i+1,1,data[1],style2)
        sheet1.write(i+1,2,rollno[i],style2)

    file = os.listdir("Attendance Sheet")

    if sheet in file:
        os.remove("Attendance Sheet/attendance.xls")

    wb.save('Attendance Sheet/attendance.xls')

    print("Attendance Sheet Successfully Generated")

    connection.close()
