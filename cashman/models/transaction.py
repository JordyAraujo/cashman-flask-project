from cashman.db import get_db


def get_all():
    return get_db().execute(
        'SELECT "INCOME" AS "type", *'
        ' FROM income'
        ' UNION ALL'
        ' SELECT "EXPENSE" AS "type", *'
        ' FROM expense'
    ).fetchall()