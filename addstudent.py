#Student Module
import sqlite3
from tkinter import *
from tkinter import messagebox, ttk


class StudentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x500+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

    #Title of Course
        title=Label(self.root,text="Manage Student Details",font=("times new roman",20,"bold"),bg="#CC3366",fg="white").place(x=0,y=0,relwidth=1,height=40)
    #Variables
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_adm_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()

    #Categories of student details 1 side
        rollno = Label(self.root,text="Roll No.",font=("times new roman",15,"bold"),bg="white").place(x=10,y=60)
        name = Label(self.root,text="Name",font=("times new roman",15,"bold"),bg="white").place(x=10,y=100)
        email = Label(self.root,text="Email",font=("times new roman",15,"bold"),bg="white").place(x=10,y=140)
        gender = Label(self.root,text="Gender",font=("times new roman",15,"bold"),bg="white").place(x=10,y=180)

        state = Label(self.root,text="Aadhar_No.",font=("times new roman",15,"bold"),bg="white").place(x=10,y=220)
        self.state1 = Entry(self.root,textvariable=self.var_state,font=("times new roman",15,"bold"),bg="lightyellow")
        self.state1.place(x=150,y=220,width=150)

        city = Label(self.root,text="City",font=("times new roman",15,"bold"),bg="white").place(x=330,y=220)
        self.city1 = Entry(self.root,textvariable=self.var_city,font=("times new roman",15,"bold"),bg="lightyellow")
        self.city1.place(x=380,y=220,width=110)

        pin = Label(self.root,text="PRN No.",font=("times new roman",15,"bold"),bg="white").place(x=510,y=220)
        self.pin1 = Entry(self.root,textvariable=self.var_pin,font=("times new roman",15,"bold"),bg="lightyellow")
        self.pin1.place(x=595,y=220,width=120)


        address = Label(self.root,text="Address",font=("times new roman",15,"bold"),bg="white").place(x=10,y=260)

    #Entry Fields 1
        self.rollno1 = Entry(self.root,textvariable=self.var_roll,font=("times new roman",15,"bold"),bg="lightyellow")
        self.rollno1.place(x=150,y=60,width=200)

        name1 = Entry(self.root,textvariable=self.var_name,font=("times new roman",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)
        email1 = Entry(self.root,textvariable=self.var_email,font=("times new roman",15,"bold"),bg="lightyellow").place(x=150,y=140,width=200)

        self.gender1 = ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=("times new roman",15,"bold"),state="readonly",justify=CENTER)
        self.gender1.place(x=150,y=180,width=200)
        self.gender1.current(0)

    #Address
        self.address = Text(self.root,font=("times new roman",15,"bold"),bg="lightyellow")
        self.address.place(x=150,y=260,width=540,height=100)


    #Categories of student details 2 side
        dob = Label(self.root,text="D.O.B",font=("times new roman",15,"bold"),bg="white").place(x=360,y=60)
        contact = Label(self.root,text="Contact",font=("times new roman",15,"bold"),bg="white").place(x=360,y=100)
        admission = Label(self.root,text="Class",font=("times new roman",15,"bold"),bg="white").place(x=360,y=140)
        self.admission = ttk.Combobox(self.root,textvariable=self.var_adm_date,values=("Select","FE","SE","TE","BE"),font=("times new roman",15,"bold"),state="readonly",justify=CENTER)
        self.admission.place(x=480,y=140,width=200)
        self.admission.current(0)
        course = Label(self.root,text="Course",font=("times new roman",15,"bold"),bg="white").place(x=360,y=180)

        self.dob1 = Entry(self.root,textvariable=self.var_dob,font=("times new roman",15,"bold"),bg="lightyellow")
        self.dob1.place(x=480,y=60,width=200)

        contact1 = Entry(self.root,textvariable=self.var_contact,font=("times new roman",15,"bold"),bg="lightyellow").place(x=480,y=100,width=200)
        self.txt_Course=ttk.Combobox(self.root,textvariable=self.var_course,font="goudy 15 ",values=("Select","IT","Computer","AIDS","EXTC","Computer Science"),state='readonly',justify=CENTER)
        self.txt_Course.place(x=480,y=180,width=200)
        self.txt_Course.current(0)

    # Buttons
        self.add_btn=Button(self.root,text="Save",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.add)
        self.add_btn.place(x=150,y=400,width=120,height=50)
        self.update_btn=Button(self.root,text="Update",font=("times new roman",15,"bold"),bg="green",fg="white",cursor="hand2",command=self.update)
        self.update_btn.place(x=290,y=400,width=120,height=50)
        self.delete_btn=Button(self.root,text="Delete",font=("times new roman",15,"bold"),bg="grey",fg="white",cursor="hand2",command=self.delete)
        self.delete_btn.place(x=430,y=400,width=120,height=50)
        self.clear_btn=Button(self.root,text="Clear",font=("times new roman",15,"bold"),bg="orange",fg="white",cursor="hand2",command=self.clear)
        self.clear_btn.place(x=570,y=400,width=120,height=50)

    #Search Panel
        self.var_search=StringVar()
        search_rollno = Label(self.root,text="Search By Roll No. ",font=("times new roman",15,"bold"),bg="white").place(x=720,y=60)
        search_rollno1 = Entry(self.root,textvariable=self.var_search,font=("times new roman",15,"bold"),bg="lightyellow").place(x=890,y=60,width=160,height=30)
        btn_search=Button(self.root,text="Search",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=100,height=30)

    #Content
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=360)

    #Table    
        #Scroll bar for table to view all headings
        scroly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrolx=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        # Columns and headings and adding commands for the functioning of scroll bar   
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrolx.set,yscrollcommand=scroly.set)
        scrolx.pack(side=BOTTOM,fill=X)
        scroly.pack(side=RIGHT,fill=Y)
        scrolx.config(command=self.CourseTable.xview)
        scroly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("roll",text="Roll No")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("dob",text="D.O.B")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("admission",text="class")
        self.CourseTable.heading("course",text="Course")
        self.CourseTable.heading("state",text="Aadhar_No.")
        self.CourseTable.heading("city",text="City")
        self.CourseTable.heading("pin",text="PRN")
        self.CourseTable.heading("address",text="Address")

        self.CourseTable["show"]="headings"

        self.CourseTable.column("roll",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("email",width=100)
        self.CourseTable.column("gender",width=100)
        self.CourseTable.column("dob",width=100)
        self.CourseTable.column("contact",width=100)
        self.CourseTable.column("admission",width=100)
        self.CourseTable.column("course",width=100)
        self.CourseTable.column("state",width=100)
        self.CourseTable.column("city",width=100)
        self.CourseTable.column("pin",width=100)
        self.CourseTable.column("address",width=100)


        self.CourseTable.pack(fill=BOTH,expand=1)

        self.CourseTable.bind("<ButtonRelease-1>",self.get_data) #When you click on any cid row it will show details on their sections get_data function is defined below

        self.show() 


    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_adm_date.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.address.delete("1.0",END)
        self.rollno1.config(state=NORMAL)

        self.var_search.set("")

    def delete(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_roll.get()=="" :
                messagebox.showerror("Error","Roll No should be required ",parent=self.root)
            else:
                cur.execute("Select * from student1 where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error, Select The Student From the List first",parent=self.root)
                else:
                    p=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                    if p==True:
                        cur.execute("Delete from student1 where roll=? ",(self.var_roll.get(),))
                        conn.commit()
                        messagebox.showinfo("Delete","Student deleted Successfully",parent=self.root)
                        self.clear() #We are calling clear because we declare show in to that
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def get_data(self,event):
        self.rollno1.config(state="readonly")
        self.rollno1

        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]

        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_adm_date.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])

        self.address.delete("1.0",END)
        self.address.insert(END,row[11])


# Adding Details and Saving
    def add(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_roll.get()==""or self.var_name.get()=="" or self.var_email.get()=="" or self.var_course=="Select":
                messagebox.showerror("Error","Roll No., Student name, Email and Course must required",parent=self.root)
            else:
                cur.execute("Select * from student1 where roll=?",(self.var_roll.get(),)) #Due to tupple we added , at last
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error, Roll No. is already Present",parent=self.root)
                else:
                    cur.execute("Insert into student1 (roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_adm_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),

                        self.address.get("1.0",END)
                    ) )
                    conn.commit()
                    messagebox.showinfo("Great","Student Added Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    #Updating Details
    def update(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No should be required",parent=self.root)
            else:
                cur.execute("Select * from student1 where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Student From List",parent=self.root)
                else:
                    cur.execute("Update student1 set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where  roll=? ",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_adm_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),

                        self.address.get("1.0",END),
                        self.var_roll.get()
                    ) )
                    conn.commit()
                    messagebox.showinfo("Great","Student Update Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def show(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            cur.execute("Select * from student1")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            cur.execute("Select * from student1 where roll=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row !=None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record Found",parent=self.root)    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")




if __name__=="__main__":
    root=Tk()
    obj=StudentClass(root)
    root.mainloop()