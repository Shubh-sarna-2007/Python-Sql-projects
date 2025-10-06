from config import DB_PASSWORD
import mysql.connector as mys
mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="bank")
mycon=mydb.cursor()
def create_file():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="bank")
    mycon=mydb.cursor()
    mycon.execute("create table if not exists account(acc_no int PRIMARY KEY,name VARCHAR(50),age int,phone bigint,dob varchar(20),address varchar(100),adhaar_no bigint,bank_balance bigint);")
    mydb.commit()

create_file()

def create_newfile():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="bank")
    mycon=mydb.cursor()
    mycon.execute("create table if not exists loan(acc_no int PRIMARY KEY,name varchar(50),principal bigint,rate_ofinterest int,time int);")
    mydb.commit()

create_newfile()

def add_file():
    while True:
        a_no=int(input("enter the account number of the client : "))
        n=input("enter the name of the client : ")
        a=int(input("enter the age of the client : "))
        ph_no=int(input("enter the phone number of the client : "))
        d=input("enter the date of birth of the client : ")
        addr=input("enter the address of the client : ")
        adhr_no=int(input("enter the adhaar number of the client : "))
        bank_b=int(input("enter the bank balance of the client : "))
        mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="bank")
        mycon=mydb.cursor()

        sql="insert into account (acc_no,name,age,phone,dob,address,adhaar_no,bank_balance) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"
        values = (a_no,n,a,ph_no,d,addr,adhr_no,bank_b)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans=input("do you want to continue with entries(y/n) : ").strip().lower()
        if ans=='n':
            print("thank you for registering in our bank ")
            break
        mycon.close()

def check_balance():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="bank")
    mycon=mydb.cursor()
    mycon.execute("select * from account;")
    x=mycon.fetchall()
    for i in x:
        print("the bank balance of ",i[1],"is", i[7])

def deposit_money():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="bank")
    mycon=mydb.cursor()
    while True:
        ch=input("do you want to deposit money? (y/n) : ").strip().lower()
        if ch!='y':
            print("Can't deposit money")
            break

        a_no=input("enter the account number to deposit money : ")
        if not a_no:
            print("account number is required ")
            continue

        a_no=int(a_no)
        mycon.execute("select * from account where acc_no=%s",(a_no,))
        r=mycon.fetchone()
        
        if not r:
            print("sorry account number not found ")
            continue

        else:
            new_bankbalance=int(input("enter the money to be deposited : "))
            mycon.execute("update account set bank_balance=bank_balance+%s where acc_no=%s",(new_bankbalance,a_no))
            print("bank balance updated ")
            mydb.commit()
            mycon.close()

def withdraw_money():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="bank")
    mycon=mydb.cursor()
    while True:
        ch=input("do you want to withdraw money? (y/n) : ").strip().lower()
        if ch!='y':
            print("can't withdraw money")
            break

        a_no=int(input("enter the account number to withdraw money : "))
        if not a_no:
            print("account number is required ")
            continue

        a_no=int(a_no)
        mycon.execute("select * from account where acc_no=%s",(a_no,))
        r=mycon.fetchone()
        
        if not r:
            print("sorry account number not found ")
            continue

        else:
            new_balance=int(input("enter the money to be withdrawn : "))
            mycon.execute("update account set bank_balance=bank_balance-%s where acc_no=%s",(new_balance,a_no))
            print("bank balance updated ")
            mydb.commit()
            mycon.close()

