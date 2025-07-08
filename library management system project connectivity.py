from config import DB_PASSWORD
import mysql.connector as mys
mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="library")
mycon=mydb.cursor()

def create_books():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="library")
    mycon=mydb.cursor()
    mycon.execute("create table if not exists books(book_id int,title varchar(100),author varchar(100),genre varchar(50),publication_year date,copies_availaible int);")
    mydb.commit()

create_books()

def create_transaction():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="library")
    mycon=mydb.cursor()
    mycon.execute("create table if not exists transaction(transaction_id int,member_id int,book_id int,issue_date date,due_date date,return_date date,fine int);")
    mydb.commit()

create_transaction()

def add_books():
    while True:
        mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="library")
        mycon=mydb.cursor()
        book_id=int(input("enter book id : "))
        title=input("enter the title of the book : ")
        author=input("enter the name of the author of the book: ")
        genre=input("enter the genre of the book: ")
        publication_year=input("enter the year of publication of the book : ")
        copies_available=int(input("enter the number of copies available : "))
        sql="insert into books (book_id,title,author,genre,publication_year,copies_available) VALUES(%s,%s,%s,%s,%s,%s);"
        values=(book_id,title,author,genre,publication_year,copies_available)

        mycon.execute(sql,values)
        mydb.commit()
        mydb.close()
        mycon.close()

        ans=input("do you want to enter more entries(y/n) : ").strip().lower()
        if ans=="n":
            print("thank you for adding the details of the book in the table ")
            break
        mycon.close()
    

def add_transaction():
    while True:
        mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="library")
        mycon=mydb.cursor()
        transaction_id=int(input("enter the transaction id of the person : "))
        member_id=int(input("enter the member id of the person : "))
        book_id=int(input("enter the book_id of the book : "))
        issue_date=input("enter the issue date of the book issued : ")
        due_date=input("enter the due date of the book to be returned : ")
        return_date=input("enter the return date of the book : ")
        fine=int(input("enter the fine on the book issued : "))
        sql="insert into transaction (transaction_id,member_id,book_id,issue_date,due_date,return_date,fine) VALUES(%s,%s,%s,%s,%s,%s,%s);"
        values=(transaction_id,member_id,book_id,issue_date,due_date,return_date,fine)

        mycon.execute(sql,values)
        mydb.commit()
        mydb.close()
        mycon.close()

        ans=input("do you want to enter more entries(y/n) : ").strip().lower()
        if ans=="n":
            print("thank you for adding the details of the transactions of the library in the table ")
            break
        mycon.close()


def update_books():
     mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="library")
     mycon=mydb.cursor()
     while True:
         ch=input("do you want to update entries in the books table(y/n) : ")
         if ch!="y":
             print("exiting the updation menu ")
             break
         
         book_id=input("enter the book id : ").strip()
         if not book_id():
             print("book id is required ")
             continue
        
         print("what do you want to update ? : ")
         print("a. for book id of the book : ")
         print("b. for title of the book : ")
         print("c. for the author of the book : ")
         print("d. for the genre of the book : ")
         print("e. for the publication year of the book : ")
         print("f. for the copies available of the book : ")
         print("g. for exiting the updation menu ")

         ch=input("enter your choices (a-g) : ").strip().lower()
         if ch == 'a':
             b_id=int(input("enter the book id to update : "))
             if b_id:
                 mycon.execute("update book set book_id=%s where book_id=%s",(int(b_id),book_id))
                 print("record updated")
                 mydb.commit()
                 mycon.close()
        
         elif ch == 'b':
             t=input("enter the title of the book to update : ")
             if t:
                 mycon.execute("update book set title=%s where book_id=%s",(int(t),book_id))
                 print("record updated")
                 mydb.commit()
                 mycon.close()
         
         elif ch == 'c':
             a=input("enter the author of the book to update : ")
             if a:
                 mycon.execute("update book set author=%s where book_id=%s",(a,book_id))
                 print("record updated")
                 mydb.commit()
                 mycon.close()

         elif ch == 'd':
             g=input("enter the genre of the book to update : ")
             if g:
                 mycon.execute("update book set genre=%s where book_id=%s",(g,book_id))
                 print("record updated")
                 mydb.commit()
                 mycon.close()

         elif ch == 'e':
             p_year=input("enter the publication year of the book to update : ")
             if p_year:
                 mycon.execute("update book set publication_year=%s where book_id=%s",(int(p_year),book_id))
                 print("record updated")
                 mydb.commit()
                 mycon.close()
        
         elif ch == 'f':
             copies=int(input("enter the copies available of the book to update : "))
             if copies:
                 mycon.execute("update book set copies_available=%s where book_id=%s",(int(copies),book_id))
                 print("record updated")
                 mydb.commit()
                 mycon.close()
        
         elif ch == 'g':
             print("sorry ! but no information is updated ")
             break
         
         else:
             print("sorry invalid operation ")
             break

