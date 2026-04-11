'''


'''
expenses = [12000, 3500, 7800, 2100, 9400]
total = 0
average = 0

def calculate_total(expenses):
    total = 0
    for sum in expenses:
        total = total + sum
    return total
total = calculate_total(expenses)

def calculate_average(expenses):
    total = calculate_total(expenses)
    average = total / len(expenses)
    return average

average = calculate_average(expenses)

def get_spending_level(expenses):
    spending = calculate_average(expenses)
    if spending > 8000:
        return "High"
    elif spending > 4000 and spending < 8000:
        return "Moderate"
    else:
        return "Low"
    
spending = get_spending_level(expenses)

def get_highest_expenses(expenses):
    return max(expenses)

highest = get_highest_expenses(expenses)


def display_summary(expenses):
    print(f"Total Spent     : {total}")
    print(f"Averge Expenses : {average}")
    print(f"Highest EXpenses: {highest}")
    print(f"Spending Level  : {spending}")

display_summary(expenses)