
class SKUDoesNotExist(Exception):
    def __init__(self, serial_number, message='Cant find SKU for serial number'):
        self.serial_number = serial_number
        self.message = message

    def __str__(self):
        return  '{} {}'.format(self.message, self.serial_number)

class TestR:
    pass