import requests
import csv

def fetch_data(api_url, params):
    try:
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            # Assuming the API returns data in JSON format
            api_data = response.json()
            return api_data
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def append_to_csv(data):
    try:
        with open('output.csv', mode='a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())

            # Check if the file is empty and write headers if needed
            if csv_file.tell() == 0:
                writer.writeheader()

            # Write data to CSV
            writer.writerows(data)
        print(f"Data appended to {'output.csv'}")
    except Exception as e:
        print(f"Error appending to CSV: {e}")

def main():
    # Example API URL, replace with the actual API endpoint
    api_url = 'https://65a9fd5e081bd82e1d95d238.mockapi.io/person_details'

    # csv_file_path = 'output.csv'
    # Get user input for parameter choice
    print("Choose a parameter:")
    print("1. Id \t2. Name \t3.Department \t4.Enrollment \t5.Company \t6.Availability")
    choice = input("Enter the number corresponding to your choice: ")

    # Get user input for parameter value
    if choice == '1':
        param_name = 'id'
    elif choice == '2':
        param_name = 'Name'
    elif choice == '3':
        param_name = 'Department'
    elif choice == '4':
        param_name = 'Enrollment'
    elif choice == '5':
        param_name = 'Company'
    elif choice == '6':
        param_name = 'Available'
    else:
        print("Invalid choice. Exiting.")
        return

    param_value = input(f"Enter the value for {param_name}: ")

    # Construct parameters as a dictionary
    params = {
        param_name: param_value,
    }

    # Call the function to fetch data from the API
    api_data = fetch_data(api_url, params)

    # Process the retrieved data
    if api_data:
        print("Result Data:")
        print(api_data)
        # Add your code to process and display the data as needed

        append_to_csv(api_data)

main()
# if __name__ == "__main__":
#     main()
