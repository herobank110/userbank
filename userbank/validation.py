import re
from typing import Union
from flask.wrappers import Request
from userbank.model import NewUserRecord, UpdateUserRecord

email_regex = re.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
phone_num_regex = re.compile('^[+0-9][0-9]{10,12}$')


def is_valid_put_user(req: Request) -> bool:
    """:returns: Whether the request for PUT /api/user is valid.
    """
    return (
        # Must be JSON request body.
        req.is_json
        # If defined, first and last name must be at least one char long.
        and (req.json.get('firstName') is None
             or (type(req.json.get('firstName')) == str
                 and len(req.json.get('firstName')) >= 1))
        and (req.json.get('lastName') is None
             or (type(req.json.get('lastName')) == str
                 and len(req.json.get('lastName')) >= 1))
        # If defined, email must match pattern.
        and (req.json.get('email') is None
             or (type(req.json.get('email')) == str
                 and email_regex.match(req.json.get('email'))))
        # If defined, phone number must match pattern (considers length).
        and (req.json.get('phoneNum') is None
             or (type(req.json.get('phoneNum')) == str
                 and phone_num_regex.match(req.json.get('phoneNum'))))
        # At least one field must be defined.
        and (req.json.get('firstName') is not None
             or req.json.get('lastName') is not None
             or req.json.get('email') is not None
             or req.json.get('phoneNum') is not None))


def is_valid_post_user(req: Request) -> bool:
    """:returns: Whether the request for POST /api/user is valid.
    """
    # Same criteria as PUT user but all fields must be defined.
    return (is_valid_put_user(req)
            and req.json.get('firstName') is not None
            and req.json.get('lastName') is not None
            and req.json.get('email') is not None
            and req.json.get('phoneNum') is not None)


def make_new_user_record(req: Request):
    return (is_valid_post_user(req)
            and NewUserRecord(req.json.get('firstName'),
                              req.json.get('lastName'),
                              req.json.get('email'),
                              req.json.get('phoneNum'))
            or None)


def make_user_id(id_: str):
    """:returns: Integer ID if valid.
    """
    try:
        id_int = int(id_)
        # Only positive integers allowed.
        if id_int > 0:
            return id_int
    except:
        return


def make_update_user_record(id_: int, req: Request
                            ) -> Union[UpdateUserRecord, None]:
    # Impossible to return int since id_int is only allowed to be
    # positive, non-zero or None, so if falsy will not be int.
    return ((id_int := make_user_id(id_))
            and is_valid_put_user(req)
            and UpdateUserRecord(id_int,
                                 req.json.get('firstName'),
                                 req.json.get('lastName'),
                                 req.json.get('email'),
                                 req.json.get('phoneNum'))
            or None)
