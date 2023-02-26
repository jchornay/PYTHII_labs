#Jonathan Chornay
#CMSY 257 Spring 2023 Class
#Professor Charles Edwards
#
#Lab 2 Problem 1

#imports class ProductionWorker
from Lab2a_classes import ProductionWorker

def main():

    name = input("Employee Name: ")
    number = input("Employee Number: ")

    #prompts for shift until valid response is given (1 or 2)
    shift = ""
    while(shift!="1" and shift !="2"):
        shift = input("Shift (1 or 2): ")

    if shift == "1":
        shift = "Day"
    else:
        shift = "Night"

    pay = input("Hourly Pay: ")

    #create ProductionWorker object
    employee1 = ProductionWorker(name, number, shift, pay)

    print(f"\n"
          f"Employee name: {employee1.get_name()}\n"
          f"Employee number: {employee1.get_number()}\n"
          f"Shift: {employee1.get_shiftNum()}\n"
          f"Hourly pay: ${employee1.get_hourlyPay()}.00 per hour")

if __name__ == '__main__':
    main()