from config import DB_PASSWORD
import mysql.connector as mys
def create_file():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="college")
    mycon=mydb.cursor()
create_file()

def add_data():
      while True:
        st=int(input("enter the student number: "))
        age=int(input("enter the age of the student: "))
        name=input("enter the name of the student: ")
        branch=input("enter the branch name: ")
        fees=int(input("enter the fees of the student for 4 years: "))
        hostel_block=input("enter the hostel block (A-H): ")
        room_no=int(input("enter the room number of the student: "))
        mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="college")
        mycon=mydb.cursor()

        sql= "insert into student(stud_no,age,name,branch,fees,hostel_block,room_no) VALUES(%s, %s, %s, %s, %s, %s, %s);"
        values = (st, age, name, branch, fees, hostel_block, room_no)

        mycon.execute(sql, values)

        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("Do you want to continue with entries (y/n): ").strip().lower()
        if ans=='n':
            print("thank you for admission")
            break
        mycon.close()

def modify_data():
     mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="college")
     mycon=mydb.cursor() 
     while True:
        ch = input("Do you want to update entries? (y/n): ").strip().lower()
        if ch != 'y':
            print("Exiting update menu.")
            break
        
        stud_no = input("Enter student number to update: ").strip()
        if not stud_no:
            print("Student number is required!")
            continue

        print("What do you want to update?")
        print("a. for Student Number")
        print("b. for Age")
        print("c. for Name")
        print("d. for Branch")
        print("e. for Fees")
        print("f. for Hostel Block")
        print("g. for Room Number")
        print("h. for cancel")

        choice = input("Enter your choice (a-i): ").strip()
        if choice == 'a':
            new_s = int(input("Enter the updated student number: "))
            if new_s:
                mycon.execute("UPDATE student SET stud_no=%s WHERE stud_no=%s", (new_s, stud_no))
                print("Student number updated.")
                mydb.commit()

        elif choice == 'b':
            new_age = int(input("Enter the updated age: "))
            if new_age:
                mycon.execute("UPDATE student SET age=%s WHERE stud_no=%s", (int(new_age),stud_no))
                print("Age updated.")
                mydb.commit()

        elif choice == 'c':
            new_name = input("Enter the updated name: ")
            if new_name:
                mycon.execute("UPDATE student SET name=%s WHERE stud_no=%s", (new_name, stud_no))
                print("Name updated.")
                mydb.commit()

        elif choice == 'd':
            new_branch = input("Enter the updated branch: ")
            if new_branch:
                mycon.execute("UPDATE student SET branch=%s WHERE stud_no=%s", (new_branch, stud_no))
                print("Branch updated.")
                mydb.commit()

        elif choice == 'e':
            new_fees = int(input("Enter the updated fees: "))
            if new_fees:
                mycon.execute("UPDATE student SET fees=%s WHERE stud_no=%s", (int(new_fees),stud_no))
                print("Fees updated.")
                mydb.commit()

        elif choice == 'f':
            new_block = input("Enter the updated hostel block: ")
            if new_block:
                mycon.execute("UPDATE student SET hostel_block=%s WHERE stud_no=%s", (new_block, stud_no))
                print("Hostel block updated.")
                mydb.commit()

        elif choice == 'g':
            new_room = int(input("Enter the updated room number: "))
            if new_room:
                mycon.execute("UPDATE student SET room_no=%s WHERE stud_no=%s", (int(new_room),stud_no))
                print("Room number updated.")
                mydb.commit()

        

        elif choice == 'h':
                print("update cancelled ")
                break
        
        else:
            print("invalid operation ")
            break
        
        mydb.commit()
        mycon.close()

def display_data():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="college")
    mycon=mydb.cursor() 
    mycon.execute("select * from student;")
    x=mycon.fetchall()
    for i in x:
        print("the number of records in the given table is ",len(x))
        print("the records are as follows : ")
        print(i)

