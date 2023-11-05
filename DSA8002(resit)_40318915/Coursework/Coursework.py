#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sqlite3
import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)


# Function which displays the main menu of the library
def main_menu():
    try:
        print("                                  L I B R A R Y   M E N U                        \n\n\n\n")
        print("1. Add Books\n\n")
        print("2. Add Members\n\n")
        print("3. Search Book\n\n")
        print("4. Issue Book\n\n")
        print("5. Loaned Books\n\n")
        print("6. Return Book\n\n")
        print("7. Logout\n\n")
        print("8. Exit\n\n")

        choice = int(input("Enter your Choice(Only Numbers).......:"))
        if choice == 1:
            return Library.add_books()
        elif choice == 2:
            return Library.library_members()
        elif choice == 3:
            return book_search.search_books()
        elif choice == 4:
            return loan_book.search_book2(),loan_book.book_loan()
        elif choice == 5:
            return Loaned_books.show_loaned_books()
        elif choice == 6:
            return Loaned_books.return_books()
        elif choice == 7:
            print("You Have Been Logged Out\n\n")
            return Administrator.administrator()
        else:
            print("Application Closed \n\n")
            pass

    except:
        print("Enter Proper Details \n\n")
        click = input("Enter Any Button to Continue.....:")
        return main_menu()

# Class which will stores all details abot library
class Library:
    # Function which will add the new books to our library database
    def add_books():
        try:
            print("                                 Add Books                        \n\n\n")
            # opens a connection to the SQLite database file
            con = sqlite3.connect('library.db')

            # creates a cursor which will be used throughout of your database programming with Python
            cur = con.cursor()

            # Checks whether the table is already created
            listOfTables = cur.execute(
          """SELECT name FROM sqlite_master WHERE type='table' AND name='LIBRARY_BOOKS'; """).fetchall()

            isbn = int(input("Enter the ISBN :"))
            title = input("Enter the Book Title :")
            author = input("Enter the Author name :")
            year = int(input("Enter the Year :"))
            edition = input("Enter the Edition :")
            val = (isbn, title, author, year, edition, "Available")


            if listOfTables == []:
                cur.execute("""create table LIBRARY_BOOKS (Book_ISBN int PRIMARY KEY,
                Title nvarchar(255) NOT NULL,
                Author_Name nvarchar(255),
                Year int,
                Edition nvarchar(100),
                Loan_Status nvarchar(255));""")

                query = """ Insert into LIBRARY_BOOKS(Book_ISBN,Title,Author_Name,Year,Edition,Loan_Status) values(?,?,?,?,?,?)"""
                cur.execute(query, val)
                con.commit()
                cur.close()
                # Closes the connection
                con.close()
                print("Book Added Sucessfully")
                click = input("Enter Any Button to Continue.....:")
                return main_menu()
            else:
                query = """ Insert into LIBRARY_BOOKS(Book_ISBN,Title,Author_Name,Year,Edition,Loan_Status) values(?,?,?,?,?,?)"""
                cur.execute(query, val)
                con.commit()
                cur.close()
                con.close()
                print("Book Added Sucessfully")
                click = input("Enter Any Button to Continue.....:")
                return main_menu()

        except:
            print("Enter Proper Details \n\n")
            click = input("Enter Any Button to Continue.....:")
            return main_menu()

    #Function which will add new members to our database
    def library_members():
        try:
            print("                                 Add Members                        \n\n\n")
            con = sqlite3.connect('library.db')
            cur = con.cursor()
            listOfTables = cur.execute(
          """SELECT name FROM sqlite_master WHERE type='table' AND name='LIBRARY_MEMBERS'; """).fetchall()

            username = input("Enter the USERNAME (Email Address) :")
            password = input("Enter the Password :")
            name = input("Enter the Full name :")
            address = input("Enter the Address :")
            contact = int(input("Enter the Contact Number :"))
            plan = input("Enter the plan Basic or Premium ?")
            val = (username,password,name,address,contact,plan)


            if listOfTables == []:
                cur.execute("""create table LIBRARY_MEMBERS (Username nvarchar(255) PRIMARY KEY,
                Password nvarchar(255) NOT NULL,
                Full_Name nvarchar(255),
                Address nvarchar(255) ,
                Contact_Number int,
                Plan nvarchar(255));""")
                # Inserts new members details to our database
                query = """ Insert into LIBRARY_MEMBERS(Username,Password,Full_Name,Address,Contact_Number,Plan) values(?,?,?,?,?,?)"""
                cur.execute(query,val)
                con.commit()
                cur.close()
                con.close()
                print("Member Added\n\n")
                click = input("Enter Any Button to Continue.....:")
                return main_menu()
            else:
                query = """ Insert into LIBRARY_MEMBERS(Username,Password,Full_Name,Address,Contact_Number,Plan) values(?,?,?,?,?,?)"""
                cur.execute(query,val)
                con.commit()
                cur.close()
                con.close()
                print("Member Added\n\n")
                click = input("Enter Any Button to Continue.....:")
                return main_menu()
        except:
            print("Enter Proper Details \n\n")
            click = input("Enter Any Button to Continue.....:")
            return main_menu()


