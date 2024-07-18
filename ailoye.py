
from tkinter import *
from PIL import ImageTk,Image
root=Tk()
img1= Image.open("bgk.jpg")
rm1 = img1.resize((250, 200))
img11 = ImageTk.PhotoImage(rm1)
l1 = Label(image=img11)
l1.image = img1
l1.pack(padx=50,pady=20)
l=Label(root,text="Aihole",font=("italic",50,"bold","underline"))
l.place(x=640,y=230)
t=Text(root,width=130,height=11,font=("normal",20,))
des="""              Aihole has been mentioned in Hindu myths. It has a natural axe-shaped rock on the Malaprabha river bank north of 
the  settlement, as well as a  footprint on a rock  in the river. According to mythology,  Parashurama, the sixth Vishnu avatar, 
cleaned his axe here after slaying arrogant Kshatriyas who were abusing their military authority, giving the region its crimson 
hue. A 19th-century  local legend  held that rock footprints in the river  belonged to Parashurama. A location near the Meguti 
hillocks has signs  of prehistoric  human occupation. Aihole is  historically  significant and has been been to as the “cradle of
Hindu rock construction.”   """
t.insert(END, des)
t.place(x=5,y=350)
root.mainloop()