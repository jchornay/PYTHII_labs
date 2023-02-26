#Jonathan Chornay
#CMSY 257 Spring 2023 Class
#Professor Charles Edwards
#
#Lab 2 Problem 3

from Lab2c_classes import Triangle

def main():
    triangle1 = Triangle()

    triangle1.set_side2(1.5)
    triangle1.set_color("yellow")

    print()
    print(triangle1)
    print(f"Area: {triangle1.getArea():.4} units squared"
          f"\nPerimeter: {triangle1.getPerimeter()} units"
          f"\nColor: {triangle1.get_color()}"
          f"\nFilled: {str(triangle1.get_filled())}")


if __name__ == "__main__":
    main()