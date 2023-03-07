# Jonathan Chornay
# CMSY 257 Spring 2023 Class
# Professor Charles Edwards
#
# Lab 3 Problem 2

def main():
    loop = True

    while loop:

        # try block that sends user input to sum() method
        try:
            print(sum(int(input("Enter integer to calculate sum of previous integers: "))))

        # error message assuming invalid entry
        except:

            print("User input must be positive integer!")

        # allows user to sum another number or exit loop
        if input("Sum another number? Y/N ").lower().strip() == "n":
            loop = False


def sum(input):
    # recursively adds numbers in reverse sequence from input to 0
    if input > 0:
        return input + sum(input - 1)
    # base case, i.e. if zero is passed to sum() function, function returns zero
    else:
        return 0


if __name__ == '__main__':
    main()
