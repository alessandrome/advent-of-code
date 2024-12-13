import math
import re
import sys

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
        conditional_pattern = re.compile(r'do\(\).*don\'t\(\)|^.*(?!)(do\(\)|don\'t\(\))|do\(\).*$')
        matches = re.findall(mul_pattern, input)
        conditional_matches_1 = re.findall(r'do\(\).*don\'t\(\)', input)
        conditional_matches_2 = re.findall(r'do\(\)(?!.*don\'t\(\)).*$', input)
        conditional_matches_3 = re.findall(r'^.*?(?=do\(\)|don\'t\(\))', input)
        # conditional_matches_4 = re.findall(r'do\(\).*don\'t\(\)', input)
        print(matches)
        print(conditional_matches_1)
        print(conditional_matches_2)
        print(conditional_matches_3)
        for match in (conditional_matches_1 + conditional_matches_2 + conditional_matches_3):
            mul_matches = re.findall(mul_pattern, match)
            print(f"Mul matches: {mul_matches}")
            for mul_match in mul_matches:
                split = mul_match[4:-1].split(',')
                l_val = int(split[0])
                r_val = int(split[1])
                conditional_sum_mul += l_val * r_val
        for match in matches:
            split = match[4:-1].split(',')
            l_val = int(split[0])
            r_val = int(split[1])
            sum_mul += l_val * r_val
        print(f"Sum of mul: {sum_mul}")
        print(f"Cond. sum of mul: {conditional_sum_mul}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(2)
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(3)
