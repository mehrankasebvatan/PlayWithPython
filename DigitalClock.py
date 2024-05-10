from tkinter import *
import time

window = Tk()
window.title("Digital Clock")


def myTime():
    hour = time.strftime('%I')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    am_pm = time.strftime('%p')
    day = time.strftime("%A")
    zone = time.strftime("%Z")
    myLabel.config(text=f"{hour}:{minute}:{second} {am_pm}")
    myLabel2.config(text=f"{day} , {zone}")
    myLabel.after(1000, myTime)


myLabel = Label(window, text="", font=(
    'Arial', 50), fg='white')
myLabel.pack()
myLabel2 = Label(window, text="", font=(
    'Arial', 30), fg='white')
myLabel2.pack()

myTime()
window.mainloop()
