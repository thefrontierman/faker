from .codes import codes
import contextlib


def unidecode(txt: str) -> str:
    chars = ""
    for ch in txt:
        codepoint = ord(ch)

        with contextlib.suppress(IndexError):
            chars += codes[codepoint]
    return chars
