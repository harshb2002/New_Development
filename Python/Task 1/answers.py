#  answers CSV file 

import csv

answers=['[A]:Wick van Rossum''\t\t\tB:Rasmus Lerdorf''\n[C]:Guido van Rossum''\t\t\tD:Niene Stomma',
     'A:object-oriented programming''\t\t\t\tB:structured programming''\nC:functional programming''\t\t\t\t[D]:All of These',
     'A:No''\t\t\t\t[B]:Yes''\nC:Machine Dependent''\t\tD:None of these',
     'A:.python''\t\t\t[B]:.py''\nC:.pl''\t\t\t\tD:.p', 
     'A:Capitalized''\t\t\t[B]:lower case''\n[C]:UPPER CASE''\t\t\tD:None of these',
     '[A]:Indentation''\t\t\t\tB:Key''\nC:Brackets''\t\t\t\tD:All of these',
     'A:Function''\t\t\t[B]:def''\nC:Fun''\t\t\t\tD:Define',
     'A://''\t\t\t\t[B]:#''\nC:!''\t\t\t\tD:/*',
     'A:Pip Install Python''\t\t\t\tB:Pip Install Packages''\n[C]:Preferred Installer Program''\t\t\tD:All of these',
     'A:|''\t\t\t[B]://''\nC:/''\t\t\tD:%' ]

file_path = 'answers.csv'

with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Answers'])

    for answer in answers:
        writer.writerow([answer])
        print('/'.join([answer]))
        print()