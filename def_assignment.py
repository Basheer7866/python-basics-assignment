'''
Assignment: Python Functions and Lists

You are building a simple marks analysis utility. Complete the following tasks in order.

Task 1. Write a function calculate_total(marks) that accepts a list of marks and returns their sum.

Task 2. Write a function calculate_average(marks) that calls calculate_total() and returns the average.

Task 3. Write a function get_grade(average) that returns "A" if average > 90, "B" if average > 75, and "C" otherwise.

Task 4. Write a function display_report(marks) that calls all three functions above and prints:

Total: <value>
Average: <value>
Grade: <value>
Task 5. Add a docstring to each function describing what it does.

Test your solution with the list [88, 76, 95, 60, 82].

'''

total = 0
average = 0

marks = [88, 76, 95, 60, 82]

def calculate_total(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total

total = calculate_total(marks)
# print(total)



def calculate_average(marks):
    total = calculate_total(marks)
    average = total / len(marks)
    return average

average = calculate_average(marks)
# print(average)

def get_grade(average):
    if average > 90:
        return "A"
    elif average > 75:
        return "B"

grade = get_grade(average)
# print(grade)

def display_report(marks):
    print(f" Total   : {total} \n Average : {average} \n Grade   : {grade}")
    

display_report(marks)
