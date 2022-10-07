#         profile = {
#             'militaryLife': {
#                 'enlistment': {
#                     'date': assert_non_nullish_date_and_format(data['enlistment_date']),
#                     'militaryDistrict': data['military_district_name'],
#                     'postedToDate': assert_non_nullish_date_and_format(data['posted_date']),
#                     'postedFrom': data['posted_from_corps']
#                 },
#                 'embarkationUnit': {
#                     'embarkationUnit': translate_superscript(data['embarkation_unit'], lang),
#                     'section': translate_superscript(data['section'], lang),
#                     'attachedCorps': data['attached_corps'],
#                     'training': {
#                         'start': assert_non_nullish_date_and_format(data['training_start']),
#                         'location': data['training_location'],
#                         'locationType': data['training_location_type']
#                     },
#                     'transportUnitedKindgom': {
#                         'id': translate_transport_ref(data['transport_uk_ref'], lang),
#                         'vessel': data['transport_uk_vessel'],
#                         'departure': assert_non_nullish_date_and_format(data['transport_uk_start']),
#                         'from': data['transport_uk_origin'],
#                         'arrival': assert_non_nullish_date_and_format(data['transport_uk_end']),
#                         'to': data['transport_uk_destination'],
#                     }
#                 },
#                 'medals': map_medals(medals)
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
