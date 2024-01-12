def datetime_to_str(date):
    date_to_str = str(date)
    return (
        date_to_str
        if all([date_to_str[2] == "-", date_to_str[5] == "-"])
        else date_to_str[8:] + "-" + date_to_str[5:7] + "-" + date_to_str[:4]
    )