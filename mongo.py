import pymongo
from pymongo import MongoClient
import time

def post_message():
    try:

        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client['student2']
        collection = db['post']


        print("\nOptions:")
        print("1. Post a message")
        print("2. Search for a title")
        print("3. Get number of messages sent by a user")
        option = int(input("Enter your choice: "))

        if option == 1:
            title = input("Enter the title of the post: ").capitalize()
            username = input("Enter your username: ").capitalize()
            message = input("Enter your message: ")
            post_data = {"title": title, "username": username, "message": message}
            collection.insert_one(post_data)
            print("Post added successfully!")

        elif option == 2:
            title_query = input("Enter the title to search for: ").capitalize()
            posts = collection.find({"title": {"$regex": title_query, "$options": "i"}})
            print("\nSearch Results:")
            found_posts = False
            for post in posts:
                print(post)
                found_posts = True
            if not found_posts:
                print("You don't have any messages yet.")
                time.sleep(1)
            
        elif option == 3:
            username = input("Enter the username to get message count: ").capitalize()
            count = collection.count_documents({"username": username})
            print(f"\nNumber of messages sent by {username}: {count}")

        else:
            print("Invalid option!")

    except pymongo.errors.ConnectionFailure as e:
        print(f"Connection to MongoDB failed: {e}")

    except ValueError:
        print("Invalid input! Please enter a valid option.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        if 'client' in locals() and client:
            client.close()