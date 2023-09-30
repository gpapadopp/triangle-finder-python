from itertools import combinations


class PredefinedAlgorithm:
    def __init__(self, input_numbers: list):
        self.input_numbers = input_numbers
        self.all_combinations = []
        self.all_acceptable_values = []
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

    def _generate_all_combinations(self):
        self.all_combinations = list(set(combinations(self.input_numbers, 3)))

    def _check_combination(self, combination: tuple) -> bool:
        side_a = int(combination[0])
        side_b = int(combination[1])
        side_c = int(combination[2])
        if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
            return True
        else:
            return False
