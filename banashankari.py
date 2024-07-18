
from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.configure(bg="#bbffbb")
img1= Image.open("ban0.jpg")
img2= Image.open("ban1.jpeg")
img3= Image.open("ban2.jpeg")
img4= Image.open("ban3.jpg")
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
    l=Label(root,text="Banashankari Temple",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
    l.place(x=540,y=280)
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
    l=Label(root,text="Banashankari Temple",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
    l.place(x=540,y=280)
    if no==1:
        b1=Button(root,text="<<",state=DISABLED)
        b1.place(x=550,y=150)
b1=Button(root,text="<<",command=back, state=DISABLED)
b2=Button(root,text=">>",command=lambda: forward(2))
b1.place(x=550,y=150)
b2.place(x=955,y=150)
l=Label(root,text="Banashankari Temple",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
l.place(x=540,y=280)
t=Text(root,width=130,height=8,font=("normal",20,),bg="#bbffbb")
des="""          Banashankari  Devi   Temple  (or  Banashankari  temple) is a Hindu shrine  located  at  Cholachagudda  near  Badami, 
in  Bagalkot  district,  Karnataka,  India.   The  temple  is  popularly  called   'Shakambhari'  'Banashankari  or   Vanashankari'
since  it  is  located  in  the  Tilakaaranya  forest.  The  temple  deity  is  also  called  the  Shakambhari (Kannada: ಶಾಕoಭರಿ),
an incarnation of the goddess Parvati.

         The  temple  attracts  devotees  from  Karnataka  as well as the neighbouring state of Maharashtra. The original temple
was  built  by  the  7th  century  Badami  Chalukya  kings,  who  worshipped  goddess  Banashankari  as  their  tutelary deity.
The temple celebrates its annual festival called Banashankari jatre, in the months of January or February.
 
         The festival comprises cultural programmes,  boat festival as well as a Rath yatra, when the temple goddess is paraded
around  the  city  in  a  chariot.  Banshakhari  is  a  form  of  Maa Shakambhari  Devi  whose  real, main and ancient temple is
located  in  Saharanpur  District  in  Uttar  Pradesh.  It  is  also  known as  Shaktipeeth  Shakambhari Devi. There are statues 
of Bhima, Bhramari, Shatakshi and Ganesha along with mother."""
t.insert(END, des)
t.place(x=5,y=420)
root.geometry("1532x840")
root.mainloop()