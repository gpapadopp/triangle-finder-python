from itertools import combinations
import random


class RandomNumbersAlgorithm:
    def __init__(self, array_length: int, start_number: int, end_number: int):
        self.array_length = array_length
        self.start_number = start_number
        self.end_number = end_number
        self.random_numbers = []
        self.all_combinations = []
        self.all_acceptable_values = []
        self._generate_random_array()
        self._generate_all_combinations()

    def find_all_possible_triangles(self):
        for combination in self.all_combinations:
            if self._check_combination(combination):
                self.all_acceptable_values.append(combination)

    def print_data(self):
        print("You can make " + str(len(self.all_acceptable_values)) + " triangles")
        print("All acceptable triangles (as combinations) are the following:")
        for combination in self.all_acceptable_values:
            print(combination)

    def _generate_random_array(self):
        self.random_numbers = [random.randint(self.start_number, self.end_number) for _ in range(self.array_length)]

    def _generate_all_combinations(self):
        self.all_combinations = list(set(combinations(self.random_numbers, 3)))

    def _check_combination(self, combination: tuple) -> bool:
        side_a = int(combination[0])
        side_b = int(combination[1])
        side_c = int(combination[2])
        if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
            return True
        else:
            return False
