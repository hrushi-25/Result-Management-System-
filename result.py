from os import name
from tkinter import*
from PIL import Image,ImageTk  
from tkinter import ttk,messagebox
import sqlite3
class ResultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x650")
        self.root.config(bg="white")
        self.root.focus_force()

        title=Label(self.root,text="Add Student Result",font=("times new roman",20,"bold"),bg="#CC3366",fg="white").place(x=0,y=0,relwidth=1,height=40)

        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_mvi=IntVar()
        self.var_coa=IntVar()
        self.var_at=IntVar()
        self.var_os=IntVar()
        self.var_cn=IntVar()
        self.var_total=StringVar()
        self.var_cgpa=StringVar()
        self.rool_list=[]
        self.fetch_roll()

        select = Label(self.root,text="Select Student",font=("times new roman",20,"bold"),bg="white").place(x=50,y=50)
        roll = Label(self.root,text="ROll No  :",font=("times new roman",15,"bold"),bg="white").place(x=50,y=100)
        name = Label(self.root,text="Name  :",font=("times new roman",15,"bold"),bg="white").place(x=50,y=140)

        mvi = Label(self.root,text="EM-IV  :",font=("times new roman",15,"bold"),bg="white").place(x=50,y=180)
        coa = Label(self.root,text="COA  :",font=("times new roman",15,"bold"),bg="white").place(x=50,y=220)
        at = Label(self.root,text="AT  :",font=("times new roman",15,"bold"),bg="white").place(x=50,y=260)
        os = Label(self.root,text="OS  :",font=("times new roman",15,"bold"),bg="white").place(x=50,y=300)
        cn = Label(self.root,text="CNND  :",font=("times new roman",15,"bold"),bg="white").place(x=50,y=340)
        total = Label(self.root,text="Total Marks  :",font=("times new roman",20,"bold"),bg="white").place(x=50,y=400)
        pointer = Label(self.root,text="CGPA  :",font=("times new roman",20,"bold"),bg="white").place(x=50,y=470)

        total_e =Entry(self.root,textvariable=self.var_total,font=("times new roman",15,"bold"),bg="lightyellow").place(x=250,y=410,width=200)
        cgpa_e =Entry(self.root,textvariable=self.var_cgpa,font=("times new roman",15,"bold"),bg="lightyellow").place(x=250,y=480,width=200)

        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.rool_list,font=("times new roman",20,"bold"),state='readonly',justify=CENTER)
        self.txt_student.place(x=250,y=50,width=200)
        self.txt_student.set("Select")
        self.roll = Entry(self.root,font=("times new roman",15,"bold"),textvariable=self.var_roll,bg="lightyellow",state='readonly').place(x=150,y=100,width=200)
        self.name = Entry(self.root,font=("times new roman",15,"bold"),textvariable=self.var_name,bg="lightyellow",state='readonly').place(x=150,y=140,width=200)

        self.mvi = Entry(self.root,textvariable=self.var_mvi,font=("times new roman",15,"bold"),bg="lightyellow")
        self.mvi.place(x=150,y=180,width=200)
        coa1 = Entry(self.root,textvariable=self.var_coa,font=("times new roman",15,"bold"),bg="lightyellow").place(x=150,y=220,width=200)
        at1 = Entry(self.root,textvariable=self.var_at,font=("times new roman",15,"bold"),bg="lightyellow").place(x=150,y=260,width=200)
        os1 = Entry(self.root,textvariable=self.var_os,font=("times new roman",15,"bold"),bg="lightyellow").place(x=150,y=300,width=200)
        cn1 = Entry(self.root,textvariable=self.var_cn,font=("times new roman",15,"bold"),bg="lightyellow").place(x=150,y=340,width=200)
        # self.welcom_result()

        #==============Result Area=================================
        Result_Frame=Frame(self.root,bd=10,relief=GROOVE)
        Result_Frame.place(x=655,y=55,width=600,height=500)
        result_title=Label(Result_Frame,text="Result",font="arial 18 bold",relief=GROOVE,bd=5).pack(fill=X)
        scrol_y=Scrollbar(Result_Frame,orient=VERTICAL)
        self.txtarea=Text(Result_Frame,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack()
        self.welcom_r()

        self.total_btn=Button(self.root,text="Calculate",command=self.total,font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        self.total_btn.place(x=670,y=565,width=120,height=50)
        self.genarate_btn=Button(self.root,text="Genarate_Result",command=self.result_area,font=("times new roman",15,"bold"),bg="green",fg="white",cursor="hand2")
        self.genarate_btn.place(x=800,y=565,width=150,height=50)
        self.Print_btn=Button(self.root,text="Print",command=self.print_result,font=("times new roman",15,"bold"),bg="lightblue",fg="white",cursor="hand2")
        self.Print_btn.place(x=970,y=565,width=120,height=50)
        self.clear_btn=Button(self.root,text="Exit",font=("times new roman",15,"bold"),command=self.exit,bg="lightgreen",fg="white",cursor="hand2")
        self.clear_btn.place(x=1120,y=565,width=120,height=50)
        self.search_btn=Button(self.root,text="Search",font=("times new roman",15,"bold"),command=self.search,bg="green",fg="white",cursor="hand2")
        self.search_btn.place(x=480,y=50,width=120,height=40)

    def total(self):
        self.total_marks=(
                            (self.var_mvi.get())+
                            (self.var_coa.get())+
                            (self.var_at.get())+
                            (self.var_os.get())+
                            (self.var_cn.get())
                        )
        self.var_total.set(str(self.total_marks))
        self.var_cgpa.set(str(self.total_marks*0.025))

    def fetch_roll(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            cur.execute("Select roll from student1")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.rool_list.append(row[0])
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            cur.execute("select roll,name from student1 where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_roll.set(row[0])
                self.var_name.set(row[1])
            else:
                messagebox.showerror("Error","Record Not Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def welcom_r(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\tKonkan Gyanpeeth College Of Engineering,Karjat\n")
        self.txtarea.insert(END,"\n===================================================================\n")
        self.txtarea.insert(END,f"\nStudent Name :{self.var_name.get()}\n")
        self.txtarea.insert(END,f"\nStudent Roll_No :{self.var_roll.get()}\n")
        self.txtarea.insert(END,"\n===================================================================\n")
        self.txtarea.insert(END,f"\nSr_No\t\tSubject\t\tMarks_Obtained\t\tTotal_Marks")
        self.txtarea.insert(END,"\n===================================================================\n")


    def result_area(self):
        self.welcom_r()
        if self.mvi!=0:
            self.txtarea.insert(END,f"\n1.\t\tEM-IV\t\t{self.var_mvi.get()}\t\t\t80")
        if self.var_coa!=0:
            self.txtarea.insert(END,f"\n2.\t\tCOA\t\t{self.var_coa.get()}\t\t\t80")
        if self.var_at!=0:
            self.txtarea.insert(END,f"\n3.\t\tAT\t\t{self.var_at.get()}\t\t\t80")
        if self.var_os!=0:
            self.txtarea.insert(END,f"\n4.\t\tOS\t\t{self.var_os.get()}\t\t\t80")
        if self.var_cn!=0:
            self.txtarea.insert(END,f"\n5.\t\tCNND\t\t{self.var_cn.get()}\t\t\t80\n")
            self.txtarea.insert(END,"\n===================================================================\n")
            self.txtarea.insert(END,f"\nTotal Marks :{self.var_total.get()}\n")
            self.txtarea.insert(END,f"\nCGPA :{self.var_cgpa.get()}\n")
            


    def print_result(self):
        op=messagebox.askyesno("Save Result","Do You Want To Save Result?",parent=self.root)
        if op>0:
            self.result_data=self.txtarea.get('1.0',END)
            f1=open(str(self.var_roll.get())+".txt","w")
            f1.write(self.result_data)
            f1.close()
        else:
            return
        
    def exit(self):
        op=messagebox.askyesno("Confirm","Do You really Want to Exit ?",parent=self.root)
        if op==True:
            self.root.destroy()






if __name__=="__main__":
    root=Tk()
    obj=ResultClass(root)
    root.mainloop()