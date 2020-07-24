import datetime

def is_leap_year(year):
    ### Returns True if a year is a leap year and False if otherwise.
    ### Link with facts about leap years:
    ###   https://www.mathsisfun.com/leap-years.html
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def age_in_days(birth_day, birth_month, birth_year):
    '''
    A function which returns the age of a person in days
    and takes as parameters the birth day, birth month and birth year.
    '''
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    today = datetime.date.today()
    age = -birth_day

    if birth_year < today.year:
        for month in range(birth_month - 1, 12):
            age += days_in_months[month]

        for year in range(birth_year + 1, today.year):
            if is_leap_year(year):
                age += 366
            else:
                age += 365

        for month in range(0, today.month - 1):
            age += days_in_months[month]

        age += today.day
    elif birth_month < today.month:
        for month in range(birth_month - 1, today.month - 1):
            age += days_in_months[month]
        age += today.day
    else:
        age += today.day

    return age


def main():
    month = input("Enter the birth month: ")
    day = input("Enter the birth day: ")
    year = input("Enter the birth year: ")
    print("Your age in days is equal to " + str(age_in_days(day, month, year)))

main()
