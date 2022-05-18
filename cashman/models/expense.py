from cashman.db import get_db


def get_all_expenses():
    return get_db().execute(
        'SELECT *'
        ' FROM expense'
    ).fetchall()


def get_one_expense(id):
    return get_db().execute(
        'SELECT id, value'
        ' FROM expense'
        ' WHERE id = ?',
        (id,)
    ).fetchone()


def add_expense(value):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'INSERT INTO expense'
        ' (value)'
        ' VALUES (?)',
        (value,)
    )
    db.commit()
    return cursor.lastrowid


def update_expense(id, value):
    db = get_db()
    db.execute(
        'UPDATE expense'
        ' SET value = ?'
        ' WHERE id = ?',
        (value, id)
    )
    db.commit()


def delete_expense(id):
    db = get_db()
    db.execute(
        'DELETE FROM expense'
        ' WHERE id = ?',
        (id,)
    )
    db.commit()