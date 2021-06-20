from typing import Union
from userbank import db_connection
from userbank.model import PostUser


def _query(format: str, *args: Union[str, int, float]):
    """Internal implementation for database queries.

    :param format: Format string, may contain %s, %d etc.
    :param args: Values for placeholders in `format`, if any.
    :return: Whether the query was successful.
    """
    try:
        conn = db_connection()
        with conn, conn.cursor() as cur:
            cur.execute(format, args)
    except:
        return False
    return True


def add_user(user: PostUser):
    """Create a new user record.

    :param user: Data of user to create. ID is automatically generated.
    :return: Whether the insertion was made.
    """
    return _query("Insert into users (first_name, last_name, email, phone_num) "
                  "values (%s, %s, %s, %s);",
                  user.first_name, user.last_name, user.email, user.phone_num)
