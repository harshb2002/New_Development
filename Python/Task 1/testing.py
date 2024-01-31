# print("Enter the input : \n1 for Converting Celcius to Fahrenheit \n2 for Converting Fahrenheit to Celsius \n3 for exit")

# while True:
#     choice = int(input("Enter your choice '1' or '2' or '3' : "))
#     if(choice == 1):
#         c = int(input("Enter the Celcius : "))
#         f = (c * 1.8) + 32
#         print("Fahrenheit : ",f)
#     elif(choice == 2):
#         f = int(input("Enter the Fahrenheit : "))
#         c = (f - 32) // 1.8
#         print("Celsius : ",c)
#     if(choice == 3):
#         exit()

# import csv (logic 1)

# def answer():
#     with open('answers.csv', mode='r') as file:
#         reader = csv.reader(file)# Skip headers if present
#         next(reader)
#         for row in reader:
#             print('/'.join(row))
# answer()

# def question():
#     with open('questions.csv', mode='r',newline='') as file:
#         reader = csv.reader(file)# Skip headers if present
#         next(reader)
#         for row in reader:
#             print('/'.join(row))
# question()

# def question_answer():
#     answer_reader = answer()
#     question_reader = question()

#     for question in question_reader:
#         try:
#             answer = next(answer_reader)
#             print(question)
#             print(answer)
#         except StopIteration:
#             print("No more answers available.")
#             break
#     question_answer()

#if row2 in reader2:
    #     if ['A'] in reader2[row2]:
    #         print("A is the Correct Answer")
    #     elif 'B' in reader2[row2]:
    #         print("B is the Correct Answer")

import csv
# def check_ans():
#     with open('answers.csv', mode='r',newline='') as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             # print(''.join(row))
#             if "[A]" in row[0]:
#                 print("A is the Correct Answer")
#             elif "[B]" in row[0]:
#                 print("B is the Correct Answer")
#             elif "[C]" in row[0]:
#                 print("C is the Correct Answer")
#             elif "[D]" in row[0]:
#                 print("D is the Correct Answer")
# check_ans()