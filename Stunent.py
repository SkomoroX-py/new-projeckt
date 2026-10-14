class FullTimeEmployee:
    """Staff employee with a fixed monthly salary."""
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class HourlyEmployee:
    """Hourly employee (paid for hours worked)."""
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Contractor:
    """Contractor (payment for the completed project or a fixed fee)."""
    def __init__(self, name, project_fee):
        self.name = name
        self.project_fee = project_fee

    def calculate_salary(self):
        return self.project_fee


# 1. Creating a list of different types of employees
employees = [
    FullTimeEmployee(name="Олександр (Штат)", monthly_salary=30000),
    HourlyEmployee(name="Марія (Погодинно)", hourly_rate=250, hours_worked=120),
    Contractor(name="Дмитро (Фріланс)", project_fee=15000),
    FullTimeEmployee(name="Олена (Штат)", monthly_salary=45000)
]

# 2. We output each person's calculated salary in a single loop.
print("Розрахунок заробітної плати працівників:")
print("-" * 45)
for employee in employees:
    salary = employee.calculate_salary()
    print(f"Працівник: {employee.name:<20} | Зарплата: {salary:>7} грн.")
