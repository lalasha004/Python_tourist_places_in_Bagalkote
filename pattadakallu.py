
from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.configure(bg="#bbffbb")
img1= Image.open("p2.jpg")
img2= Image.open("p1.jpeg")
img3= Image.open("p3.jpg")
img4= Image.open("p4.jpeg")
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
    l=Label(root,text="Pattadakallu",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
    l.place(x=630,y=280)
    if no==4:
        b2=Button(root,text=">>",state=DISABLED)
        b2.place(x=955,y=150)

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
    l=Label(root,text="Pattadakallu",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
    l.place(x=630,y=280)
    if no==1:
        b1=Button(root,text="<<",state=DISABLED)
        b1.place(x=550,y=150)
b1=Button(root,text="<<",command=back, state=DISABLED)
b2=Button(root,text=">>",command=lambda: forward(2))
b1.place(x=550,y=150)
b2.place(x=955,y=150)
l=Label(root,text="Pattadakallu",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
l.place(x=630,y=280)
t=Text(root,width=130,height=8,font=("normal",20,),bg="#bbffbb")
des="""              The Pattadakal monuments are situated in the Indian state of  Karnataka, approximately  165 kilometres (103 miles)
southeast of Belgaum, 265  kilometres (165  miles) northeast  of  Goa, 14 miles (23 km)  from  Badami  via Karanataka  state 
highway SH14, and approximately 6 miles (9.7 km) from Aihole, surrounded by sandstone mountains and the Malprabha river 
valley. Over 150 Hindu, Jain, and Buddhist  structures and archaeological  findings date from the 4th to 10th centuries CE, in 
addition to pre-historic dolmens and  cave  paintings  preserved  within the Pattadakal-Badami-Aihole region.  Pattadakal is a
small settlement on the banks of the Malaprabha river. Ptolemy referred to Pattadakal as Petrigal,but it was afterwards known 
as Raktapura (Red Town) and Pattadakal Kisuvolal.   """
t.insert(END, des)
t.place(x=5,y=420)
root.geometry("1532x840")
root.mainloop()