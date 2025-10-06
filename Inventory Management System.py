from config import DB_PASSWORD
import mysql.connector as mys
mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
mycon = mydb.cursor()

def createtable1():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    mycon.execute("create table if not exists product(product_id int,product_name varchar(20),category varchar(20),price int,quantity int,supplier_id int,reorder_level int);")
    mydb.commit()

createtable1()

def createtable2():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    mycon.execute("create table if not exists suppliers(supplier_id int,supplier_name varchar(20),contact_info bigint,address varchar(100));")
    mydb.commit()

createtable2()

def createtable3():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    mycon.execute("create table if not exists customers(customer_id int,customer_name varchar(20),address varchar(100),mobile bigint);")
    mydb.commit()

createtable3()

def createtable4():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    mycon.execute("create table if not exists transactions(transaction_id int,product_id int,transaction_type varchar(20),quantity int,date date,user_id int);")
    mydb.commit()

createtable4()

def createtable5():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    mycon.execute("create table if not exists users(user_id int,user_name varchar(20),password varchar(100),role varchar(20));")
    mydb.commit()

createtable5()

def addfile1():
    while True:
        p_id = int(input("Enter the product id : "))
        p_name = input("Enter the product name : ")
        categ = input("Enter the category : ")
        p = int(input("Enter the price : "))
        quant = int(input("Enter the quantity : "))
        s_id = int(input("Enter the supplier id : "))
        r_level = int(input("Enter the reorder level : "))
        mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
        mycon = mydb.cursor()

        sql = "insert into product (product_id,product_name,category,price,quantity,supplier_id,reorder_level) VALUES(%s,%s,%s,%s,%s,%s,%s);"
        values = (p_id,p_name,categ,p,quant,s_id,r_level)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("Enter do you want to add more entries : ")
        if ans == 'n':
            print("Thank you for entering data in this table")
            break
        mycon.close()
        
def addfile2():
    while True:
        s_id = int(input("Enter the supplier id : "))
        s_name = input("Enter the supplier name : ")
        c_info = int(input("Enter the contact number : "))
        address = input("Enter the address of the supplier : ")
        mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
        mycon = mydb.cursor()

        sql = "insert into suppliers (supplier_id,supplier_name,contact_info,address) VALUES(%s,%s,%s,%s);"
        values = (s_id,s_name,c_info,address)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("Enter do you want to add more entries : ")
        if ans == 'n':
            print("Thank you for entering the data")
            break
        mycon.close()

def addfile3():
    while True:
        c_id = int(input("Enter the customer id : "))
        c_name = input("Enter the customer name : ")
        address = input("Enter the address of the customer : ")
        mobile = int(input("Enter the mobile number of the customer : "))
        mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
        mycon = mydb.cursor()

        sql = "insert into customers (customer_id,customer_name,address,mobile) VALUES(%s,%s,%s,%s);"
        values = (c_id,c_name,address,mobile)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("Enter do you want to add more entries : ")
        if ans == 'n':
            print("Thank you for entering the data")
            break
        mycon.close()

def addfile4():
    while True:
        t_id = int(input("Enter the transaction id : "))
        p_id = int(input("Enter the product id : "))
        t_type = input("Enter the transaction type : ")
        quantity = int(input("Enter the quantity : "))
        date = input("Enter the date of transaction : ")
        u_id = int(input("Enter the user id : "))
        mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
        mycon = mydb.cursor()

        sql = "insert into transactions (transaction_id,product_id,transaction_type,quantity,date,user_id) VALUES(%s,%s,%s,%s,%s,%s);"
        values = (t_id,p_id,t_type,quantity,date,u_id)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("Enter do you want to add more entries : ")
        if ans == 'n':
            print("Thank you for entering the data")
            break
        mycon.close()

def addfile5():
    while True:
        u_id = int(input("Enter the user id : "))
        u_name = input("Enter the user name : ")
        pwd = input("Enter the password : ")
        role = input("Enter the role ")
        mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
        mycon = mydb.cursor()

        sql = "insert into users (user_id,supplier_name,contact_info,address) VALUES(%s,%s,%s,%s);"
        values = (u_id,u_name,pwd,role)

        mycon.execute(sql,values)
        mydb.commit()
        mycon.close()
        mydb.close()

        ans = input("Enter do you want to add more entries : ")
        if ans == 'n':
            print("Thank you for entering the data")
            break
        mycon.close()