class Administrator:

    # Function which allows to login administrator/operator
    def administrator_login():
        try:
            print("                                  Login                        \n\n")
            username = input('Enter the USERNAME (Email Address) :')
            password = input("Enter the Password :")

            con = sqlite3.connect('library.db')
            cur = con.cursor()
            query = """select Username from LIBRARY_ADMINISTRATOR"""
            cur.execute(query)
            values = cur.fetchall()
            if (username,) in values:
                query = ("""select Password from LIBRARY_ADMINISTRATOR where Username=?""")
                cur.execute(query,(username,))
                pass_val = cur.fetchall()

                if (password,) in pass_val:
                    print("Login Succesful \n\n")
                    cur.close()
                    con.close()
                    return main_menu()
                else:
                    print("password incorrect \n\n")
                    cur.close()
                    con.close()
                    click = input("Enter Any Button to Continue.....:")
                    return Administrator.administrator()

            else:
                print("No Username found \n\n")
                cur.close()
                con.close()
                click = input("Enter Any Button to Continue.....:")
                return Administrator.administrator()
        except:
            print("Enter Proper Details \n\n")
            click = input("Enter Any Button to Continue.....:")
            return Administrator.administrator()

    # Function which Creates New Administrator/operator Account
    def administrator_sigin():
        try:
            print("                                 Signin                        \n\n")
            con = sqlite3.connect('library.db')
            cur = con.cursor()
            listOfTables = cur.execute(
            """SELECT name FROM sqlite_master WHERE type='table' AND name='LIBRARY_ADMINISTRATOR'; """).fetchall()

            name = input("Enter the Full name :")
            username = input("Enter the USERNAME (Email Address) :")
            password = input("Enter the Password :")
            val=(name, username, password)

            if listOfTables == []:
                cur.execute("""create table LIBRARY_ADMINISTRATOR (Full_Name nvarchar(255),Username nvarchar(255) PRIMARY KEY,
                    Password nvarchar(255) NOT NULL);""")

                query = """ Insert into LIBRARY_ADMINISTRATOR(Full_Name,Username,Password) values(?,?,?)"""
                cur.execute(query,val)
                con.commit()
                cur.close()
                con.close()
                print("Account Created \n\n")
                click = input("Enter Any Button to Continue.....:")
                return Administartor.administrator_login()
            else:
                query = """ Insert into LIBRARY_ADMINISTRATOR(Full_Name,Username,Password) values(?,?,?)"""
                cur.execute(query, val)
                con.commit()
                cur.close()
                con.close()
                print("Account Created \n\n")
                click = input("Enter Any Button to Continue.....:")
                return Administrator.administrator_login()

        except:
            print("Enter Proper Details \n\n")
            click = input("Enter Any Button to Continue.....:")
            return Administrator.administrator()

    # Administrator/operator main page function
    def administrator():
        try:
            print("                                 Adminstrator Login                        \n\n")
            print("1. Login    \n\n")
            print("2. Don't have account? signin    \n\n")

            option = int(input("Enter Your choice 1 or 2 ?"))
            if option == 1:
                return Administrator.administrator_login()
            else:
                return Administrator.administrator_sigin()
        except:
            print("Enter Proper Details \n\n")
            click = input("Enter Any Button to Continue.....:")
            return Administrator.administrator()


