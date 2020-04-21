from django.core.exceptions import ValidationError
from .sncheck import validate_serial_number


def serial_number_length_validator(serial_number):
    if len(serial_number) != 20:
        raise ValidationError('Serial number length should be 20 symbols', code='invalid length')


def serial_number_validator(serial_number):
    validation = validate_serial_number(serial_number)
    if validation == False:
        raise ValidationError("Serial number isn't valid", code='invalid serial number')
    elif validation == 'Error':
        raise ValidationError("Couldn't check serial number validation", code='validation error')
