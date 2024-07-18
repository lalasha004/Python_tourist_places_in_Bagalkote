from playsound import playsound
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
root=tk.Tk()
root.configure(bg="#bbffbb")

img1= Image.open("kudala.jpg")
img2= Image.open("kudal2.jpg")
img3= Image.open("kudal3.jpg")
img4= Image.open("kudal4.jpg")
rm1 = img1.resize((350, 250))
img11 = ImageTk.PhotoImage(rm1)
l1 =Label(image=img11)
l1.image = img1
l1.pack(padx=50,pady=20)

rm2 = img2.resize((350, 250))
img12 = ImageTk.PhotoImage(rm2)
l1 =Label(image=img12)
l1.image = img2

rm3 = img3.resize((350, 250))
img13 = ImageTk.PhotoImage(rm3)
l1 =Label(image=img13)
l1.image = img3

rm4 = img4.resize((350, 250))
img14 = ImageTk.PhotoImage(rm4)
l1 =Label(image=img14)
l1.image = img4



ls=[img11,img12,img13,img14]



def forward(no):
    global l
    global bf 
    global bb
    l.place_forget()
    l=Label(image=ls[no-1])
    b2=Button(root,text=">>",command=lambda: forward(no+1))
    b1=Button(root,text="<<",command=lambda: back(no-1))
    l.place(x=590,y=20)
    b1.place(x=550,y=150)
    b2.place(x=955,y=150)
    l=Label(root,text="Kudalasangama",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
    l.place(x=593,y=270)
    if no==4:
        b2=Button(root,text=">>",state=DISABLED)
        b2.place(x=955,y=150)
    playsound("manjunatha.mp3")

def back(no):
    global l
    global bf 
    global bb
    l.place_forget()
    l=Label(image=ls[no-1])
    b2=Button(root,text=">>",command=lambda: forward(no+1))
    b1=Button(root,text="<<",command=lambda: back(no-1))
    l.place(x=590,y=20)
    b1.place(x=550,y=150)
    b2.place(x=955,y=150)
    l=Label(root,text="Kudalasangama",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
    l.place(x=593,y=270)
    if no==1:
        b1=Button(root,text="<<",state=DISABLED)
        b1.place(x=550,y=150)
b1=Button(root,text="<<",command=back, state=DISABLED)
b2=Button(root,text=">>",command=lambda: forward(2))
b1.place(x=550,y=150)
b2.place(x=955,y=150)
l=Label(root,text="Kudalasangama",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
l.place(x=593,y=270)
t=Text(root,width=130,height=5,font=("normal",20,),bg="#bbffbb")
des="""           Kudalasangama (sometimes spelled Kudala Sangama) is a significant pilgrimage site for Lingayats in India. It is around 
15 kilometres (9.3 miles) from the Almatti Dam in Karnataka’s Bagalkot district. The Krishna and Malaprabha Rivers meet here 
and run east to Srisaila (another pilgrimage site) in Andhra Pradesh. The Aikya Mantapa, or sacred Samdhi of Basavanna, the 
founder of the Lingayat branch  of Hindu  religion,  is here, as is Linga, which  is considered to be self-born (Swayambhu). The 
Kudala Sangama Development Board is in charge of upkeep and development.          """
t.insert(END, des)
t.place(x=5,y=420)
photo=tk.PhotoImage(file="ico.png")
root.wm_iconphoto(False,photo)
root.title("Kudala sangham")
root.geometry("1535x840")

root.mainloop()