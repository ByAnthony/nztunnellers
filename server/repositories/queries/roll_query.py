# -*- coding: utf-8 -*-
def roll_query():
    return """SELECT
        t.id
        , t.surname
        , t.forename
        , t.serial
        , DATE_FORMAT(t.birth_date, '%Y-%m-%d') AS birth_date
        , t.birth_year
        , DATE_FORMAT(t.death_date, '%Y-%m-%d') AS death_date
        , t.death_year
        FROM tunneller t ORDER BY t.surname, t.forename"""
