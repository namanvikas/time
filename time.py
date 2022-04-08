import pytz
import time 
from datetime import datetime

root=Tk()
root.title("time")
root.geometry("600x400")

clock_image=ImageTk.photoImage(Image.open("clock.jpeg"))

#---------Australia---------
australia_label=Label(root,text="Australia")
australia_label.place(relx=0.2,rely=0.05,anchor=CENTE)

australia_image=Label(root)
australia_image["image"]=clock_image
australia_image.place(relx=0.2,rely=0.35,anchor=CENTER)

australia_time=Label(root)
austrlia_time.place(relx=0.2,rely=0.65,anchor=CENTER)

class Australia():
    def time(self):
      home=pytz.timezone('Australia/ACT')
      local_time=datetime.now(home)
      current_time=local_time.strftime("%H:%M:%S")
      australia_time["text"]="time:"+current_time
      australia_time.after(200,self.time)
        
obj_australia=Australia()
australia_btn=Button(root,text="show time",command=obj.time)
australia_btn.place(relx=0.2,rely=0.8,anchor=CENTER) 

#---------Japan---------
japan_label=Label(root,text="Japan")
japan_label.place(relx=0.2,rely=0.05,anchor=CENTE)

japan_image=Label(root)
japan_image["image"]=clock_image
japan_image.place(relx=0.2,rely=0.35,anchor=CENTER)

japan_time=Label(root)
japan_time.place(relx=0.2,rely=0.65,anchor=CENTER)

class India():
    def time(self):
      home=pytz.timezone('Japan')
      local_time=datetime.now(home)
      current_time=local_time.strftime("%H:%M:%S")
      japan_time["text"]="time:"+current_time
      japan_time.after(200,self.time)
        
obj_japan=Japan()
japan_btn=Button(root,text="show time",command=obj.time)
japan_btn.place(relx=0,rely=0.8,anchor=CENTER) 
 
root.mainloop()