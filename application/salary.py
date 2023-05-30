from pprint import pprint


class Salary:

    def __init__(self, name):
        self.name = name

    def calculate_salary(self, salary, additional_payments):
        res = salary+additional_payments
        pprint(res)
