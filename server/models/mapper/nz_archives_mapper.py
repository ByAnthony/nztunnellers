def map_nz_archives(nz_archives):
    link = 'https://collections.archives.govt.nz/web/arena/search#/item/aims-archive/R'
    return [{'reference': row['nz_archives_ref'],
            'url': '{}{}'.format(link, row['nz_archives_url'])} for row in nz_archives]
