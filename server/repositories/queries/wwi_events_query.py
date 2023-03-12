# -*- coding: utf-8 -*-
def wwi_events_query():
    return """SELECT
        DATE_FORMAT(event_join.event_date, '%%Y-%%m-%%d') AS date
        , event_join.event_en AS event

        FROM event_join

        WHERE event_join.event_t_id=%s ORDER BY date ASC"""
