from typing import List, Union
from userbank import db_connection
from userbank.model import PostUser


def _query(query: str, *args: Union[str, int, float]):
    """Internal implementation for database queries.

    :param query: Format string, may contain %s, %d etc.
    :param args: Values for placeholders in `format`, if any.
    :return: Cursor object for further manipulation, or None.
    """
    try:
        conn = db_connection()
        cur = conn.cursor()
        cur.execute(query, args)
        yield cur
        conn.commit()
    except:
        return


def get_all_user_ids() -> Union[List[int], None]:
    """:returns: List of ID of all users in database.
    """
    cur, = _query("Select id from users;")
    rows = cur.fetchall()
    cur.close()
    return [r[0] for r in rows]


def add_user(user: PostUser) -> bool:
    """Create a new user record.

    :param user: Data of user to create. ID is automatically generated.
    :return: Whether the insertion was made.
    """
    cur, = _query("Insert ito users (first_name, last_name, email, phone_num) "
                  "values (%s, %s, %s, %s);",
                  user.first_name, user.last_name, user.email, user.phone_num)
    if cur:
        cur.close()
    return cur is not None
