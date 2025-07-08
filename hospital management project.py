from config import DB_PASSWORD
import mysql.connector as mys
mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
mycon = mydb.cursor() 

def create_file1():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    mycon.execute("create table if not exists patient(p_id int , name varchar(50) , dob date , gender varchar(20) , address varchar(100) , contact_no bigint , adhaar_no bigint);")
    mydb.commit()

create_file1()

def create_file2():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    mycon.execute("create table if not exists doctor(d_id int , d_name varchar(50) , specialization varchar(100) , contact bigint);")
    mydb.commit()

create_file2()

def create_file3():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    mycon.execute("create table if not exists appointment(appointment_id int PRIMARY KEY , d_id int , p_id int , d_name varchar(50) , p_name varchar(50) , date date , time time , status varchar(50));")
    mydb.commit()

create_file3()

def create_file4():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    mycon.execute("create table if not exists med_record(med_record int PRIMARY KEY , p_id int , appointment_id int , diagnosis varchar(255) , prescription varchar(255) , test_results varchar(255) , date_ofentry date , notes text);")
    mydb.commit()

create_file4()

def create_file5():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    mycon.execute("create table if not exists billing(bill_id int , p_id int , appointment_id int , amount bigint , date_issued date , payment_status varchar(20) , payment_method varchar(20) , due_date date);")
    mydb.commit()

create_file5()

def create_file6():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    mycon.execute("create table if not exists department(department_id int PRIMARY KEY , department_name varchar(100) , location varchar(200));")
    mydb.commit()

create_file6()

def create_file7():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    mycon.execute("create table if not exists room_types(RoomType_id int PRIMARY KEY , room_type varchar(50) , description varchar(100));")
    mydb.commit()

create_file7()

def create_file8():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    mycon.execute("create table if not exists room(room_id int PRIMARY KEY , RoomType_id int , room_no int , capacity int , status varchar(100));")
    mydb.commit()

create_file8()

def create_file9():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    mycon.execute("create table if not exists medicine(med_id int PRIMARY KEY , name varchar(100) , stock int , expiry_date date , dosage varchar(100) , type varchar(50));")
    mydb.commit()

create_file9()

def create_file10():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    mycon.execute("create table if not exists pharmacy(pharmacy_id int PRIMARY KEY , med_id int , p_id int , quantity int , date_dispensed date);")
    mydb.commit()

create_file10()

def create_file11():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    mycon.execute("create table if not exists lab_tests(test_id int PRIMARY KEY , test_name varchar(50) , cost int);")
    mydb.commit()

create_file11()

def create_file12():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    mycon.execute("create table if not exists test_records(record_id int PRIMARY KEY , p_id int , appointment_id int , test_id int , result varchar(50) , date_conducted date);")
    mydb.commit()

create_file12()

def add_record1():
    while True:
        p_id = int(input("enter the patient id : "))
        name = input("enter the name of the patient : ")
        dob = input("enter the date of birth : ")
        gender = input("enter the gender of the patient : ")
        address = input("enter the address of the patient : ")
        contact_no = int(input("enter the contact number of the patient : "))
        adhaar_no = int(input("enter the adhaar number of the patient : "))
        mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
        mycon = mydb.cursor()

        sql = "insert into patient (p_id , name , dob , gender , address , contact_no , adhaar_no) VALUES(%s,%s,%s,%s,%s,%s,%s);"
        values = (p_id , name , dob , gender , address , contact_no , adhaar_no)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("do you want to enter more entries(y/n) : ").strip().lower()
        if ans == 'n':
            print("thank you for entering data about the patient ")
            break
        mycon.close()


def add_record2():
    while True:
        d_id = int(input("enter the doctor id : "))
        d_name = input("enter the name of the doctor : ")
        sp = input("enter the specialisation : ")
        contact = int(input("enter the contact number of the doctor : "))
        mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
        mycon = mydb.cursor()

        sql = "insert into doctor (d_id , d_name , specialization , contact) VALUES(%s,%s,%s,%s);"
        values = (d_id , d_name , sp , contact)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("do you want to enter more entries(y/n) : ").strip().lower()
        if ans == 'n':
            print("thank you for entering data about the doctor ")
            break
        mycon.close()

def add_record3():
    while True:
        a_id = int(input("enter the appointment id : "))
        d_id = input("enter the doctor id : ")
        p_id = input("enter the patient id : ")
        d_name = input("enter the name of the doctor : ")
        p_name = input("enter the name of the patient : ")
        date = input("enter the date of appointment : ")
        time = input("enter the time of the appointment : ")
        status = input("enter the status of the appointment : ")
        mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
        mycon = mydb.cursor()

        sql = "insert into appointment (appointment_id, d_id , p_id , d_name , p_name , date , time , status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"
        values = (a_id , d_id , p_id , d_name , p_name , date , time , status)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("do you want to enter more entries(y/n) : ").strip().lower()
        if ans == 'n':
            print("thank you for entering data about the appointment ")
            break
        mycon.close()

def add_record4():
    while True:
        med_record = int(input("enter the medical record : "))
        p_id = int(input("enter the patient id : "))
        a_id = int(input("enter the appointment id : "))
        diagnosis = input("enter the diagnosis of the patient : ")
        prescription = input("enter the prescription given by the doctor : ")
        test = input("enter the test results : ")
        date = input("enter the date of the entry : ")
        notes = input("enter the notes given by the doctor : ")
        mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
        mycon = mydb.cursor()

        sql = "insert into med_record (med_record , p_id , a_id ,diagnosis , prescription , test_results , date_ofentry , notes) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"
        values = (med_record , p_id , a_id ,diagnosis , prescription , test , date , notes)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("do you want to enter more entries(y/n) : ").strip().lower()
        if ans == 'n':
            print("thank you for entering data about the medical records ")
            break
        mycon.close()

def add_record5():
    while True:
        b_id = int(input("enter the bill id : "))
        p_id = int(input("enter the patient id : "))
        a_id = int(input("enter the appointment id : "))
        amount = int(input("enter the amount : "))
        date_issued = input("enter the date of bill issued : ")
        payment_status = input("enter the payment status : ")
        payment_method = input("enter the payment method : ")
        due_date = input("enter the due date of the bill to be paid : ")
        mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
        mycon = mydb.cursor()
        sql = "insert into billing (bill_id , p_id , appointment_id , amount , date_issued , payment_status , payment_method , due_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"
        values = (b_id , p_id , a_id , amount , date_issued , payment_status , payment_method , due_date)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("do you want to enter more entries(y/n) : ").strip().lower()
        if ans == 'n':
            print("thank you for entering data about the billing records ")
            break
        mycon.close()

def add_record6():
    while True:
        department_id = int(input("enter the department id : "))
        department_name = input("enter the department name : ")
        location = input("enter the location of the department : ")
        mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
        mycon = mydb.cursor()
        sql = "insert into department (department_id , department_name , location) VALUES(%s,%s,%s);"
        values = (department_id , department_name , location)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("do you want to enter more entries(y/n) : ").strip().lower()
        if ans == 'n':
            print("thank you for entering data about the department records ")
            break
        mycon.close()

def add_record7():
    while True:
        r_typeid = int(input("enter the room type id : "))
        r_type = input("enter the room type : ")
        description = input("enter the description : ")
        mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
        mycon = mydb.cursor()
        sql = "insert into room_types (RoomType_id , room_type , description) VALUES(%s,%s,%s);"
        values = (r_typeid , r_type , description)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("do you want to enter more entries(y/n) : ").strip().lower()
        if ans == 'n':
            print("thank you for entering data about the room types records ")
            break
        mycon.close()

def add_record8():
    while True:
        r_id = int(input("enter the room id : "))
        r_typeid = int(input("enter the room type id : "))
        r_no = int(input("enter the room number : "))
        capacity = int(input("enter the capacity : "))
        status = input("enter the status : ")
        mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
        mycon = mydb.cursor()
        sql = "insert into room (room_id , RoomType_id , room_no , capacity , status) VALUES(%s,%s,%s,%s,%s);"
        values = (r_id , r_typeid , r_no , capacity , status)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("do you want to enter more entries(y/n) : ").strip().lower()
        if ans == 'n':
            print("thank you for entering data about the room records ")
            break
        mycon.close()

def add_record9():
    while True:
        med_id = int(input("enter the medicine id : "))
        name = input("enter the name of the medicine : ")
        stock = int(input("enter the stock available of the medicine : "))
        expiry_date = input("enter the expiry date of the medicine : ")
        dosage = input("enter the dosage of the medicine : ")
        type = input("enter the type of medicine : ")
        mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
        mycon = mydb.cursor()
        sql = "insert into medicine (med_id , name , stock , expiry_date , dosage , type) VALUES(%s,%s,%s,%s,%s,%s);"
        values = (med_id , name , stock , expiry_date , dosage , type)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("do you want to enter more entries(y/n) : ").strip().lower()
        if ans == 'n':
            print("thank you for entering data about the medicine records ")
            break
        mycon.close()

