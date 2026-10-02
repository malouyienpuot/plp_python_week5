import argparse

from .generator import generate_password


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a secure random password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length (default: 12)")
    parser.add_argument("--no-uppercase", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-lowercase", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument("--avoid-ambiguous", action="store_true", help="Avoid ambiguous characters")
    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        include_uppercase=not args.no_uppercase,
        include_lowercase=not args.no_lowercase,
        include_digits=not args.no_digits,
        include_symbols=not args.no_symbols,
        avoid_ambiguous=args.avoid_ambiguous,
    )
    print(password)


if __name__ == "__main__":
    main()
