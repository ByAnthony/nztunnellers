# -*- coding: utf-8 -*-
def front_events_query():
    return """SELECT
        DATE_FORMAT(event_join.event_date, '%%Y-%%m-%%d') AS date
        , event_join.event_en AS event

        FROM event_join

        WHERE event_join.event_t_id=%s ORDER BY date ASC, event_join.event_sequence"""


def company_events_query():
    return """SELECT
        DATE_FORMAT(company_events.company_events_date, '%Y-%m-%d') AS date
        , company_events.company_events_event AS event

        FROM company_events

        ORDER BY date ASC"""