def delete_data():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="college")
    mycon=mydb.cursor()
    mycon.execute("select * from student;")
    x=mycon.fetchall()
    while True:
        c=input("do you want to delete entries(y/n): ").strip().lower()
        if c!='y':
            print("exiting the deletion menu ")
            break
        else:
          print("what do you want to delete?")
          print("A. for Student Number")
          print("B. for Age")
          print("C. for Name")
          print("D. for Branch")
          print("E. for Fees")
          print("F. for Hostel Block")
          print("G. for Room Number")
          print("H. for Cancel")

          c=input("enter your choice(A-H): ")
          if c == 'A':
              s=int(input("enter the student number you want to delete :"))
              mycon.execute("select * from student where stud_no=%s",(s,))
              o=mycon.fetchall()
              if not o:
                  print("no record found with such student number")
              else:
                  mycon.execute("delete from student where stud_no=%s",(s,))
                  mydb.commit()
          
          elif c == 'B':
              a=int(input("enter the age you want to delete: "))
              mycon.execute("select count(*) from student where age=%s",(a,))
              o=mycon.fetchall()
              if not o:
                  print("no records found with this age ")
              else:
                  mycon.execute("delete from student where age=%s",(a,))

          elif c == 'C':
              n=input("enter the name you want to delete: ")
              mycon.execute("select count(*) from student where age=%s",(n,))
              o=mycon.fetchall()
              if not o:
                  print("no records found with this age ")
              else:
                  mycon.execute("delete from student where name=%s",(n,))

          elif c == 'D':
              b=input("enter the branch name you want to delete : ")
              mycon.execute("select count(*) from student where branch=%s",(b,))
              o=mycon.fetchall()
              if not o:
                  print("no records found with this branch")
              else:
                  mycon.execute("delete from student where branch=%s",(b,))
          elif c == "E":
              f=int(input("enter the fees you want to delete: "))
              mycon.execute("select count(*) from student where fees=%s",(f,))
              o=mycon.fetchall()
              if not o:
                  print("no records found with this fees")
              else:
                  mycon.execute("delete from student where fees=%s",(f,))

          elif c == "F":
              h=input("enter hostel block you want to delete : ")
              mycon.execute("select count(*) from student where hostel_block=%s",(h,))
              o=mycon.fetchall()
              if not o:
                  print("no records found with this hostel number")
              else:
                  mycon.execute("delete from student where hostel_block=%s",(h,))
            
          elif c == "G":
              r=int(input("enter room number you want to delete : "))
              mycon.execute("select count(*) from student where room_no=%s",(r,))
              o=mycon.fetchall()
              if not o:
                  print("no records founs with such room number")
              else:
                  mycon.execute("delete from student where room_no=%s",(r,))

          elif c == "H":
              print("deletion cancelled ")
              break
          
          else:
              print("invalid operation ")
              break

def search_data():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="college")
    mycon=mydb.cursor()
    
    while True:
        k=input("do you want to search entries(y/n) : ").strip().lower()
        if k!='y':
            print("exiting the selection menu")
            break
        else:
            print("what do you want to search ? ")
            print("a. for Student Number")
            print("b. for Age")
            print("c. for Name")
            print("d. for Branch")
            print("e. for Fees")
            print("f. for Hostel Block")
            print("g. for Room Number")
            print("h. for Cancel")

            o=input("enter your choice(a-h): ").strip()
            if o == "a":
                s=int(input("enter the student number to search : "))
                mycon.execute("select * from student where stud_no=%s",(s,))

            elif o == "b":
                a=int(input("enter the age to search : "))
                mycon.execute("select * from student where age=%s",(a,))
            
            elif o == "c":
                n=input("enter the name to search : ")
                mycon.execute("select * from student where name=%s",(n,))


            elif o == "d":
                b=input("enter the branch name to search : ")
                mycon.execute("select * from student where branch=%s",(b,))
            
            elif o == "e":
                f=int(input("enter the fees to search : "))
                mycon.execute("select * from student where fees=%s",(f,))


            elif o == "f":
                h=input("enter the hostel block to search : ")
                mycon.execute("select * from student where hostel_block=%s",(h,))
            
            elif o == "g":
                r=int(input("enter the room number to search : "))
                mycon.execute("select * from student where room_no=%s",(r,))

            elif o =="h":
                print("search cancelled ")
                break
            
            else:
                print("sorry invalid operation ")
                break
            
            x=mycon.fetchall()
            if not x:
                print("no records found for your search")
            else:
                print("number of records found: ",len(x))
                for row in x:
                    print(row)

    mycon.close()
    mydb.close()

def menu():
    while True:
        print("Welcome to College Management System ")
        print("1. for addition of data ")
        print("2. for modification of data ")
        print("3. for display of data ")
        print("4. for deletion of data ")
        print("5. for searching of data ")
        print("6. for exiting the program")
        choice=input("enter your choice(1-5): ")

        if choice=="1":
            add_data()
        
        elif choice=="2":
            modify_data()

        elif choice=="3":
            display_data()
        
        elif choice=="4":
            delete_data()
        
        elif choice=="5":
            search_data()
        
        elif choice=="6":
            print("exiting programme!! Good Bye!!")
            break
        else:
            print("Invalid choice . Please enter a number between (1-6) : ")

menu()