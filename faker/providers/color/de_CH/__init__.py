from collections import OrderedDict

from faker.typing import OrderedDictType

from ..de import Provider as BaseProvider


class Provider(BaseProvider):
    # ClassVar would conflict with the base class's instance-variable declaration (mypy [misc]).
    all_colors: OrderedDictType[str, str] = OrderedDict(  # noqa: RUF012
        (color_name.replace("ß", "ss"), color_hexcode) for color_name, color_hexcode in BaseProvider.all_colors.items()
    )