class book_search:
    # Function for searching the books using title
    def search_books():
        try:
            print("                                 Search Books                        \n\n\n")
            search = input("Enter the Book Name :")
            key_word = "%"+search+"%"
            con = sqlite3.connect('library.db')
            cur = con.cursor()
            Query = """Select * from LIBRARY_BOOKS where Title like ? """
            query = cur.execute(Query,(key_word,))
            book_val = query.fetchall()
            if len(book_val)>0:
                cols = [column[0] for column in query.description]
                results = pd.DataFrame.from_records(data = book_val, columns = cols)
                print(results,"\n\n")
            else:
                print("No Book Found try different keyword \n\n")
            cur.close()
            con.close()
            click = input("Enter Any Button to Continue.....:")
            return main_menu()
        except:
            print("Enter Proper Details \n\n")
            click = input("Enter Any Button to Continue.....:")
            return main_menu()

    # Function for doing inheritance
    def search_book2():
        try:
            print("                                 Search Books                        \n\n\n")
            search = input("Enter the Book Name :")
            key_word = "%"+search+"%"
            con = sqlite3.connect('library.db')
            cur = con.cursor()
            Query = """Select * from LIBRARY_BOOKS where Title like ? """
            query = cur.execute(Query,(key_word,))
            book_val = query.fetchall()
            if len(book_val)>0:
                cols = [column[0] for column in query.description]
                results = pd.DataFrame.from_records(data = book_val, columns = cols)
                print(results,"\n\n")
            else:
                print("No Book Found try different keyword\n\n")
            cur.close()
            con.close()
        except:
            print("Enter Proper Details \n\n")
            click = input("Enter Any Button to Continue.....:")
            return main_menu()

# Single level inheritance for listing the books search
class loan_book(book_search):
    # Function for loaning a book to member and adds it to a table
    def book_loan():
        try:
            print("                                 Loan Books                        \n\n\n")
            con = sqlite3.connect('library.db')
            cur = con.cursor()
            listOfTables = cur.execute(
            """SELECT name FROM sqlite_master WHERE type='table' AND name='LOAN_STATUS'; """).fetchall()

            if listOfTables == []:
                book = int(input("Enter the ISBN of Book :"))
                member = input("Enter the Member Username(Email Address) :")
                date = input("Enter Date(yyyy-mm-dd) :")
                query = """select Title from LIBRARY_BOOKS where Book_ISBN =?"""
                cur.execute(query, (book,))
                value = cur.fetchone()
                book_title = value[0]
                val = (book, book_title, member, date)
                cur.execute(("""create table LOAN_STATUS (Book_ISBN int,Title nvarchar(255),Username nvarchar(255),Date date NOT NULL);"""))
                query = """ insert into LOAN_STATUS values(?,?,?,?)"""
                cur.execute(query,(val))
                con.commit()
                # Updates the book status to loaned
                query = """update LIBRARY_BOOKS set Loan_Status=? where Book_ISBN=?"""
                cur.execute(query, ('Loaned',book))
                con.commit()
                cur.close()
                con.close()
                print("Thank You\n\n")
                click = input("Enter Any Button to Continue.....:")
                return main_menu()


            else:
                book = int(input("Enter the ISBN of Book :"))
                cur.execute("select Loan_Status from LIBRARY_BOOKS where Book_ISBN ="+str(book) +"")
                val = cur.fetchone()
                status = val[0]
                # Checks whether the book is loaned or available
                if status =='Available':
                    member = input("Enter the Member Username (Email Address) :")
                    query = """select Plan from LIBRARY_MEMBERS where Username =?"""
                    cur.execute(query, (member,))
                    plan_val = cur.fetchone()
                    plan_value = plan_val[0]
                    # Checks whether the member plan is basic or premium
                    if plan_value == 'Basic' or 'basic':
                        query="""select count(Username) from LOAN_STATUS where Username =?"""
                        limit_val = cur.execute(query,(member,))
                        for i in limit_val:
                            limit = int(i[0])
                        # Checks how many books loaned by member
                        if limit<2:
                            date = input("Enter Date(yyyy-mm-dd) :")
                            query = """select Title from LIBRARY_BOOKS where Book_ISBN =?"""
                            cur.execute(query,(book,))
                            value = cur.fetchone()
                            book_title = value[0]
                            tot_val = (book,book_title,member,date)
                            query = """ insert into LOAN_STATUS values(?,?,?,?)"""
                            cur.execute(query, (tot_val))
                            con.commit()
                            query = """update LIBRARY_BOOKS set Loan_Status=? where Book_ISBN=?"""
                            cur.execute(query, ("Loaned",book))
                            con.commit()
                            cur.close()
                            con.close()
                            print("Thank You\n\n")
                            click = input("Enter Any Button to Continue.....:")
                            return main_menu()
                        else:
                            print("Books cannot be loaned, Please return the loaned books\n\n")
                            click = input("Enter Any Button to Continue.....:")
                            return main_menu()
                    else:
                        query = """select count(Username) from LOAN_STATUS where Username =?"""
                        limit_val=cur.execute(query,(member,))
                        for i in limit_val:
                            limit = int(i[0])

                        if limit<4:
                            date = input("Enter Date(yyyy-mm-dd) :")
                            query = """select Title from LIBRARY_BOOKS where Book_ISBN =?"""
                            cur.execute(query,(book,))
                            value = cur.fetchone()
                            book_title = value[0]
                            tot_val = (book,book_title,member,date)
                            query = """ insert into LOAN_STATUS values(?,?,?,?)"""
                            cur.execute(query, (tot_val))
                            con.commit()
                            query = """update LIBRARY_BOOKS set Loan_Status=? where Book_ISBN=?"""
                            cur.execute(query, ("Loaned",book))
                            con.commit()
                            cur.close()
                            con.close()
                            print("Thank You \n\n")
                            click = input("Enter Any Button to Continue.....:")
                            return main_menu()
                        else:
                            print("Books cannot be loaned, Please return the loaned books\n\n")
                            click = input("Enter Any Button to Continue.....:")
                            return main_menu()

                else:
                    print("Book Unavailable\n\n")
                    click = input("Enter Any Button to Continue.....:")
                    return main_menu()

        except:
            print("Enter Proper Details \n\n")
            click = input("Enter Any Button to Continue.....:")
            return main_menu()

