import os
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk
from result import ResultClass # type: ignore

from addstudent import StudentClass


class Dash1:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x700+100+50")
        self.root.config(bg="white")
        self.root.title("Admin Dashboard")
        #==========Logo===============

        self.logo=ImageTk.PhotoImage(file="\\Result_Management_System-main\\icons\\KONKAN.jpg")
        title= Label(self.root,text="Student Result Management System",compound=LEFT,image=self.logo ,padx=30,font="goudy 28 bold", bg="#bdd7ee", fg="black").place(x=0,y=0,relwidth=1,height=110)
        title= Label(self.root,text="Konkan Gyanpeeth College Of Engineering,Karjat,Raigad 410201",font="goudy 18", bg="#bdd7ee", fg="black").pack(side=BOTTOM,fill=X)

        #=======Menu=============
        M_lbl=LabelFrame(self.root, text="Menu",font=("times new roman","15"),bg="white")
        M_lbl.place(x=11,y=115,width=300, height=550)

        #============Buttons==============

        btn_student=Button(M_lbl,text="Add Student",font=("times new roman","30"),bg="#4472c5",fg="white",relief=RIDGE,borderwidth=5,cursor="hand2",command=self.add_student).place(x=10,y=50,height=75,width=270)

        btn_Add_result=Button(M_lbl,text="Add Result",font=("times new roman","30"),bg="#e97f34",fg="white",relief=RIDGE,borderwidth=5,cursor="hand2",command=self.add_result).place(x=10,y=155,height=75,width=270)

        btn_Logout=Button(M_lbl,text="Logout",font=("times new roman","30"),bg="#fec000",fg="white",relief=RIDGE,borderwidth=5,cursor="hand2",command=self.logout).place(x=10,y=260,height=75,width=270)

        btn_exit=Button(M_lbl,text="Exit",font=("times new roman","30"),bg="#a0cb8c",fg="white",relief=RIDGE,borderwidth=5,cursor="hand2",command=self.exit).place(x=10,y=360,height=75,width=270)

        #============Image===================

        self.bg_Img=ImageTk.PhotoImage(file="\\Result_Management_System-main\\icons\\dashboardimg.jpg")
        self.img_lbl= Label(self.root, image=self.bg_Img,bg="white" ).place(x=430, y=200)

    def add_student(self):
        self.new_win2=Toplevel(self.root)
        self.new_obj2=StudentClass(self.new_win2)

    def add_result(self):
        self.new_win4=Toplevel(self.root)
        self.new_obj4=ResultClass(self.new_win4)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do You really Want to Logout ?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("Python form.py")

    def exit(self):
        op=messagebox.askyesno("Confirm","Do You really Want to Exit ?",parent=self.root)
        if op==True:
            self.root.destroy()





if __name__=="__main__":
    root=Tk()
    obj=Dash1(root)
    root.mainloop()