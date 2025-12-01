import os
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk

from dashboard import Dash1


class Admin:
    def __init__(self,root):
        self.root=root
        self.root.geometry("940x600")
        self.root.config(bg="white")
        self.root.title("Admin Login")
        self.root.focus_force()

        self.bg_Img=ImageTk.PhotoImage(file="/Result_Management_System-main/icons/logo1.jpg")
        self.pass_Img=ImageTk.PhotoImage(file="/Result_Management_System-main/icons/pass.png")
        self.user_Img=ImageTk.PhotoImage(file="/Result_Management_System-main/icons/user_icon.png")

        self.uname=StringVar()
        self.pass1=StringVar()

        label1 = Label(self.root, text="Admin Login", font="goudy 40 bold", bg="white", fg="black").pack(side=TOP, fill="x")
        Login_Frame = Frame(self.root, bg="white")
        Login_Frame.place(x=150, y=300)

        self.img_lbl= Label(self.root, image=self.bg_Img,bg="white" ).place(x=400, y=100)

        user_lbl = Label(Login_Frame, text="Username", font="goudy 20 bold", compound=LEFT, bg="white").grid(row=5, column=3, padx=20, pady=10)
        pass_lbl = Label(Login_Frame, text="Password", font="goudy 20 bold", compound=LEFT, bg="white").grid(row=7, column=3, padx=20, pady=35)

        text_user=Entry(Login_Frame, bd=5,textvariable=self.uname, relief=GROOVE, font=("",15)).grid(row=5, column=5, padx=20)
        text_passr=Entry(Login_Frame, bd=5, textvariable=self.pass1 ,relief=GROOVE, font=("",15)).grid(row=7, column=5, padx=20)

        btn =Button(Login_Frame,command=self.login, text="LOGIN", width=15, font="goudy 20 bold", bg="black", fg="white", cursor="hand2").grid(row=9, column=5)

    def login(self):
        if self.uname.get()=="" or self.pass1.get()=="":
            messagebox.showerror("Error", "All Fields Are Required",parent=self.root)
        elif self.uname.get()!=("Nishant") or self.pass1.get()!=("123"):
            messagebox.showerror("Error", "Invalid Username or Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.uname.get()}\n Your Password: {self.pass1.get()}",parent=self.root)
            os.system("python \\Result_Management_System-main\\code_files\\dashboard.py")

    def admin_dash(self):
        self.new_win1=Toplevel(self.root)
        self.new_obj1=Dash1(self.new_win1)

if __name__=="__main__":
    root=Tk()
    obj=Admin(root)
    root.mainloop()
