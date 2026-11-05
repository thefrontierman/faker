from itertools import product

from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``de_DE`` locale.

    Source for rules for swift location codes:

    - https://www.ebics.de/de/datenformate
    """

    bban_format = "##################"
    country_code = "DE"

    first_place = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "23456789"
    second_place = "ABCDEFGHIJKLMNPQRSTUVWXYZ" + "0123456789"
    swift_location_codes = tuple(
        str(i) + str(j) for i, j in product(first_place, second_place)
    )
