from typing import List, Union
from userbank import db_connection
from userbank.model import PostUser


def _query(query: str, *args: Union[str, int, float]):
    """Internal implementation for database queries.

    :param query: Format string, may contain %s, %d etc.
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

    :param query: Format string, may contain %s, %d etc.
    :param args: Values for placeholders in `query`, if any.
    :return: Rows from the database, otherwise None.
    """
    if 1:
    # try:
        connection = db_connection()
        with connection, connection.cursor() as cursor:
            cursor.execute(query, args)
            # Yielding the cursor here would fail. It would be closed
            # even while in this context!
            return cursor.fetchall()
    # except:
    #     return


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
    if rows := _query_fetch("Select first_name, last_name, email, phone_num "
                            "from users where id = %s;",
                            id_):
        # Zero length array is falsy.
        return PostUser(*rows[0])


def add_user(user: PostUser):
    """Create a new user record.

    :param user: Data of user to create. ID is automatically generated.
    :return: Whether the insertion was made.
    """
    return _query("Insert into users (first_name, last_name, email, phone_num) "
                  "values (%s, %s, %s, %s);",
                  user.first_name, user.last_name, user.email, user.phone_num)
