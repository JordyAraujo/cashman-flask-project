from cashman.db import get_db


def get_all():
    return (
        get_db()
        .execute(
            """
                SELECT
                    *
                FROM income
            """
        )
        .fetchall()
    )


def get_one(income_id):
    return (
        get_db()
        .execute(
            """
                SELECT
                    id,
                    value
                FROM
                    income
                WHERE
                    id = ?
            """,
            (income_id,),
        )
        .fetchone()
    )


def add(value):
    db_conn = get_db()
    cursor = db_conn.cursor()
    cursor.execute(
        """
            INSERT INTO
                income (value)
            VALUES
                (?)
        """,
        (value,),
    )
    db_conn.commit()
    return cursor.lastrowid


def update(income_id, value):
    db_conn = get_db()
    db_conn.execute(
        """
            UPDATE
                income
            SET
                value = ?
            WHERE
                id = ?
        """,
        (value, income_id),
    )
    db_conn.commit()


def delete(income_id):
    db_conn = get_db()
    db_conn.execute(
        """
            DELETE FROM
                income
            WHERE
                id = ?
        """,
        (income_id,),
    )
    db_conn.commit()
