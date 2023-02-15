# -*- coding: utf-8 -*-
def nz_archives_query() -> str:
    return """SELECT
        nz_archives.nz_archives_ref AS reference
        , nz_archives.nz_archives_url AS url

        FROM nz_archives
        LEFT JOIN tunneller ON tunneller.id=nz_archives.nz_archives_t_id
        WHERE tunneller.id=%s"""