def add_record10():
    while True:
        pharmacy_id = int(input("enter the pharmacy id : "))
        med_id = int(input("enter the medicine id : "))
        p_id = int(input("enter the patient id : "))
        quantity = int(input("enter the quantity of the medicine : "))
        date_dispensed = input("enter the date the medicine was dispensed : ")
        mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
        mycon = mydb.cursor()
        sql = "insert into pharmacy (pharmacy_id , med_id , p_id , quantity , date_dispensed) VALUES(%s,%s,%s,%s,%s);"
        values = (pharmacy_id , med_id , p_id , quantity , date_dispensed)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("do you want to enter more entries(y/n) : ").strip().lower()
        if ans == 'n':
            print("thank you for entering data about the pharmacy records ")
            break
        mycon.close()

def add_record11():
    while True:
        test_id = int(input("enter the test id : "))
        test_name = input("enter the name of the test : ")
        cost = int(input("enter the cost of the test : "))
        mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
        mycon = mydb.cursor()
        sql = "insert into lab_tests (test_id , test_name , cost) VALUES(%s,%s,%s);"
        values = (test_id , test_name , cost)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("do you want to enter more entries(y/n) : ").strip().lower()
        if ans == 'n':
            print("thank you for entering data about the lab test records ")
            break
        mycon.close()

def add_record12():
    while True:
        record_id = int(input("enter the record id of the test : "))
        p_id = int(input("enter the patient id : "))
        a_id = int(input("enter the appointment id : "))
        test_id = int(input("enter the test id : "))
        result = input("enter the result of the test : ")
        date_conducted = input("enter the date when the test was conducted : ")
        mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
        mycon = mydb.cursor()
        sql = "insert into test_records (record_id , patient_id , appointment_id , test_id , result , date_conducted) VALUES(%s,%s,%s,%s,%s,%s);"
        values = (record_id , p_id , a_id , test_id , result , date_conducted)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("do you want to enter more entries(y/n) : ").strip().lower()
        if ans == 'n':
            print("thank you for entering data about the test records ")
            break
        mycon.close()

def search_record1():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("enter do you want to search entries (y/n) : ")
        if k!='y':
            print("exiting the search menu : ")
            break
        else:
            print("what do you want to search in this table ? ")
            print("A. for the patient id of the patient")
            print("B. for the name of the patient")
            print("C. for the date of birth of the patient")
            print("D. for the gender of the patient")
            print("E. for the address of the patient")
            print("F. for the contact number of the patient")
            print("G. for the adhaar number of the patient")
            print("H. for the cancellation of the programme")

            ch = input("enter your choice(A-H) : ").strip().upper()
            if ch == 'A':
                pa_id = int(input("enter the patient id to search : "))
                mycon.execute("select * from patient where p_id=%s",(pa_id,))

            elif ch == 'B':
                n = input("enter the name of the patient to search : ")
                mycon.execute("select * from patient where name=%s",(n,))

            elif ch == 'C':
                d = input("enter the date of birth of the patient to search : ")
                mycon.execute("select * from patient where dob=%s",(d,))

            elif ch == 'D':
                g = input("enter the gender of the patient to search : ")
                mycon.execute("select * from patient where gender=%s",(g,))

            elif ch == 'E':
                a = input("enter the address of the patient to search : ")
                mycon.execute("select * from patient where address=%s",(a,))

            elif ch == 'F':
                c_no = int(input("enter the contact number of the patient to search : "))
                mycon.execute("select * from patient where contact_no=%s",(c_no,))

            elif ch == 'G':
                adhaar = int(input("enter the adhaar number of the patient : "))
                mycon.execute("select * from patient where adhhar_no=%s",(adhaar,))
            
            elif ch == 'H':
                print("cancelling the search menu")
                break

            x = mycon.fetchall()
            if not x:
                print("no records found with your search")
            else:
                print("number of records found : ",len(x))
                for row in x:
                    print(row)
    mycon.close()
    mydb.close()

def search_record2():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("enter do you want to search entries (y/n) : ")
        if k!='y':
            print("exiting the search menu : ")
            break
        else:
            print("what do you want to search in this table ? ")
            print("A. for the doctor id of the doctor")
            print("B. for the name of the doctor")
            print("C. for the specialization of the doctor")
            print("D. for the contact number of the doctor")
            print("E. for the cancellation of the programme")

            ch = input("enter your choice(A-E) : ").strip().upper()
            if ch == 'A':
                do_id = int(input("enter the doctor id to search : "))
                mycon.execute("select * from doctor where d_id=%s",(do_id,))

            elif ch == 'B':
                n = input("enter the name of the doctor to search : ")
                mycon.execute("select * from doctor where name=%s",(n,))

            elif ch == 'C':
                s = input("enter the specialization of the doctor to search : ")
                mycon.execute("select * from doctor where specialization=%s",(s,))

            elif ch == 'D':
                c = int(input("enter the contact number of the doctor to search : "))
                mycon.execute("select * from doctor where contact=%s",(c,))

            elif ch == 'E':
                print("cancelling the search menu")
                break

            x = mycon.fetchall()
            if not x:
                print("no records found with your search")
            else:
                print("number of records found : ",len(x))
                for row in x:
                    print(row)
    mycon.close()
    mydb.close()

def search_record3():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("enter do you want to search entries (y/n) : ")
        if k!='y':
            print("exiting the search menu : ")
            break
        else:
            print("what do you want to search in this table ? ")
            print("A. for the appointment id")
            print("B. for the doctor id")
            print("C. for the patient id")
            print("D. for the doctor name")
            print("E. for the patient name")
            print("F. for the date of appointment")
            print("G. for the time of appointment")
            print("H. for the status of appointment")
            print("I. for the cancellation of the programme")

            ch = input("enter your choice(A-H) : ").strip().upper()
            if ch == 'A':
                app_id = int(input("enter the appointment id to search : "))
                mycon.execute("select * from appointment where p_id=%s",(app_id,))

            elif ch == 'B':
                doc = int(input("enter the doctor id to search : "))
                mycon.execute("select * from appointment where d_id=%s",(doc,))

            elif ch == 'C':
                p = int(input("enter the patient id to search : "))
                mycon.execute("select * from appointment where p_id=%s",(p,))

            elif ch == 'D':
                d_n = input("enter the name of the doctor to search : ")
                mycon.execute("select * from appointment where d_name=%s",(d_n,))

            elif ch == 'E':
                p_n = input("enter the patient name to search : ")
                mycon.execute("select * from appointment where p_name=%s",(p_n,))

            elif ch == 'F':
                doa = input("enter the date of appointment to search : ")
                mycon.execute("select * from appointment where date=%s",(doa,))

            elif ch == 'G':
                t = input("enter the time of the appointment to search : ")
                mycon.execute("select * from appointment where time=%s",(t,))
            
            elif ch == 'H':
                st = input("enter the status of the appointment to search : ")
                mycon.execute("select * from appointment where status=%s",(st,))
            elif ch == 'I':
                print("cancelling the search menu")
                break

            x = mycon.fetchall()
            if not x:
                print("no records found with your search")
            else:
                print("number of records found : ",len(x))
                for row in x:
                    print(row)
    mycon.close()
    mydb.close()

def search_record4():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("enter do you want to search entries (y/n) : ")
        if k!='y':
            print("exiting the search menu : ")
            break
        else:
            print("what do you want to search in this table ? ")
            print("A. for the medicine id")
            print("B. for the patient id")
            print("C. for the appointment id")
            print("D. for the diagnosis of the patient")
            print("E. for the prescription given by the doctor")
            print("F. for the test results")
            print("G. for the date of entry")
            print("H. for the notes")
            print("I. for the cancellation of the programme")

            ch = input("enter your choice(A-H) : ").strip().upper()
            if ch == 'A':
                m_id = int(input("enter the medicine id to search : "))
                mycon.execute("select * from med_record where med_id=%s",(m_id,))

            elif ch == 'B':
                p = int(input("enter the patient id to search : "))
                mycon.execute("select * from med_record where p_id=%s",(p,))

            elif ch == 'C':
                a = int(input("enter the appointment id to search : "))
                mycon.execute("select * from med_record where appointment_id=%s",(a,))

            elif ch == 'D':
                diag = input("enter the diagnosis given by doctor to search : ")
                mycon.execute("select * from med_record where diagnosis=%s",(diag,))

            elif ch == 'E':
                pres = input("enter the prescription given to search : ")
                mycon.execute("select * from med_record where prescription=%s",(pres,))

            elif ch == 'F':
                t_r = input("enter the test results to search : ")
                mycon.execute("select * from med_record where test_results=%s",(t_r,))

            elif ch == 'G':
                d_e = input("enter the date of entry of appointment to search : ")
                mycon.execute("select * from med_record where date_ofentry=%s",(d_e,))
            
            elif ch == 'H':
                no = input("enter the notes to search : ")
                mycon.execute("select * from med_record where notes=%s",(no,))
            elif ch == 'I':
                print("cancelling the search menu")
                break

            x = mycon.fetchall()
            if not x:
                print("no records found with your search")
            else:
                print("number of records found : ",len(x))
                for row in x:
                    print(row)
    mycon.close()
    mydb.close()

