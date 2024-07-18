from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import datetime
from subprocess import *
class interface:
    def __init__(self,root):
        self.f=Frame(width=1530,height=835,bg="sky blue")
        self.f.propagate(0)
        self.f.place(x=0,y=0)
        self.l=Label(self.f,text="WELCOME TO BAGALKOT DISTRICT",font=("new Time",20,"bold"),fg="dark red",bg="sky blue")
        self.l.place(x=15,y=30)
        self.b=Button(self.f,text="About..",width=9,height=2,font=("normal",9),fg="dark red",bg="sky blue",command=self.about)
        self.b.place(x=520,y=30)
        self.l1=Label(self.f,text=("7 Best Places to Visit in Bagalkot..!"),font=("Gabriola",55,"bold"),bg="sky blue")
        self.l1.place(x=15,y=59)
        self.img1 = Image.open("b.jpg") 
        self.rm1 = self.img1.resize((1000, 630))
        self.img11 = ImageTk.PhotoImage(self.rm1)
        self.l1 = Label(image=self.img11)
        self.l1.image = self.img1
        self.l1.place(x=15,y=180)
        self.img2 = Image.open("bagalkot.jpg")
        self.r2 = self.img2.resize((460, 380))
        self.img12 = ImageTk.PhotoImage(self.r2)
        self.l2 = Label(image=self.img12)
        self.l2.image = self.img2
        self.l2.place(x=1050,y=20)
        self.l3=Button(self.f,text=("Badami Caves"),font=("new times",15,"bold"),fg="purple",bg="sky blue",command=self.open_f11,width=20)
        self.l3.place(x=1165,y=420)
        self.l3=Button(self.f,text=("Aihole"),font=("new times",15,"bold"),fg="purple",bg="sky blue",command=self.open_f2,width=20)
        self.l3.place(x=1165,y=470)
        self.l4=Button(self.f,text=("Pattadakal"),font=("new times",15,"bold"),fg="purple",bg="sky blue",command=self.open_f3,width=20)
        self.l4.place(x=1165,y=520)
        self.l5=Button(self.f,text=("Mahakuta"),font=("new times",15,"bold"),fg="purple",bg="sky blue",command=self.open_f4,width=20)
        self.l5.place(x=1165,y=570)
        self.l6=Button(self.f,text=("Kudalasangama"),font=("new times",15,"bold"),fg="purple",bg="sky blue",command=self.open_f5,width=20)
        self.l6.place(x=1165,y=620)
        self.l7=Button(self.f,text=("Almatti"),font=("new times",15,"bold"),fg="purple",bg="sky blue",command=self.open_f6,width=20)
        self.l7.place(x=1165,y=670)
        self.l8=Button(self.f,text=("Banashankari temple"),font=("new times",15,"bold"),fg="purple",bg="sky blue",command=self.open_f7,width=20)
        self.l8.place(x=1165,y=720)
        self.l=Label(self.f,text="Have a Nice Day :) ",font=("Gabriola",37,"bold"),fg="dark red",bg="sky blue",width=28)
        self.l.place(x=1000,y=761)
    def about(self):
        self.f1=Frame(width=500,height=820,bg="#ccffff")
        self.f1.propagate(0)
        self.f1.place(x=1025,y=5)
        current_time=datetime.datetime.now()
        self.img3 = Image.open("bgk2.jpg")
        self.rm3 = self.img3.resize((250, 200))
        self.img13 = ImageTk.PhotoImage(self.rm3)
        self.l3 = Label(self.f1,image=self.img13)
        self.l3.image = self.img3
        self.l3.pack(padx=50,pady=20)
        self.ll=Label(self.f1,text=('Bagalkot'),font=("Gabriola",52,"bold"),fg="dark red",bg="#ccffff")
        self.ll.place(x=145,y=225)
        self.l9=Label(self.f1,text=(" \n Area: 49.06 km²\n\n Elevation: 537 m\n\n District: Bagalakote\n\n Weather: 23 °C\n\n Wind E at 8 km/h\n\n  Area code: 08354\n\n"),font=("new times",15,"bold"),fg="black",bg="#ccffff")
        self.l9.place(x=140,y=330)
        self.a=Label(self.f1,text=('Time: ',current_time),font=("new times",18,"bold"),fg="black",bg="#ccffff")
        self.a.place(x=60,y=650)
        self.c=Button(self.f1,text=("Back"),font=("normal",10),fg="black",bg="sky blue",command=self.back)
        self.c.place(x=240,y=720)
    def back(self):
        self.f1.place_forget() 
    def open_f11(self):
        call(["python","badami.py"]) 
    def open_f2(self):
        call(["python","aihole.py"]) 
    def open_f3(self):
        call(["python","pattadakallu.py"])
    def open_f4(self):
        call(["python","mahakuta.py"])  
    def open_f5(self):
        call(["python","Kudalasangama.py"]) 
    def open_f6(self):
        call(["python","alamatti.py"])
    def open_f7(self):
        call(["python","banashankari.py"])             
        
root=tk.Tk()
m=interface(root)
root.title("Bagalkot World")
root.geometry("1532x840")
photo=tk.PhotoImage(file="ico.png")
root.wm_iconphoto(False,photo)
root.mainloop()