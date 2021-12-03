from django.core.exceptions import ValidationError


def validate_price(value: int) -> None:
    if not value >= 0:
        raise ValidationError('Price can\'t be negative')
    if not value <= 100000000000 - 1:
        raise ValidationError('Price can\'t be greater than 1,000,000.00')

