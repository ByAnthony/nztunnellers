month_col = {'en': 'months', 'fr': 'mois'}
year_col = {'en': 'years', 'fr': 'ans'}


def month_year_mapper(month, lang):
    if month is not None:
        if int(month) < int(24):
            return '{} {}'.format(month, month_col[lang])
        if int(month) >= int(24):
            result = int(month) // int(12)
            return '{} {}'.format(result, year_col[lang])
    return None
