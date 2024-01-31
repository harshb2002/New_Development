import csv

# def check_answer():
#     with open('answers.csv', 'r', newline='') as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             print('/'.join(row))
#             # if '[A]' in row[0]:
#             #     print("A is the Correct Answer")
#             # elif '[B]' in row[0]:
#             #     print("B is the Correct Answer")
#             # elif '[C]' in row[0]:
#             #     print("C is the Correct Answer")
#             # elif '[D]' in row[0]:
#             #     print("D is the Correct Answer")
#     check_answer()


answers = [ 'A : Wick van Rossum' '\t\t\tB : Rasmus Lerdorf ' '\n[C] : Guido van Rossum' '\t\t\tD : Niene Stomma\n',   
            'A : object-oriented programming', ' \t\tB : structured programming', ' \nC : functional programming', ' \t\t\t[D] : All of These\n',
            'A : No', ' \t\t\t\t[B] : Yes', ' \nC : Machine Dependent', ' \t\tD : None of these\n',
            'A : .python', ' \t\t\t[B] : .py', ' \nC : .pl', ' \t\t\tD : .p\n',
            'A : Capitalized', ' \t\tB : lower case', ' \nC : UPPER CASE', ' \t\t\t[D] : None of these\n',
            '[A] : Indentation', ' \t\tB : Key', ' \nC : Brackets', ' \t\t\tD : All of these\n',
            'A : Function', ' \t\t\t[B] : def', ' \nC : Fun', ' \t\t\tD : Define\n',
            'A : //', ' \t\t[B] : #', ' \nC : !', ' \t\tD : /*\n',
            'A : Pip Installs Python', ' \t\t\tB : Pip Installs Packages', ' \n[C] : Preferred Installer Program', ' \t\tD : All of these\n',
            'A : |', ' \t\t\t[B] : //', ' \nC : /', ' \t\t\tD : %\n' ]

for row in answers:
    if '[A]' in row:
        print("A is the Correct Answer")
    elif '[B]' in row:
        print("B is the Correct Answer")
    elif '[C]' in row:
        print("C is the Correct Answer")
    elif '[D]' in row:
        print("D is the Correct Answer")