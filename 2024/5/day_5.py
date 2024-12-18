import math
import re
import sys


def correct_lists(incorrect_lists, before_dict, after_dict):
    corrected_lists = []
    for incorrect_list in incorrect_lists:

    return corrected_lists


def check_problem_one(items, before_dict, after_dict):
    valid_lists = []
    incorrect_list = []
    for list_to_check in items:
        valid_list = True
        for i in range(len(list_to_check) - 1):
            next_item = list_to_check[i + 1]
            item = list_to_check[i]
            if not next_item in after_dict[item]:
                valid_list = False
                break
        valid_lists.append(list_to_check) if valid_list else incorrect_list.append(list_to_check)
    return valid_lists


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
                        if after not in after_items:
                            after_items[after] = []
                        if before not in before_items:
                            before_items[before] = []
                        # Add to dictionary
                        before_items[after].append(before)
                        after_items[before].append(after)
                else:
                    lines_to_check.append([int(el) for el in line.split(",")])
        print(f"Before dict: {before_items}")
        print(f"After dict: {after_items}")
        print(f"Lines to Check: {lines_to_check}")
        valid_lists = check_problem_one(lines_to_check, before_items, after_items)
        print(f"Num. of valid lists: {len(valid_lists)}")
        used_pages = [l[int(len(l)/2)] for l in valid_lists]
        print(f"Sum middle-pages: {sum(used_pages)}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(2)
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(3)
