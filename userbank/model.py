from userbank.utils.struct import ctor

@ctor.init_list
class PostUser:
    first_name: str
    last_name: str
    email: str
    phone_num: str
