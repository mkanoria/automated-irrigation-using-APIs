from tkinter import *
from script import generate_value
from hardware_control import turned_on
import sys

def stop_fun():
    root.destroy()
    sys.exit()
#first screen
gate=0
def use_coor():#using coordinates, contains code that opens new window
    
    frame1=Frame(root)
    frame2=Frame(root)
    frame3=Frame(root)
    frame4=Frame(root)
    frame5=Frame(root)
    frame1.pack(side=TOP)
    frame2.pack(side=TOP)
    frame3.pack(side=BOTTOM)
    frame4.pack(side=BOTTOM)
    frame5.pack(side=BOTTOM)
    ment=StringVar()
    def get_data():
        mtext=ment.get()
        Label(frame5,text="Entered values are - " + mtext).pack(side=TOP)
        data = mtext.split(',')
        # data = generate_value(mtext)
        Label(frame5,text="Temperature is " + str(data["temp"]) + " F").pack(side=TOP)
        Label(frame5,text="Moisture is " + str(data["moisture"]) + " mm").pack(side=TOP)
        Label(frame5,text="Water required for these conditions is: " + str(data["WATER_REQUIRED"]) + " mm").pack(side=TOP)
        Label(frame5,text="Predicted Rain is: " + str(data["precip"]) + " mm").pack(side=TOP)
        wat = round(data["WATER_AFTER_PRECIP"], 2)
        Label(frame5,text="Required water after Rain " + wat + " mm").pack(side=TOP)
         
    #proper format- homebut1=Button(frame1,text="go home shelf 1-linearly",command=home1 ,bg="green",fg="blue")
    root.title("AUTOMATIC GARDEN IRRIGATION SYSTEM")
    lbl = Label(frame1, text="COORDINATES ",font=("Times New Roman", 14))
    homebut1=Button(frame2,text="START",command=get_data,bg="green",fg="white",width=20,height=2)
    homebut2=Button(frame2,text="STOP",command=stop_fun,bg="red",fg="white",width=20,height=2)
    mentry=Entry(frame1,textvariable=ment)
    lbl2 = Label(frame1, text="Enter location - ")
    helplf = LabelFrame(frame1, text=" Quick Help ")
    helplf.pack()
    lbl.pack(side=TOP)
    lbl2.pack(side=TOP)
    mentry.pack()
    homebut1.pack(side=LEFT,fill=BOTH)
    homebut2.pack(side=RIGHT,fill=BOTH)
               
    root.mainloop()

def use_add():  #using address, contains code that opens new window
    frame1=Frame(root)
    frame2=Frame(root)
    frame3=Frame(root)
    frame4=Frame(root)
    frame5=Frame(root)
    frame1.pack(side=TOP)
    frame2.pack(side=TOP)
    frame3.pack(side=BOTTOM)
    frame4.pack(side=BOTTOM)
    frame5.pack(side=BOTTOM)
    ment=StringVar()
    def get_data():
        mtext=ment.get()
        Label(frame5,text="Entered location - " + mtext).pack(side=TOP)
        data = generate_value(mtext)
        Label(frame5,text="Temperature is " + str(data["temp"]) + " F").pack(side=TOP)
        Label(frame5,text="Moisture is " + str(data["moisture"]) + " mm").pack(side=TOP)
        Label(frame5,text="Water required for these conditions is: " + str(data["WATER_REQUIRED"]) + " mm").pack(side=TOP)
        Label(frame5,text="Predicted Rain is: " + str(data["precip"]) + " mm").pack(side=TOP)
        fwat = round(data["WATER_AFTER_PRECIP"]+0.5)
        Label(frame5,text="Required water after Rain " + str(round(data["WATER_AFTER_PRECIP"], 2)) + " mm").pack(side=TOP)
        turned_on(fwat)
        
    #proper format- homebut1=Button(frame1,text="go home shelf 1-linearly",command=home1 ,bg="green",fg="blue")
    root.title("AUTOMATIC GARDEN IRRIGATION SYSTEM")
    lbl = Label(frame1, text="ADDRESS",font=("Times New Roman", 14))
    homebut1=Button(frame2,text="START",command=get_data,bg="green",fg="white",width=20,height=2)
    homebut2=Button(frame2,text="STOP",command=stop_fun,bg="red",fg="white",width=20,height=2)
    mentry=Entry(frame1,textvariable=ment)
    lbl2 = Label(frame1, text="Enter address - ")
    helplf = LabelFrame(frame1, text=" Quick Help ")
    helplf.pack()
    lbl.pack(side=TOP)
    lbl2.pack(side=TOP)
    mentry.pack()
    homebut1.pack(side=LEFT,fill=BOTH)
    homebut2.pack(side=RIGHT,fill=BOTH)
               
    root.mainloop()

root=Tk()
frame1=Frame(root)
frame1.pack(side=TOP)
root.title("AUTOMATIC IRRIGATION SYSTEM")
lbl = Label(frame1, text="AUTOMATIC IRRIGATION SYSTEM",font=("Times New Roman", 18))
coorbut=Button(frame1,text="Use Coordinates",command=use_coor,bg="green",fg="white",width=20,height=2)
addbut=Button(frame1,text="Use Address",command=use_add,bg="green",fg="white",width=20,height=2)


lbl.pack(side=TOP)

coorbut.pack(side=LEFT,fill=BOTH)
addbut.pack(side=RIGHT,fill=BOTH)

root.mainloop()