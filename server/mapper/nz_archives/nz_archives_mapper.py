def map_nz_archives(nz_archives):
    return [{'reference': row['nz_archives_ref'],
            'url': row['nz_archives_url']} for row in nz_archives]