def update_data():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="bank")
    mycon=mydb.cursor()
    while True:
        ch=input("do you want to update entries? (y/n) : ")
        if ch!='y':
            print("exiting updation menu")
            break

        a_no=input("enter the account number : ").strip()
        if not a_no:
            print("account number is required ")
            continue

        print("what do you want to update ? : ")
        print("a. for account number of the client : ")
        print("b. for name of the client : ")
        print("c. for the age of the client : ")
        print("d. for the phone number of the client : ")
        print("e. for the date of birth of the client : ")
        print("f. for the address of the client : ")
        print("g. for the adhaar number of the client : ")
        print("h. for the bank balance of the client : ")
        print("i. for cancel the updation of the programme : ")

        choice=input("enter your choice (a-i) : ").strip()
        
        if choice == 'a':
            new_accno=int(input("enter the new account number of the client : "))
            if new_accno:
                mycon.execute("update account set acc_no=%s where acc_no=%s",(int(new_accno),a_no))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif choice == 'b':
            new_name=input("enter the new name of the client : ")
            if new_name:
                mycon.execute("update account set name=%s where acc_no=%s",(new_name,a_no))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif choice == 'c':
            new_age=int(input("enter the new age of the client : "))
            if new_age:
                mycon.execute("update account set age=%s where acc_no=%s",(int(new_age),a_no))
                print("record updated")
                mydb.commit()
                mycon.close()
        
        elif choice == 'd':
            new_phoneno=int(input("enter the new phone number of the client : "))
            if new_phoneno:
                mycon.execute("update account set phone=%s where acc_no=%s",(int(new_phoneno),a_no))
                print("record updated")
                mydb.commit()
                mycon.close()
        
        elif choice == 'e':
            new_dob=input("enter the new date of birth of the client : ")
            if new_dob:
                mycon.execute("update account set dob=%s where acc_no=%s",(new_dob,a_no))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif choice == 'f':
            new_add=input("enter the new address of the client : ")
            if new_add:
                mycon.execute("update account set address=%s where acc_no=%s",(new_add,a_no))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif choice == 'g':
            new_adhaar=int(input("enter the new adhaar number of the client : "))
            if new_adhaar:
                mycon.execute("update account set adhaar_no=%s where acc_no=%s",(int(new_adhaar),a_no))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif choice == 'h':
            new_bankbalance=int(input("enter the new bank balance of the client : "))
            if new_bankbalance:
                mycon.execute("update account set bank_balance=%s where acc_no=%s",(int(new_bankbalance),a_no))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif choice == 'i':
            print("sorry ! but no information is updated ! ")
            break

        else:
            print("sorry invalid operation ! ")
            break

def delete_data():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="bank")
    mycon=mydb.cursor()
    mycon.execute("select * from account;")
    x=mycon.fetchall()
    while True:
        c=input("do you want to delete entries? (y/n) : ").strip().lower()
        if c!='y':
            print("exiting the deletion menu ")
            break

        else:
            print("what do you want to delete ? : ")
            print("A. for account number of the client : ")
            print("B. for name of the client : ")
            print("C. for the age of the client : ")
            print("D. for the phone number of the client : ")
            print("E. for the date of birth of the client : ")
            print("F. for the address of the client : ")
            print("G. for the adhaar number of the client : ")
            print("H. for the bank balance of the client : ")
            print("I. for cancel the updation of the programme : ")

            c=input("enter your choice(A-I) : ")
            if c == 'A':
                ac_no=int(input("enter the account number of the client to delete : "))
                mycon.execute("select * from account where acc_no=%s;",(ac_no,))
                o=mycon.fetchall()
                if not o:
                    print("No records found with such account number ")
                else:
                    mycon.execute("delete from account where acc_no=%s",(ac_no,))
                    print("record deleted")
                    mydb.commit()

            elif c == 'B':
                na=input("enter the name of the client to delete : ")
                mycon.execute("select * from account where name=%s;",(na,))
                o=mycon.fetchall()
                if not o:
                    print("No records found with such name ")
                else:
                    mycon.execute("delete from account where name=%s",(na,))
                    print("record deleted")
                    mydb.commit()
            
            elif c == 'C':
                ag=int(input("enter the age of the client to delete : "))
                mycon.execute("select * from account where age=%s;",(ag,))
                o=mycon.fetchall()
                if not o:
                    print("No records found with such age ")
                else:
                    mycon.execute("delete from account where age=%s",(ag,))
                    print("record deleted")
                    mydb.commit()
            
            elif c == 'D':
                ph=int(input("enter the phone number of the client to delete : "))
                mycon.execute("select * from account where phone=%s;",(ph,))
                o=mycon.fetchall()
                if not o:
                    print("No records found with such phone number")
                else:
                    mycon.execute("delete from account where phone=%s",(ph,))
                    print("record deleted")
                    mydb.commit()

            elif c == 'E':
                d=input("enter the date of birth of the client to delete : ")
                mycon.execute("select * from account where dob=%s;",(d,))
                o=mycon.fetchall()
                if not o:
                    print("No records found with such date of birth")
                else:
                    mycon.execute("delete from account where dob=%s",(d,))
                    print("record deleted")
                    mydb.commit()

            
            elif c == 'F':
                ad=input("enter the address of the client to delete : ")
                mycon.execute("select * from account where address=%s;",(ad,))
                o=mycon.fetchall()
                if not o:
                    print("No records found with such account number ")
                else:
                    mycon.execute("delete from account where address=%s",(ad,))
                    print("record deleted")
                    mydb.commit()
            
            elif c == 'G':
                adhr=int(input("enter the adhaar number of the client to delete : "))
                mycon.execute("select * from account where adhaar_no=%s;",(adhr,))
                o=mycon.fetchall()
                if not o:
                    print("No records found with such adhaar number ")
                else:
                    mycon.execute("delete from account where adhaar_no=%s",(adhr,))
                    print("record deleted")
                    mydb.commit()

            elif c == 'H':
                bank_b=int(input("enter the bank balance of the client to delete : "))
                mycon.execute("select * from account where bank_balance=%s;",(bank_b,))
                o=mycon.fetchall()
                if not o:
                    print("No records found with such bank balance ")
                else:
                    mycon.execute("delete from account where bank_balance=%s",(bank_b,))
                    print("record deleted")
                    mydb.commit()

            elif c == 'I':
                print("deletion cancelled ")
                break
            
            else:
                print("Invalid operation ")
                break

