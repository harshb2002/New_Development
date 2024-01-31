## Questions CSV file

import csv

questions = [
    ["1) Who developed Python Programming Language ?"],
    ["2) Which type of Programming does Python support ?"],
    ["3) Is Python case sensitive when dealing with identifiers ?"],
    ["4) Which of the following is the correct extension of the Python file ?"],
    ["5) All keywords in Python are in ?"],
    ["6) Which of the following is used to define a block of code in Python language ?"],
    ["7) Which keyword is used for function in Python language ?"],
    ["8) Which of the following character is used to give single-line comments in Python ?"],
    ["9) What does pip stand for python ?"],
    ["10) Which of the following is the truncation division operator in Python ?"]
]

file_path = 'questions.csv'

with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Questions'])

    for question in questions:
        writer.writerow(question)

print(f"CSV file '{file_path}' with questions has been created successfully!")