def search_record5():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("enter do you want to search entries (y/n) : ")
        if k!='y':
            print("exiting the search menu : ")
            break
        else:
            print("what do you want to search in this table ? ")
            print("A. for the bill id")
            print("B. for the patient id")
            print("C. for the appointment id")
            print("D. for the amount")
            print("E. for the date issued")
            print("F. for the payment status")
            print("G. for the payment method")
            print("H. for the due date")
            print("I. for the cancellation of the programme")

            ch = input("enter your choice(A-H) : ").strip().upper()
            if ch == 'A':
                b_id = int(input("enter the bill id to search : "))
                mycon.execute("select * from billing where bill_id=%s",(b_id,))

            elif ch == 'B':
                p = int(input("enter the patient id to search : "))
                mycon.execute("select * from billing where p_id=%s",(p,))

            elif ch == 'C':
                a = int(input("enter the appointment id to search : "))
                mycon.execute("select * from billing where appointment_id=%s",(a,))

            elif ch == 'D':
                am = int(input("enter the amount to search : "))
                mycon.execute("select * from billing where amount=%s",(am,))

            elif ch == 'E':
                d_i= input("enter the issue date of the bill to search : ")
                mycon.execute("select * from billing where date_issued=%s",(d_i,))

            elif ch == 'F':
                p_status = input("enter the payment status to search : ")
                mycon.execute("select * from billing where payment_status=%s",(p_status,))

            elif ch == 'G':
                p_method = input("enter the payment method to search : ")
                mycon.execute("select * from billing where payment_method=%s",(p_method,))
            
            elif ch == 'H':
                dd = input("enter the due date of bill to be paid to search : ")
                mycon.execute("select * from billing where due_date=%s",(dd,))
            elif ch == 'I':
                print("cancelling the search menu")
                break

            x = mycon.fetchall()
            if not x:
                print("no records found with your search")
            else:
                print("number of records found : ",len(x))
                for row in x:
                    print(row)
    mycon.close()
    mydb.close()

def search_record6():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("enter do you want to search entries (y/n) : ")
        if k!='y':
            print("exiting the search menu : ")
            break
        else:
            print("what do you want to search in this table ? ")
            print("A. for the department id")
            print("B. for the department name")
            print("C. for the location")
            print("D. for the cancellation of programme")

            ch = input("enter your choice(A-D) : ").strip().upper()
            if ch == 'A':
                dep_id = int(input("enter the department id to search : "))
                mycon.execute("select * from department where department_id=%s",(dep_id,))

            elif ch == 'B':
                dep_name = input("enter the department name to search : ")
                mycon.execute("select * from department where department_name=%s",(dep_name,))

            elif ch == 'C':
                l = input("enter the location to search : ")
                mycon.execute("select * from department where location=%s",(l,))

            elif ch == 'D':
                print("cancelling the search menu")
                break

            x = mycon.fetchall()
            if not x:
                print("no records found with your search")
            else:
                print("number of records found : ",len(x))
                for row in x:
                    print(row)
    mycon.close()
    mydb.close()

def search_record7():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("enter do you want to search entries (y/n) : ")
        if k!='y':
            print("exiting the search menu : ")
            break
        else:
            print("what do you want to search in this table ? ")
            print("A. for the room type id")
            print("B. for the room type")
            print("C. for the description")
            print("D. for the cancellation of programme")

            ch = input("enter your choice(A-D) : ").strip().upper()
            if ch == 'A':
                roomtype_id = int(input("enter the room type id to search : "))
                mycon.execute("select * from room_types where RoomType_id=%s",(roomtype_id,))

            elif ch == 'B':
                room_type = input("enter the type of room to search : ")
                mycon.execute("select * from room_types where room_type=%s",(room_type,))

            elif ch == 'C':
                desc = input("enter the description about the room type to search : ")
                mycon.execute("select * from room_types where description=%s",(desc,))

            elif ch == 'D':
                print("cancelling the search menu")
                break

            x = mycon.fetchall()
            if not x:
                print("no records found with your search")
            else:
                print("number of records found : ",len(x))
                for row in x:
                    print(row)
    mycon.close()
    mydb.close()

def search_record8():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("enter do you want to search entries (y/n) : ")
        if k!='y':
            print("exiting the search menu : ")
            break
        else:
            print("what do you want to search in this table ? ")
            print("A. for the room id")
            print("B. for the room type id")
            print("C. for the room number")
            print("D. for the capacity")
            print("E. for the status")
            print("F. for the cancellation of programme")

            ch = input("enter your choice(A-F) : ").strip().upper()
            if ch == 'A':
                room_id = int(input("enter the room id to search : "))
                mycon.execute("select * from room where room_id=%s",(room_id,))

            elif ch == 'B':
                roomtype_id = input("enter the room type id to search : ")
                mycon.execute("select * from room where RoomType_id=%s",(roomtype_id,))

            elif ch == 'C':
                room_no = int(input("enter the room number to search : "))
                mycon.execute("select * from room where room_no=%s",(room_no,))

            elif ch == 'D':
                capacity = int(input("enter the capacity of the rooms to search : "))
                mycon.execute("select * from room where capacity=%s",(capacity,))

            elif ch == 'E':
                status = input("enter the status of the room to search : ")
                mycon.execute("select * from room where status=%s",(status,))

            elif ch == 'F':
                print("cancelling the search menu")
                break

            x = mycon.fetchall()
            if not x:
                print("no records found with your search")
            else:
                print("number of records found : ",len(x))
                for row in x:
                    print(row)
    mycon.close()
    mydb.close()

def search_record9():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("enter do you want to search entries (y/n) : ")
        if k!='y':
            print("exiting the search menu : ")
            break
        else:
            print("what do you want to search in this table ? ")
            print("A. for the medicine id")
            print("B. for the name")
            print("C. for the stock")
            print("D. for the expiry date")
            print("E. for the dosage")
            print("F. for the type")
            print("G. for the cancellation of programme")

            ch = input("enter your choice(A-G) : ").strip().upper()
            if ch == 'A':
                med_id = int(input("enter the medicine id to search : "))
                mycon.execute("select * from medicine where med_id=%s",(med_id,))

            elif ch == 'B':
                name = input("enter the medicine name to search : ")
                mycon.execute("select * from medicine where name=%s",(name,))

            elif ch == 'C':
                stock = int(input("enter the stock of medicine to search : "))
                mycon.execute("select * from medicine where stock=%s",(stock,))

            elif ch == 'D':
                expiry_date = input("enter the expiry date of the rooms to search : ")
                mycon.execute("select * from medicine where expiry_date=%s",(expiry_date,))

            elif ch == 'E':
                dosage = input("enter the medicine dosage to search : ")
                mycon.execute("select * from medicine where dosage=%s",(dosage,))

            elif ch == 'F':
                type = input("enter the type of medicine to search : ")
                mycon.execute("select * from medicine where type=%s",(type,))

            elif ch == 'G':
                print("cancelling the search menu")
                break

            x = mycon.fetchall()
            if not x:
                print("no records found with your search")
            else:
                print("number of records found : ",len(x))
                for row in x:
                    print(row)
    mycon.close()
    mydb.close()

def search_record10():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("enter do you want to search entries (y/n) : ")
        if k!='y':
            print("exiting the search menu : ")
            break
        else:
            print("what do you want to search in this table ? ")
            print("A. for the pharmacy id")
            print("B. for the medicine id")
            print("C. for the patient id")
            print("D. for the quantity")
            print("E. for the date dispensed")
            print("F. for the cancellation of programme")

            ch = input("enter your choice(A-F) : ").strip().upper()
            if ch == 'A':
                pharmacy_id = int(input("enter the pharmacy id to search : "))
                mycon.execute("select * from pharmacy where pharmacy_id=%s",(pharmacy_id,))

            elif ch == 'B':
                med_id = int(input("enter the medicine id to search : "))
                mycon.execute("select * from pharmacy where med_id=%s",(med_id,))

            elif ch == 'C':
                p_id = int(input("enter the patient id to search : "))
                mycon.execute("select * from pharmacy where p_id=%s",(p_id,))

            elif ch == 'D':
                quantity = int(input("enter the quantity to search : "))
                mycon.execute("select * from pharmacy where quantity=%s",(quantity,))

            elif ch == 'E':
                date_dispensed = input("enter the date the medicine dispensed to search : ")
                mycon.execute("select * from pharmacy where date_dispensed=%s",(date_dispensed,))

            elif ch == 'F':
                print("cancelling the search menu")
                break

            x = mycon.fetchall()
            if not x:
                print("no records found with your search")
            else:
                print("number of records found : ",len(x))
                for row in x:
                    print(row)
    mycon.close()
    mydb.close()

def search_record11():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("enter do you want to search entries (y/n) : ")
        if k!='y':
            print("exiting the search menu : ")
            break
        else:
            print("what do you want to search in this table ? ")
            print("A. for the test id")
            print("B. for the test name")
            print("C. for the cost")
            print("D. for the cancellation of programme")

            ch = input("enter your choice(A-D) : ").strip().upper()
            if ch == 'A':
                test_id = int(input("enter the test id to search : "))
                mycon.execute("select * from lab_tests where test_id=%s",(test_id,))

            elif ch == 'B':
                test_name = input("enter the test name to search : ")
                mycon.execute("select * from lab_tests where test_name=%s",(test_name,))

            elif ch == 'C':
                cost = int(input("enter the cost to search : "))
                mycon.execute("select * from lab_tests where cost=%s",(cost,))

            elif ch == 'D':
                print("cancelling the search menu")
                break

            x = mycon.fetchall()
            if not x:
                print("no records found with your search")
            else:
                print("number of records found : ",len(x))
                for row in x:
                    print(row)
    mycon.close()
    mydb.close()

