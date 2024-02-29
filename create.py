import sqlite3
import login

conn = sqlite3.connect("student_database.db")
cur = conn.cursor()

cur.execute(''' create table if not exists student
            (student_username text primary key,first_name text, last_name text,
            password text, phone_number int, address text, status default "active")
''')

conn.commit()
conn.close()

def create_student():
    try:
        student_username = input("enter student_username: ")

        conn = sqlite3.connect("student_database.db")
        cur = conn.cursor()
        cur.execute('''select * from student where student_username = ?''',(student_username,))

        result = cur.fetchone()

        if result is None:

            print("user is not exists, you can create user first")

            student_username = input("enter unique student username(text): ")
            first_name = input('enter your first name(text): ').capitalize()
            last_name = input("enter your last name(text): ").capitalize()
            password = input("enter your password(text): ")
            phone_no = int(input("enter your phn no(intger): "))
            adress = input("enter your address(text): ").capitalize()

            cur.execute(''' insert into student values (?,?,?,?,?,?,? )''',(student_username,first_name,last_name,
                                                                            password, phone_no,adress,"active"))
            
            print("\n user sucessfully created ")

        else:
            print(" \n user is already exists ")
            
            
    except ValueError:
        print("\nInvalid input. Please ensure telephone number is an integer.")
    
    except sqlite3.Error as e:
        print("\nAn error occurred:", e)

    finally:
        conn.commit()
        conn.close()
    
