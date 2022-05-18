from cashman.db import get_db


def get_all():
    return get_db().execute(
        'SELECT *'
        ' FROM expense'
    ).fetchall()


def get_one(id):
    return get_db().execute(
        'SELECT id, value'
        ' FROM expense'
        ' WHERE id = ?',
        (id,)
    ).fetchone()


def add(value):
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


def update(id, value):
    db = get_db()
    db.execute(
        'UPDATE expense'
        ' SET value = ?'
        ' WHERE id = ?',
        (value, id)
    )
    db.commit()


def delete(id):
    db = get_db()
    db.execute(
        'DELETE FROM expense'
        ' WHERE id = ?',
        (id,)
    )
    db.commit()