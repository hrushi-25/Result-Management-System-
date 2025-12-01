from tkinter import *
from PIL import Image, ImageTk
from stud_dashboard import Dash2
from tkinter import messagebox
import sqlite3
import os
class Stud:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x600+230+80")
        self.root.config(bg="white")
        self.root.title("Student Login")
        self.root.focus_force()

        self.uname=StringVar()
        self.pass1=StringVar()

        self.bg_Img=ImageTk.PhotoImage(file="\\Result_Management_System-main\\icons\\logo1.jpg")
        self.pass_Img=ImageTk.PhotoImage(file="/Result_Management_System-main/icons/pass.png")
        self.user_Img=ImageTk.PhotoImage(file="/Result_Management_System-main/icons/user_icon.png")

        label1 = Label(self.root, text="Student Login", font="goudy 40 bold", bg="white", fg="black").pack(side=TOP, fill="x")
        Login_Frame = Frame(self.root, bg="white")
        Login_Frame.place(x=150, y=300)

        self.img_lbl= Label(self.root, image=self.bg_Img,bg="white" ).place(x=400, y=100)

        user_lbl = Label(Login_Frame, text="Username", font="goudy 20 bold", compound=LEFT, bg="white").grid(row=5, column=3, padx=20, pady=10)
        pass_lbl = Label(Login_Frame, text="Password", font="goudy 20 bold", compound=LEFT, bg="white").grid(row=7, column=3, padx=20, pady=35)

        text_user=Entry(Login_Frame, bd=5,textvariable=self.uname ,relief=GROOVE, font=("",15)).grid(row=5, column=5, padx=20)
        text_passr=Entry(Login_Frame, bd=5,textvariable=self.pass1, relief=GROOVE, font=("",15)).grid(row=7, column=5, padx=20)

        btn =Button(Login_Frame, text="LOGIN",command=self.login, width=15, font="goudy 20 bold", bg="black", fg="white", cursor="hand2").grid(row=9, column=5)
        
    def login(self): 
        if self.uname.get()=="" or self.pass1.get()=="":
            messagebox.showerror("Error", "All Fields Are Required",parent=self.root)
        else:
            try:
                conn=sqlite3.connect(database="ResultManagementSystem.db")
                cur=conn.cursor()
                cur.execute("select * from student1 where email=? and dob=?",(self.uname.get(),self.pass1.get()))
                row=cur.fetchone()
                os.system("python /Result_Management_System-main/code_files/stud_dashboard.py")
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)

    def stud_dash(self):
        self.new_win2=Toplevel(self.root)
        self.new_obj2=Dash2(self.new_win2)

if __name__=="__main__":
    root=Tk()
    obj=Stud(root)
    root.mainloop()