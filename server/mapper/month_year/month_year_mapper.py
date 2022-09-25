def month_year_mapper(month, lang):
    if month is not None:
        if int(month) < int(24):
            if lang == 'en':
                return '{} months'.format(month)
            if lang == 'fr':
                return '{} mois'.format(month)
        if int(month) >= int(24):
            result = int(month) // int(12)
            if lang == 'en':
                return '{} years'.format(result)
            if lang == 'fr':
                return '{} ans'.format(result)
    return None