def search_record12():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("enter do you want to search entries (y/n) : ")
        if k!='y':
            print("exiting the search menu : ")
            break
        else:
            print("what do you want to search in this table ? ")
            print("A. for the record id")
            print("B. for the patient id")
            print("C. for the appointment id")
            print("D. for the test id")
            print("E. for the result")
            print("F. for the date the result was conducted")
            print("G. for the cancellation of programme")

            ch = input("enter your choice(A-G) : ").strip().upper()
            if ch == 'A':
                record_id = int(input("enter the record id to search : "))
                mycon.execute("select * from test_records where record_id=%s",(record_id,))

            elif ch == 'B':
                p_id = int(input("enter the patient id to search : "))
                mycon.execute("select * from test_records where patient_id=%s",(p_id,))

            elif ch == 'C':
                a_id = int(input("enter the appointment id to search : "))
                mycon.execute("select * from test_records where appointment_id=%s",(a_id,))

            elif ch == 'D':
                t_id = int(input("enter the test id to search : "))
                mycon.execute("select * from test_records where test_id=%s",(t_id,))

            elif ch == 'E':
                result = input("enter the result to search : ")
                mycon.execute("select * from test_records where result=%s",(result,))
            
            elif ch == 'F':
                d_conducted = input("enter the date the test was conducted to search : ")
                mycon.execute("select * from test_records where date_conducted=%s",(d_conducted,))

            elif ch == 'G':
                print("cancelling the search menu")
                break

            x = mycon.fetchall()
            if not x:
                print("no records found with your search")
            else:
                print("number of records found : ",len(x))
                for row in x:
                    print(row)
    mycon.close()
    mydb.close()

