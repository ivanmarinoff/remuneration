"""
remuneration base module.

This is the principal module of the remuneration project.
here you put your main classes and objects.
"""

NAME = "remuneration"

class Employee:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class HourlyPay(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def weekly_pay(self, hours):
        if hours <= 40:
            return hours * self.salary
        else:
            excess = self.salary * 1.5
            return (hours - 40) * excess + 40 * self.salary


class Payment(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def weekly_pay(self, hours):
        return self.salary / 52


class Manager(Payment):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def weekly_pay(self, hours):
        return self.bonus + super().weekly_pay(hours)


def main():
    staff = []
    staff.append(HourlyPay("Petkov, Ivan", 30.0))
    staff.append(Payment("Nikolova, Maya", 52000.0))
    staff.append(Manager("Novakov, Gosho", 104000.0, 50.0))
    for employee in staff:
        hours = int(input("Hours worked by " + employee.get_name() + ": "))
        pay = employee.weekly_pay(hours)
        print("Remuneration: %.2f" % pay)


if __name__ == "__main__":
    main()



