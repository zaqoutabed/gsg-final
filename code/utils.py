def is_valid_name(name):
    import re

    if not isinstance(name, str):
        return False, "Add String only"
    name = name.strip()
    name = re.sub(" +", " ", name)
    if len(name) < 4 or len(name) > 40:
        return False, "name should be between 4 and 40 characters"
    regex = r"^[a-zA-Z\s]+$"
    if not re.search(regex, name):
        return False, "Only alphabetical and white spaces allowed"

    return True, name


def is_valid_address(address):
    if not isinstance(address, str):
        return False, "Add String only"
    import re

    address = address.strip()
    address = re.sub(" +", " ", address)
    if len(address) == 0:
        return False, "Address in required"
    regex = r"^[a-zA-Z0-9\s_-]+$"
    if not re.search(regex, address):
        return False, "Only alphabetical, (-), (_) and white spaces allowed"
    return True, address


def is_valid_level(level):
    levels = []
    if level not in levels:
        return False, "Select Level from {}".format(", ".join(levels))
    return True, ""


def is_valid_dob(dob):
    from datetime import datetime

    try:
        date = datetime.strptime(dob, "%Y-%m-%d")
        return True, ""
    except ValueError:
        return False, "Invalid Date {} Use format YYYY-MM-DD".format(dob)


def is_valid_email(email):
    import re

    regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
    email = email.strip()
    email = re.sub(" +", " ", email)
    if re.search(regex, email):
        return True, email
    return False, "Invalid Email Address"


def is_valid_mobile_number(mobile):
    import re

    regex = r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"
    mobile = mobile.strip()
    mobile = re.sub(" +", " ", mobile)
    if re.search(regex, mobile):
        return True, mobile
    return False, "Invalid Mobile"

def is_valid_id(id):
    try:
        id_flot = float(id)
        id = int(id)
        if id_flot != id or id <= 0:
            raise Exception("only positive values Allowed")
        return True, id
    except Exception as e:
        return False, "Only Positive values Allowed"

def is_valid_float(num):
    try:
        num = float(num)
        if num < 0:
            raise Exception("only positive values Allowed")
        return True, num
    except:
        return False, "Only Positive values Allowed"


def is_valid_time(time_string):
    from datetime import datetime
    time_string = time_string +":00"
    try:
        # Parse the time string
        time = datetime.strptime(time_string, '%H:%M:%S')
        return True, ""
    except ValueError:
        # The time string was not in the correct format
        return False, "Invalid Time {} Use format HH:MM 24 hour format".format(time_string)

def is_valid_duration(start_time, duration):
    from datetime import datetime, timedelta
    try:
        start_time = datetime.strptime(start_time, '%H:%M:%S')
        end_time = start_time + timedelta(hours=duration)
        if end_time.date() > start_time.date():
            return False, f"Duration {duration} not valid (end time is in diff date)"
        return True, end_time.time()
    except Exception as e:
        return False, f"Duration {duration} not valid"
