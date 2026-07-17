def get_full_name(ism, famiiya, otasi=""):
    if otasi:
        return f"{ism} {otasi} {famiiya}".title()
    else:
        return f"{ism} {famiiya}".title()
