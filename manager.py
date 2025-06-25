from logging import exception
from types import new_class
import shapes

shapes_list = list()

def main_menu():
    c = input("to create a new shape enter 1:\n"
              "to print all the shapes enter 2:\n"
              "to exit print 3:\n")
    try:
        choice = int(c)
        if choice == 1:
            shape_menu()
            main_menu()
        elif choice == 2:
            show_all()
            main_menu()
        elif choice == 3:
            print("Goodbye! thank you for using calculator.")
        else:
            print("no legal choice entered.")
            shape_menu()
    except ValueError:
        print("Invalid input. Please enter a number.")

def shape_menu():
    c = input("to create Rectangle enter 1:\n"
              "to create Square enter 2:\n"
              "to create Triangle enter 3:\n"
              "to create Circle enter 4:\n"
              "to create Hexagon enter 5:\n")
    try:
        choice = int(c)
        if choice == 1:
            create_rectangle()
        elif choice == 2:
            create_square()
        elif choice == 3:
            create_triangle()
        elif choice == 4:
            create_circle()
        elif choice == 5:
            create_hexagon()
        else:
            print("no legal choice entered.")
            shape_menu()
    except ValueError:
        print("Invalid input. Please enter a number.")
        shape_menu()

def create_rectangle():
    try:
        weight = int(input("weight:"))
        height = int(input("height:"))
        shape = shapes.Rectangle(weight, height)
        shapes_list.append(shape)
    except ValueError:
        print("Invalid input. try again.")
        create_rectangle()

def create_square():
    try:
        side = int(input("side:"))
        shape = shapes.Square(side)
        shapes_list.append(shape)
    except ValueError:
        print("Invalid input. try again.")
        create_square()

def create_triangle():
    try:
        side1 = int(input("side 1:"))
        side2 = int(input("side 2:"))
        side3 = int(input("side 3:"))
        shape = shapes.Triangle(side1, side2, side3)
        shapes_list.append(shape)
    except ValueError:
        print("Invalid input. try again.")
        create_triangle()

def create_circle():
    try:
        radius = int(input("radius:"))
        shape = shapes.Circle(radius)
        shapes_list.append(shape)
    except ValueError:
        print("Invalid input. try again.")
        create_circle()

def create_hexagon():
    try:
        side = int(input("side:"))
        shape = shapes.Hexagon(side)
        shapes_list.append(shape)
    except ValueError:
        print("Invalid input. try again.")
        create_hexagon()

def show_all():
    if len(shapes_list) < 1:
        print("you didn't created any shape yet.")
    else:
        for i in range(len(shapes_list)):
            print(f"{i+1}: {str()}")