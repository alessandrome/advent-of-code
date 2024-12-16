import math
import re
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day_5.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    lines_to_check = []  # As Table where each cell is a single character
    before_items = {}
    after_items = {}
    try:
        with open(file_path, 'r') as file:
            rules = True
            for line in file:
                if rules:
                    if line == "\n":
                        rules = False
                    else:
                        before, after = (int(el) for el in line.split("|"))
                        # Init if not in dictionary
                        if after not in before_items:
                            before_items[after] = []
                        if before not in after_items:
                            after_items[before] = []
                        # Add to dictionary
                        before_items[after].append(before)
                        after_items[before].append(after)
                else:
                    lines_to_check.append([int(el) for el in line.split(",")])
        print(before_items)
        print(after_items)
        print(lines_to_check)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(2)
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(3)
