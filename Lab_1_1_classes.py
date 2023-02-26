#Jonathan Chornay
#CMSY 257 Spring 2023 Class
#Professor Charles Edwards
#
#Lab 1 Problem 1

#defines class Patient and Procedure
class Patient:

    #define __init__ method and attributes
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip, phone, emergency_name, emergency_phone):

        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name

        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip = zip
        self.__phone = phone

        self.__emergency_name = emergency_name
        self.__emergency_phone = emergency_phone

    #getters and setters for each class attribute
    def get_first_name(self):
        return self.__firstname
    def set_first_name(self, first_name):
        self.__firstname = first_name

    def get_middle_name(self):
        return self.__middle_name
    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

    def get_last_name(self):
        return self.__last_name
    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_address(self):
        return self.__address
    def set_address(self,address):
        self.__address = address

    def get_city(self):
        return self.__city
    def set_city(self, city):
        self.__city = city

    def get_state(self):
        return self.__state
    def set_state(self, state):
        self.__state = state

    def get_zip(self):
        return self.__zip
    def set_zip(self, zip):
        self.__zip = zip

    def get_phone(self):
        return self.__phone
    def set_phone(self, phone):
        self.__phone = phone

    def get_emergency_name(self):
        return self.__emergency_name
    def set_emergency_name(self, emergency_name):
        self.__emergency_name = emergency_name

    def get_emergency_phone(self):
        return self.__emergency_phone
    def set_emergency_phone(self, emergency_phone):
        self.__emergency_phone = emergency_phone

    #defines __str__ method for patient
    def __str__(self):
        return f'Name: {self.__first_name} {self.__middle_name} {self.__last_name}\n' \
               f'Address: {self.__address}, {self.__city}, {self.__state} {self.__zip}\n' \
               f'Phone: {self.__phone}\n' \
               f'\n' \
               f'Emergency Contact: {self.__emergency_name}, {self.__emergency_phone}'




#defines class Procedure
class Procedure:

    # define __init__ method and attributes
    def __init__(self, proc_name, proc_date, proc_doc, proc_charge):
        self.__proc_name = proc_name
        self.__proc_date = proc_date
        self.__proc_doc = proc_doc
        self.__proc_charge = proc_charge

    # getters and setters for each class attribute
    def get_proc_name(self):
        return self.__proc_name
    def set_proc_name(self, proc_name):
        self.__proc_name = proc_name

    def get_proc_date(self):
        return self.__proc_date
    def set_proc_date(self, proc_date):
        self.__proc_date = proc_date

    def get_proc_doc(self):
        return self.__proc_doc
    def set_proc_doc(self, proc_doc):
        self.__proc_doc = proc_doc

    def get_proc_charge(self):
        return self.__proc_charge
    def set_proc_charge(self, proc_charge):
        self.__proc_charge = proc_charge

    # defines __str__ method for patient
    def __str__(self):
        return f'Procedure: {self.__proc_name}\n' \
               f'Date: {self.__proc_date}\n' \
               f'Provider: {self.__proc_doc}\n' \
               f'Charge: {self.__proc_charge}\n'