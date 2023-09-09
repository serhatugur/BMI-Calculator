import numbers
import tkinter
from tkinter import *

import self

#Window
win= Tk()
win.title("BMI Calculator")
win.minsize(width=400, height=400)
win.maxsize(width=400, height=400)
bg = PhotoImage(file="bck.jpg")
label1 = Label(win, image = bg)
label1.place(x = 0, y = 0)
win.iconbitmap("calculator2.ico")

#label1
my_label = Label(text="Enter Your Weight(kg)",font =("Arial",12,"italic"))
my_label.config(bg="gray")
my_label.pack()
my_label.place(x= 120, y= 40,)

#entry1
my_entry = Entry(width= 20)
my_entry.pack()
my_entry.place(x= 140, y= 80)
my_entry.focus()
my_entry.config(bg="darkgray")


#label2
my_label2 = Label(text="Enter Your Height(cm)",font =("Arial",12,"italic"))
my_label2.config(bg="gray")
my_label2.pack()
my_label2.place(x=120, y=150)

#entry2
my_entry2 = Entry(width=20)
my_entry2.pack()
my_entry2.place(x=140, y=190 )
my_entry2.config(bg="darkgray")


def cal_sum():
    try:
        t1=int(my_entry.get())
        t2=int(my_entry2.get())
        bmi = t1 / (t2 / 100) ** 2
        bmi = round(bmi, 1)
        answer.config(text=bmi)
    except ValueError:
        answer.config(text="Please enter a valid number!")
    if bmi < 18.5:
        answer.config(text="You are underweight,BMI:" + str(bmi))
    if bmi >= 30:
        answer.config(text="You are obese,BMI:" + str(bmi))
    elif(bmi >=18.5) and (bmi <=24.9):
        answer.config(text="You are normal weight,BMI:" + str(bmi))
    elif(bmi >=25) and (bmi <=29.9):
        answer.config(text="You are overweight,BMI:" + str(bmi))







#answerlabel
answer = Label(win,)
answer.pack()
answer.place(x=80 , y= 295)
answer.config(width=35)
answer.config(bg="darkgray")


#button
my_button = Button(win,text="Calculate", command=cal_sum)
my_button.pack()
my_button.place(x=165 , y= 250 )
my_button.config(width=10)
my_button.config(bg="gray")









































win.mainloop()