# Class for displaying the loaned books by member
class Loaned_books:
    def show_loaned_books():
        try:
            print("                                 Loaned Books                        \n\n\n")
            con = sqlite3.connect('library.db')
            cur=con.cursor()
            query=cur.execute("select Title,Username from LOAN_STATUS")
            book_val=query.fetchall()
            if len(book_val)>0:
                cols = ["Title","Username"]
                results= pd.DataFrame.from_records(data = book_val, columns = cols)
                print(results,"\n\n")
            else:
                print("No Books Loaned \n\n")
            cur.close()
            con.close()
            click=input("Enter Any Button to Continue.....:")
            return main_menu()
        except:
            print("No Books Loaned or Enter Correct Details \n\n")
            click = input("Enter Any Button to Continue.....:")
            return main_menu()


    # Function for returning the books by member to library
    def return_books():
        try:
            print("                                 Return Books                        \n\n\n")
            username=input("Enter the Username(Email Address) :")
            con = sqlite3.connect('library.db')
            cur=con.cursor()
            Query="""select Book_ISBN,Title,Username from LOAN_STATUS where Username=?"""
            query=cur.execute(Query,(username,))
            user_val=query.fetchall()
            if len(user_val)>0:
                cols = ["Book_ISBN","Title","Username"]
                results= pd.DataFrame.from_records(data = user_val, columns = cols)
                print(results,"\n\n")
                isbn=int(input("Enter the ISBN :"))

                # Checks how many days the book loaned by member

                query="""SELECT julianday('now') - julianday(Date) FROM LOAN_STATUS where Username=? and Book_ISBN=?"""
                cur.execute(query,(username,isbn))
                fine_days=cur.fetchone()
                days=int(fine_days[0])

                print("Total Days :", days , "days\n\n")
                # Calculates the fine amount
                if days>60:
                    print("Fine Amount 10pounds \n\n")
                else:
                    print("Thank You \n\n")

                query="""delete from LOAN_STATUS where Book_ISBN=?"""
                cur.execute(query,(isbn,))
                query="""update LIBRARY_BOOKS set Loan_Status=? where Book_ISBN=?"""
                cur.execute(query,('Available',isbn))
                con.commit()

            else:
                print("No Books Loaned By User  \n\n")
            cur.close()
            con.close()
            click=input("Enter Any Button to Continue.....:")
            return main_menu()
        except:
            print("Enter Proper Details \n\n")
            click=input("Enter Any Button to Continue.....:")
            return main_menu()


Administrator.administrator()

# In[ ]:





# In[ ]:




