import maskpass,csv

print("Enter the Type of User : \t\t\t1 Admin \t\t\t2 Student \t\t\t3 Exit")
while True:
    choice = input("Enter your choice '1' , '2' or '3' : ")
    if choice == '1':
        print("You have selected to Login as a Admin")

        # admin Login
        def fun2():
            pwd = maskpass.askpass()
            if pwd == 'Admin@123':
                print("Access Granted to Admin Side !")

                print("You want to add : \t1.Add Q/A or \t2.Add Student : ")
                admin_choice = input("Enter your choice '1' or '2' : ")

                if admin_choice == '1':
                    print("You have selected to Add Q/A")

                    n = int(input("Enter the number of Q/A you want to add : "))
                    i=0
                    count=0
                    with open('questions.csv', 'r',newline='') as file:
                        reader1 = csv.reader(file)
                        next(reader1)
                        for file in reader1:
                            count+=1

                    count+=1       
                    while i < n:
                        questions = input(f"Enter Question : ")
                        answer_a = input("Enter option A : ")
                        answer_b = input("Enter option B : ")
                        answer_c = input("Enter option C : ")
                        answer_d = input("Enter option D : ")
                        correct_ans = (input("Correct answer : ")).upper()
                        i+=1
                        
                        
                        with open('questions.csv', 'a', newline='') as question_file:
                            writer = csv.writer(question_file)
                            writer.writerow([f'{count}) {questions}'])

                        option_A = 'A'
                        option_B = 'B'
                        option_C = 'C'
                        option_D = 'D'

                        if correct_ans == 'A':
                            option_A = '[A]'
                        elif correct_ans == 'B':
                            option_B = '[B]'
                        elif correct_ans == 'C':
                            option_C = '[C]'
                        elif correct_ans == 'D':
                            option_D = '[D]'

                        with open('answers.csv', 'a', newline='') as answer_file:
                            writer = csv.writer(answer_file)
                            writer.writerow([f"{option_A}:{answer_a} \t\t\t {option_B}:{answer_b} \n {option_C}:{answer_c} \t\t\t {option_D}:{answer_d}"])


                elif admin_choice == '2':
                    from student_login import func
                    func()

            else:
                print("Invalid password")
                fun2()

        def fun1():
            uname = (input("Enter admin username : "))
            if uname =='admin':
                fun2()
            else:
                print("Invalid username")
                fun1()

        fun1()



    elif choice == '2':
        print("You have selected to Login as a Student")

            # Function to check if the provided username exists in the CSV file
        def check_username(username,password):
            with open('user_login.csv', mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip headers if present
                for row in reader:
                    if row[0] == username and row[1] == password:
                        return True
            return False

        # while True:
        # Get user input for username and password
        input_username = input("Enter student username: ")
        input_password = maskpass.askpass(prompt="Enter student password : ")
        

        # Check if the provided username already exists in the CSV file
        if check_username(input_username,input_password):
            # print("Username already exists in the CSV file.")
            print(input_username +" "+"is logined now.")

            # for rendering questions and answers
            with open('questions.csv', 'r') as row1:
                with open('answers.csv', 'r') as row2:
                    reader1 = csv.reader(row1)
                    reader2 = csv.reader(row2)
                    next(reader1)
                    next(reader2)
                    marks = 0
                    remove1 = '['
                    remove2 = ']'
                    for row1, row2 in zip(reader1, reader2):
                        clean1 = [element.replace(remove1, '') for element in row2]
                        clean2 = [element.replace(remove2, '') for element in clean1]
                        print(''.join(row1))
                        print(''.join(clean2))
                        ans = input("Enter your answers : ").upper()
                        print() 
                        
                        if 'A]' in row2[0]:
                            check='A'
                            if ans == check:
                                marks += 1

                            if 'B]' in row2[0]:
                                check='B'
                                if ans == check:
                                    marks+=1

                            elif 'C]' in row2[0]:
                                check='C'
                                if ans == check:
                                    marks+=1

                            elif 'D]' in row2[0]:
                                check='D'
                                if ans == check:
                                    marks+=1

                        elif 'B]' in row2[0]:
                            check='B'
                            if ans == check:
                                marks += 1

                            if 'A]' in row2[0]:
                                check='A'
                                if ans == check:
                                    marks+=1

                            elif 'C]' in row2[0]:
                                check='C'
                                if ans == check:
                                    marks+=1

                            elif 'D]' in row2[0]:
                                check='D'
                                if ans == check:
                                    marks+=1

                        elif 'C]' in row2[0]:
                            check='C'
                            if ans == check:
                                marks += 1

                            if 'A]' in row2[0]:
                                check='A'
                                if ans == check:
                                    marks+=1

                            elif 'B]' in row2[0]:
                                check='B'
                                if ans == check:
                                    marks+=1

                            elif 'D]' in row2[0]:
                                check='D'
                                if ans == check:
                                    marks+=1

                        elif 'D]' in row2[0]:
                            check='D'
                            if ans == check:
                                marks += 1

                            if 'A]' in row2[0]:
                                check='A'
                                if ans == check:
                                    marks+=1

                            elif 'B]' in row2[0]:
                                check='B'
                                if ans == check:
                                    marks+=1

                            elif 'C]' in row2[0]:
                                check='C'
                                if ans == check:
                                    marks+=1

                    counter=0
                    with open('questions.csv','r',newline='') as file:
                        reader1 = csv.reader(file)
                        next(reader1)
                        for file in reader1:
                            counter += 1
                    # print(input_username+' scored',(marks*100)/counter,"%")

                        
                        
                    results = [input_username,round((marks*100)/counter,2)]
                    with open('results.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(results)

                    percentage = (marks*100)/counter
                    def percentage_bar(percentage):
                        # if percentage < 0 or percentage > 100:
                        #     print("Invalid percentage. Please enter a percentage between 0 and 100.")
                        #     return

                        bar_length = 20
                        filled_length = int(bar_length * percentage / 100)

                        # Define rectangle characters
                        filled_char = '█'
                        empty_char = ' '

                        bar = filled_char * filled_length + empty_char * (bar_length - filled_length)

                        print(input_username+f' Scored : [{bar}] {percentage}%')

                    percentage_bar(percentage)

            
        else:
            print("Please ask admin to register student first.")
            break
            
    elif choice == '3':
        exit()