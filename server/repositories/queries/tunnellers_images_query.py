# -*- coding: utf-8 -*-
def tunnellers_images_query() -> str:
    return """SELECT
        t.id
        , t.image

        FROM tunneller t WHERE t.image IS NOT NULL"""
