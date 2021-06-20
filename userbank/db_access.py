from typing import List, Union
from userbank import db_connection
from userbank.model import UpdateUserRecord, UserRecord, NewUserRecord


def _query(query: str, *args: Union[str, int, float]):
    """Internal implementation for database queries.

    :param query: Format string, may contain %s.
    :param args: Values for placeholders in `query`, if any.
    :return: Whether the query was successful.
    """
    try:
        connection = db_connection()
        with connection, connection.cursor() as cursor:
            cursor.execute(query, args)
    except:
        return False
    return True


def _query_fetch(query: str, *args: Union[str, int, float]):
    """Database query that retrieves rows.

    :param query: Format string, may contain %s.
    :param args: Values for placeholders in `query`, if any.
    :return: Rows from the database, otherwise None.
    """
    try:
        connection = db_connection()
        with connection, connection.cursor() as cursor:
            cursor.execute(query, args)
            # Yielding the cursor here would fail. It would be closed
            # even while in this context!
            return cursor.fetchall()
    except:
        return


def get_all_user_ids() -> Union[List[int], None]:
    """:returns: List of ID of all users in database, or None if query
    failed.
    """
    if rows := _query_fetch("Select id from users;"):
        return [row[0] for row in rows]


def get_user_by_id(id_: int):
    """:returns: List of ID of all users in database, or None if query
    failed.
    """
    if rows := _query_fetch("Select id, first_name, last_name, email, phone_num "
                            "from users where id = %s;",
                            id_):
        # Zero length array is falsy.
        return UserRecord(rows[0][0], rows[0][1], rows[0][2], rows[0][3],
                          rows[0][4].strip())


def add_user(user: NewUserRecord):
    """Create a new user record.

    :param user: Data of user to create. ID is automatically generated.
    :return: Whether the insertion was made.
    """
    return _query("Insert into users (first_name, last_name, email, phone_num) "
                  "values (%s, %s, %s, %s);",
                  user.first_name, user.last_name, user.email, user.phone_num)


def update_user(user: UpdateUserRecord):
    """Update a user record.

    :param user: Details about user to update.
    :return: Whether the update was successful.
    """
    return _query("Update users "
                  + ", ".join(filter(None,
                                     (user.first_name and 'set first_name = %s',
                                      user.last_name and 'set last_name = %s',
                                      user.email and 'set email = %s',
                                      user.phone_num and 'set phone_num = %s')))
                  + "where id = %s;",
                  *filter(None, (user.first_name, user.last_name,
                                 user.email, user.phone_num)),
                  user.id_)


def delete_user(id_: int):
    """Delete a user record.

    :param id_: ID of the user to delete.
    :return: Whether the deletion was successful.
    """
    return _query("Delete from users where id = %s;", id_)
