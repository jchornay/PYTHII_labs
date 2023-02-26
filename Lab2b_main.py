#Jonathan Chornay
#CMSY 257 Spring 2023 Class
#Professor Charles Edwards
#
#Lab 2 Problem 2

#imports employee class
from Lab2a_classes import Employee

class ShiftSupervisor(Employee):

    #initializes attributes for superclass as well as those specific to subclass (salary, bonus)
    def __init__(self, name, number, salary, bonus):
        super().__init__(name, number)
        self.__salary = salary
        self.__bonus = bonus

    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        self.__salary = salary

    def get_bonus(self):
        return self.__bonus
    def set_bonus(self, bonus):
        self.__bonus = bonus

#main method
def main():

    name = input("Employee Name: ")

    #repeats prompts until user inputs integer for employee number, salary, and bonus respectively
    number = None
    while(number is None):
        try:
            number = int(input("Employee Number: "))
        except:
            print("Employee number must be numerical characters only!")

    salary = None
    while (salary is None):
        try:
            salary = int(input("Salary: "))
        except:
            print("Employee salary must be numerical characters only!")

    bonus = None
    while (bonus is None):
        try:
            bonus = int(input("Bonus: "))
        except:
            print("Employee bonus must be numerical characters only!")

    #creates employee2 object
    employee2 = ShiftSupervisor(name, number, salary, bonus)

    print(f"\n"
          f"Employee name: {employee2.get_name()}\n"
          f"Employee number: {employee2.get_number()}\n"
          f"Salary: ${employee2.get_salary():,.2f}\n"
          f"Bonus: ${employee2.get_bonus():,.2f}")

if __name__ == '__main__':
    main()