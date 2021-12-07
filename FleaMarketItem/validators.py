from django.core.exceptions import ValidationError


def validate_price(value: int) -> None:
    if not value >= 0:
        raise ValidationError('It is not possible to use a negative price')
    if not value <= 100000:
        raise ValidationError('The price must be less 100.000')

