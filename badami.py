
from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.configure(bg="#bbffbb")
img1= Image.open("bd2.jpg")
img2= Image.open("bd1.jpeg")
img3= Image.open("bd3.jpg")
img4= Image.open("bd4.jpg")
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
    l=Label(root,text="Badami Caves",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
    l.place(x=593,y=270)
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
    l=Label(root,text="Badami Caves",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
    l.place(x=593,y=270)
    if no==1:
        b1=Button(root,text="<<",state=DISABLED)
        b1.place(x=550,y=150)
b1=Button(root,text="<<",command=back, state=DISABLED)
b2=Button(root,text=">>",command=lambda: forward(2))
b1.place(x=550,y=150)
b2.place(x=955,y=150)
l=Label(root,text="Badami Caves",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
l.place(x=593,y=270)
t=Text(root,width=130,height=8,font=("normal",20,),bg="#bbffbb")
des="""         The Badami cave temples are located in the town of Badami in Karnataka,India’s north-central region. The temples are
located around 88 miles (142 kilometres) east of Belgavi (IATA Code: IXT) and 87 miles (140 kilometres) northwest of Hampi.
The Malaprabha River is about 3 miles (4.8 kilometres) distant.
          The  cave  temples are  14  miles  (23  kilometres) from  the  UNESCO  world  heritage  site  Pattadakal  and  22 miles 
(35 kilometres)  from  Aihole,  another  site  with  over  a  hundred  ancient  and  early  mediaeval  Hindu,  Jain, and Buddhist 
structures."""
t.insert(END, des)
t.place(x=5,y=420)
root.geometry("1532x840")
root.mainloop()