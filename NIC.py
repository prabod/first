from Tkinter import *	# Import all definitions from tkinter
from datetime import *
import tkMessageBox

class DOBfinder:
	def __init__(self):
			window = Tk() #Create a Window
			window.title("Date of Birth Finder") #Set a Title
			
			menubar = Menu( window) #Create a Menu
			window.config( menu = menubar)
			
			filemenu = Menu( menubar, tearoff = 0) #File dropdown
			menubar.add_cascade( label = "File", menu = filemenu)
			filemenu.add_command( label = "Quit", command = window.quit) #child item Quit
			
			helpmenu = Menu( menubar, tearoff = 0) #Help dropdown
			menubar.add_cascade( label = "Help", menu = helpmenu)
			helpmenu.add_command( label = "About", command =self.info) #child item About
			
			NICFrame = Frame(window) #Create a Frame to NIC 
			NICFrame.pack()
			NICLable1 = Label(NICFrame, text = "Enter Your NIC Number To Find Your DOB")
			NICLable2 = Label(NICFrame, text = "Enter Your NIC Number:") #Create a Label to NIC
			self.NIC = StringVar()
			
			NICEnter = Entry(NICFrame, textvariable = self.NIC, ) #Create an Entry for NIC
			NICButton = Button(NICFrame, text = "Find", command =self.FindDate) #Create a Button for NIC
			
			
			NICLable1.grid(row = 1, column = 1, columnspan = 3)
			NICLable2.grid(row = 2, column = 1)
			NICEnter.grid(row = 2, column = 2)
			NICButton.grid(row = 2, column = 3)
			
			frame1 = Frame(window) #Create a Frame to NIC 
			frame1.pack()
			
			#labels to display result
			self.lable1 = Label(frame1)
			self.lable2 = Label(frame1) 
			
			self.lable3 = Label(frame1)
			self.lable4 = Label(frame1) 
			
			frame2 = Frame(window) #Create a Frame to NIC 
			frame2.pack()
			
			self.lable5 = Label(frame2)
			self.lable6 = Label(frame2)
			self.lable7 = Label(frame2)
			self.lable8 = Label(frame2)
			self.lable9 = Label(frame2)
	
			
			self.lable1.grid(row = 1, column = 1)
			self.lable2.grid(row = 1, column = 2)
			self.lable3.grid(row = 2, column = 1)
			self.lable4.grid(row = 2, column = 2)
			
			self.lable5.grid(row = 1, column = 1)
			self.lable6.grid(row = 1, column = 2)
			self.lable7.grid(row = 1, column = 3)
			self.lable8.grid(row = 1, column = 4)
			self.lable9.grid(row = 1, column = 5)
			
			
			window.mainloop()
	
	# function to find the DoB	
	def FindDate(self):
			Nic=self.NIC.get()
			year=eval("19" + Nic[0:2])
			if Nic[2] == '0':
				i=3
			else:
				i=2
			yday=eval(Nic[i:5])
			
			if yday<500:
				mf = "Male"
			else:
				mf = "Female"
				yday-=500
				
			if eval(Nic[0:2])%4 == 0:
				temp = date.fromordinal(date(year, 1, 1).toordinal()+yday-1)
			else:
				yday-=1
				temp = date.fromordinal(date(year, 1, 1).toordinal()+yday-1)
			
			DOB = temp.strftime("%A %d. %B %Y")
			today = date.today()
			age = today - temp
			years = age.days // 365
			
			my_birthday = date(today.year, temp.month, temp.day)
	 		if my_birthday < today:
	   			my_birthday = my_birthday.replace(year=today.year + 1)
			time_to_birthday = abs(my_birthday - today)
			days = 365-time_to_birthday.days
			
			if time_to_birthday.days<20:
				years-=1
			
			self.lable1["text"] = "Your Birthday is"
			self.lable2["text"] = DOB

			self.lable3["text"] = "Your Gender is"
			self.lable4["text"] = mf
			
			self.lable5["text"] = "Your Age is"
			self.lable6["text"] = str(years)
			self.lable7["text"] = "Years And"
			self.lable8["text"] = str(days)
			self.lable9["text"] = "Days"
			
			
	def info(self):
			tkMessageBox.showinfo("About", "This Application is Developed by \n Prabod Rathnayaka\n")
DOBfinder()
		
		
