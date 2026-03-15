class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.domains = domains  # (list of valid domains; example: "com", "net")
        self.mails = mails  # (list of the valid mails; example: "gmail", "abv")
        self.min_length = min_length  # (of the username; example: in "peter@gmail.com" "peter" is the username)

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str):
        return mail in self.mails

    def __is_domain_valid(self, domain: str):
        return domain in self.domains

    def validate(self, email):
        name, mail_and_domain = email.split("@")
        mail, domain = mail_and_domain.split(".")

        return self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)


mails = ["gmail", "softuni"]

domains = ["com", "bg"]

email_validator = EmailValidator(6, mails, domains)

print(email_validator.validate("pe77er@gmail.com"))

print(email_validator.validate("georgios@gmail.net"))

print(email_validator.validate("stamatito@abv.net"))

print(email_validator.validate("abv@softuni.bg"))
