
from tkinter import *
from PIL import ImageTk,Image
root=Tk()
img1= Image.open("bgk.jpg")
rm1 = img1.resize((250, 200))
img11 = ImageTk.PhotoImage(rm1)
l1 = Label(image=img11)
l1.image = img1
l1.pack(padx=50,pady=20)
l=Label(root,text="Kudalasangama",font=("italic",50,"bold","underline"))
l.place(x=490,y=230)
t=Text(root,width=130,height=11,font=("normal",20,))
des="""           Kudalasangama (sometimes spelled Kudala Sangama) is a significant pilgrimage site for Lingayats in India. It is around 
15 kilometres (9.3 miles) from the Almatti Dam in Karnataka’s Bagalkot district. The Krishna and Malaprabha Rivers meet here 
and run east to Srisaila (another pilgrimage site) in Andhra Pradesh. The Aikya Mantapa, or sacred Samdhi of Basavanna, the 
founder of the Lingayat branch  of Hindu  religion,  is here, as is Linga, which  is considered to be self-born (Swayambhu). The 
Kudala Sangama Development Board is in charge of upkeep and development.          """
t.insert(END, des)
t.place(x=5,y=350)
root.mainloop()