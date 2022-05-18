from cashman.db import get_db


def get_all():
    return (
        get_db()
        .execute(
            """
            SELECT
                *
            FROM
                expense
        """
        )
        .fetchall()
    )


def get_one(expense_id):
    return (
        get_db()
        .execute(
            """
                SELECT
                    id,
                    value
                FROM
                    expense
                WHERE
                    id = ?
            """,
            (expense_id,),
        )
        .fetchone()
    )


def add(value):
    db_conn = get_db()
    cursor = db_conn.cursor()
    cursor.execute(
        """
            INSERT INTO
                expense (value)
            VALUES
                (?)
        """,
        (value,),
    )
    db_conn.commit()
    return cursor.lastrowid


def update(expense_id, value):
    db_conn = get_db()
    db_conn.execute(
        """
            UPDATE
                expense
            SET
                value = ?
            WHERE
                id = ?
        """,
        (value, expense_id),
    )
    db_conn.commit()


def delete(expense_id):
    db_conn = get_db()
    db_conn.execute(
        """
            DELETE FROM
                expense
            WHERE id = ?
        """,
        (expense_id,),
    )
    db_conn.commit()
