from tkinter import *
import sqlite3
import os
import addStudent
import addFaculty
import train
import captureClassImage

class Select_Section:
	def __init__(self,first):
		self.first=first
		self.first.title("Smart Attendance")
		self.first.state("zoomed")
		self.Heading=Label(first,text="SMART ATTENDANCE",fg="Green",font =100,bg="white")
		self.Heading.config(font=("Courier", 70))
		self.Heading.place(x=200,y=10)
		self.Admin_Button=Button(first,text="Admin Login",bg="Green",font = (30),width=30,fg="white",command=self.admin)
		self.Admin_Button.place(x=450,y=290)
		self.Faculty_Button=Button(first,text="Faculty Login",bg="Green",font = (30),width=30,fg="white",command=self.Faculty)
		self.Faculty_Button.place(x=450,y=340)
	def admin(self):
		self.Admin_login_window = Toplevel(self.first)
		obj_A = Admin_Login(self.Admin_login_window)
	def Faculty(self):
		self.Faculty_login_window = Toplevel(self.first)
		obj_F = Faculty_Login(self.Faculty_login_window)
class Admin_Login:
	def __init__(self,Admin):
		self.Admin=Admin
		self.Admin.title("Smart Attendance")
		self.Admin.state("zoomed")
		self.Heading=Label(self.Admin,text="SMART ATTENDANCE",fg="Green",font =100,bg="white")
		self.Heading.config(font=("Courier", 70))
		self.Heading.place(x=200,y=10)
		self.User_ID=Label(self.Admin,text="User ID: ",font=(20),bg="white",fg="black")
		self.User_ID.place(x=350,y=250)
		self.User_ID_entry=Entry(self.Admin,font=(20))
		self.User_ID_entry.place(x=500,y=250)
		self.Password=Label(self.Admin,text="Password:",font=(20),bg="white",fg="black")
		self.Password.place(x=350,y=300)
		self.Password_entry=Entry(self.Admin,font=(20),show="*")
		self.Password_entry.place(x=500,y=300)
		self.Login_Button=Button(self.Admin,text="Login",bg="Green",font = (30),width=35,fg="white",command=self.Login_Validate)
		self.Login_Button.place(x=350,y=350)
	def Login_Validate(self):
		if(self.User_ID_entry.get()!="admin" or self.Password_entry.get()!="password"):
			self.Password_Incorrect=Label(self.Admin,text="Password Incorrect",font=(20),bg="white",fg="red")
			self.Password_Incorrect.place(x=750,y=300)
		else:
			try:
				self.Password_Incorrect.destroy()
			except:
				pass
			self.Add_Train()
	def Add_Train(self):
		self.AddStudent_Train = Toplevel(self.Admin)
		self.AddStudent_Train.state("zoomed")
		self.Heading=Label(self.AddStudent_Train,text="SMART ATTENDANCE",fg="Green",font =100,bg="white")
		self.Heading.config(font=("Courier", 70))
		self.Heading.place(x=200,y=10)
		self.Add_Student_Button=Button(self.AddStudent_Train,text="Add Student",bg="Green",font = (30),width=30,fg="white",command=self.AddStudent)
		self.Add_Student_Button.place(x=450,y=290)
		self.Add_Faculty_Button=Button(self.AddStudent_Train,text="Add Faculty",bg="Green",font = (30),width=30,fg="white",command=self.AddFaculty)
		self.Add_Faculty_Button.place(x=450,y=340)
		self.Train_Model_Button=Button(self.AddStudent_Train,text="Train Model",bg="Green",font = (30),width=30,fg="white",command=self.Train_model)
		self.Train_Model_Button.place(x=450,y=390)
	def AddStudent(self):
		self.Add = Toplevel(self.Admin)
		self.Add.state("zoomed")
		self.Heading=Label(self.Add,text="SMART ATTENDANCE",fg="Green",font =100,bg="white")
		self.Heading.config(font=("Courier", 70))
		self.Heading.place(x=200,y=10)
		self.Student_Name=Label(self.Add,text="Student Name:",font=(20),bg="white",fg="black")
		self.Student_Name.place(x=350,y=250)
		self.Student_Name_entry=Entry(self.Add,font=(20))
		self.Student_Name_entry.place(x=500,y=250)
		self.Section=Label(self.Add,text="Section:",fg="black",font = (30),bg="white")
		self.Section.place(x=350,y=300)
		self.choices = ["Select Section",'A','B','C','D','E','F','G','H','I']
		self.Var = StringVar(self.Add)
		self.Var.set('Select Section')
		self.Popup_Menu=OptionMenu(self.Add,self.Var ,*self.choices)
		self.Popup_Menu.place(x=500,y=300,width=150)
		self.University_Roll=Label(self.Add,text="University Roll:",font=(20),bg="white",fg="black")
		self.University_Roll.place(x=350,y=350)
		self.University_Roll_entry=Entry(self.Add,font=(20))
		self.University_Roll_entry.place(x=500,y=350)
		self.Section_Roll_NO=Label(self.Add,text="Section Roll No:",font=(20),bg="white",fg="black")
		self.Section_Roll_NO.place(x=350,y=400)
		self.Section_Roll_NO_entry=Entry(self.Add,font=(20))
		self.Section_Roll_NO_entry.place(x=500,y=400)
		self.Take_Image=Button(self.Add,text="Take Image",bg="Green",font = (30),width=35,fg="white",command=self.Validate)
		self.Take_Image.place(x=350,y=450)
		#self.Register=Button(self.Add,text="Register",bg="Green",font = (30),width=35,fg="white",command=self.Validate)
		#self.Register.place(x=350,y=500)
	def Validate(self):
		try:
			self.Incorrect.destroy()
		except:
			pass
		flag=1
		for i in self.Student_Name_entry.get():
			if((i>='A' and i<='Z') or (i>='a' and i<='z') or i==" "):
				flag=1
			else:
				flag=0
				self.Incorrect=Label(self.Add,text="Incorrect Student Name",font=(20),bg="white",fg="red")
				self.Incorrect.place(x=710,y=250)
				break
		if(len(self.Student_Name_entry.get())==0):
			flag=0
			self.Incorrect=Label(self.Add,text="Enter Student Name",font=(20),bg="white",fg="red")
			self.Incorrect.place(x=710,y=250)
		elif(self.Var.get()=="Select Section"):
			flag=0
			self.Incorrect=Label(self.Add,text="Select Section",font=(20),bg="white",fg="red")
			self.Incorrect.place(x=710,y=300)
		elif(len(self.University_Roll_entry.get())!=9):
			flag=0
			self.Incorrect=Label(self.Add,text="Incorrect University Roll Number",font=(20),bg="white",fg="red")
			self.Incorrect.place(x=710,y=350)
		elif(len(self.Section_Roll_NO_entry.get())!=2):
			flag=0
			self.Incorrect=Label(self.Add,text="Incorrect Section Roll Number",font=(20),bg="white",fg="red")
			self.Incorrect.place(x=710,y=400)
		if(flag==1):
			try:
				self.Incorrect.destroy()
			except:
				pass
			message = addStudent.takeimage(self.Var.get(), int(self.University_Roll_entry.get()))
			self.Register=Button(self.Add,text="Register",bg="Green",font = (30),width=35,fg="white",command=self.AddToDatabase)
			self.Register.place(x=350,y=500)
			self.Message = Label(self.Add, text = message, font = (20), bg = "white", fg="red")
			self.Message.place(x=350, y=550)

	def AddToDatabase(self):
                self.Message.destroy()
                message = addStudent.addstudent(self.Student_Name_entry.get(), int(self.University_Roll_entry.get()), int(self.Section_Roll_NO_entry.get()), self.Var.get())
                self.Message = Label(self.Add, text = message, font = (20), bg = "white", fg="red")
                self.Message.place(x=350, y=550)
	def AddFaculty(self):
		self.Add_Faculty = Toplevel(self.Admin)
		self.Add_Faculty.state("zoomed")
		self.Heading=Label(self.Add_Faculty,text="SMART ATTENDANCE",fg="Green",font =100,bg="white")
		self.Heading.config(font=("Courier", 70))
		self.Heading.place(x=200,y=10)
		self.Faculty_Name=Label(self.Add_Faculty,text="Faculty Name:",font=(20),bg="white",fg="black")
		self.Faculty_Name.place(x=350,y=250)
		self.Faculty_Name_entry=Entry(self.Add_Faculty,font=(20))
		self.Faculty_Name_entry.place(x=520,y=250)
		self.Faculty_ID=Label(self.Add_Faculty,text="Faculty ID:",font=(20),bg="white",fg="black")
		self.Faculty_ID.place(x=350,y=300)
		self.Faculty_ID_entry=Entry(self.Add_Faculty,font=(20))
		self.Faculty_ID_entry.place(x=520,y=300)
		self.New_Password=Label(self.Add_Faculty,text="New Password:",font=(20),bg="white",fg="black")
		self.New_Password.place(x=350,y=350)
		self.New_Password_entry=Entry(self.Add_Faculty,font=(20), show='*')
		self.New_Password_entry.place(x=520,y=350)
		self.Confirm_Password=Label(self.Add_Faculty,text="Confirm Password:",font=(20),bg="white",fg="black")
		self.Confirm_Password.place(x=350,y=400)
		self.Confirm_Password_entry=Entry(self.Add_Faculty,font=(20), show='*')
		self.Confirm_Password_entry.place(x=520,y=400)
		self.Register=Button(self.Add_Faculty,text="Register",bg="Green",font = (30),width=35,fg="white",command=self.FacultyValidate)
		self.Register.place(x=350,y=450)
	def FacultyValidate(self):
		try:
			self.Incorrect.destroy()
		except:
			pass
		flag=1
		for i in self.Faculty_Name_entry.get():
			if((i>='A' and i<="Z") or (i>='a' and i<="z") or i==" "):
				flag=1
			else:
				flag=0
				self.Incorrect=Label(self.Add_Faculty,text="Incorrect Faculty Name",font=(20),bg="white",fg="red")
				self.Incorrect.place(x=720,y=250)
				break
		if(len(self.Faculty_Name_entry.get())==0):
			flag=0
			self.Incorrect=Label(self.Add_Faculty,text="Enter Faculty Name",font=(20),bg="white",fg="red")
			self.Incorrect.place(x=720,y=250)
		elif(len(self.Faculty_ID_entry.get())<8):
			flag=0
			self.Incorrect=Label(self.Add_Faculty,text="Faculty Id should greater then 8",font=(20),bg="white",fg="red")
			self.Incorrect.place(x=720,y=300)
		elif(len(self.New_Password_entry.get())<8):
			flag=0
			self.Incorrect=Label(self.Add_Faculty,text="Password cantain minimum 8 characters",font=(20),bg="white",fg="red")
			self.Incorrect.place(x=720,y=350)
		elif(self.New_Password_entry.get()!=self.Confirm_Password_entry.get()):
			flag=0
			self.Incorrect=Label(self.Add_Faculty,text="Password not Matched",font=(20),bg="white",fg="red")
			self.Incorrect.place(x=720,y=400)
		if(flag==1):
			try:
				self.Incorrect.destroy()
			except:
				pass
		message = addFaculty.addfaulty(self.Faculty_ID_entry.get(),self.Faculty_Name_entry.get(),self.New_Password_entry.get())
		self.Message = Label(self.Add_Faculty, text = message, font = (20), bg = "white", fg="red")
		self.Message.place(x=350, y=500)
	def Train_model(self):
		self.Train = Toplevel(self.Admin)
		self.Train.state("zoomed")
		self.Heading=Label(self.Train,text="SMART ATTENDANCE",fg="Green",font =100,bg="white")
		self.Heading.config(font=("Courier", 70))
		self.Heading.place(x=200,y=10)
		self.Section=Label(self.Train,text="Section:",fg="black",font = (30),bg="white")
		self.Section.place(x=350,y=300)
		self.choices = ["Select Section",'A','B','C','D','E','F','G','H','I']
		self.Var = StringVar(self.Train)
		self.Var.set('Select Section')
		self.Popup_Menu=OptionMenu(self.Train,self.Var ,*self.choices)
		self.Popup_Menu.place(x=500,y=300,width=150)
		self.Train_button=Button(self.Train,text="Train Model",bg="Green",font = (30),width=35,fg="white",command=self.section_Validate)
		self.Train_button.place(x=350,y=450)
	def section_Validate(self):
		if(self.Var.get()=="Select Section"):
			self.Incorrect=Label(self.Train,text="Select Section",font=(20),bg="white",fg="red")
			self.Incorrect.place(x=710,y=300)
		else:
			try:
				self.Incorrect.destroy()
			except:
				pass

		message = train.trainmodel(self.Var.get())
		self.Message = Label(self.Train, text = message, font = (20), bg = "white", fg="red")
		self.Message.place(x=350, y=500)

