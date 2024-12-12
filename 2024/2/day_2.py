import math
import sys


def check_difference_safeness(levels_diff):
    is_increasing = None
    for diff in levels_diff:
        if not (abs(diff) > 0 and abs(diff) < 4):
            return False
        if is_increasing is None:
            is_increasing = diff > 0
        else:
            if is_increasing and diff < 0 or not is_increasing and diff > 0:
                return False
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day_2.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    values = []
    values_differences = []
    values_safeness = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                last_values = [int(el) for el in line.split(' ')]
                values.append(last_values)
                last_differences = [last_values[i+1] - last_values[i] for i in range(len(last_values) - 1)]
                values_differences.append(last_differences)
                values_safeness.append(1 if check_difference_safeness(last_differences) else 0)
        print(f"Number of elements: {len(values)}")
        print(f"Number of safe levels: {sum(values_safeness)}")  # Request for Day 2 - Part 1 problem
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(2)
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(3)
