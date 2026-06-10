#  Write a program that takes a year as input and determines if it is a leap year.
# Rules for leap years: a year is a leap year if it’s divisible by 4,
# unless it’s also divisible by 100 but not by 400.
# Given Input: year = 2024
# Expected Output: 2024 is a leap year


# A year is a leap year if it is divisible by 4. However, if it is divisible by 100, it is NOT a leap year UNLESS it is also divisible by 400.
def find_leapyear(current_year):
    condition_1 = current_year % 4 == 0 and current_year % 100 != 0
    condition_2 = current_year % 400 == 0
    return f"{current_year} is a leap year" if condition_1 or condition_2 else f"{current_year} is not a leap year"


if __name__ == "__main__" :
    result = find_leapyear(2020)
    print(result)