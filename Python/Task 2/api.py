import requests , csv

def fetch_student_data(api_url, student_id):
    params = {        
        "id" : student_id
        }

    try:
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            # Assuming the API returns data in JSON format
            student_data = response.json()
            return student_data
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def append_to_csv(data):
    try:
        with open('student_details.csv', mode='a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())

            # Check if the file is empty and write headers if needed
            if csv_file.tell() == 0:
                writer.writeheader()

            # Write data to CSV
            writer.writerows(data)
        print(f"Data appended to {'student_details.csv'}")
    except Exception as e:
        print(f"Error appending to CSV: {e}")

def main():
    # Example API URL, replace with the actual API endpoint
    api_url = 'https://65a9fd5e081bd82e1d95d238.mockapi.io/person_details'
    
    id = int(input("Enter student id: "))    

    # Call the function to fetch student data from the API
    student_data = fetch_student_data(api_url, id)

    # Process the retrieved student data
    if student_data:
        print("Student Data:")
        print(student_data)
        # Add your code to process and display the student data as needed

        append_to_csv(student_data)

if __name__ == "__main__":
    main()
