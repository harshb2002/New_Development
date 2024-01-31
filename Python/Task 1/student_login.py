import csv


# Function to check if the provided username exists in the CSV file
def check_username(username,password):
    with open('user_login.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip headers if present
        for row in reader:
            if row[0] == username and row[1] == password:
                return True
    return False

# Function to append new user data to the CSV file
def append_user(username, password):
    with open('user_login.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    print("New user added successfully.")

def func():
    while True:
        # Get user input for username and password
        input_username = input("Enter student username: ")
        input_password = input("Enter student password: ")

        # Check if the provided username already exists in the CSV file
        if check_username(input_username,input_password):
            print("Username already exists.")
        else:
            append_user(input_username, input_password)
            while True:
                choice = input("Do you want to another user ? (yes/no): ").lower()
                if choice == 'yes':
                    func()
                elif choice == 'no':
                    return True
                else:
                    print("Invalid input")
        return True                
                
func()