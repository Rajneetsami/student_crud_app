import sqlite3
import time
import mongo

def update_student_first_name(first_name,student_username,):
    try:
        conn = sqlite3.connect("student_database.db")
        cur = conn.cursor()
        
        cur.execute('''UPDATE student set first_name = ? WHERE student_username = ?''',(first_name, student_username))
        conn.commit()
        conn.close()
    except Exception as e:
        print("\nError occurred while updating first name:", e)

def update_student_last_name(last_name, student_username):
    try:
        conn = sqlite3.connect("student_database.db")
        cur = conn.cursor()
        
        cur.execute('''UPDATE student set last_name = ? WHERE student_username =?''',(last_name, student_username))
        conn.commit()
        conn.close()
    except Exception as e:
        print("\nError occurred while updating last name:", e)


def update_student_password(password, student_username):
    try:
        conn = sqlite3.connect("student_database.db")
        cur = conn.cursor()
        
        cur.execute('''UPDATE student set password = ? WHERE student_username = ?''',(password, student_username))
        conn.commit()
        conn.close()
    except Exception as e:
        print("\nError occurred while updating password:", e)

def update_student_address(address,student_username):
    try:
        conn = sqlite3.connect("student_database.db")
        cur = conn.cursor()
        
        cur.execute('''UPDATE student set address = ? WHERE student_username = ?''',(address,student_username,))
        conn.commit()
        conn.close()
    except Exception as e:
        print("\nError occurred while updating adress:", e)


def update_student_phone_no(phone_no,student_username):
    try:
        conn = sqlite3.connect("student_database.db")
        cur = conn.cursor()
        
        cur.execute('''UPDATE student set phone_no = ? WHERE student_username = ?''',(phone_no,student_username))
        conn.commit()
        conn.close()
    except Exception as e:
        print("\nError occurred while updating phone no:", e)




def soft_delete_student_record(student_username):
    try:
        conn = sqlite3.connect("student_database.db")
        cur = conn.cursor()

        cur.execute('''SELECT status FROM student WHERE student_username = ?''', (student_username,))
        status = cur.fetchone()

        if status and status[0] == 'inactive':
            print("\nstudent is already inactive.")
            time.sleep(2)
        
        else:
            cur.execute('''UPDATE student SET status = 'inactive' WHERE student_username = ?''', (student_username,))
            print("\nRecord marked as inactive successfully.")
            time.sleep(2)
        

        conn.commit()
        conn.close()
    except Exception as e:
        print("\nError occurred while soft deleting record:", e)


def is_logged_in(student_username):

    while True:
        try:
        
            print("\tchoose option 1. Updation ")
            print("\tchoose option 2. Deletion")
            print("\tchoose option 3. post message or searching for title or message_count per user ")
            print("\tchoose option 4. Exit")

            choice = int(input("\nenter your choice: "))
        
            if choice == 1:
                while True:
                    print("\noption1: update first name: ")
                    print("\noption2: update last name: ")
                    print("\noption3: update password: ")
                    print("\noption4: update phone no: ")
                    print("\noption5: update adress: ")
                    print("\noption6: exit")

                    option  = int(input("\nenter your option: "))

                    if option == 1:
                        update_first_name = input("\nenter first name: ").capitalize()
                        update_student_first_name(update_first_name,student_username)
                        print( "\nfirst name successfully updated")
                        time.sleep(0.5)

                    elif option == 2:
                        update_last_name = input("\nenter last name: ").capitalize()
                        update_student_last_name(update_last_name,student_username)
                        print("\nlast name successfully updated")
                        time.sleep(0.5)
                    
                    elif option == 3:
                        update_password = input("\nenter password:  ")
                        update_student_password(update_password, student_username)
                        print("\npassword successfully updated")
                        time.sleep(0.5)
                    
                    elif option == 4:
                        update_phone_no = int(input("\nenter telephone: "))
                        update_student_phone_no(update_phone_no,student_username)
                        print("\nphone no successfully updated")
                        time.sleep(0.5)

                    elif option == 5:
                        update_address = input("\nenter address: ").capitalize()
                        update_student_address(update_address, student_username)
                        print("\naddress successfully updated")
                    
                        time.sleep(0.5)
                    
                    elif option == 6:
                        break
                    
                    else:
                        print("\ninvalid input")
                        time.sleep(0.5)
                
            elif choice == 2:
                soft_delete_student_record(student_username)

            elif choice ==3:
                mongo.post_message()

            elif choice == 4:
                print("\nYour are sucessfully logga ut")
                time.sleep(0.5)
                break
            
            else:
                print("invalid input")
    

        except Exception as e:
            print("\nError occurred in is_logged_in function:", e)
                


                




