from tkinter import *
import os
from PIL import Image, ImageTk
from tkinter import messagebox,ttk
from project import EditClass
class Dash2:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x700")
        self.root.config(bg="white")
        self.root.title("Student Dashboard")
        self.root.focus_force()
        self.root.resizable(False, False)

        self.var_roll1=StringVar()

        lbl_roll=Label(self.root,text="View Result  :",font="goudy 28 bold",bg="white").place(x=50,y=80)
        lbl_roll=Label(self.root,text="Roll No.",font="goudy 24 bold",bg="white")
        lbl_roll.place(x=50,y=170)
        entry_roll=Entry(self.root,textvariable=self.var_roll1,font="goudy 18 bold",bg="lightyellow").place(x=200,y=170,width=140,height=40)
        title= Label(self.root,text="Student Result Management System",font="goudy 28 bold", bg="#bdd7ee", fg="black").place(x=0,y=0,relwidth=1,height=50)

        btn_viewresult=Button(self.root,text="Submit",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.viewresult).place(x=50,y=250,width=150,height=50)

    def viewresult(self):
        op=messagebox.askyesno("Confirm","Do You really Want to View Result ?",parent=self.root)
        if op==True:
            os.system(r"D:\\Result_Management_System-main\\code_files\\"+str(self.var_roll1.get())+".txt")



if __name__=="__main__":
    root=Tk()
    obj=Dash2(root)
    root.mainloop()