def update_transaction():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="library")
    mycon=mydb.cursor()
    while True:
         ch=input("do you want to update entries in the transaction table(y/n) : ")
         if ch!="y":
             print("exiting the updation menu ")
             break
         
         book_id=input("enter the book id : ").strip()
         if not book_id():
             print("book id is required ")
             continue
         
         print("what do you want to update ? : ")
         print("a. for transaction id  of the book : ")
         print("b. for member id  of the book : ")
         print("c. for the book id of the book : ")
         print("d. for the date of the book issued : ")
         print("e. for the due date of the book issued : ")
         print("f. for the return date of the book issued : ")
         print("g. for the fine on the book issued")
         print("h. for exiting the updation menu ")

         ch=input("enter the choice (a-h) : ").strip()
         if ch == 'a':
             t_id=int(input("enter the transaction id of the book to update : "))
             if t_id:
                 mycon.execute("update transaction set transaction_id=%s where book_id=%s",(int(t_id),book_id))
                 print("record updated")
                 mydb.commit()
                 mycon.close()
        
         elif ch == 'b':
             m_id=int(input("enter the member id of the book to update : "))
             if m_id:
                 mycon.execute("update book set member_id=%s where book_id=%s",(int(m_id),book_id))
                 print("record updated")
                 mydb.commit()
                 mycon.close()

         elif ch == 'c':
             b_id=int(input("enter the book id to update : "))
             if b_id:
                 mycon.execute("update book set book_id=%s where book_id=%s",(int(b_id),book_id))
                 print("record updated")
                 mydb.commit()
                 mycon.close()

         elif ch == 'd':
             is_date=input("enter the date of issue to update : ")
             if is_date:
                 mycon.execute("update book set issue_date=%s where book_id=%s",(is_date,book_id))
                 print("record updated")
                 mydb.commit()
                 mycon.close()

         elif ch == 'e':
             d_date=input("enter the due date of the book to update : ")
             if d_date:
                 mycon.execute("update book set due_date=%s where book_id=%s",(d_date,book_id))
                 print("record updated")
                 mydb.commit()
                 mycon.close()
        
         elif ch == 'f':
             r_date=input("enter the return date of the book to update : ")
             if r_date:
                 mycon.execute("update book set return_date=%s where book_id=%s",(r_date,book_id))
                 print("record updated")
                 mydb.commit()
                 mycon.close()

         elif ch == 'g':
             f=int(input("enter the fine to update : "))
             if f:
                 mycon.execute("update book set fine=%s where book_id=%s",(int(f),book_id))
                 print("record updated")
                 mydb.commit()
                 mycon.close()
        
         elif ch == 'h':
             print("sorry ! but no information is updated ")
             break
         
         else:
             print("sorry ! invalid operation ")
             break
        
