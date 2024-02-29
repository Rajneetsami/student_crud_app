Overview
This repository contains Python scripts for a student management system. The system allows users to create student accounts, log in, post messages, search for titles, and retrieve the number of messages sent by a user. Data is stored in SQLite databases and MongoDB, and scheduling tasks are implemented using the schedule library.

Files
main.py: This file contains the main function to execute the student management system. It provides options for creating user accounts, logging in, and exiting the application.
create.py: This file contains functions for creating student accounts. It interacts with the SQLite database to insert student records.
login.py: This file handles the login functionality for students. It verifies user credentials against the SQLite database and records login activities in a CSV file,and schedules tasks for data transfer.
mongo.py: This file manages the posting of messages functionality. It allows users to post messages, search for titles, and retrieve the number of messages sent by a user. MongoDB is used to store message data.


Setup
To run the student management system, follow these steps:

Install Python on your system if not already installed.
Create an virtual environment (recommended)
Install the required Python libraries by running pip install -r requirements.txt.
Ensure that MongoDB is installed and running on your system.
Run the main.py file to start the application.

Usage
Upon running the application, users will be prompted with a menu to choose from various options:

Create User: Allows users to create student accounts by providing necessary details.
Login: Allows students to log in using their credentials.
Exit: Terminates the application.
After logging in, users can perform the following actions:

Update Profile: Allows users to update their profile information, including first name, last name, password, phone number, and address.
Delete Account: Allows users to soft delete their account, marking it as inactive.
Post Message: Allows users to post messages, search for titles, and retrieve the number of messages sent by a user


