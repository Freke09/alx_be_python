from datetime import datetime, timedelta

current_date = datetime.now()
formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")

def display_current_datetime():
    print(formatted)

def calculate_future_date():
    number_of_days = int(input("Enter number of days to add to the current date: "))
    future_date = timedelta(days=number_of_days) + current_date
    return future_date.strftime("%Y-%m-%d")


display_current_datetime()
future_date = calculate_future_date()
print(future_date)

# today = datetime.datetime.now()
# formarted_date = today.strftime("%Y-%m-%d %H:%M:%S")
# print(formarted_date)
