# Task No. 1
# Digital Clock										

from tkinter import *
from time import *

root = Tk()					#--> making the tkinter window
root.title("Digital Clock")			#--> title of the tkinter window
root.geometry("450x200+50+50")			#--> size(dimension) of the tkinter window	
root.configure(bg = "lightblue")		#--> background color of the tkinter window is set to be "lightblue"	
root.eval('tk::PlaceWindow . center') 		#--> It's used to Placing clock at the centre of the tkinter window



time_lab = Label(root,font=("Digital-7",50),fg="black", bg= "lightblue")	#--> font(Digital-7) is used for give a feel of an digital clock
time_lab.pack()

day_lab = Label(root,font=("Tw cen MT",25), fg = "black", bg = "lightblue")
day_lab.pack()

date_lab = Label(root,font=("times new roman",30),fg = "black",  bg = "lightblue")
date_lab.pack()


def update():

    time_str = strftime("%I:%M:%S %p")	#--> 1. %I:- Hour(12-hour clock)   2. %M:- Minutes   3. %S:- Seconds  4. %p:- checks the time and displays AM or PM
    time_lab.config(text=time_str)

    day_str = strftime("%A")		#--> %A:- weekday
    day_lab.config(text=day_str)

    date_str = strftime("%d/%m/%Y")	#--> 1. %d:- date  2. %m:- month  3. %Y:- year
    date_lab.config(text=date_str)

    root.after(1000,update)	# root.after() :- It delays the fuction like Sleep(). In this case, the time is delayed 1000 milliseconds i.e. 1 second which will give us appropriate time

update()		#--> To call the function 
root.mainloop()		#--> To display the window