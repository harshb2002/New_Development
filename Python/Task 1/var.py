# import matplotlib.pyplot as plt
# import numpy as np

# while True:
#     def create_loading_bar(percentage):
#         if percentage < 0 or percentage > 100:
#             print("Invalid percentage. Please enter a percentage between 0 and 100.")
#             return

#         # Create a horizontal loading bar
#         fig, ax = plt.subplots()
#         ax.barh(0, percentage, color='green', edgecolor='black', height=1.0)

#         # Customize the plot
#         ax.set_xlim(0, 100)
#         ax.set_xticks(np.arange(0, 110, 10))
#         ax.set_yticks([])
#         ax.set_title('Loading Bar - Exam Percentage')

#         # Add the percentage label
#         ax.text(percentage + 2, 0, f'{percentage}%', va='center', fontsize=12, fontweight='bold')

#         plt.show()

# # Get percentage input from the user
#     try:
#         percentage = float(input("Enter the percentage obtained in the examination: "))
#         create_loading_bar(percentage)
#     except ValueError:
#         print("Invalid input. Please enter a numerical value for the percentage.")


# def create_horizontal_bar(percentage):
#     if percentage < 0 or percentage > 100:
#         print("Invalid percentage. Please enter a percentage between 0 and 100.")
#         return

#     # Determine the number of characters for the bar
#     bar_length = int(percentage / 2)
    
#     # Create the horizontal bar chart using ASCII characters
#     bar_chart = "[" + "=" * bar_length + ">" + " " * (50 - bar_length) + "]"
    
#     # Display the percentage and the bar chart in the terminal
#     print(f"Percentage: {percentage}%")
#     print(bar_chart)

# # Get percentage input from the user
# try:
#     percentage = float(input("Enter the percentage: "))
#     create_horizontal_bar(percentage)
# except ValueError:
#     print("Invalid input. Please enter a numerical value for the percentage.")

# from texttable import Texttable

# def convert_to_bar_chart(percentage):
#     if not (0 <= percentage <= 100):
#         print("Invalid percentage. Please enter a percentage between 0 and 100.")
#         return

#     table = Texttable()
#     table.add_rows([['Percentage', 'Bar Chart']])
#     table.add_rows([['{:.2f}%'.format(percentage), '|' * int(percentage)]])
#     print(table.draw())

# try:
#     percentage = float(input("Enter the percentage: "))
#     convert_to_bar_chart(percentage)
# except ValueError:
#     print("Invalid input. Please enter a numerical value for the percentage.")


# from texttable import Texttable

# def create_horizontal_bar_chart(percentage):
#     if percentage < 0 or percentage > 100:
#         print("Invalid percentage. Please enter a percentage between 0 and 100.")
#         return

#     # Create a texttable object
#     table = Texttable()

#     # Set the width of the table
#     table.set_cols_width([10, 50])

#     # Add a row for the horizontal bar
#     table.add_row(['', '-' * int(percentage / 2)])

#     # Add a row for the percentage label
#     table.add_row(['Percentage', f'{percentage}%'])

#     # Print the table
#     print(table.draw())

# # Get percentage input from the user
# try:
#     percentage = float(input("Enter the percentage: "))
#     create_horizontal_bar_chart(percentage)
# except ValueError:
#     print("Invalid input. Please enter a numerical value for the percentage.")



# def create_loading_bar(percentage):
#     if percentage < 0 or percentage > 100:
#         print("Invalid percentage. Please enter a percentage between 0 and 100.")
#         return

#     bar_length = 20
#     filled_length = int(bar_length * percentage / 100)

#     bar = '[' + '=' * filled_length + ' ' * (bar_length - filled_length) + ']'
#     print(f'Loading Bar: {bar} {percentage}%')

# # Get percentage input from the user
# try:
#     percentage = float(input("Enter the percentage obtained: "))
#     create_loading_bar(percentage)
# except ValueError:
#     print("Invalid input. Please enter a numerical value for the percentage.")


def create_loading_bar(percentage):
    if percentage < 0 or percentage > 100:
        print("Invalid percentage. Please enter a percentage between 0 and 100.")
        return

    bar_length = 20
    filled_length = int(bar_length * percentage / 100)

    # Define rectangle characters
    filled_char = '█'
    empty_char = ' '

    bar = filled_char * filled_length + empty_char * (bar_length - filled_length)

    print(f'Loading Bar: [{bar}] {percentage}%')

# Get percentage input from the user
try:
    percentage = float(input("Enter the percentage obtained: "))
    create_loading_bar(percentage)
except ValueError:
    print("Invalid input. Please enter a numerical value for the percentage.")