def search_record1():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    while True:
        k = input("Enter do you want search entries(y/n) : ")
        if k!='y':
            print("Exiting the search menu")
            break
        else:
            print("What do you want to search in this table ? ")
            print("A. for product id ")
            print("B. for product name ")
            print("C. for category of the product ")
            print("D. for price of the product ")
            print("E. for quantity of the product ")
            print("F. for the supplier id ")
            print("G. for the reorder level of the product ")
            print("H. for the cancellation of the program ")

            ch = input("Enter your choice(A-H) : ").strip().upper()
            if ch == 'A':
                p_id = int(input("Enter the product id to search : "))
                mycon.execute("select * from product where product_id=%s",(p_id,))
            
            elif ch == 'B':
                pu_name = input("Enter the product name to search : ")
                mycon.execute("select * from product where product_name=%s",(pu_name,))
            
            elif ch == 'C':
                category = input("Enter the category to search : ")
                mycon.execute("select * from product where category=%s",(category,))
            
            elif ch == 'D':
                price = int(input("Enter the price of the product to search : "))
                mycon.execute("select * from product where price=%s",(price,))
            
            elif ch == 'E':
                quantity = int(input("Enter the quantity of the product to search : "))
                mycon.execute("select * from product where quantity=%s",(quantity,))

            elif ch == 'F':
                su_id = int(input("Enter the supplier id to search : "))
                mycon.execute("select * from product where supplier_id=%s",(su_id,))

            elif ch == 'G':
                re_level = int(input("Enter the reorder level of the product to search : "))
                mycon.execute("select * from product where reorder_level=%s",(re_level,))

            elif ch == 'H':
                print("Exiting the search menu")
                break

            x = mycon.fetchall()
            if not x:
                print("Records found with your search")
            else:
                print("number of records : ",len(x))
                for row in x:
                    print(row)
    mycon.close()
    mydb.close()

def search_record2():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    while True:
        k = input("Enter do you want search entries(y/n) : ")
        if k!='y':
            print("Exiting the search menu")
            break
        else:
            print("What do you want to search in this table ? ")
            print("A. for supplier id ")
            print("B. for supplier name ")
            print("C. for contact info of the supplier ")
            print("D. for address of the supplier ")
            print("E. for the cancellation of the program ")

            ch = input("Enter your choice(A-E) : ").strip().upper()
            if ch == 'A':
                su_id = int(input("Enter the supplier id to search : "))
                mycon.execute("select * from suppliers where supplier_id=%s",(su_id,))
            
            elif ch == 'B':
                su_name = input("Enter the supplier name to search : ")
                mycon.execute("select * from suppliers where supplier_name=%s",(su_name,))
            
            elif ch == 'C':
                c_info = int(input("Enter the contact info to search : "))
                mycon.execute("select * from suppliers where contact_info=%s",(c_info,))
            
            elif ch == 'D':
                address = input("Enter the address of the supplier to search : ")
                mycon.execute("select * from suppliers where address=%s",(address,))

            elif ch == 'E':
                print("Exiting the search menu")
                break

            x = mycon.fetchall()
            if not x:
                print("Records found with your search")
            else:
                print("number of records : ",len(x))
                for row in x:
                    print(row)
    mycon.close()
    mydb.close()

def search_record3():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    while True:
        k = input("Enter do you want search entries(y/n) : ")
        if k!='y':
            print("Exiting the search menu")
            break
        else:
            print("What do you want to search in this table ? ")
            print("A. for customer id ")
            print("B. for customer name ")
            print("C. for address of the customer ")
            print("D. for mobile number of the customer ")
            print("E. for the cancellation of the program ")

            ch = input("Enter your choice(A-E) : ").strip().upper()
            if ch == 'A':
                cu_id = int(input("Enter the customer id to search : "))
                mycon.execute("select * from customers where customer_id=%s",(cu_id,))
            
            elif ch == 'B':
                cu_name = input("Enter the customer name to search : ")
                mycon.execute("select * from customers where customer_name=%s",(cu_name,))
            
            elif ch == 'C':
                address = input("Enter the address of the customer to search : ")
                mycon.execute("select * from customers where address=%s",(address,))

            elif ch == 'D':
                mob_no = int(input("Enter the mobile number of the customer to search : "))
                mycon.execute("select * from customes where mobile_no=%s",(mob_no,))

            elif ch == 'E':
                print("Exiting the search menu")
                break

            x = mycon.fetchall()
            if not x:
                print("Records found with your search")
            else:
                print("number of records : ",len(x))
                for row in x:
                    print(row)
    mycon.close()
    mydb.close()

