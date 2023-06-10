from datetime import datetime, timedelta

def get_date_n_days_before(start_date, num_days):
    date_obj = datetime.strptime(start_date, '%y-%m-%d')
    new_date_obj = date_obj - timedelta(days=num_days)
    new_date = new_date_obj.strftime('%y-%m-%d')
    return new_date


if __name__ == "__main__":
    start_date = "16-12-10"
    num_days = 11

    result_date = get_date_n_days_before(start_date, num_days)
    print(result_date)
