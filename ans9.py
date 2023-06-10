from datetime import datetime

def is_less_than_difference_days(from_date, to_date, difference):
    from_date_obj = datetime.strptime(from_date, "%y-%m-%d")
    to_date_obj = datetime.strptime(to_date, "%y-%m-%d")
    difference_in_days = abs((to_date_obj - from_date_obj).days)
    return difference_in_days < difference


if __name__ == "__main__":
    from_date = "23-06-05"
    to_date = "23-06-10"
    difference = 7

    result = is_less_than_difference_days(from_date, to_date, difference)
    print(result)