def delete_data():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="library")
    mycon=mydb.cursor()
    mycon.execute("select * from books,transaction where books.book_id=transaction.book_id;")
    x=mycon.fetchall()
    while True:
        ch=input("do you wanto delete entries(y/n) : ").strip().lower()
        if ch!='y':
            print("exiting the deletion menu ")
            break

        else:
         print("what do you want to delete ? : ")
         print("A. for book id of the book : ")
         print("B. for title of the book : ")
         print("C. for the author of the book : ")
         print("D. for the genre of the book : ")
         print("E. for the publication year of the book : ")
         print("F. for the copies available of the book : ")
         print("G. for transaction id  of the book : ")
         print("H. for member id  of the book : ")
         print("I. for the date of the book issued : ")
         print("J. for the due date of the book issued : ")
         print("K. for the return date of the book issued : ")
         print("L. for the fine on the book issued")
         print("M. for exiting the deletion menu ")

         c=input("enter your choice(A-M) : ").strip().upper()
         if c == 'A':
             b_id=int(input("enter the book id to delete : "))
             mycon.execute("select * from books,transaction where book_id=%s;",(b_id,))
             o=mycon.fetchall()
             if not o:
                 print("no records found with such book id ")
             else:
                 mycon.execute("delete from books,transaction where book_id=%s;",(b_id))
                 print("record deleted")
                 mydb.commit()
        
         elif c == 'B':
             t=input("enter the title of the book to delete : ")
             mycon.execute("select * from books,transaction where title=%s;",(t,))
             o=mycon.fetchall()
             if not o:
                 print("no records found with such title ")
             else:
                 mycon.execute("delete from books,transaction where title=%s;",(t,))
                 print("record deleted")
                 mydb.commit()
        
         elif c == 'C':
             a=input("enter the author of the book to delete : ")
             mycon.execute("select * from books,transaction where author=%s;",(a,))
             o=mycon.fetchall()
             if not o:
                 print("no records found with such author name ")
             else:
                 mycon.execute("delete from books,transaction where author=%s;",(a,))
                 print("record deleted")
                 mydb.commit()
        
         elif c == 'D':
             g=input("enter the genre of the book to delete : ")
             mycon.execute("select * from books,transaction where genre=%s;",(g,))
             o=mycon.fetchall()
             if not o:
                 print("no records found with such genre ")
             else:
                 mycon.execute("delete from books,transaction where genre=%s;",(g,))
                 print("record deleted")
                 mydb.commit()

         elif c == 'E':
             p_year=input("enter the publication year of the book to delete : ")
             mycon.execute("select * from books,transaction where publication_year=%s;",(p_year,))
             o=mycon.fetchall()
             if not o:
                 print("no records found with such publication year ")
             else:
                 mycon.execute("delete from books,transaction where publication_year=%s;",(p_year,))
                 print("record deleted")
                 mydb.commit()

         elif c == 'F':
             c_available=input("enter the copies available of the book to delete : ")
             mycon.execute("select * from books,transaction where copies_available=%s;",(c_available,))
             o=mycon.fetchall()
             if not o:
                 print("no records found with such copies available ")
             else:
                 mycon.execute("delete from books,transaction where copies_available=%s;",(c_available,))
                 print("record deleted")
                 mydb.commit()

         elif c == 'G':
             t_id=input("enter the transaction id of the book to delete : ")
             mycon.execute("select * from books,transaction where transaction_id=%s;",(t_id,))
             o=mycon.fetchall()
             if not o:
                 print("no records found with such transaction id ")
             else:
                 mycon.execute("delete from books,transaction where transaction_id=%s;",(t_id,))
                 print("record deleted")
                 mydb.commit()

         elif c == 'H':
             m=input("enter the member id of the book to delete : ")
             mycon.execute("select * from books,transaction where member_id=%s;",(m,))
             o=mycon.fetchall()
             if not o:
                 print("no records found with such member id ")
             else:
                 mycon.execute("delete from books,transaction where member_id=%s;",(m,))
                 print("record deleted")
                 mydb.commit()

         elif c == 'I':
             i=input("enter the issue date of the book to delete : ")
             mycon.execute("select * from books,transaction where issue_date=%s;",(i,))
             o=mycon.fetchall()
             if not o:
                 print("no records found with such issue date ")
             else:
                 mycon.execute("delete from books,transaction where issue_date=%s;",(i,))
                 print("record deleted")
                 mydb.commit()

         elif c == 'J':
             d=input("enter the due date of the book to delete : ")
             mycon.execute("select * from books,transaction where due_date=%s;",(d,))
             o=mycon.fetchall()
             if not o:
                 print("no records found with such due data ")
             else:
                 mycon.execute("delete from books,transaction where due_date=%s;",(d,))
                 print("record deleted")
                 mydb.commit()

         elif c == 'K':
             r=input("enter the return date of the book to delete : ")
             mycon.execute("select * from books,transaction where return_date=%s;",(r,))
             o=mycon.fetchall()
             if not o:
                 print("no records found with such return date")
             else:
                 mycon.execute("delete from books,transaction where return_date=%s;",(r,))
                 print("record deleted")
                 mydb.commit()
        
         elif c == 'L':
             f=input("enter the fine on the book to delete : ")
             mycon.execute("select * from books,transaction where fine=%s;",(f,))
             o=mycon.fetchall()
             if not o:
                 print("no records found with such fine ")
             else:
                 mycon.execute("delete from books,transaction where fine=%s;",(f,))
                 print("record deleted")
                 mydb.commit()

         elif c == 'M':
             print("sorry! exiting the deletion menu ")
             break
         
         else:
             print("sorry! invalid operation ")
             break
         