def search_data():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="bank")
    mycon=mydb.cursor()

    while True:
        k=input("do you want to search entries? (y/n) : ")
        if k!='y':
            print("exiting the search menu")
            break
        else:
            print("what do you want to search ? ")
            print("A. for account number of the client : ")
            print("B. for name of the client : ")
            print("C. for the age of the client : ")
            print("D. for the phone number of the client : ")
            print("E. for the date of birth of the client : ")
            print("F. for the address of the client : ")
            print("G. for the adhaar number of the client : ")
            print("H. for the bank balance of the client : ")
            print("I. for cancel the updation of the programme : ")
            
            o=input("enter your choice (A-H) : ").strip().upper()
            if o == 'A':
                acco_no=int(input("enter the account number to search : "))
                mycon.execute("select * from account where acc_no=%s",(acco_no,))
            
            elif o == 'B':
                name=input("enter the name of the client to search : ")
                mycon.execute("select * from account where name=%s",(name,))
            
            elif o == 'C':
                age=int(input("enter the age of the client to search : "))
                mycon.execute("select * from account where age=%s",(age,))

            elif o == 'D':
                phone_no=int(input("enter the phone number of the client to search : "))
                mycon.execute("select * from account where phone=%s",(phone_no,))

            elif o == 'E':
                dob=input("enter the date of birth of the client to search : ")
                mycon.execute("select * from account where dob=%s",(dob,))

            elif o == 'F':
                address=input("enter the address of the client to search : ")
                mycon.execute("select * from account where phone=%s",(phone_no,))

            elif o == 'G':
                adhaar_no=int(input("enter the adhaar number of the client to search : "))
                mycon.execute("select * from account where adhaar_no=%s",(adhaar_no,))

            elif o == 'H':
                bank_balance=int(input("enter the bank balance of the client to search : "))
                mycon.execute("select * from account where bank_balance=%s",(bank_balance,))

            elif o == 'I':
                print("canelling the search menu ")
                break

            x=mycon.fetchall()
            if not x:
                print("no records found with your search ")
            else:
                print("number of records found  :",len(x))
                for row in x:
                    print(row)

    mycon.close()
    mydb.close()

def add_loandata():
    while True:
        a_no=int(input("enter the account number of the client : "))
        n=input("enter the name of the client : ")
        p=int(input("enter the principal amount : "))
        r=int(input("enter the rate of interest : "))
        t=int(input("enter the duration (in years) : "))

        mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="bank")
        mycon=mydb.cursor()

        sql="insert into loan (acc_no,name,principal,rate_ofinterest,time) VALUES(%s,%s,%s,%s,%s);"
        values = (a_no,n,p,r,t)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans=input("do you want to continue with entries(y/n) : ").strip().lower()
        if ans=='n':
            print("thank you for registering in our bank ")
            break
        mycon.close()

