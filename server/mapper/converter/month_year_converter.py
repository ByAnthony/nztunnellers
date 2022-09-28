def convert_month_year(month, lang):

    mois = 'mois'

    month_col = {'en': 'month', 'fr': mois}
    months_col = {'en': 'months', 'fr': mois}
    years_col = {'en': 'years', 'fr': 'ans'}

    if month is not None:
        if int(month) == 1:
            return '{} {}'.format(month, month_col[lang])
        if int(month) > int(1) and int(month) < int(24):
            return '{} {}'.format(month, months_col[lang])
        if int(month) >= int(24):
            result = int(month) // int(12)
            return '{} {}'.format(result, years_col[lang])
    return None
