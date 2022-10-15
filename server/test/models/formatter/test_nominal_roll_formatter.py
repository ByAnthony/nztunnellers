from ....models.formatter import nominal_roll_formatter


volume = 'III'
roll = '75'
page = '3'

en = 'en'
fr = 'fr'

no_break_space = '\N{NO-BREAK SPACE}'
roll_number_col = {'en': 'Roll No.', 'fr': 'Liste n\N{DEGREE SIGN}'}

title_1919 = {'en': 'Nominal Rolls of New Zealand Expeditionary Force',
              'fr': 'Liste nominative du corps expéditionnaire néo-zélandais'}
title_1916 = {'en': 'Nominal Roll of New Zealand Expeditionary Force, 1915. New Zealand Engineers Tunnelling Company',
              'fr': 'Liste nominative du corps expéditionnaire néo-zélandais, 1915. Compagnie de tunneliers'}


def test_if_volume_and_roll_are_not_none_and_lang_en_returns_nominal_roll():
    assert nominal_roll_formatter.format_nominal_roll(volume, roll, page, en) == {
        'title': title_1919[en],
        'town': 'Wellington',
        'publisher': 'Government Printer',
        'date': '1914-1919',
        'volume': 'Volume{}{}'.format(no_break_space, volume),
        'roll': '{}{}{}'.format(roll_number_col[en], no_break_space, roll),
        'page': 'p.{}{}'.format(no_break_space, page)}


def test_if_volume_and_roll_are_not_none_and_lang_fr_returns_nominal_roll():
    assert nominal_roll_formatter.format_nominal_roll(volume, roll, page, fr) == {
        'title': title_1919[fr],
        'town': 'Wellington',
        'publisher': 'Government Printer',
        'date': '1914-1919',
        'volume': 'Volume{}{}'.format(no_break_space, volume),
        'roll': '{}{}{}'.format(roll_number_col[fr], no_break_space, roll),
        'page': 'p.{}{}'.format(no_break_space, page)}


def test_if_volume_and_roll_are_none_and_lang_en_returns_nominal_roll():
    assert nominal_roll_formatter.format_nominal_roll(None, None, page, en) == {
        'title': title_1916[en],
        'town': 'Wellington',
        'publisher': 'Government Printer',
        'date': '1916',
        'page': 'p.{}{}'.format(no_break_space, page)}


def test_if_volume_and_roll_are_none_and_lang_fr_returns_nominal_roll():
    assert nominal_roll_formatter.format_nominal_roll(None, None, page, fr) == {
        'title': title_1916[fr],
        'town': 'Wellington',
        'publisher': 'Government Printer',
        'date': '1916',
        'page': 'p.{}{}'.format(no_break_space, page)}
