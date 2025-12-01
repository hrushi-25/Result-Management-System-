def new_func():
    #Database File
    import sqlite3
    def create_db():
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()
#Table Creation for Student Page
        cur.execute("Create table if not exists student1(roll INTEGER primary key AutoIncrement,name text,email test,gender text,dob text,contact text,admission text,course text,state text,city text,pin text,address text)")
        conn.commit()


        conn.close()

    create_db()

new_func()