"""
Ознакомиться со статьёй:
https://webdevblog.ru/nasledovanie-i-kompoziciya-rukovodstvo-po-oop-python/?ysclid=l4s48k34055078402
Реализовать первый вариант системы PayrollSystem (в разделе "Создание иерархии классов") по диаграмме в файле
 # HW_3_UML.jpg
Прислать реализацию с вашим собственным тестом.
"""


# Вариант 2 формами оплаты труда.
class Employee:
    """
    Класс, содержащий информацию о сотрудниках: id, name
    """
    def __init__(self, id_employee, name, payment_rate):
        self.id_employee = id_employee
        self.name = name
        self.payment_rate = payment_rate


class SalaryTime(Employee):
    """
    Повременная оплата труда.
    """

    def __init__(self, id_employee, name, payment_rate, hours_worked):
        super().__init__(id_employee, name, payment_rate)
        self.hours_worked = hours_worked

    def calculate_payroll(self):
        salary_fixed = self.hours_worked * self.payment_rate
        return salary_fixed


class SalaryTimeBonus(SalaryTime):
    """
    Повременная-премиальная оплата труда.
    """

    def __init__(self, id_employee, name, payment_rate, hours_worked, bonus):
        super().__init__(id_employee, name, payment_rate, hours_worked)
        self.bonus = bonus

    def calculate_payroll(self):
        salary_fixed = super().calculate_payroll()
        return salary_fixed * (1 + self.bonus/100)


class SalaryPieceWork(Employee):
    """
    Сдельная оплата труда.
    """
    def __init__(self, id_employee, name, payment_rate, number_products):
        super().__init__(id_employee, name, payment_rate)
        self.number_products = number_products

    def calculate_payroll(self):
        return self.payment_rate * self.number_products


class PayrollSystem:
    def calculate_payroll(self, employees):
        """
        Класс реализует метод .calculate_payroll(), который принимает коллекцию сотрудников и печатает
        их табельный номер, имя и сумму начисленной заработной платы.
        """
        print('Calculating Payroll')
        print('=================================')
        for employee in employees:
            print(f'Табельный номер:{employee.id_employee}; ФИО: {employee.name}; Ставка з/п: {employee.payment_rate}')
            print(f'Информация о заработной плате: {employee.calculate_payroll()} руб.')
            print('')
        print('=================================')


salary_Ivanov = SalaryTime(501121, 'Иванов Василий Петрович', 1150, 40)
salary_Petrov = SalaryTimeBonus(501122, 'Петров Семен Иванович', 2100, 20, 75)
salary_Sidorov = SalaryPieceWork(501123, 'Сидоров Петр Васильевич', 35, 1500)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll([
    salary_Ivanov,
    salary_Petrov,
    salary_Sidorov
])
