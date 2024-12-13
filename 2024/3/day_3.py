import math
import re
import sys


def mul_str(str):
    split = str[4:-1].split(',')
    l_val = int(split[0])
    r_val = int(split[1])
    return l_val * r_val


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day_3.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    values_l = []
    values_r = []
    similarity_values = {}  # {value: [count_on_left_side, count_on_right_side]}
    input = ''
    sum_mul = 0
    conditional_sum_mul = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                input += line
        mul_pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
        conditional_pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)')
        mul_enabled = True
        matches = re.findall(mul_pattern, input)
        conditional_matches = re.findall(conditional_pattern, input)
        # conditional_matches_4 = re.findall(r'do\(\).*don\'t\(\)', input)
        print(matches)
        print(conditional_matches)
        for match in conditional_matches:
            if mul_enabled and match.startswith('mul'):
                conditional_sum_mul += mul_str(match)
            elif match == 'do()':
                mul_enabled = True
            else:
                mul_enabled = False
            # print(mul_enabled, match, conditional_sum_mul)
        for match in matches:
            sum_mul += mul_str(match)
        print(f"Sum of mul: {sum_mul}")
        print(f"Cond. sum of mul: {conditional_sum_mul}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(2)
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(3)
