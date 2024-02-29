
import csv
from create import create_student
import login


def main_function():
    try:
        while True:
                print("\n1) create user")
                print("\n2) login")
                print("\n3) exit")

                choice = input("enter your choice: ")
                if choice == "1":
                    create_student()
                    

                elif choice == "2":
                    login.student_login()

                elif choice == "3":
                    print("\nthank u for visting my application")
                    break

                else:
                    print("invalid input")

    except Exception as e:
        print("an error occur", e)


if __name__ == "__main__" :
    try:
        main_function()
        print("\nschedule task has been in processing..... ")
        login.schedule_task()
        print("\nData transfer and processing completed.")


    except Exception as e:
        print("\nAn unexpected error occurred:",e)
