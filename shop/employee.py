from requests import request


class Employee:
    """
    A sample employee class used for unit testing
    """
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first_name = first
        self.last_name = last
        self.pay = pay

    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@decagon.dev"

    @property
    def fullname(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def get_schedule(self):
        resp = request('GET', "https://company.com")
        if resp.ok:
            return resp.text
        else:
            return "Bad response"
