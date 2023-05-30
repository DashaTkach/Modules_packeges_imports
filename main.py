from application.salary import Salary
from application.db.people import People
from datetime import date

if __name__ == '__main__':
    division = People('marketing')
    per_salary = Salary('Ivan Ivanov')
    print(Salary.calculate_salary(per_salary, 100000, 50000))
    print(People.get_employees(division, 'Ivan Ivanov', 'Kolya Smirnov'))
    print(date.today())
