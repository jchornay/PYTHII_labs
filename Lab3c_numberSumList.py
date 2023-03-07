# Jonathan Chornay
# CMSY 257 Spring 2023 Class
# Professor Charles Edwards
#
# Lab 3 Problem 3

def main():
    loop = True

    while loop:

        # try block that saves user input as list of integers
        try:
            numList = [int(i) for i in input("Enter list of integers separated by commas: ").split(',')]
            print(f"Sum of {numList} is {sumList(numList)}\n")

        # error message assuming invalid entry
        except:
            print("Error: invalid input")

        # allows user to sum another list or exit loop
        if input("Enter another list? Y/N ").lower().strip() == "n":
            loop = False


def sumList(input):
    # recursively adds first element of input list to shortened version of itself
    if len(input) > 0:
        return input[0] + sumList(input[1:len(input)])

    # base case, i.e. if length of remaining list is zero
    else:
        return 0


if __name__ == '__main__':
    main()
