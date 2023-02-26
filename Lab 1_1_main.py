#Jonathan Chornay
#CMSY 257 Spring 2023 Class
#Professor Charles Edwards
#
#Lab 1 Problem 1

#imports Patient and Procedure classes
from Lab_1_1_classes import Patient
from Lab_1_1_classes import Procedure

def main():

    #instantiates patient and procedure objects
    patient1 = Patient(first_name="Walter",middle_name="Hartwell", last_name="White", address="406 Negra Arroyo Lane",city="Alberqueque",state="NM",zip=20008,phone=1234567890,emergency_name="Skylar",emergency_phone=999)

    procedure1 = Procedure(proc_name="Physical Exam", proc_date="2/20/2023", proc_doc="Dr. Irvine", proc_charge=250)
    procedure2 = Procedure(proc_name="X-ray", proc_date="2/20/2023", proc_doc="Dr. Jamison", proc_charge=500)
    procedure3 = Procedure(proc_name="Blood test", proc_date="2/20/2023", proc_doc="Dr. Smith", proc_charge=200)

    #calls __str__ function from each instance
    print(patient1)
    print(f'{procedure1}\n{procedure2}\n{procedure3}')

if __name__ == '__main__':
    main()
