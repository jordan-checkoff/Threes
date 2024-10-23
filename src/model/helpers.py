
def can_combine(val1, val2):
    if val1 == 0:
        return True if val2 != 0 else False
    elif val1 == 1:
        return True if val2 == 2 else False
    elif val1 == 2:
        return True if val2 == 1 else False
    else:
        return True if val1 == val2 else False