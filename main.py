from consoles.console import Console
from algorithm.user_numbers import UserNumbersAlgorithm
from algorithm.predefined_algorithm import PredefinedAlgorithm
from algorithm.random_numbers_algorithm import RandomNumbersAlgorithm


def first_startup_menu_dialog():
    print("Welcome to Triangle Finder\n\n")
    print("Enter a number to continue:")
    print("1. Enter your numbers as sides of the triangle")
    print("2. Run program with predefined values (7, 10, 5, 4, 8, 7)")
    print("3. Run program with random numbers\n\n")


def read_number_list() -> list:
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


console_functions = Console()

first_startup_menu_dialog()
user_choice = input("Your choice: ")

console_functions.clear_console()

if int(user_choice) == 1:
    # User Defined Numbers
    all_user_numbers = read_number_list()
    algorithm_functions = UserNumbersAlgorithm(all_user_numbers)
    algorithm_functions.find_all_possible_triangles()
    algorithm_functions.print_data()
elif int(user_choice) == 2:
    # Predefined Numbers
    predefined_numbers = [7, 10, 5, 4, 8, 7]
    algorithm_functions = PredefinedAlgorithm(predefined_numbers)
    algorithm_functions.find_all_possible_triangles()
    algorithm_functions.print_data()
elif int(user_choice) == 3:
    # Array with Random Numbers
    list_length = input("Give the length of the array: ")
    start_number = input("Give the start number of the random function: ")
    end_number = input("Give the end number of the random function: ")
    algorithm_functions = RandomNumbersAlgorithm(int(list_length), int(start_number), int(end_number))
    algorithm_functions.find_all_possible_triangles()
    algorithm_functions.print_data()

console_functions.pause_system()
