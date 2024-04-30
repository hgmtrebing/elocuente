from math import floor
from decimal import Decimal, ROUND_FLOOR

from src.BiDict import BiDict

_spanish_nums = BiDict()
_spanish_nums.add('cero', 0)
_spanish_nums.add('uno', 1)
_spanish_nums.add('dos', 2)
_spanish_nums.add('tres', 3)
_spanish_nums.add('cuatro', 4)
_spanish_nums.add('cinco', 5)
_spanish_nums.add('seis', 6)
_spanish_nums.add('siete', 7)
_spanish_nums.add('ocho', 8)
_spanish_nums.add('nueve', 9)
_spanish_nums.add('diez', 10)
_spanish_nums.add('once', 11)
_spanish_nums.add('doce', 12)
_spanish_nums.add('trece', 13)
_spanish_nums.add('catorce', 14)
_spanish_nums.add('quince', 15)
_spanish_nums.add('dieciséis', 16)
_spanish_nums.add('diecisiete', 17)
_spanish_nums.add('dieciocho', 18)
_spanish_nums.add('diecinueve', 19)
_spanish_nums.add('veinti', 20)

_spanish_nums.add('veintiuno', 21)
_spanish_nums.add('veintidós', 22)
_spanish_nums.add('veintitrés', 23)
_spanish_nums.add('veinticuatro', 24)
_spanish_nums.add('veinticinco', 25)
_spanish_nums.add('veintiséis', 26)
_spanish_nums.add('veintisiete', 27)
_spanish_nums.add('veintiocho', 28)
_spanish_nums.add('veintinueve', 29)

_spanish_nums.add('treinta', 30)
_spanish_nums.add('cuarenta', 40)
_spanish_nums.add('cincuenta', 50)
_spanish_nums.add('sesenta', 60)
_spanish_nums.add('setenta', 70)
_spanish_nums.add('ochenta', 80)
_spanish_nums.add('noventa', 90)
_spanish_nums.add('cien', 100)

_MENOS = 'menos'
_Y = 'y'


def number_to_spanish(number: int | float | Decimal):
    if type(number) is not float and type(number) is not int and type(number) is not Decimal:
        raise TypeError("Number must be a float or an int!")

    if type(number) is not Decimal:
        number = Decimal(str(number))

    spanish = ""
    if number < 0:
        spanish += (_MENOS + " ")

    decimal_part = abs(number % 1)
    integer_part = abs(number.to_integral_value(rounding=ROUND_FLOOR))

    if integer_part < 30:
        spanish += str(_spanish_nums.get(int(integer_part))[0])

    return spanish



def spanish_to_number(spanish):
    pass
