from userbank.utils.struct import ctor


@ctor.init_list
class PostUser:
    first_name = ""
    last_name = ""
    email = ""
    phone_num = ""
