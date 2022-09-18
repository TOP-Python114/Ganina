"""
Ознакомиться со статьёй:
https://webdevblog.ru/nasledovanie-i-kompoziciya-rukovodstvo-po-oop-python/?ysclid=l4s48k34055078402
Реализовать первый вариант системы PayrollSystem (в разделе "Создание иерархии классов") по диаграмме в файле
 # HW_3_UML.jpg
Прислать реализацию с вашим собственным тестом.
"""


# Вариант  - разбор задачи из статьи
class Employee:
    """
    класс обрабатывает общий интерфейс для каждого типа сотрудника является базовым классом для всех типов сотрудников.
    """
    def __init__(self, id_emp, name):
        self.id_emp = id_emp
        self.name = name


class SalaryEmployee(Employee):
    """
    Класс для рассчета еженедельной заработной платы сотрудника
    """
    def __init__(self, id_emp, name, weekly_salary):
        super().__init__(id_emp, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class CommissionEmployee(SalaryEmployee):
    """
    Класс для расчета зарплаты торговых партнеров, которым выплачивается фиксированная зарплата и комиссия.
    """
    def __init__(self, id_emp, name, weekly_salary, commission):
        super().__init__(id_emp, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


class HourlyEmployee(Employee):
    """
    Класс для расчета зарплаты рабочих, которые получают почасовую оплату.
    """
    def __init__(self, id_emp, name, hours_worked, hour_rate):
        super().__init__(id_emp, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class PayrollSystem:
    def calculate_payroll(self, employees):
        """
        Класс обрабатывает платежную ведомость
        """
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Табельный номер: {employee.id_emp} - {employee.name}')
            print(f'Сумма начисленной заработной платы: {employee.calculate_payroll()} руб.')
            print('')


salary_employee = SalaryEmployee(1712, 'Малинкин Сергей Васильевич', 25000)
hourly_employee = HourlyEmployee(2815, 'Канинкина Галина Степановна', 550, 50)
commission_employee = CommissionEmployee(3721, 'Яблочкин Иван Петрович', 10000, 1700)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])
