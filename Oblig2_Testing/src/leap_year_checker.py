def is_leap_year(year):
    if is_divisible_by(year, 4):
        if is_divisible_by(year, 400):
            return True
        elif not is_divisible_by(year, 100):
            return True
    return False


def is_divisible_by(num_to_div, div_by):
    if num_to_div % div_by == 0:
        return True
    return False