def search_loanamt():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="bank")
    mycon=mydb.cursor()

    while True:
        t=input("do you want to search for the interest of a certain account numnber (y/n) : ")
        if t!='y':
            print("exiting this search menu ")
            break
        
        else:
            print("how do you want to search for loan interest amount through : ")
            print("A. for account number ")
            print("B. for name ")
            print("C. for exiting the program ")

            x=input("enter your choice(A-C) : ").strip()
            if x == 'A':
                ac_n=int(input("enter the account number to search through : "))
                mycon.execute("select acc_no,(principal * rate_ofinterest * time) / 100 AS interest from loan where acc_no=%s",(ac_n,))
            
            elif x == 'B':
                nam=input("enter the name to search through : ")
                mycon.execute("select name,(principal * rate_ofinterest * time) / 100 AS interest from loan where name=%s",(nam,))

            elif x == 'C':
                print("Cancelling this search menu ")
                break

            else:
                print("Invalid operation ")
                break

            x=mycon.fetchall()
            if not x:
                print("no records found with your search ")
            else:
                for row in x:
                    acc_no = row[0]
                    interest = row[1]
                    print("Account Number: " + str(acc_no) + ", Interest: " + str(interest))
    mydb.close()
    mycon.close()

def delete_loan():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="bank")
    mycon=mydb.cursor()

    while True:
        t=input("do you want to delete an account from loan data (y/n) : ")
        if t!='y':
            print("exiting this deletion menu ")
            break
        
        else:
            print("how do you want to delete an account from loan table through  : ")
            print("A. for account number ")
            print("B. for name ")
            print("C. for principal amount : ")
            print("D. for Rate of interest : ")
            print("E. for time : ")
            print("F. for exiting the program ")

            o=input("enter your choice (A-F) : ").strip().upper()

            if o == 'A':
                ac_no=int(input("enter the account number of the client to delete : "))
                mycon.execute("select * from loan where acc_no=%s;",(ac_no,))
                o=mycon.fetchall()
                if not o:
                    print("No records found with such account number ")
                else:
                    mycon.execute("delete from loan where acc_no=%s",(ac_no,))
                    print("record deleted")
                    mydb.commit()

            elif o == 'B':
                n=int(input("enter the name of the client to delete : "))
                mycon.execute("select * from loan where name=%s;",(n,))
                o=mycon.fetchall()
                if not o:
                    print("No records found with such account number ")
                else:
                    mycon.execute("delete from loan where name=%s",(n,))
                    print("record deleted")
                    mydb.commit()
            
            elif o == 'C':
                p=int(input("enter the principal amount of the client to delete : "))
                mycon.execute("select * from loan where principal=%s;",(p,))
                o=mycon.fetchall()
                if not o:
                    print("No records found with such account number ")
                else:
                    mycon.execute("delete from loan where principal=%s",(p,))
                    print("record deleted")
                    mydb.commit()
            
            elif o == 'D':
                r=int(input("enter the rate of interest of the loan of the client to delete : "))
                mycon.execute("select * from loan where rate_ofinterest=%s;",(r,))
                o=mycon.fetchall()
                if not o:
                    print("No records found with such account number ")
                else:
                    mycon.execute("delete from loan where rate_ofinterest=%s",(r,))
                    print("record deleted")
                    mydb.commit()
            
            elif o == 'E':
                t=int(input("enter the time duration of the loan of the client to delete : "))
                mycon.execute("select * from loan where time=%s;",(t,))
                o=mycon.fetchall()
                if not o:
                    print("No records found with such account number ")
                else:
                    mycon.execute("delete from loan where time=%s",(t,))
                    print("record deleted")
                    mydb.commit()
            
            elif o == 'F':
                print("sorry! no information deleted ")
                break

            else:
                print("invalid operation ")
                break


def menu():
    while True:
        print("\nWelcome to bank management system ")
        print("1. for addition of data")
        print("2. for checking of balance")
        print("3. for depositing money")
        print("4. for withdrawing money")
        print("5. for updating data")
        print("6. for deleting data")
        print("7. for searching data")
        print("8. for addtition of loan data")
        print("9. for searching interest amount on loan ")
        print("10. for deleting account from loan table ")
        print("11. for exiting the program")

        ch=input("enter your choice(1-11) : ")
        if ch == '1':
            add_file()
        
        elif ch == '2':
            check_balance()

        elif ch == '3':
            deposit_money()
        
        elif ch == '4':
            withdraw_money()

        elif ch == '5':
            update_data()
        
        elif ch == '6':
            delete_data()
        
        elif ch == '7':
            search_data()
        
        elif ch == '8':
            add_loandata()

        elif ch == '9':
            search_loanamt()

        elif ch == '10':
            delete_loan()

        elif ch == '11':
            print("exiting program !! Good bye !!")
            break

        else:
            print("invalid choice. Please enter a number between (1-10) : ")

menu()