import secrets
import string
from typing import Optional


class PasswordGenerator:
    """Generate secure random passwords from configurable character sets."""

    LOWERCASE = string.ascii_lowercase
    UPPERCASE = string.ascii_uppercase
    DIGITS = string.digits
    SYMBOLS = string.punctuation

    @staticmethod
    def _build_charset(
        *,
        include_uppercase: bool = True,
        include_lowercase: bool = True,
        include_digits: bool = True,
        include_symbols: bool = True,
        avoid_ambiguous: bool = False,
    ) -> str:
        charset = ""

        if include_lowercase:
            charset += PasswordGenerator.LOWERCASE
        if include_uppercase:
            charset += PasswordGenerator.UPPERCASE
        if include_digits:
            charset += PasswordGenerator.DIGITS
        if include_symbols:
            charset += PasswordGenerator.SYMBOLS

        if avoid_ambiguous:
            charset = "".join(ch for ch in charset if ch not in "0O1Il|/\\`'\"" )

        if not charset:
            raise ValueError("At least one character set must be enabled.")

        return charset

    @classmethod
    def generate(
        cls,
        length: int = 12,
        *,
        include_uppercase: bool = True,
        include_lowercase: bool = True,
        include_digits: bool = True,
        include_symbols: bool = True,
        avoid_ambiguous: bool = False,
        custom_charset: Optional[str] = None,
    ) -> str:
        if length <= 0:
            raise ValueError("Password length must be greater than 0.")

        if custom_charset is not None:
            charset = custom_charset
            if not charset:
                raise ValueError("Custom charset cannot be empty.")
        else:
            charset = cls._build_charset(
                include_uppercase=include_uppercase,
                include_lowercase=include_lowercase,
                include_digits=include_digits,
                include_symbols=include_symbols,
                avoid_ambiguous=avoid_ambiguous,
            )

        return "".join(secrets.choice(charset) for _ in range(length))


def generate_password(
    length: int = 12,
    *,
    include_uppercase: bool = True,
    include_lowercase: bool = True,
    include_digits: bool = True,
    include_symbols: bool = True,
    avoid_ambiguous: bool = False,
    custom_charset: Optional[str] = None,
) -> str:
    return PasswordGenerator.generate(
        length,
        include_uppercase=include_uppercase,
        include_lowercase=include_lowercase,
        include_digits=include_digits,
        include_symbols=include_symbols,
        avoid_ambiguous=avoid_ambiguous,
        custom_charset=custom_charset,
    )
