import leap_year_checker


# Test Acceptance criteria for leap year
def test_year_is_leap_year_when_divisible_by_4_not_100():
    assert leap_year_checker.is_leap_year(4)
    assert leap_year_checker.is_leap_year(204)
    assert leap_year_checker.is_leap_year(44)
    assert leap_year_checker.is_leap_year(2008)
    assert leap_year_checker.is_leap_year(32)
    assert not leap_year_checker.is_leap_year(100)
    assert not leap_year_checker.is_leap_year(200)
    assert not leap_year_checker.is_leap_year(300)
    assert not leap_year_checker.is_leap_year(600)
    assert not leap_year_checker.is_leap_year(900)


def test_year_is_leap_year_when_divisible_by_400():
    assert leap_year_checker.is_leap_year(400)
    assert leap_year_checker.is_leap_year(800)
    assert leap_year_checker.is_leap_year(2400)
    assert leap_year_checker.is_leap_year(4000)
    assert leap_year_checker.is_leap_year(400 * 34)


# Test Acceptance criteria for not leap year
def test_year_is_not_leap_year_when_not_divisible_by_4():
    assert not leap_year_checker.is_leap_year(5)
    assert not leap_year_checker.is_leap_year(20077)
    assert not leap_year_checker.is_leap_year(2007)
    assert not leap_year_checker.is_leap_year(2021)
    assert not leap_year_checker.is_leap_year(7)


def test_year_is_not_leap_year_when_divisible_by_100_not_400():
    assert not leap_year_checker.is_leap_year(1700)
    assert not leap_year_checker.is_leap_year(1800)
    assert not leap_year_checker.is_leap_year(1500)
    assert not leap_year_checker.is_leap_year(700)
    assert not leap_year_checker.is_leap_year(1900)


"""
Accceptance Criterias

** A year is a leap year: 
    - When it is divisible by 4, but not 100
    - When it is divisible by 400

** A year is not a leap year: 
    - When it is not divisible by 4
    - When it is divisible by 100, but not 400

"""
