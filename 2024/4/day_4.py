import math
import re
import sys

xmas = 'XMAS'
xmas_reverse = xmas[::-1]

HORIZONTAL = 0
VERTICAL = 1
HORIZONTAL_REVERSE = 2
VERTICAL_REVERSE = 3
TOP_RIGHT = 4
BOTTOM_RIGHT = 5
TOP_LEFT = 6
BOTTOM_LEFT = 7

def get_coords(row, col, direction):
    # Straight
    if direction == HORIZONTAL:
        return [(row, col), (row, col + 1), (row, col + 2), (row, col + 3)]
    if direction == VERTICAL:
        return [(row, col), (row + 1, col), (row + 2, col), (row + 3, col)]
    if direction == HORIZONTAL_REVERSE:
        return [(row, col), (row, col - 1), (row, col - 2), (row, col - 3)]
    if direction == VERTICAL_REVERSE:
        return [(row, col), (row - 1, col), (row - 2, col), (row - 3, col)]
    # Oblique
    if direction == TOP_RIGHT:
        return [(row, col), (row - 1, col + 1), (row - 2, col + 2), (row - 3, col + 3)]
    if direction == BOTTOM_RIGHT:
        return [(row, col), (row + 1, col + 1), (row + 2, col + 2), (row + 3, col + 3)]
    if direction == TOP_LEFT:
        return [(row, col), (row - 1, col - 1), (row - 2, col - 2), (row - 3, col - 3)]
    if direction == BOTTOM_LEFT:
        return [(row, col), (row + 1, col - 1), (row + 2, col - 2), (row + 3, col - 3)]


def xmas(table):
    width = len(table[0])
    height = len(table)
    for row in range(height):
        for col in range(width):
            if table[row][col] == xmas[0]:
                if col <= width - len(xmas):
                    coords = [(row, col)]
                    to_check = table[row][col] + table[row][col + 1] + table[row][col + 2] + table[row][col + 3]
    split = str[4:-1].split(',')
    l_val = int(split[0])
    r_val = int(split[1])
    return l_val * r_val


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day_4.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    input_string = []  # As Table where each cell is a single character
    try:
        with open(file_path, 'r') as file:
            for line in file:
                input_string.append([*line])
        # print(input_string[0])
        # print(input_string[1])
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(2)
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(3)