def search_record4():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    while True:
        k = input("Enter do you want search entries(y/n) : ")
        if k!='y':
            print("Exiting the search menu")
            break
        else:
            print("What do you want to search in this table ? ")
            print("A. for transaction id ")
            print("B. for product id ")
            print("C. for transaction type ")
            print("D. for quantity of the product ")
            print("E. for the date of transaction ")
            print("F. for the user id of the transaction ")
            print("G. for the cancellation of the program ")

            ch = input("Enter your choice(A-G) : ").strip().upper()
            if ch == 'A':
                t_id = int(input("Enter the transaction id to search : "))
                mycon.execute("select * from transactions where transaction_id=%s",(t_id,))
            
            elif ch == 'B':
                p_id = int(input("Enter the product id to search : "))
                mycon.execute("select * from transactions where product_id=%s",(p_id,))
            
            elif ch == 'C':
                t_type = input("Enter the transaction type to search : ")
                mycon.execute("select * from transactions where transaction_type=%s",(t_type,))
            
            elif ch == 'D':
                quantity = int(input("Enter the quantity of the product to search : "))
                mycon.execute("select * from transactions where quantity=%s",(quantity,))

            elif ch == 'E':
                date = input("Enter the date of transaction to search : ")
                mycon.execute("select * from transactions where supplier_id=%s",(date,))

            elif ch == 'F':
                u_id = int(input("Enter the user id of the transaction to search : "))
                mycon.execute("select * from transactions where user_id=%s",(u_id,))

            elif ch == 'G':
                print("Exiting the search menu")
                break

            x = mycon.fetchall()
            if not x:
                print("Records found with your search")
            else:
                print("number of records : ",len(x))
                for row in x:
                    print(row)
    mycon.close()
    mydb.close()

def search_record5():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    while True:
        k = input("Enter do you want search entries(y/n) : ")
        if k!='y':
            print("Exiting the search menu")
            break
        else:
            print("What do you want to search in this table ? ")
            print("A. for user id ")
            print("B. for user name ")
            print("C. for password ")
            print("D. for role of the user ")
            print("E. for the cancellation of the program ")

            ch = input("Enter your choice(A-E) : ").strip().upper()
            if ch == 'A':
                u_id = int(input("Enter the user id to search : "))
                mycon.execute("select * from users where user_id=%s",(u_id,))
            
            elif ch == 'B':
                u_name = input("Enter the user name to search : ")
                mycon.execute("select * from users where user_name=%s",(u_name,))
            
            elif ch == 'C':
                pwd = input("Enter the password of the user to search : ")
                mycon.execute("select * from users where password=%s",(pwd,))
            
            elif ch == 'D':
                role = input("Enter the role of the user to search : ")
                mycon.execute("select * from users where role=%s",(role,))

            elif ch == 'E':
                print("Exiting the search menu")
                break

            x = mycon.fetchall()
            if not x:
                print("Records found with your search")
            else:
                print("number of records : ",len(x))
                for row in x:
                    print(row)
    mycon.close()
    mydb.close()

