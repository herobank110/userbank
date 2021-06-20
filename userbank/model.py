from typing import Union
from userbank.utils.struct import ctor


@ctor.init_list
class NewUserRecord:
    """User details to be added to database.
    """
    first_name = ""
    last_name = ""
    email = ""
    phone_num = ""


@ctor.init_list
class UpdateUserRecord:
    """User details to update existing user in database with.
    """
    id_ = 1
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    email: Union[str, None] = None
    phone_num: Union[str, None] = None


@ctor.init_list
class UserRecord:
    """Details for a user in the database.
    """
    id_ = 1
    first_name = ""
    last_name = ""
    email = ""
    phone_num = ""
