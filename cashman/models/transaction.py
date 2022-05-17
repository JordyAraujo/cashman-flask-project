from cashman.db import get_db
from cashman.models.enum import TransactionType


def get_one_transaction(id):
    return get_db().execute(
        'SELECT id, transaction_type, value'
        ' FROM transact'
        ' WHERE id = ?',
        (id,)
    ).fetchone()


def get_all_transactions():
    return get_db().execute(
        'SELECT *'
        ' FROM transact'
    ).fetchall()


def add_transaction(transaction_type, value):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'INSERT INTO transact'
        ' (transaction_type, value)'
        ' VALUES (?, ?)',
        (transaction_type, value)
    )
    db.commit()
    return cursor.lastrowid


def update_transaction(id, transaction_type, value):
    db = get_db()
    db.execute(
        'UPDATE transact'
        ' SET transaction_type = ?, value = ?'
        ' WHERE id = ?',
        (transaction_type, value, id)
    )
    db.commit()


def delete_transaction(id):
    db = get_db()
    db.execute(
        'DELETE FROM transact'
        ' WHERE id = ?',
        (id,)
    )
    db.commit()


def get_all_incomes():
    return get_db().execute(
        'SELECT *'
        ' FROM transact'
        ' WHERE transaction_type = "INCOME"'
    ).fetchall()