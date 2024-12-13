import math
import sys


def calculate_diff(levels):
    return [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

def substitute_diff(levels_diff, index):
    if index == 0:
        return levels_diff[index + 1:]
    if index == len(levels_diff) - 1:
        return levels_diff[:index]
    return levels_diff[:index] + [levels_diff[index] + levels_diff[index + 1]] + levels_diff[index + 2:]


def check_difference_safeness(levels_diff):
    is_increasing = None
    for i in range(len(levels_diff)):
        diff = levels_diff[i]
        if not (0 < abs(diff) < 4):
            return i
        if is_increasing is None:
            is_increasing = diff > 0
        else:
            if is_increasing and diff < 0 or not is_increasing and diff > 0:
                return i
    return -1

def stupid_check_safeness_with_dampener(levels):
    def generate_dampened_sublist(_levels: list):
        _sub_levels = [_levels]
        for i in range(len(_levels)):
            level = _levels.copy()
            level.pop(i)
            _sub_levels.append(level)
        return _sub_levels

    found = False
    sub_levels = generate_dampened_sublist(levels)
    for level in sub_levels:
        print(level)
        if check_difference_safeness(calculate_diff(level)) == -1:
            found = True
            break
    print(f'------ {found} -----')
    return found

def check_safeness_with_dampener(levels_diff):
    positive, negative, zeros, problems_i = [], [], [], []
    for i in range(len(levels_diff)):
        diff = levels_diff[i]
        if diff > 0:
            positive.append(i)
            problems_i.append(i)
        elif diff < 0:
            negative.append(i)
            problems_i.append(i)
        else:
            zeros.append(i)
            problems_i.append(i)
    dampened = False
    safe = check_difference_safeness(levels_diff)
    if safe != -1:
        dampened = True
        if safe == len(levels_diff) - 1:
            safe = -1
        else:
            new_levels_diff = levels_diff[:safe]
            new_levels_diff.append(levels_diff[safe] + levels_diff[safe+1])
            if safe < len(levels_diff) - 2:
                new_levels_diff += levels_diff[safe+2:]
            print(levels_diff, ' ---- ', new_levels_diff)
            safe = check_difference_safeness(new_levels_diff)
    return safe == -1, dampened


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day_2.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    values = []
    values_differences = []
    values_safeness = []
    values_safeness_with_dampener = []
    try:
        safe_values = []
        unsafe_values = []
        dampened_safe_values = []
        with open(file_path, 'r') as file:
            for line in file:
                last_values = [int(el) for el in line.split(' ')]
                values.append(last_values)
                last_differences = [last_values[i+1] - last_values[i] for i in range(len(last_values) - 1)]
                values_differences.append(last_differences)

                if check_difference_safeness(last_differences) == -1:
                    safe_values.append(last_values)
                    values_safeness.append(1)
                else:
                    if stupid_check_safeness_with_dampener(last_values):
                        dampened_safe_values.append(last_values)
                    else:
                        unsafe_values.append(last_values)
                # values_safeness.append(1 if check_difference_safeness(last_differences) == -1 else 0)
                # values_safeness_with_dampener.append(1 if check_safeness_with_dampener(last_differences)[0] else 0)
                values_safeness_with_dampener.append(1 if stupid_check_safeness_with_dampener(last_differences) else 0)
        print(f"Number of elements: {len(values)}")
        # print(f"Number of safe levels: {sum(values_safeness)}")  # Request for Day 2 - Part 1 problem
        # print(f"Number of safe dampered levels: {sum(values_safeness_with_dampener)}")  # Request for Day 2 - Part 2 problem
        print(f"Number of safe levels: {len(safe_values)}")  # Request for Day 2 - Part 1 problem
        print(f"Number of unsafe levels: {len(unsafe_values)}")  # Request for Day 2 - Part 2 problem
        print(f"Number of dampened safe levels: {len(dampened_safe_values)}")  # Request for Day 2 - Part 2 problem
        print(f"{[71, 69, 70, 69, 66]} - Safe: {stupid_check_safeness_with_dampener(calculate_diff([71, 69, 70, 69, 66]))}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(2)
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(3)
