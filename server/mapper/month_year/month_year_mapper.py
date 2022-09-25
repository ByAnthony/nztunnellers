def month_year_mapper(month):
    if month is not None:
        if int(month) < int(24):
            return '{} months'.format(month)
        if int(month) >= int(24):
            result = int(month) // int(12)
            return '{} years'.format(result)
    return None
