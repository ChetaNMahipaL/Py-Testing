"""
    This module helps to check palindrome day
"""
import datetime

def validate_date(day, month, year):
    """
        To check if the reversed date is valid or not
    """
    try:
        # Attempt to create a datetime object with the given date
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False

def main(year_old):
    """
        Main function is here
    """
    try:
        year_temp = int(year_old)
        if len(year_old) < 5 and year_temp > 0:
            while len(year_old) < 4:
                year_old = '0' + year_old
            # print(year_old)
            day_new = year_old[2:]
            day_new = day_new[::-1]
            month_new = year_old[:2]
            month_new = month_new[::-1]
            if validate_date(int(day_new), int(month_new), int(year_old)):
                ans = f"{day_new}-{month_new}-{year_old}"
            else:
                ans = "No Palindrome days available in the given year"
            print(ans)
            return ans
        ans_t ="Enter a valid year"
        print(ans_t)
        return ans_t
    except ValueError:
        ans_t ="Enter a valid year"
        print(ans_t)
        return ans_t

if __name__ == "__main__":
    year_input = input("Enter year: ")
    main(year_input)