def update_record1():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the updation menu")
            break
        
        p_id = input("enter the patient id : ").strip()
        if not p_id:
            print("patient id is required")
            continue
        
        print("what do you want to update in this table ? ")
        print("A. for the patient id of the patient")
        print("B. for the name of the patient")
        print("C. for the date of birth of the patient")
        print("D. for the gender of the patient")
        print("E. for the address of the patient")
        print("F. for the contact number of the patient")
        print("G. for the adhaar number of the patient")
        print("H. for the cancellation of the programme")

        ch = input("enter your choice(A-H) : ").strip().upper()
        if ch == 'A':
            pat_id = int(input("enter the new patient id of the patient : "))
            if pat_id:
                mycon.execute("update patient set p_id=%s where p_id=%s",(int(pat_id),p_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'B':
            na = input("enter the new name of the patient : ")
            if pat_id:
                mycon.execute("update patient set name=%s where p_id=%s",(na,p_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'C':
            d_ofbirth = input("enter the new date of birth of the patient : ")
            if d_ofbirth:
                mycon.execute("update patient set dob=%s where p_id=%s",(d_ofbirth,p_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'D':
            g = input("enter the new gender of the patient : ")
            if g:
                mycon.execute("update patient set gender=%s where p_id=%s",(g,p_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'E':
            add = input("enter the new address of the patient : ")
            if add:
                mycon.execute("update patient set address=%s where p_id=%s",(add,p_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'F':
            c_no = int(input("enter the new contact number of the patient : "))
            if c_no:
                mycon.execute("update patient set contact_no=%s where p_id=%s",(int(c_no),p_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'G':
            adhr = int(input("enter the new adhaar number of the patient : "))
            if pat_id:
                mycon.execute("update patient set adhaar_no=%s where p_id=%s",(int(adhr),p_id))
                print("record updated")
                mydb.commit()
                mycon.close()
            
        elif ch == 'H':
            print("sorry ! no information updated !")
            break

def update_record2():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the updation menu")
            break
        
        d_id = input("enter the patient id : ").strip()
        if not d_id:
            print("patient id is required")
            continue
        
        print("what do you want to update in this table ? ")
        print("A. for the doctor id of the doctor")
        print("B. for the name of the doctor")
        print("C. for the specialization of the doctor")
        print("D. for the contact number of the doctor")
        print("E. for the cancellation of the programme")

        ch = input("enter your choice(A-E) : ").strip().upper()
        if ch == 'A':
            doc_id = int(input("enter the new doctor id of the doctor : "))
            if doc_id:
                mycon.execute("update doctor set d_id=%s where d_id=%s",(int(doc_id),d_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'B':
            doc_name = input("enter the new name of the doctor : ")
            if doc_name:
                mycon.execute("update doctor set d_name=%s where d_id=%s",(doc_name, d_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'C':
            sp = input("enter the specialization of the doctor : ")
            if sp:
                mycon.execute("update doctor set specialization=%s where d_id=%s",(sp, d_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'D':
            c_no = int(input("enter the contact number of the doctor : "))
            if c_no:
                mycon.execute("update doctor set contact=%s where d_id=%s",(int(c_no), d_id))
                print("record updated")
                mydb.commit()
                mycon.close()
            
        elif ch == 'E':
            print("sorry ! no information updated !")
            break

def update_record3():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the updation menu")
            break
        
        appointment_id = input("enter the appointment id").strip()
        if not appointment_id:
            print("appointment id is required")
            continue
        
        print("what do you want to update in this table ? ")
        print("A. for the appointment id")
        print("B. for the doctor id")
        print("C. for the patient id")
        print("D. for the name of the doctor")
        print("E. for the name of the patient")
        print("F. for the date of the appointment")
        print("G. for the time of the appointment")
        print("H. for the status of the doctor")
        print("I. for the cancellation of the programme")

        ch = input("enter your choice(A-I) : ").strip().upper()
        if ch == 'A':
            a_id = int(input("enter the new appointment id : "))
            if a_id:
                mycon.execute("update appointment set appointment_id=%s where appointment_id=%s",(int(a_id),appointment_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'B':
            d_id = int(input("enter the new doctor id : "))
            if d_id:
                mycon.execute("update appointment set d_id=%s where appointment_id=%s",(int(d_id),appointment_id))
                print("record updated")
                mydb.commit()
                mycon.close()


        elif ch == 'C':
            p_id = int(input("enter the new patient id : "))
            if a_id:
                mycon.execute("update appointment set p_id=%s where appointment_id=%s",(int(p_id),appointment_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'D':
            d_name = input("enter the new name of the doctor : ")
            if d_name:
                mycon.execute("update appointment set d_name=%s where appointment_id=%s",(d_name,appointment_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'E':
            p_name = input("enter the new name of the patient : ")
            if p_name:
                mycon.execute("update appointment set p_name=%s where appointment_id=%s",(p_name,appointment_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'F':
            doa = input("enter the new date of appointment : ")
            if doa:
                mycon.execute("update appointment set date=%s where appointment_id=%s",(doa,appointment_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'G':
            time = input("enter the new time of the appointment : ")
            if time:
                mycon.execute("update appointment set time=%s where appointment_id=%s",(time,appointment_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'H':
            st = input("enter the new status of the appointment : ")
            if st:
                mycon.execute("update appointment set status=%s where appointment_id=%s",(st,appointment_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'I':
            print("sorry ! no information updated !")
            break

def update_record4():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the updation menu")
            break
        
        med_record = input("enter the medical record : ").strip()
        if not med_record:
            print("medical record is required")
            continue
        
        print("what do you want to update in this table ? ")
        print("A. for the medical record")
        print("B. for the patient id")
        print("C. for the appointment id")
        print("D. for the diagnosis by the doctor")
        print("E. for the prescription by the doctor")
        print("F. for the test results")
        print("G. for the date of entry of the record")
        print("H. for the notes given by the doctor")
        print("I. for the cancellation of the programme")

        ch = input("enter your choice(A-I) : ").strip().upper()
        if ch == 'A':
            m_record = int(input("enter the new medical record : "))
            if m_record:
                mycon.execute("update med_record set med_record=%s where med_record=%s",(int(m_record),med_record))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'B':
            pat_id = int(input("enter the new patient id : "))
            if pat_id:
                mycon.execute("update med_record set p_id=%s where med_record=%s",(int(pat_id),med_record))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'C':
            a_id = int(input("enter the new appointment id : "))
            if a_id:
                mycon.execute("update med_record set appointment_id=%s where med_record=%s",(int(a_id),med_record))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'D':
            d = input("enter the new diagnosis : ")
            if d:
                mycon.execute("update med_record set diagnosis=%s where med_record=%s",(d,med_record))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'E':
            p = input("enter the new prescription : ")
            if p:
                mycon.execute("update med_record set prescription=%s where med_record=%s",(p,med_record))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'F':
            t_results = input("enter the new test results : ")
            if t_results:
                mycon.execute("update med_record set test_results=%s where med_record=%s",(t_results,med_record))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'G':
            dat = input("enter the new date : ")
            if dat:
                mycon.execute("update med_record set date=%s where med_record=%s",(dat,med_record))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'H':
           notes = input("enter the new notes : ")
           if notes:
                mycon.execute("update med_record set notes=%s where med_record=%s",(notes,med_record))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'I':
            print("sorry ! no information updated !")
            break

def update_record5():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the updation menu")
            break
        
        b_id = input("enter the bill id :").strip()
        if not b_id:
            print("bill id is required")
            continue
        
        print("what do you want to update in this table ? ")
        print("A. for the bill id")
        print("B. for the patient id")
        print("C. for the appointment id")
        print("D. for the amount")
        print("E. for the issue date of the bill")
        print("F. for the payment status")
        print("G. for the payment method")
        print("H. for the due date of the bill to be paid")
        print("I. for the cancellation of the programme")

        ch = input("enter your choice(A-I) : ").strip().upper()
        if ch == 'A':
            b_id = int(input("enter the new bill id : "))
            if b_id:
                mycon.execute("update billing set bill_id=%s where bill_id=%s",(int(b_id),b_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'B':
            p_id = int(input("enter the new patient id : "))
            if p_id:
                mycon.execute("update billing set p_id=%s where bill_id=%s",(int(p_id),b_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'C':
            a_id = int(input("enter the new appointment id : "))
            if a_id:
                mycon.execute("update billing set appointment_id=%s where bill_id=%s",(int(a_id),b_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'D':
            a = int(input("enter the amount : "))
            if a:
                mycon.execute("update billing set amount=%s where bill_id=%s",(int(a),b_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'E':
            d_issue = input("enter the new issue date of the bill : ")
            if d_issue:
                mycon.execute("update billing set date_issued=%s where bill_id=%s",(d_issue,b_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'F':
            p_status = input("enter the new payment status : ")
            if p_status:
                mycon.execute("update billing set payment_status=%s where bill_id=%s",(p_status,b_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'G':
            p_method = input("enter the new payment method : ")
            if p_method:
                mycon.execute("update billing set payment_method=%s where bill_id=%s",(p_method,b_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'H':
           d_date = input("enter the new due date : ")
           if d_date:
                mycon.execute("update billing set due_date=%s where bill_id=%s",(d_date,b_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'I':
            print("sorry ! no information updated !")
            break

def update_record6():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the updation menu")
            break
        
        d_id = input("enter the department id :").strip()
        if not d_id:
            print("bill id is required")
            continue
        
        print("what do you want to update in this table ? ")
        print("A. for the department id")
        print("B. for the department name")
        print("C. for the location")
        print("D. for the cancellation of the programme")

        ch = input("enter your choice(A-D) : ").strip().upper()
        if ch == 'A':
            dep_id = int(input("enter the new department id : "))
            if d_id:
                mycon.execute("update department set department_id=%s where department_id=%s",(int(dep_id),d_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'B':
            dep_name = input("enter the new department name : ")
            if dep_name:
                mycon.execute("update department set department_name=%s where department_id=%s",(dep_name,d_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'C':
            loc = input("enter the new location : ")
            if loc:
                mycon.execute("update department set location=%s where department_id=%s",(loc,d_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'D':
            print("sorry ! no information updated !")
            break

def update_record7():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the updation menu")
            break
        
        r_typeid = input("enter the room type id :").strip()
        if not r_typeid:
            print("room type id is required")
            continue
        
        print("what do you want to update in this table ? ")
        print("A. for the room type id")
        print("B. for the room type")
        print("C. for the description")
        print("D. for the cancellation of the programme")

        ch = input("enter your choice(A-D) : ").strip().upper()
        if ch == 'A':
            ro_typeid = int(input("enter the new room type id : "))
            if ro_typeid:
                mycon.execute("update room_types set RoomType_id=%s where RoomType_id=%s",(int(ro_typeid),r_typeid))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'B':
            ro_type = input("enter the new room type : ")
            if ro_type:
                mycon.execute("update room_types set room_type=%s where RoomType_id=%s",(ro_type,r_typeid))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'C':
            desc = input("enter the description : ")
            if desc:
                mycon.execute("update room_types set description=%s where RoomType_id=%s",(desc,r_typeid))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'D':
            print("sorry ! no information updated !")
            break

def update_record8():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the updation menu")
            break
        
        r_id = input("enter the room id :").strip()
        if not r_id:
            print("room id is required")
            continue
        
        print("what do you want to update in this table ? ")
        print("A. for the room id")
        print("B. for the room type id")
        print("C. for the room number")
        print("D. for the capacity")
        print("E. for the status")
        print("F. for the cancellation of the programme")

        ch = input("enter your choice(A-f) : ").strip().upper()
        if ch == 'A':
            ro_id = int(input("enter the new room id : "))
            if ro_id:
                mycon.execute("update room set room_id=%s where room_id=%s",(int(ro_id),r_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'B':
            ro_typeid = int(input("enter the new room type id : "))
            if ro_typeid:
                mycon.execute("update room set RoomType_id=%s where room_id=%s",(int(ro_typeid),r_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'C':
            ro_no = int(input("enter the new room id : "))
            if ro_no:
                mycon.execute("update room set room_no=%s where room_id=%s",(int(ro_no),r_id))
                print("record updated")
                mydb.commit()
                mycon.close()
                
        elif ch == 'D':
            cap = int(input("enter the capacity : "))
            if cap:
                mycon.execute("update room set capacity=%s where room_id=%s",(int(cap),r_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'E':
            st = input("enter the new status : ")
            if st:
                mycon.execute("update room set status=%s where room_id=%s",(st,r_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'F':
            print("sorry ! no information updated !")
            break

def update_record9():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the updation menu")
            break
        
        med_id = input("enter the medical id :").strip()
        if not med_id:
            print("medical id is required")
            continue
        
        print("what do you want to update in this table ? ")
        print("A. for the medical id")
        print("B. for the name")
        print("C. for the stock")
        print("D. for the expiry date")
        print("E. for the dosage")
        print("F. for the type")
        print("G. for the cancellation of the programme")

        ch = input("enter your choice(A-G) : ").strip().upper()
        if ch == 'A':
            m_id = int(input("enter the new medical id : "))
            if m_id:
                mycon.execute("update medicine set med_id=%s where med_id=%s",(int(m_id),med_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'B':
            n = input("enter the new name : ")
            if n:
                mycon.execute("update medicine set name=%s where med_id=%s",(n,med_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'C':
            s = int(input("enter the new stock : "))
            if s:
                mycon.execute("update medicine set stock=%s where med_id=%s",(int(s),med_id))
                print("record updated")
                mydb.commit()
                mycon.close()
        elif ch == 'D':
            exp_date = input("enter the new expiry date : ")
            if exp_date:
                mycon.execute("update medicine set expiry_date=%s where med_id=%s",(exp_date,med_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'E':
            dos = int(input("enter the new dosage : "))
            if dos:
                mycon.execute("update medicine set dosage=%s where med_id=%s",(int(dos),med_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'F':
            t = input("enter the new type : ")
            if t:
                mycon.execute("update medicine set type=%s where med_id=%s",(t,med_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'G':
            print("sorry ! no information updated !")
            break

def update_record10():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the updation menu")
            break
        
        pharmacy_id = input("enter the pharmacy id :").strip()
        if not pharmacy_id:
            print("pharmacy id is required")
            continue
        
        print("what do you want to update in this table ? ")
        print("A. for the pharmacy id")
        print("B. for the medical id")
        print("C. for the patient id")
        print("D. for the quantity")
        print("E. for the date dispensed")
        print("F. for the cancellation of the programme")

        ch = input("enter your choice(A-F) : ").strip().upper()
        if ch == 'A':
            ph_id = int(input("enter the new pharmacy id : "))
            if ph_id:
                mycon.execute("update pharmacy set pharmacy_id=%s where pharmacy_id=%s",(int(ph_id),pharmacy_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'B':
            m_id = int(input("enter the new medical id : "))
            if m_id:
                mycon.execute("update pharmacy set med_id=%s where pharmacy_id=%s",(int(m_id),pharmacy_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'C':
            pat_id = int(input("enter the new patient id : "))
            if ph_id:
                mycon.execute("update pharmacy set pat_id=%s where pharmacy_id=%s",(int(pat_id),pharmacy_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'D':
            q = int(input("enter the new quantity : "))
            if q:
                mycon.execute("update pharmacy set quantity=%s where pharmacy_id=%s",(int(q),pharmacy_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'E':
            d_disp = input("enter the new dispensed date of the medicine : ")
            if d_disp:
                mycon.execute("update pharmacy set date_dispensed=%s where pharmacy_id=%s",(int(d_disp),pharmacy_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'F':
            print("sorry ! no information updated !")
            break

def update_record11():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the updation menu")
            break
        
        test_id = input("enter the test id :").strip()
        if not test_id:
            print("test id is required")
            continue
        
        print("what do you want to update in this table ? ")
        print("A. for the test id")
        print("B. for the test name")
        print("C. for the cost")
        print("D. for the cancellation of the programme")

        ch = input("enter your choice(A-D) : ").strip().upper()
        if ch == 'A':
            t_id = int(input("enter the new test id : "))
            if t_id:
                mycon.execute("update lab_tests set test_id=%s where test_id=%s",(int(t_id),test_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'B':
            t_name = input("enter the new test name : ")
            if t_name:
                mycon.execute("update lab_tests set test_name=%s where test_id=%s",(t_name,test_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'C':
            c = int(input("enter the new cost : "))
            if c:
                mycon.execute("update lab_tests set cost=%s where test_id=%s",(int(c),test_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'D':
            print("sorry ! no information updated !")
            break

def update_record12():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the updation menu")
            break
        
        record_id = input("enter the record id :").strip()
        if not record_id:
            print("record id is required")
            continue
        
        print("what do you want to update in this table ? ")
        print("A. for the record id")
        print("B. for the patient id")
        print("C. for the appointment id")
        print("D. for the test id")
        print("E. for the result")
        print("F. for the date conducted")
        print("G. for the cancellation of the programme")

        ch = input("enter your choice(A-G) : ").strip().upper()
        if ch == 'A':
            rec_id = int(input("enter the new record id : "))
            if rec_id:
                mycon.execute("update test_records set record_id=%s where record_id=%s",(int(rec_id),record_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'B':
            pat_id = int(input("enter the new patient id : "))
            if pat_id:
                mycon.execute("update test_records set p_id=%s where record_id=%s",(int(pat_id),record_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'C':
            app_id = int(input("enter the new appointment id : "))
            if app_id:
                mycon.execute("update test_records set appointment_id=%s where record_id=%s",(int(app_id),record_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'D':
            t_id = int(input("enter the new test id : "))
            if t_id:
                mycon.execute("update test_records set test_id=%s where record_id=%s",(int(t_id),record_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'E':
            res = input("enter the new result : ")
            if res:
                mycon.execute("update test_records set result=%s where record_id=%s",(res,record_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'F':
            d_conduct = input("enter the new date the test was conducted : ")
            if d_conduct:
                mycon.execute("update test_records set date_conducted=%s where record_id=%s",(d_conduct,record_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'G':
            print("sorry ! no information updated !")
            break

def delete_record1():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to delete entries (y/n) ? ")
        if k!='y':
            print("exiting the deletion menu")
            break
        else:
            print("what do you want to delete in this table ? ")
            print("A. for the patient id of the patient")
            print("B. for the name of the patient")
            print("C. for the date of birth of the patient")
            print("D. for the gender of the patient")
            print("E. for the address of the patient")
            print("F. for the contact number of the patient")
            print("G. for the adhaar number of the patient")
            print("H. for the cancellation of the programme")

            ch = input("enter your choice(A-H) : ").strip().upper()
            if ch == 'A':
                pat_id = int(input("enter the  patient id of the patient to delete : "))
                mycon.execute("select * from patient where p_id=%s;",(pat_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such patient id")
                else:
                    mycon.execute("delete from patient where p_id=%s;",(pat_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'B':
                nam = input("enter the  name of the patient to delete : ")
                mycon.execute("select * from patient where name=%s;",(nam,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such patient name")
                else:
                    mycon.execute("delete from patient where name=%s;",(nam,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'C':
                d_ob = input("enter the  date of birth of patient to delete : ")
                mycon.execute("select * from patient where dob=%s;",(d_ob,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such patient having this dob")
                else:
                    mycon.execute("delete from patient where dob=%s;",(d_ob,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'D':
                ge = input("enter the  gender of patient to delete : ")
                mycon.execute("select * from patient where gender=%s;",(ge,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such patient having this gender")
                else:
                    mycon.execute("delete from patient where gender=%s;",(ge,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'E':
                add = input("enter the address of patient to delete : ")
                mycon.execute("select * from patient where address=%s;",(add,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such patient having this address")
                else:
                    mycon.execute("delete from patient where address=%s;",(add,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'F':
                c_no = int(input("enter the contact number of patient to delete : "))
                mycon.execute("select * from patient where contact_no=%s;",(c_no,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such patient having this contact number")
                else:
                    mycon.execute("delete from patient where contact_no=%s;",(c_no,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'G':
                adhr_no = int(input("enter the adhaar number of patient to delete : "))
                mycon.execute("select * from patient where adhaar_no=%s;",(adhr_no,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such patient having this adhaar number")
                else:
                    mycon.execute("delete from patient where adhaar_no=%s;",(adhr_no,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'H':
                print("sorry ! no record deleted")
                break

def delete_record2():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the deletion menu")
            break
        else:
            print("what do you want to delete in this table ? ")
            print("A. for the doctor id of the doctor")
            print("B. for the name of the doctor")
            print("C. for the specialization of the doctor")
            print("D. for the contact number of the doctor")
            print("E. for the cancellation of the programme")

            ch = input("enter your choice(A-E) : ").strip().upper()
            if ch == 'A':
                doc_id = int(input("enter the  doctor id of the doctor to delete : "))
                mycon.execute("select * from doctor where d_id=%s;",(doc_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such doctor id")
                else:
                    mycon.execute("delete from doctor where d_id=%s;",(doc_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'B':
                doc_name = input("enter the name of the doctor to delete : ")
                mycon.execute("select * from doctor where d_name=%s;",(doc_name,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such doctor name")
                else:
                    mycon.execute("delete from doctor where d_name=%s;",(doc_name,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'C':
                spec = input("enter the specialization of the doctor to delete : ")
                mycon.execute("select * from doctor where specialization=%s;",(spec,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such specialization")
                else:
                    mycon.execute("delete from doctor where specialization=%s;",(spec,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'D':
                co = int(input("enter the contact number of the doctor to delete : "))
                mycon.execute("select * from doctor where contact=%s;",(co,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such contact number")
                else:
                    mycon.execute("delete from doctor where contact=%s;",(co,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'E':
                print("sorry ! no record deleted")
                break

def delete_record3():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the deletion menu")
            break
        else:
            print("what do you want to delete in this table ? ")
            print("A. for the appointment id")
            print("B. for the doctor id")
            print("C. for the patient id")
            print("D. for the doctor name")
            print("E. for the patient name")
            print("F. for the date of appointment")
            print("G. for the time of appointment")
            print("H. for the status of appointment")
            print("I. for the cancellation of the programme")

            ch = input("enter your choice(A-I) : ").strip().upper()
            if ch == 'A':
                app_id = int(input("enter the appointment id of the patient to delete : "))
                mycon.execute("select * from appointment where appointment_id=%s;",(app_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such appointment id")
                else:
                    mycon.execute("delete from appointment where appointment_id=%s;",(app_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'B':
                doc_id = int(input("enter the doctor id to delete : "))
                mycon.execute("select * from appointment where d_id=%s;",(doc_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such doctor id")
                else:
                    mycon.execute("delete from appointment where d_id=%s;",(doc_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'C':
                pat_id = int(input("enter the patient id to delete : "))
                mycon.execute("select * from appointment where p_id=%s;",(pat_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such patient id")
                else:
                    mycon.execute("delete from appointment where p_id=%s;",(pat_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'D':
                doc_name = input("enter the doctor name to delete : ")
                mycon.execute("select * from appointment where d_name=%s;",(doc_name,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such doctor name")
                else:
                    mycon.execute("delete from appointment where d_name=%s;",(doc_name,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'E':
                pat_name = input("enter the patient name to delete : ")
                mycon.execute("select * from appointment where p_name=%s;",(pat_name,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such patient name")
                else:
                    mycon.execute("delete from appointment where p_name=%s;",(pat_name,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'F':
                doa = input("enter the date of appointment to delete : ")
                mycon.execute("select * from appointment where date=%s;",(doa,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such date of appointment")
                else:
                    mycon.execute("delete from appointment where date=%s;",(doa,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'G':
                t = input("enter the time to delete : ")
                mycon.execute("select * from appointment where time=%s;",(t,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such time")
                else:
                    mycon.execute("delete from appointment where time=%s;",(t,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'H':
                s = input("enter the status to delete : ")
                mycon.execute("select * from appointment where status=%s;",(s,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such status")
                else:
                    mycon.execute("delete from appointment where status=%s;",(s,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'I':
                print("sorry ! no record deleted")
                break

def delete_record4():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the deletion menu")
            break
        else:
            print("what do you want to update in this table ? ")
            print("A. for the medical record")
            print("B. for the patient id")
            print("C. for the appointment id")
            print("D. for the diagnosis by the doctor")
            print("E. for the prescription by the doctor")
            print("F. for the test results")
            print("G. for the date of entry of the record")
            print("H. for the notes given by the doctor")
            print("I. for the cancellation of the programme")

            ch = input("enter your choice(A-I) : ").strip().upper()
            if ch == 'A':
                m_id = int(input("enter the medicine id to delete : "))
                mycon.execute("select * from med_record where med_record=%s;",(m_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such medical id")
                else:
                    mycon.execute("delete from med_record where med_record=%s;",(m_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'B':
                pat_id = int(input("enter the patient id to delete : "))
                mycon.execute("select * from med_record where p_id=%s;",(pat_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such patient id")
                else:
                    mycon.execute("delete from med_record where p_id=%s;",(pat_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'C':
                app_id = int(input("enter the appointment id to delete : "))
                mycon.execute("select * from med_record where appointment_id=%s;",(app_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such appointment id")
                else:
                    mycon.execute("delete from med_record where appointment_id=%s;",(app_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'D':
                dia = input("enter the diagnosis to delete : ")
                mycon.execute("select * from med_record where diagnosis=%s;",(dia,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such diagnosis")
                else:
                    mycon.execute("delete from med_record where diagnosis=%s;",(dia,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'E':
                presc = input("enter the prescription to delete : ")
                mycon.execute("select * from med_record where prescription=%s;",(presc,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such prescription")
                else:
                    mycon.execute("delete from med_record where prescription=%s;",(presc,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'F':
                t_results = input("enter the test results to delete : ")
                mycon.execute("select * from med_record where test_results=%s;",(t_results,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such test results")
                else:
                    mycon.execute("delete from med_record where test_results=%s;",(t_results,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'G':
                doe = input("enter the date of entry to delete : ")
                mycon.execute("select * from med_record where date_ofentry=%s;",(doe,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such date of entry")
                else:
                    mycon.execute("delete from med_record where date_ofentry=%s;",(doe,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'H':
                note = input("enter the notes to delete : ")
                mycon.execute("select * from med_record where notes=%s;",(note,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such notes")
                else:
                    mycon.execute("delete from med_record where notes=%s;",(note,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'I':
                print("sorry ! no record deleted")
                break

def delete_record5():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the deletion menu")
            break
        else:
            print("what do you want to update in this table ? ")
            print("A. for the bill id")
            print("B. for the patient id")
            print("C. for the appointment id")
            print("D. for the amount")
            print("E. for the issue date of the bill")
            print("F. for the payment status")
            print("G. for the payment method")
            print("H. for the due date of the bill to be paid")
            print("I. for the cancellation of the programme")

            ch = input("enter your choice(A-I) : ").strip().upper()
            if ch == 'A':
                b_id = int(input("enter the bill id to delete : "))
                mycon.execute("select * from billing where bill_id=%s;",(b_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such bill id")
                else:
                    mycon.execute("delete from billing where bill_id=%s;",(b_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'B':
                pat_id = int(input("enter the patient id to delete : "))
                mycon.execute("select * from billing where p_id=%s;",(pat_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such patient id")
                else:
                    mycon.execute("delete from billing where p_id=%s;",(pat_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'C':
                app_id = int(input("enter the appointment id to delete : "))
                mycon.execute("select * from billing where appointment_id=%s;",(app_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such appointment id")
                else:
                    mycon.execute("delete from billing where appointment_id=%s;",(app_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'D':
                amt = int(input("enter the amount to delete : "))
                mycon.execute("select * from billing where amount=%s;",(amt,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such amount")
                else:
                    mycon.execute("delete from billing where amount=%s;",(amt,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'E':
                d_i = input("enter the issue date to delete : ")
                mycon.execute("select * from billing where date_issued=%s;",(d_i,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such issue date")
                else:
                    mycon.execute("delete from billing where date_issued=%s;",(d_i,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'F':
                p_stat = input("enter the payment status to delete : ")
                mycon.execute("select * from billing where payment_status=%s;",(p_stat,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such payment status")
                else:
                    mycon.execute("delete from billing where payment_status=%s;",(p_stat,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'G':
                p_method = input("enter the payment method to delete : ")
                mycon.execute("select * from billing where payment_method=%s;",(p_method,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such payment method")
                else:
                    mycon.execute("delete from billing where payment_method=%s;",(p_method,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'H':
                du_date = input("enter the due date to delete : ")
                mycon.execute("select * from billing where due_date=%s;",(du_date,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such due date")
                else:
                    mycon.execute("delete from billing where due_date=%s;",(du_date,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'I':
                print("sorry ! no record deleted")
                break

def delete_record6():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the deletion menu")
            break
        else:
            print("what do you want to update in this table ? ")
            print("A. for the department id")
            print("B. for the department name")
            print("C. for the location")
            print("D. for the cancellation of the programme")

            ch = input("enter your choice(A-D) : ").strip().upper()
            if ch == 'A':
                dep_id = int(input("enter the department id to delete : "))
                mycon.execute("select * from department where department_id=%s;",(dep_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such department id")
                else:
                    mycon.execute("delete from department where department_id=%s;",(dep_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'B':
                dep_name = input("enter the department name to delete : ")
                mycon.execute("select * from department where department_name=%s;",(dep_name,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such department name")
                else:
                    mycon.execute("delete from department where department_name=%s;",(dep_name,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'C':
                loc = input("enter the location to delete : ")
                mycon.execute("select * from department where location=%s;",(loc,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such location")
                else:
                    mycon.execute("delete from department where location=%s;",(loc,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'D':
                print("sorry ! no record deleted")
                break

def delete_record7():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the deletion menu")
            break
        else:
            print("what do you want to delete in this table ? ")
            print("A. for the room type id")
            print("B. for the room type")
            print("C. for the description")
            print("D. for the cancellation of programme")

            ch = input("enter your choice(A-D) : ").strip().upper()
            if ch == 'A':
                r_typeid = int(input("enter the room type id to delete : "))
                mycon.execute("select * from room_types where RoomType_id=%s;",(r_typeid,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such room type id")
                else:
                    mycon.execute("delete from room_types where RoomType_id=%s;",(r_typeid,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'B':
                r_t = input("enter the room type to delete : ")
                mycon.execute("select * from room_types where room_type=%s;",(r_t,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such room type")
                else:
                    mycon.execute("delete from room_types where room_type=%s;",(r_t,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'C':
                des = input("enter the description to delete : ")
                mycon.execute("select * from room_types where description=%s;",(des,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such description")
                else:
                    mycon.execute("delete from room_types where description=%s;",(des,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'D':
                print("sorry ! no record deleted")
                break

def delete_record8():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the deletion menu")
            break
        else:
            print("what do you want to update in this table ? ")
            print("A. for the room id")
            print("B. for the room type id")
            print("C. for the room number")
            print("D. for the capacity")
            print("E. for the status")
            print("F. for the cancellation of the programme")

            ch = input("enter your choice(A-F) : ").strip().upper()
            if ch == 'A':
                ro_id = int(input("enter the room id to delete : "))
                mycon.execute("select * from room where room_id=%s;",(ro_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such room id")
                else:
                    mycon.execute("delete from room where room_id=%s;",(ro_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'B':
                rotype_id = int(input("enter the room type id to delete : "))
                mycon.execute("select * from room where RoomType_id=%s;",(rotype_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such room type id")
                else:
                    mycon.execute("delete from room where RoomType_id=%s;",(rotype_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'C':
                ro_no = int(input("enter the room number to delete : "))
                mycon.execute("select * from room where room_no=%s;",(ro_no,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such room number")
                else:
                    mycon.execute("delete from room where room_no=%s;",(ro_no,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'D':
                cap = int(input("enter the capacity to delete : "))
                mycon.execute("select * from room where capacity=%s;",(cap,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such capacity")
                else:
                    mycon.execute("delete from room where capacity=%s;",(cap,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'E':
                st = input("enter the statu to delete : ")
                mycon.execute("select * from room where status=%s;",(st,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such status")
                else:
                    mycon.execute("delete from room where status=%s;",(st,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'F':
                print("sorry ! no record deleted")
                break

def delete_record9():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the deletion menu")
            break
        else:
            print("what do you want to delete in this table ? ")
            print("A. for the medical id")
            print("B. for the name")
            print("C. for the stock")
            print("D. for the expiry date")
            print("E. for the dosage")
            print("F. for the type")
            print("G. for the cancellation of the programme")

            ch = input("enter your choice(A-G) : ").strip().upper()
            if ch == 'A':
                m_id = int(input("enter the medical id to delete : "))
                mycon.execute("select * from medicine where med_id=%s;",(m_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such medical id")
                else:
                    mycon.execute("delete from medicine where med_id=%s;",(m_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'B':
                name = input("enter the name of the medicine to delete : ")
                mycon.execute("select * from medicine where name=%s;",(name,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such medicine name")
                else:
                    mycon.execute("delete from medicine where name%s;",(name,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'C':
                sto = int(input("enter the medicine stock to delete : "))
                mycon.execute("select * from medicine where stock=%s;",(sto,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such stock")
                else:
                    mycon.execute("delete from medicine where stock=%s;",(sto,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'D':
                exp_da = input("enter the expiry date of the medicine to delete : ")
                mycon.execute("select * from medicine where expiry_date=%s;",(exp_da,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such expiry date")
                else:
                    mycon.execute("delete from medicine where expiry_date=%s;",(exp_da,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'E':
                dos = input("enter the medicine dosage to delete : ")
                mycon.execute("select * from medicine where dosage=%s;",(dos,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such dosage")
                else:
                    mycon.execute("delete from medicine where dosage=%s;",(dos,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'F':
                ty = input("enter the medicine type to delete : ")
                mycon.execute("select * from medicine where type=%s;",(ty,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such medicine type")
                else:
                    mycon.execute("delete from medicine where type=%s;",(ty,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'G':
                print("sorry ! no record deleted")
                break

def delete_record10():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the deletion menu")
            break
        else:
            print("what do you want to delete in this table ? ")
            print("A. for the pharmacy id")
            print("B. for the medical id")
            print("C. for the patient id")
            print("D. for the quantity")
            print("E. for the date dispensed")
            print("F. for the cancellation of the programme")

            ch = input("enter your choice(A-F) : ").strip().upper()
            if ch == 'A':
                ph_id = int(input("enter the pharmacy id to delete : "))
                mycon.execute("select * from pharmacy where pharmacy_id=%s;",(ph_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such pharmacy id")
                else:
                    mycon.execute("delete from pharmacy where pharmacy_id=%s;",(ph_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'B':
                m_id = int(input("enter the medicine id to delete : "))
                mycon.execute("select * from pharmacy where med_id=%s;",(m_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such medicine id")
                else:
                    mycon.execute("delete from pharmacy where med_id=%s;",(m_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'C':
                pat_id = int(input("enter the patient id to delete : "))
                mycon.execute("select * from pharmacy where p_id=%s;",(pat_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such patient id")
                else:
                    mycon.execute("delete from pharmacy where p_id=%s;",(pat_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'D':
                quant = int(input("enter the quantity of medicine to delete : "))
                mycon.execute("select * from pharmacy where quantity=%s;",(quant,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such quantity")
                else:
                    mycon.execute("delete from pharmacy where quantity=%s;",(quant,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'E':
                d_dispen = input("enter the date medicine was dispensed to delete : ")
                mycon.execute("select * from pharmacy where date_dispensed=%s;",(d_dispen,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such dispensed date")
                else:
                    mycon.execute("delete from pharmacy where date_dispensed=%s;",(d_dispen,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'F':
                print("sorry ! no record deleted")
                break

def delete_record11():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the deletion menu")
            break
        else:
            print("what do you want to delete in this table ? ")
            print("A. for the test id")
            print("B. for the test name")
            print("C. for the cost")
            print("D. for the cancellation of the programme")

            ch = input("enter your choice(A-D) : ").strip().upper()
            if ch == 'A':
                te_id = int(input("enter the test id to delete : "))
                mycon.execute("select * from lab_tests where test_id=%s;",(te_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such test id")
                else:
                    mycon.execute("delete from lab_tests where test_id=%s;",(te_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'B':
                te_name = input("enter the test name to delete : ")
                mycon.execute("select * from lab_tests where test_name=%s;",(te_name,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such test name")
                else:
                    mycon.execute("delete from lab_tests where test_name=%s;",(te_name,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'C':
                cos = int(input("enter the cost to delete : "))
                mycon.execute("select * from lab_tests where p_id=%s;",(cos))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such pcost")
                else:
                    mycon.execute("delete from lab_tests where cost=%s;",(cos,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'D':
                print("sorry ! no record deleted")
                break

def delete_record12():
    mydb = mys.connect(host = "localhost" , user = "root" , password = DB_PASSWORD , database = "hospital")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the deletion menu")
            break
        else:
            print("what do you want to delete in this table ? ")
            print("A. for the record id")
            print("B. for the patient id")
            print("C. for the appointment id")
            print("D. for the test id")
            print("E. for the result")
            print("F. for the date conducted")
            print("G. for the cancellation of the programme")

            ch = input("enter your choice(A-G) : ").strip().upper()
            if ch == 'A':
                reco_id = int(input("enter the record id to delete : "))
                mycon.execute("select * from test_records where record_id=%s;",(reco_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such record id")
                else:
                    mycon.execute("delete from test_records where record_id=%s;",(reco_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'B':
                pat_id = int(input("enter the patient id to delete : "))
                mycon.execute("select * from test_records where p_id=%s;",(pat_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such patient id")
                else:
                    mycon.execute("delete from test_records where p_id=%s;",(pat_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'C':
                app_id = int(input("enter the appointment id to delete : "))
                mycon.execute("select * from test_records where appointment_id=%s;",(app_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such appointment id")
                else:
                    mycon.execute("delete from test_records where appointment_id=%s;",(app_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'D':
                t_id = int(input("enter the test id to delete : "))
                mycon.execute("select * from test_records where test_id=%s;",(t_id,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such test id")
                else:
                    mycon.execute("delete from test_records where test_id=%s;",(t_id,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'E':
                res = input("enter the result to delete : ")
                mycon.execute("select * from test_records where result=%s;",(res,))
                o = mycon.fetchall()
                if not o:
                    print("no records found with such result")
                else:
                    mycon.execute("delete from test_records where result=%s;",(res,))
                    print("record deleted")
                    mydb.commit()

            elif ch == 'F':
                date_c = input("enter the date test conducted to delete : ")
                mycon.execute("select * from test_records where date_conducted=%s;",(date_c,))

            elif ch == 'G':
                print("sorry ! no record deleted")
                break

def add_menu():
    while True:
        print("\nAdd Data:")
        print("1. Patient")
        print("2. Doctor")
        print("3. Appointment")
        print("4. Medical Record")
        print("5. Billing")
        print("6. Department")
        print("7. Room Type")
        print("8. Room")
        print("9. Medicine")
        print("10. Pharmacy")
        print("11. Lab Test")
        print("12. Test Record")
        print("0. Back")
        ch = input("Select entity to add (0 to go back): ").strip()
        if ch == '0':
            break
        elif ch == '1':
            add_record1()
        elif ch == '2':
            add_record2()
        elif ch == '3':
            add_record3()
        elif ch == '4':
            add_record4()
        elif ch == '5':
            add_record5()
        elif ch == '6':
            add_record6()
        elif ch == '7':
            add_record7()
        elif ch == '8':
            add_record8()
        elif ch == '9':
            add_record9()
        elif ch == '10':
            add_record10()
        elif ch == '11':
            add_record11()
        elif ch == '12':
            add_record12()
        else:
            print("Invalid choice. Please try again.")

def update_menu():
    while True:
        print("\nUpdate Data:")
        print("1. Patient")
        print("2. Doctor")
        print("3. Appointment")
        print("4. Medical Record")
        print("5. Billing")
        print("6. Department")
        print("7. Room Type")
        print("8. Room")
        print("9. Medicine")
        print("10. Pharmacy")
        print("11. Lab Test")
        print("12. Test Record")
        print("0. Back")
        ch = input("Select entity to update (0 to go back): ").strip()
        if ch == '0':
            break
        elif ch == '1':
            update_record1()
        elif ch == '2':
            update_record2()
        elif ch == '3':
            update_record3()
        elif ch == '4':
            update_record4()
        elif ch == '5':
            update_record5()
        elif ch == '6':
            update_record6()
        elif ch == '7':
            update_record7()
        elif ch == '8':
            update_record8()
        elif ch == '9':
            update_record9()
        elif ch == '10':
            update_record10()
        elif ch == '11':
            update_record11()
        elif ch == '12':
            update_record12()
        else:
            print("Invalid choice. Please try again.")

def delete_menu():
    while True:
        print("\nDelete Data:")
        print("1. Patient")
        print("2. Doctor")
        print("3. Appointment")
        print("4. Medical Record")
        print("5. Billing")
        print("6. Department")
        print("7. Room Type")
        print("8. Room")
        print("9. Medicine")
        print("10. Pharmacy")
        print("11. Lab Test")
        print("12. Test Record")
        print("0. Back")
        ch = input("Select entity to delete (0 to go back): ").strip()
        if ch == '0':
            break
        elif ch == '1':
            delete_record1()
        elif ch == '2':
            delete_record2()
        elif ch == '3':
            delete_record3()
        elif ch == '4':
            delete_record4()
        elif ch == '5':
            delete_record5()
        elif ch == '6':
            delete_record6()
        elif ch == '7':
            delete_record7()
        elif ch == '8':
            delete_record8()
        elif ch == '9':
            delete_record9()
        elif ch == '10':
            delete_record10()
        elif ch == '11':
            delete_record11()
        elif ch == '12':
            delete_record12()
        else:
            print("Invalid choice. Please try again.")

def search_menu():
    while True:
        print("\nSearch Data:")
        print("1. Patient")
        print("2. Doctor")
        print("3. Appointment")
        print("4. Medical Record")
        print("5. Billing")
        print("6. Department")
        print("7. Room Type")
        print("8. Room")
        print("9. Medicine")
        print("10. Pharmacy")
        print("11. Lab Test")
        print("12. Test Record")
        print("0. Back")
        ch = input("Select entity to search (0 to go back): ").strip()
        if ch == '0':
            break
        elif ch == '1':
            search_record1()
        elif ch == '2':
            search_record2()
        elif ch == '3':
            search_record3()
        elif ch == '4':
            search_record4()
        elif ch == '5':
            search_record5()
        elif ch == '6':
            search_record6()
        elif ch == '7':
            search_record7()
        elif ch == '8':
            search_record8()
        elif ch == '9':
            search_record9()
        elif ch == '10':
            search_record10()
        elif ch == '11':
            search_record11()
        elif ch == '12':
            search_record12()
        else:
            print("Invalid choice. Please try again.")

def menu():
    while True:
        print("\nWelcome to the Hospital Management System")
        print("1. Add Data")
        print("2. Update Data")
        print("3. Delete Data")
        print("4. Search Data")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_menu()
        elif choice == '2':
            update_menu()
        elif choice == '3':
            delete_menu()
        elif choice == '4':
            search_menu()
        elif choice == '5':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()