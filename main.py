import os
from sys import platform
import itertools
import random


def clear_console():
    if platform == "linux" or platform == "linux2":
        # Platform is Linux
        os.system("clear")
    elif platform == "darwin":
        # Platform is Mac OS X
        os.system("clear")
    elif platform == "win32":
        # Platform is Windows
        os.system("cls")


def system_pause_console():
    os.system("PAUSE")


def first_startup_menu_dialog():
    print("Welcome to Triangle Finder\n\n")
    print("Enter a number to continue:")
    print("1. Enter your numbers as sides of the triangle")
    print("2. Run program with predefined values (7, 10, 5, 4, 8, 7)")
    print("3. Run program with random numbers\n\n")


def read_number_list():
    number_list = []
    number_inserted = True
    while number_inserted:
        number = input("Type a number or 0 to stop: ")
        if int(number) == 0:
            number_inserted = False
        else:
            number_list.append(int(number))
    else:
        return number_list


def check_if_triangle(side_a, side_b, side_c):
    if int(side_a) + int(side_b) > int(side_c):
        if int(side_a) + int(side_c) > int(side_b):
            if int(side_b) + int(side_c) > int(side_a):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


first_startup_menu_dialog()
user_choice = input("Your choice: ")
clear_console()
if int(user_choice) == 1:
    all_user_numbers = read_number_list()
    all_possible_combinations = list(itertools.combinations(all_user_numbers, 3))
    all_possible_combinations_triangle_indexes = []
    for i in range(0, len(all_possible_combinations), 1):
        if check_if_triangle(all_possible_combinations[i][0], all_possible_combinations[i][1], all_possible_combinations[i][2]):
            all_possible_combinations_triangle_indexes.append(i)
    else:
        print("The possible triangles you can make, is ", len(all_possible_combinations_triangle_indexes))
        print("The combinations that you can make triangle is the below:")
        for i in range(0, len(all_possible_combinations_triangle_indexes), 1):
            print(all_possible_combinations[all_possible_combinations_triangle_indexes[i]])
elif int(user_choice) == 2:
    predefined_numbers = [7, 10, 5, 4, 8, 7]
    all_possible_combinations = list(itertools.combinations(predefined_numbers, 3))
    all_possible_combinations_triangle_indexes = []
    for i in range(0, len(all_possible_combinations), 1):
        if check_if_triangle(all_possible_combinations[i][0], all_possible_combinations[i][1], all_possible_combinations[i][2]):
            all_possible_combinations_triangle_indexes.append(i)
    else:
        print("The possible triangles you can make, is ", len(all_possible_combinations_triangle_indexes))
        print("The combinations that you can make triangle is the below:")
        for i in range(0, len(all_possible_combinations_triangle_indexes), 1):
            print(all_possible_combinations[all_possible_combinations_triangle_indexes[i]])
elif int(user_choice) == 3:
    list_length = input("Give the length of the array: ")
    start_number = input("Give the start number of the random function: ")
    end_number = input("Give the end number of the random function: ")
    random_generated_numbers = []
    for i in range(0, int(list_length), 1):
        random_generated_numbers.append(random.randint(int(start_number), int(end_number)))
    else:
        all_possible_combinations = list(itertools.combinations(random_generated_numbers, 3))
        all_possible_combinations_triangle_indexes = []
        for i in range(0, len(all_possible_combinations), 1):
            if check_if_triangle(all_possible_combinations[i][0], all_possible_combinations[i][1],
                                 all_possible_combinations[i][2]):
                all_possible_combinations_triangle_indexes.append(i)
        else:
            print("The possible triangles you can make, is ", len(all_possible_combinations_triangle_indexes))
            print("The combinations that you can make triangle is the below:")
            for i in range(0, len(all_possible_combinations_triangle_indexes), 1):
                print(all_possible_combinations[all_possible_combinations_triangle_indexes[i]])

system_pause_console()
