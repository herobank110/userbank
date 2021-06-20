from userbank.utils.struct import ctor


@ctor.init_list
class PostUser:
    """User details to be added to database.
    """
    first_name = ""
    last_name = ""
    email = ""
    phone_num = ""


@ctor.init_list
class UserRecord:
    """Details for a user in the database.
    """
    id_ = 1
    first_name = ""
    last_name = ""
    email = ""
    phone_num = ""
