def convert_nominal_roll(volume, roll, page, lang):

    no_break_space = '\N{NO-BREAK SPACE}'
    title_1916 = {'en': 'Nominal Rolls of New Zealand Expeditionary Force',
                  'fr': 'Liste nominative du corps expéditionnaire néo-zélandais'}
    title_1919 = {'en': 'Nominal Roll of New Zealand Expeditionary Force, 1915. New Zealand Engineers Tunnelling Company',
                  'fr': 'Liste nominative du corps expéditionnaire néo-zélandais, 1915. Compagnie de tunneliers'}
    roll_number_col = {'en': 'Roll No.', 'fr': 'Liste n\N{DEGREE SIGN}'}

    if volume and roll is not None:
        return {'title': title_1919[lang],
                'town': 'Wellington',
                'publisher': 'Government Printer',
                'date': '1914-1919',
                'volume': 'Volume{}{}'.format(no_break_space, volume),
                'roll': '{}{}{}'.format(roll_number_col[lang], no_break_space, roll),
                'page': 'p.{}{}'.format(no_break_space, page)}
    else:
        return {'title': title_1916[lang],
                'town': 'Wellington',
                'publisher': 'Government Printer',
                'date': '1916',
                'page': 'p.{}{}'.format(no_break_space, page)}