def update_record1():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the updation menu")
            break
        p_id = input("Enter the product id : ").strip()
        if not p_id:
            print("Product id is required")
            continue

        print("What do you want to upadate in this table ")
        print("A. for product id ")
        print("B. for product name ")
        print("C. for category of the product ")
        print("D. for price of the product ")
        print("E. for quantity of the product ")
        print("F. for the supplier id ")
        print("G. for the reorder level of the product ")
        print("H. for the cancellation of the program ")

        ch = input("Enter your choice (A-H) : ").strip().upper()
        if ch == 'A':
            prod_id = int(input("Enter the new product id : "))
            if prod_id:
                mycon.execute("update product set product_id=%s where product_id=%s",(int(prod_id),p_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'B':
            prod_name = input("Enter the new product name : ")
            if prod_name:
                mycon.execute("update product set product_name=%s where product_id=%s",(prod_name,p_id))
                print("record updated")
                mydb.commit()
                mycon.close()
        
        elif ch == 'C':
            categ = input("Enter the new category : ")
            if categ:
                mycon.execute("update product set category=%s where product_id=%s",(categ,p_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'D':
            pr = int(input("Enter the new price of the product : "))
            if pr:
                mycon.execute("update product set price=%s where product_id=%s",(int(pr),p_id))
                print("record updated")
                mydb.commit()
                mycon.close()
        
        elif ch == 'E':
            q = int(input("Enter the new quantity : "))
            if q:
                mycon.execute("update product set quantity=%s where product_id=%s",(int(q),p_id))
                print("record updated")
                mydb.commit()
                mycon.close()
        
        elif ch == 'F':
            su_id = int(input("Enter the supplier id  : "))
            if su_id:
                mycon.execute("update product set supplier_id=%s where product_id=%s",(int(su_id),p_id))
                print("record updated")
                mydb.commit()
                mycon.close()
        
        elif ch == 'G':
            re_level = int(input("Enter the reorder level : "))
            if re_level:
                mycon.execute("update product set reorder_level=%s where product_id=%s",(int(re_level),p_id))
                print("record updated")
                mydb.commit()
                mycon.close()
        
        elif ch == 'H':
            print("Sorry ! no information updated")
            break

def update_record2():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the updation menu")
            break
        s_id = input("Enter the supplier id : ").strip()
        if not s_id:
            print("Supplier id is required")
            continue

        print("What do you want to upadate in this table ")
        print("A. for supplier id ")
        print("B. for supplier name ")
        print("C. for contact info ")
        print("D. for address ")
        print("E. for the cancellation of the program ")

        ch = input("Enter your choice (A-E) : ").strip().upper()
        if ch == 'A':
            supp_id = int(input("Enter the new supplier id : "))
            if supp_id:
                mycon.execute("update suppliers set supplier_id=%s where supplier_id=%s",(int(supp_id),s_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'B':
            supp_name = input("Enter the new supplier name : ")
            if supp_name:
                mycon.execute("update suppliers set supplier_name=%s where supplier_id=%s",(supp_name,s_id))
                print("record updated")
                mydb.commit()
                mycon.close()
        
        elif ch == 'C':
            c_info = int(input("Enter the new contact number : "))
            if c_info:
                mycon.execute("update suppliers set contact_info=%s where supplier_id=%s",(int(c_info),s_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'D':
            add = input("Enter the new address of the supplier : ")
            if add:
                mycon.execute("update suppliers set address=%s where supplier_id=%s",(add,s_id))
                print("record updated")
                mydb.commit()
                mycon.close()
        
        elif ch == 'E':
            print("Sorry ! no information updated")
            break

def update_record3():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the updation menu")
            break
        c_id = input("Enter the customer id : ").strip()
        if not c_id:
            print("Customer id is required")
            continue

        print("What do you want to upadate in this table ")
        print("A. for customer id ")
        print("B. for customer name ")
        print("C. for address of the customer  ")
        print("D. for mobile number of the customer ")
        print("E. for the cancellation of the program ")

        ch = input("Enter your choice (A-E) : ").strip().upper()
        if ch == 'A':
            cust_id = int(input("Enter the new customer id : "))
            if cust_id:
                mycon.execute("update customers set customer_id=%s where customer_id=%s",(int(cust_id),c_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'B':
            cust_name = input("Enter the new customer name : ")
            if cust_name:
                mycon.execute("update customers set customer_name=%s where customer_id=%s",(cust_name,c_id))
                print("record updated")
                mydb.commit()
                mycon.close()
        
        elif ch == 'C':
            addr = input("Enter the new address : ")
            if addr:
                mycon.execute("update customers set address=%s where customer_id=%s",(addr,c_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'D':
            mobi_no = int(input("Enter the new mobile number of the customer : "))
            if mobi_no:
                mycon.execute("update customers set mobi_no=%s where customer_id=%s",(int(mobi_no),c_id))
                print("record updated")
                mydb.commit()
                mycon.close()
        
        elif ch == 'E':
            print("Sorry ! no information updated")
            break

def update_record4():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the updation menu")
            break
        t_id = input("Enter the transaction id : ").strip()
        if not t_id:
            print("Transaction id is required")
            continue

        print("What do you want to upadate in this table ")
        print("A. for transaction id ")
        print("B. for product id ")
        print("C. for transaction type ")
        print("D. for quantity ")
        print("E. for the date of transaction ")
        print("F. for the user id of the transaction ")
        print("G. for the cancellation of the program ")

        ch = input("Enter your choice (A-G) : ").strip().upper()
        if ch == 'A':
            tr_id = int(input("Enter the new product id : "))
            if tr_id:
                mycon.execute("update transactions set transaction_id=%s where transaction_id=%s",(int(tr_id),t_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'B':
            prod_name = input("Enter the new product name : ")
            if prod_name:
                mycon.execute("update transactions set product_id=%s where transaction_id=%s",(prod_name,t_id))
                print("record updated")
                mydb.commit()
                mycon.close()
        
        elif ch == 'C':
            t_type = input("Enter the new transaction type : ")
            if t_type:
                mycon.execute("update transactions set transaction_type=%s where transaction_id=%s",(t_type,t_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'D':
            pr = int(input("Enter the new price of the product : "))
            if pr:
                mycon.execute("update products set price=%s where product_id=%s",(int(pr),t_id))
                print("record updated")
                mydb.commit()
                mycon.close()
        
        elif ch == 'E':
            q = int(input("Enter the new quantity : "))
            if q:
                mycon.execute("update products set quantity=%s where product_id=%s",(int(prod_name),t_id))
                print("record updated")
                mydb.commit()
                mycon.close()
        
        elif ch == 'F':
            su_id = int(input("Enter the supplier id  : "))
            if su_id:
                mycon.execute("update products set supplier_id=%s where product_id=%s",(int(prod_name),t_id))
                print("record updated")
                mydb.commit()
                mycon.close()
        
        elif ch == 'G':
            print("Sorry ! no information updated")
            break

def update_record5():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    while True:
        k = input("do you want to update entries (y/n) ? ")
        if k!='y':
            print("exiting the updation menu")
            break
        u_id = input("Enter the user id : ").strip()
        if not u_id:
            print("User id is required")
            continue

        print("What do you want to upadate in this table ")
        print("A. for user id ")
        print("B. for user name ")
        print("C. for password of the user ")
        print("D. for role of the user ")
        print("E. for the cancellation of the program ")

        ch = input("Enter your choice (A-E) : ").strip().upper()
        if ch == 'A':
            us_id = int(input("Enter the new user id : "))
            if us_id:
                mycon.execute("update users set user_id=%s where user_id=%s",(int(us_id),u_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'B':
            us_name = input("Enter the new user name : ")
            if us_name:
                mycon.execute("update users set user_name=%s where user_id=%s",(us_name,u_id))
                print("record updated")
                mydb.commit()
                mycon.close()
        
        elif ch == 'C':
            pwd = input("Enter the new password of the user : ")
            if pwd:
                mycon.execute("update users set password=%s where user_id=%s",(pwd,u_id))
                print("record updated")
                mydb.commit()
                mycon.close()

        elif ch == 'D':
            role = int(input("Enter the new role of the product : "))
            if role:
                mycon.execute("update users set role=%s where user_id=%s",(role,u_id))
                print("record updated")
                mydb.commit()
                mycon.close()
        
        elif ch == 'E':
            print("Sorry ! no information updated")
            break

def delete_record1():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    while True:
         k = input("do you want to delete entries (y/n) ? ")
         if k!='y':
            print("exiting the deletion menu")
            break
         else:
             print("What do you want to delete in this table ")
             print("A. for product id ")
             print("B. for product name ")
             print("C. for category of the product ")
             print("D. for price of the product ")
             print("E. for quantity of the product ")
             print("F. for the supplier id ")
             print("G. for the reorder level of the product ")
             print("H. for the cancellation of the program ")

             ch = input("Enter your choice (A-H) : ").strip().upper()
             if ch == 'A':
                 p_id = int(input("Enter the product id to delete : "))
                 mycon.execute("select * from product where product_id=%s;",(p_id,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such product id")
                 else:
                     mycon.execute("delete from product where product_id=%s;",(p_id,))
                     print("Record deleted")
                     mydb.commit()

             elif ch == 'B':
                 p_name = input("Enter the product name to delete : ")
                 mycon.execute("select * from product where product_name=%s;",(p_name,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such product name")
                 else:
                     mycon.execute("delete from product where product_name=%s;",(p_name,))
                     print("Record deleted")
                     mydb.commit()

             elif ch == 'C':
                 cate = input("Enter the category to delete : ")
                 mycon.execute("select * from product where category=%s;",(cate,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such category")
                 else:
                     mycon.execute("delete from product where category=%s;",(cate,))
                     print("Record deleted")
                     mydb.commit()

             elif ch == 'D':
                 p = int(input("Enter the price to delete : "))
                 mycon.execute("select * from product where price=%s;",(p,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such price")
                 else:
                     mycon.execute("delete from product where price=%s;",(p,))
                     print("Record deleted")
                     mydb.commit()
            
             elif ch == 'E':
                 qu = int(input("Enter the quantity of products to delete : "))
                 mycon.execute("select * from product where quantity=%s;",(qu,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such quantity")
                 else:
                     mycon.execute("delete from product where quantity=%s;",(qu,))
                     print("Record deleted")
                     mydb.commit()

             elif ch == 'F':
                 su_id = int(input("Enter the supplier id to delete : "))
                 mycon.execute("select * from product where supplier_id=%s;",(su_id,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such supplier id")
                 else:
                     mycon.execute("delete from product where supplier_id=%s;",(su_id,))
                     print("Record deleted")
                     mydb.commit()
            
             elif ch == 'G':
                 r_level = int(input("Enter the reorder level to delete : "))
                 mycon.execute("select * from product where reorder_level=%s;",(r_level,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such reorder level")
                 else:
                     mycon.execute("delete from product where reorder_level=%s;",(r_level,))
                     print("Record deleted")
                     mydb.commit()
             
             elif ch == 'H':
                 print("Sorry! No information deleted")
                 break

def delete_record2():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    while True:
         k = input("do you want to update entries (y/n) ? ")
         if k!='y':
            print("exiting the deletion menu")
            break
         else:
             print("What do you want to delete in this table ")
             print("A. for supplier id ")
             print("B. for supplier name ")
             print("C. for contact info of the supplier ")
             print("D. for address of the supplier  ")
             print("E. for the cancellation of the program ")

             ch = input("Enter your choice (A-E) : ").strip().upper()
             if ch == 'A':
                 s_id = int(input("Enter the supplier id to delete : "))
                 mycon.execute("select * from suppliers where supplier_id=%s;",(s_id,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such supplier id")
                 else:
                     mycon.execute("delete from suppliers where supplier_id=%s;",(s_id,))
                     print("Record deleted")
                     mydb.commit()

             elif ch == 'B':
                 s_name = input("Enter the supplier name to delete : ")
                 mycon.execute("select * from suppliers where supplier_name=%s;",(s_name,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such supplier name")
                 else:
                     mycon.execute("delete from suppliers where supplier_name=%s;",(s_name,))
                     print("Record deleted")
                     mydb.commit()

             elif ch == 'C':
                 c_info = int(input("Enter the contact info to delete : "))
                 mycon.execute("select * from suppliers where c_info=%s;",(c_info,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such contact info")
                 else:
                     mycon.execute("delete from suppliers where contact_info=%s;",(c_info,))
                     print("Record deleted")
                     mydb.commit()

             elif ch == 'D':
                 add = input("Enter the address to delete : ")
                 mycon.execute("select * from suppliers where address=%s;",(add,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such address")
                 else:
                     mycon.execute("delete from suppliers where address=%s;",(add,))
                     print("Record deleted")
                     mydb.commit()
             
             elif ch == 'E':
                 print("Sorry! No information deleted")
                 break
             
def delete_record3():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    while True:
         k = input("do you want to update entries (y/n) ? ")
         if k!='y':
            print("exiting the deletion menu")
            break
         else:
             print("What do you want to delete in this table ")
             print("A. for customer id ")
             print("B. for customer name ")
             print("C. for address of the customer ")
             print("D. for mobile of the customer ")
             print("E. for the cancellation of the program ")

             ch = input("Enter your choice (A-H) : ").strip().upper()
             if ch == 'A':
                 c_id = int(input("Enter the customer id to delete : "))
                 mycon.execute("select * from customers where customer_id=%s;",(c_id,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such customer id")
                 else:
                     mycon.execute("delete from customers where customer_id=%s;",(c_id,))
                     print("Record deleted")
                     mydb.commit()

             elif ch == 'B':
                 c_name = input("Enter the customer name to delete : ")
                 mycon.execute("select * from customers where customer_name=%s;",(c_name,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such customer name")
                 else:
                     mycon.execute("delete from customers where customer_name=%s;",(c_name,))
                     print("Record deleted")
                     mydb.commit()

             elif ch == 'C':
                 add = input("Enter the address to delete : ")
                 mycon.execute("select * from customers where address=%s;",(add,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such address")
                 else:
                     mycon.execute("delete from customers where address=%s;",(add,))
                     print("Record deleted")
                     mydb.commit()

             elif ch == 'D':
                 mob = int(input("Enter the mobile number to delete : "))
                 mycon.execute("select * from customers where mobile=%s;",(mob,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such mobile number")
                 else:
                     mycon.execute("delete from customers where mobile=%s;",(mob,))
                     print("Record deleted")
                     mydb.commit()
             
             elif ch == 'E':
                 print("Sorry! No information deleted")
                 break

def delete_record4():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    while True:
         k = input("do you want to update entries (y/n) ? ")
         if k!='y':
            print("exiting the deletion menu")
            break
         else:
             print("What do you want to delete in this table ")
             print("A. for transaction id ")
             print("B. for product id ")
             print("C. for transaction type ")
             print("D. for quantity ")
             print("E. for date ")
             print("F. for the user id ")
             print("G. for the cancellation of the program ")

             ch = input("Enter your choice (A-G) : ").strip().upper()
             if ch == 'A':
                 tr_id = int(input("Enter the transaction id to delete : "))
                 mycon.execute("select * from transactions where transaction_id=%s;",(tr_id,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such transaction id")
                 else:
                     mycon.execute("delete from transactions where transaction_id=%s;",(tr_id,))
                     print("Record deleted")
                     mydb.commit()

             elif ch == 'B':
                 p_id = int(input("Enter the product id to delete : "))
                 mycon.execute("select * from transactions where product_id=%s;",(p_id,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such product id")
                 else:
                     mycon.execute("delete from transactions where product_id=%s;",(p_id,))
                     print("Record deleted")
                     mydb.commit()

             elif ch == 'C':
                 tr_type = input("Enter the transaction type to delete : ")
                 mycon.execute("select * from transactions where transaction_type=%s;",(tr_type,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such transaction type")
                 else:
                     mycon.execute("delete from transaction where transaction_type=%s;",(tr_type,))
                     print("Record deleted")
                     mydb.commit()

             elif ch == 'D':
                 q = int(input("Enter the quantity to delete : "))
                 mycon.execute("select * from transactions where quantity=%s;",(q,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such quantity")
                 else:
                     mycon.execute("delete from transactions where quantity=%s;",(q,))
                     print("Record deleted")
                     mydb.commit()
            
             elif ch == 'E':
                 date = input("Enter the date of transactions to delete : ")
                 mycon.execute("select * from transactions where date=%s;",(date,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such date")
                 else:
                     mycon.execute("delete from transactions where date=%s;",(date,))
                     print("Record deleted")
                     mydb.commit()

             elif ch == 'F':
                 u_id = int(input("Enter the user id to delete : "))
                 mycon.execute("select * from transactions where user_id=%s;",(u_id,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such user id")
                 else:
                     mycon.execute("delete from transactions where user_id=%s;",(u_id,))
                     print("Record deleted")
                     mydb.commit()
             
             elif ch == 'G':
                 print("Sorry! No information deleted")
                 break
             
def delete_record5():
    mydb = mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="inventory")
    mycon = mydb.cursor()
    while True:
         k = input("do you want to update entries (y/n) ? ")
         if k!='y':
            print("exiting the deletion menu")
            break
         else:
             print("What do you want to delete in this table ")
             print("A. for user id ")
             print("B. for user name ")
             print("C. for password of the user ")
             print("D. for role of the user ")
             print("E. for the cancellation of the program ")

             ch = input("Enter your choice (A-E) : ").strip().upper()
             if ch == 'A':
                 u_id = int(input("Enter the user id to delete : "))
                 mycon.execute("select * from users where user_id=%s;",(u_id,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such user id")
                 else:
                     mycon.execute("delete from users where user_id=%s;",(u_id,))
                     print("Record deleted")
                     mydb.commit()

             elif ch == 'B':
                 u_name = input("Enter the user name to delete : ")
                 mycon.execute("select * from users where user_name=%s;",(u_name,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such user name")
                 else:
                     mycon.execute("delete from users where user_name=%s;",(u_name,))
                     print("Record deleted")
                     mydb.commit()

             elif ch == 'C':
                 pwd = input("Enter the password of the user to delete : ")
                 mycon.execute("select * from users where password=%s;",(pwd,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such password")
                 else:
                     mycon.execute("delete from users where password=%s;",(pwd,))
                     print("Record deleted")
                     mydb.commit()

             elif ch == 'D':
                 r = input("Enter the role of the user to delete : ")
                 mycon.execute("select * from users where role=%s;",(r,))
                 o = mycon.fetchall()
                 if not o :
                     print("No records found with such role")
                 else:
                     mycon.execute("delete from users where role=%s;",(r,))
                     print("Record deleted")
                     mydb.commit()
             
             elif ch == 'E':
                 print("Sorry! No information deleted")
                 break
             
def add_menu():
    while True:
        print("\nAdd Data")
        print("1. Products")
        print("2. Suppliers")
        print("3. Customers")
        print("4. Transactions")
        print("5. Users")

        ch = input("Select entity to add(0 to go back) : ").strip()
        if ch == '0':
            break
        elif ch == '1':
            addfile1()
        elif ch == '2':
            addfile2()
        elif ch == '3':
            addfile3()
        elif ch == '4':
            addfile4()
        elif ch == '5':
            addfile5()
        else:
            print("Invalid Choice")

def update_menu():
    while True:
        print("\nUpdate Data")
        print("1. Products")
        print("2. Suppliers")
        print("3. Customers")
        print("4. Transactions")
        print("5. Users")
        ch = input("Select entity to add(0 to go back) : ").strip()
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
        else:
            print("Invalid Choice")

            
def search_menu():
    while True:
        print("\nSearch Data")
        print("1. Products")
        print("2. Suppliers")
        print("3. Customers")
        print("4. Transactions")
        print("5. Users")
        ch = input("Select entity to add(0 to go back) : ").strip()
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
        else:
            print("Invalid Choice")

def delete_menu():
    while True:
        print("\nDelete Data")
        print("1. Products")
        print("2. Suppliers")
        print("3. Customers")
        print("4. Transactions")
        print("5. Users")
        ch = input("Select entity to add(0 to go back) : ").strip()
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
        else:
            print("Invalid Choice")

def menu():
    while True:
        print("\nWelcome to Inventory Management System")
        print("1. Add Data")
        print("2. Update Data")
        print("3. Search Data")
        print("4. Delete Data")
        print("5. Exit")
        ch = input("Select entity to add(0 to go back) : ").strip()
        if ch == '0':
            break
        elif ch == '1':
            add_menu()
        elif ch == '2':
            update_menu()
        elif ch == '3':
            search_menu()
        elif ch == '4':
            delete_menu()
        elif ch == '5':
            print("Exiting the system. Thank You!")
            break
        else:
            print("Invalid Choice")
menu()