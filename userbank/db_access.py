from userbank import db_connection
from userbank.model import PostUser


def add_user(user: PostUser):
    """Create a new user record.

    :param user: Data of user to create. ID is automatically generated.
    :return: Whether the insertion was made.
    """
    try:
        conn = db_connection()
        with conn.cursor() as cur:
            cur.execute("Insert into users (first_name, last_name, email, phone_num) "
                        "values (%s, %s, %s, %s);",
                        (user.first_name, user.last_name,
                         user.email, user.phone_num))
    except:
        return False
    return True
