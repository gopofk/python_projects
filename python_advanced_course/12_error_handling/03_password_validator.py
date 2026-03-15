class PasswordTooShort(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


def password_too_common(pwd, specials):
    only_digits = pwd.isdigit()
    only_letters = pwd.isalpha()
    only_specials = all(ch in specials for ch in pwd)
    return only_digits or only_letters or only_specials


SPECIAL_CHARACTERS = {"@", "*", "&", "%"}

while True:
    password = input()
    if password == "Done":
        break

    if len(password) < 8:
        raise PasswordTooShort()

    if password_too_common(password, SPECIAL_CHARACTERS):
        raise PasswordTooCommonError()

    if any(ch in SPECIAL_CHARACTERS for ch in password):
        raise PasswordNoSpecialCharactersError()

    if " " in password:
        raise PasswordContainsSpacesError()

    print("Password is valid")
