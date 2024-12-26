class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def set_name(self, name):
        self.name = name

    def set_number(self, number):
        self.number = number

class ProductionWorker(Employee):
    def __init__(self, name, number, shift, hour_pay):
        super().__init__(name, number)
        self.shift = shift
        self.hour_pay = hour_pay
    
    def get_shift(self):
        return self.shift

    def get_hour_pay(self):
        return self.hour_pay
    
    def set_shift(self, shift):
        self.shift = shift
    def set_hour_pay(self, hour_pay):
        self.hour_pay = hour_pay

name = input("Введите имя сотрудника: ")
number = input("Введите номер сотрудника: ")
shift = int(input("Введите номер смены (1 - дневная, 2 - вечерняя): "))
hour_pay = float(input("Введите ставку почасовой оплаты: "))

worker = ProductionWorker(name, number, shift, hour_pay)

print(f"Имя: {worker.get_name()}")
print(f"Номер сотрудника: {worker.get_number()}")
print(f"Смена: {worker.get_shift()}")
print(f"Ставка почасовой оплаты: {worker.get_hour_pay()}")