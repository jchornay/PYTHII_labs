#Jonathan Chornay
#CMSY 257 Spring 2023 Class
#Professor Charles Edwards
#
#Lab 2 Problems 1 and 2 classes

#defines class Employee and subclass ProductionWorker
class Employee:

    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    #getters and setters
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_number(self):
        return self.__number
    def set_number(self, number):
        self.__number = number

class ProductionWorker(Employee):

    def __init__(self, name, number, shiftNum, hourlyPay):

        super().__init__(name, number)
        self.__shiftNum = shiftNum
        self.__hourlyPay = hourlyPay

    #getters and setters
    def get_shiftNum(self):
        return self.__shiftNum
    def set_shiftNum(self, shiftNum):
        self.__shiftNum = shiftNum

    def get_hourlyPay(self):
        return self.__hourlyPay
    def set_hourlyPay(self, hourlyPay):
        self.__hourlyPay = hourlyPay
