class Employee:
    def __init__(self, name, basic, allowance, deduction):
        self.name = name
        self.basic = basic
        self.allowance = allowance
        self.deduction = deduction

    def get_net_salary(self):
        return self.basic + self.allowance - self.deduction

employees = []
n = int(input("Enter number of employees: "))

for _ in range(n):
    name = input("Enter Name: ")
    basic = float(input("Enter Basic Salary: "))
    allowance = float(input("Enter Allowance: "))
    deduction = float(input("Enter Deduction: "))
    employees.append(Employee(name, basic, allowance, deduction))

print("\n--- Payroll Report ---")
for e in employees:
    print(f"{e.name} | Net Salary: {e.get_net_salary()}")
