from tkinter import *
from PIL import Image, ImageTk
from admin1 import Admin
from student import Stud
class RMS:
    def __init__(self,root):
        self.root=root
        
        
        self.root.geometry("1250x800+130+40")
        self.root.config(bg="#DB9F04")
        self.root.title("First Page")
        self.root.resizable(False, False)

        self.Lbl = Label(self.root, text="Login Page", font="goudy 40 bold", bg="#DB9F04", fg="white").pack(pady=25,side=TOP, fill="x")

        self.btn_1 = Button(self.root, text="Student", bg="white", cursor="hand2", fg="#DB9F04", font="goudy 24",relief=SUNKEN, command=self.student_login).place(x=370, y=650, width=200)
        self.btn_2 = Button(self.root, text="Admin", bg="white", cursor="hand2", fg="#DB9F04", font="goudy 24",relief=SUNKEN ,command=self.admin_login).place(x=670, y=650, width=200)


        self.bg_img=ImageTk.PhotoImage(file="\\Result_Management_System-main\\icons\\login.jpg")

        self.img_lbl= Label(self.root, image=self.bg_img).place(x=200, y=100, width=920, height=520)

    def admin_login(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Admin(self.new_win)

    def student_login(self):
        self.new_win1=Toplevel(self.root)
        self.new_obj1=Stud(self.new_win1)


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