def search_data():
    mydb=mys.connect(host="localhost",user="root",password=DB_PASSWORD,database="library")
    mycon=mydb.cursor()

    while True:
        k=input("do you want to search entries? (y/n) : ")
        if k!='y':
            print("exiting the search menu")
            break
        else:
            print("what do you want to search ? : ")
            print("A. for book id of the book : ")
            print("B. for title of the book : ")
            print("C. for the author of the book : ")
            print("D. for the genre of the book : ")
            print("E. for the publication year of the book : ")
            print("F. for the copies available of the book : ")
            print("G. for transaction id  of the book : ")
            print("H. for member id  of the book : ")
            print("I. for the date of the book issued : ")
            print("J. for the due date of the book issued : ")
            print("K. for the return date of the book issued : ")
            print("L. for the fine on the book issued")
            print("M. for exiting the search menu ")

            o=input("enter your choice(A-M) : ").strip().upper()
            if o == 'A':
                b_id=int(input("enter the book id of the book to search : "))
                mycon.execute("select * from books,transaction where book_id=%s;",(b_id,))
            
            elif o == 'B':
                t=input("enter the title of the book to search : ")
                mycon.execute("select * from books,transaction where title=%s;",(t,))

            elif o == 'C':
                a=input("enter the author of the book to search : ")
                mycon.execute("select * from books,transaction where author=%s;",(a,))

            elif o == 'D':
                g=input("enter the genre of the book to search : ")
                mycon.execute("select * from books,transaction where genre=%s;",(g,))

            elif o == 'E':
                p_year=input("enter the publication year of the book to delete : ")
                mycon.execute("select * from books,transaction where publication_year=%s;",(p_year,))
            
            elif o == 'F':
                c_available=input("enter the copies available of the book to delete : ")
                mycon.execute("select * from books,transaction where copies_available=%s;",(c_available,))

            elif o == 'G':
                t_id=input("enter the transaction id of the book to delete : ")
                mycon.execute("select * from books,transaction where transaction_id=%s;",(t_id,))
            
            elif o == 'H':
                m=input("enter the member id of the book to delete : ")
                mycon.execute("select * from books,transaction where member_id=%s;",(m,))

            elif o == 'I':
                i=input("enter the issue date of the book to delete : ")
                mycon.execute("select * from books,transaction where issue_date=%s;",(i,))

            elif o == 'J':
                d=input("enter the due date of the book to delete : ")
                mycon.execute("select * from books,transaction where due_date=%s;",(d,))
            
            elif o == 'K':
                r=input("enter the return date of the book to delete : ")
                mycon.execute("select * from books,transaction where return_date=%s;",(r,))

            elif o == 'L':
                f=input("enter the fine on the book to delete : ")
                mycon.execute("select * from books,transaction where fine=%s;",(f,))
            
            elif o == 'M':
                print("sorry! no information searched ")
                break

            else:
                print("sorry! invalid operation ")
                break

def menu():
    while True:
        print("Welcome to library management system")
        print("1. for addition of data in books table")
        print("2. for addition of data in transactions table")
        print("3. for updation in books table")
        print("4. for updation in transactions table")
        print("5. for deletion in books and transactions table")
        print("6. for searching in books and transactions table")
        print("7. for closing the program")

        ch=input("enter your choice (1-7) : ")
        if ch == '1':
            add_books()
        
        elif ch == '2':
            add_transaction()

        elif ch == '3':
            update_books()

        elif ch == '4':
            update_transaction()
        
        elif ch == '5':
            delete_data()

        elif ch == '6':
            search_data()

        elif ch == '7':
            print("exiting the program!! good bye!!")
            break

        else:
            print("invalid choice. please enter a choice between (1-7) : ")
            break
menu()