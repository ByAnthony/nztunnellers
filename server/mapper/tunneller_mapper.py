#         profile = {
#             'militaryLife': {
#                 'embarkationUnit': {
#                     'embarkationUnit': translate_superscript(data['embarkation_unit'], lang),
#                     'section': translate_superscript(data['section'], lang),
#                     'attachedCorps': data['attached_corps'],
#                     'training': {
#                         'start': assert_non_nullish_date_and_format(data['training_start']),
#                         'location': data['training_location'],
#                         'locationType': data['training_location_type']
#                     },
#                 },
#             },
#             'sources': {
#                 'newZealandArchives': map_nz_archives(nz_archives),
#                 'awmmCenotaph': '{}{}'.format('https://www.aucklandmuseum.com/war-memorial/online-cenotaph/record/', data['awmm_cenotaph']),
#                 'nominalRoll': format_nominal_roll(data['nominal_roll_volume'], data['nominal_roll_number'], data['nominal_roll_page'], lang),
#                 'londonGazette': map_london_gazette(london_gazette)
#             },
#             'image': {'file': data['image'], 'source': {
#                 'aucklandLibraries': format_auckland_libraries_link(data['image_source_auckland_libraries']),
#                 'archives': {'location': data['archives_name'], 'reference': data['archives_ref']},
#                 'family': translate_family(data['family_name'], lang),
#                 'newspaper': {'name': data['newspaper_name'], 'date': assert_non_nullish_date_and_format(data['newspaper_date'])},
#                 'book': {'authors': map_authors(image_source_book_authors), 'title': data['book_title'], 'town': data['book_town'], 'publisher': data['book_publisher'], 'year': data['book_year'], 'page': data['book_page']}
#             }}
#         }