class Faculty_Login:
	def __init__(self,Faculty):
		self.Faculty=Faculty
		self.Faculty.title("Smart Attendance")
		self.Faculty.state("zoomed")
		self.Heading=Label(self.Faculty,text="SMART ATTENDANCE",fg="Green",font =100,bg="white")
		self.Heading.config(font=("Courier", 70))
		self.Heading.place(x=200,y=10)
		self.User_ID=Label(self.Faculty,text="User ID: ",font=(20),bg="white",fg="black")
		self.User_ID.place(x=350,y=250)
		self.User_ID_entry=Entry(self.Faculty,font=(20))
		self.User_ID_entry.place(x=500,y=250)
		self.Password=Label(self.Faculty,text="Password:",font=(20),bg="white",fg="black")
		self.Password.place(x=350,y=300)
		self.Password_entry=Entry(self.Faculty,font=(20),show="*")
		self.Password_entry.place(x=500,y=300)
		self.Login_Button=Button(self.Faculty,text="Login",bg="Green",font = (30),width=35,fg="white",command=self.Login_Validate)
		self.Login_Button.place(x=350,y=350)
	def Login_Validate(self):
                try:
                        connection = sqlite3.connect('data.db')
                        cursor = connection.cursor()
                        cursor.execute('SELECT Password from faculty where Faculty_Id="{}"'.format(self.User_ID_entry.get()))
                        data = cursor.fetchone()
                        if(self.Password_entry.get()!= data[0]):
                                try:
                                        self.ID_Incorrect.destroy()
                                except:
                                        pass
                                self.Password_Incorrect=Label(self.Faculty,text="Password Incorrect",font=(20),bg="white",fg="red")
                                self.Password_Incorrect.place(x=750,y=300)
                        else:
                                try:
                                        self.ClassImage_AttendanceSheet()
                                        self.Password_Incorrect.destroy()
                                except:
                                        pass
                except:
                        try:
                                self.Password_Incorrect.destroy()
                        except:
                                pass
                        self.ID_Incorrect=Label(self.Faculty,text="Faculty Id Incorrect",font=(20),bg="white",fg="red")
                        self.ID_Incorrect.place(x=750,y=250)
	def ClassImage_AttendanceSheet(self):
		self.Attendance = Toplevel(self.Faculty)
		self.Attendance.state("zoomed")
		self.Heading=Label(self.Attendance,text="SMART ATTENDANCE",fg="Green",font =100,bg="white")
		self.Heading.config(font=("Courier", 70))
		self.Heading.place(x=200,y=10)
		self.Section=Label(self.Attendance,text="Section:",fg="black",font = (30),bg="white")
		self.Section.place(x=350,y=300)
		self.choices = ["Select Section",'A','B','C','D','E','F','G','H','I']
		self.Var = StringVar(self.Attendance)
		self.Var.set('Select Section')
		self.Popup_Menu=OptionMenu(self.Attendance,self.Var ,*self.choices)
		self.Popup_Menu.place(x=500,y=300,width=150)
		self.Class_Image_Button=Button(self.Attendance,text="Class Image",bg="Green",font = (30),width=35,fg="white",command=self.section_Validate)
		self.Class_Image_Button.place(x=350,y=450)
		self.Attendance_sheet_Button=Button(self.Attendance,text="Attendance Sheet",bg="Green",font = (30),width=35,fg="white",command=self.open_AttendanceSheet)
		self.Attendance_sheet_Button.place(x=350,y=500)

	def open_AttendanceSheet(self):
                path = os.getcwd()
                os.startfile("{}\\Attendance Sheet\\attendance.xls".format(path))
                
	def section_Validate(self):
		if(self.Var.get()=="Select Section"):
			self.Incorrect=Label(self.Attendance,text="Select Section",font=(20),bg="white",fg="red")
			self.Incorrect.place(x=710,y=300)
		else:
                        try:
                                captureClassImage.captureimage(self.Var.get())
                                self.Incorrect.destroy()
                        except:
                                pass

Tkinter_object=Tk()
First_Page=Select_Section(Tkinter_object)
Tkinter_object.mainloop()
