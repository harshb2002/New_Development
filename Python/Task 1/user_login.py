import csv


# function to get the data from the user
def get_user_input():
    data = []
    username = input("Enter username : ")
    password = input("Enter password : ")

    data.extend([username, password])
    return data

# declaring file path for csv file 
file_path = 'user_login.csv'

# function to append the data into the CSV file
def append_to_csv(data):
    with open('user_login.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Main program logic
while True:
    user_data = get_user_input()
    append_to_csv(user_data)

    choice = input("Do you want to another user ? (yes/no): ").lower()
    if choice == 'no':
        break