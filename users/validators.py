from django.core.exceptions import ValidationError
from datetime import date


def not_rambler_email(value: str):
    if "rambler.ru" in value:
        raise ValidationError(f"{value} on a prohibited domain")


def check_min_age(value: int):
    year_of_birth = date.today().year - value
    year_for_registration = 2014
    if year_of_birth > year_for_registration:
        raise ValidationError("To register, you must be born in 2014 or earlier.")
