from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.configure(bg="#bbffbb")
img1= Image.open("mahakuta1.jpg")
img2= Image.open("mah2.jpeg")
img3= Image.open("maha3.jpeg")
img4= Image.open("maha4.jpg")
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
    l=Label(root,text="Mahakuta",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
    l.place(x=660,y=280)
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
    l=Label(root,text="Mahakuta",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
    l.place(x=660,y=280)
    if no==1:
        b1=Button(root,text="<<",state=DISABLED)
        b1.place(x=550,y=150)
b1=Button(root,text="<<",command=back, state=DISABLED)
b2=Button(root,text=">>",command=lambda: forward(2))
b1.place(x=550,y=150)
b2.place(x=955,y=150)
l=Label(root,text="Mahakuta",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
l.place(x=660,y=280)
t=Text(root,width=130,height=8,font=("normal",20,),bg="#bbffbb")
des="""          The Mahakuta temple complex is located in Mahakuta, a hamlet in Karnataka’s Bagalkot district. It is a significant Hindu
pilgrimage site and home to a well-known  Shaiva monastery. The temples originate from the 6th or 7th centuries CE and were 
built by the early  monarchs of Badami’s  Chalukya  dynasty. The temples dating is  based on  the architectural style, which is
similar  to  that  of  the  temples  in  nearby Aihole[1],  as well  as  information  in  two  notable  inscriptions in the complex: the 
Mahakuta Pillar inscription,  dated  between  595–602  CE ( written  in  the  Sanskrit  language  and  Kannada  script); and an 
inscription of Vinapoti, a concubine of King Vijayaditya, dated between 696–733.          """
t.insert(END, des)
t.place(x=5,y=420)
root.geometry("1532x840")
root.mainloop()