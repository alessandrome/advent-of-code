import math
import re
import sys

# xmas = ['X', 'M', 'A', 'S']
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

def get_text(table, row, col, direction):
    coords = get_coords(row, col, direction)
    to_check = (table[coords[0][0]][coords[0][1]] +
                table[coords[1][0]][coords[1][1]] +
                table[coords[2][0]][coords[2][1]] +
                table[coords[3][0]][coords[3][1]])
    return coords, to_check

def xmas_counter(table):
    xmas_coords = []
    width = len(table[0])
    height = len(table)
    for row in range(height):
        for col in range(width):
            horizontal_space = col <= width - len(xmas)
            vertical_space = row <= height - len(xmas)
            horizontal_reverse_space = col >= len(xmas) - 1
            vertical_reverse_space = row >= len(xmas) - 1
            if table[row][col] == xmas[0]:
                # Horizontal
                if horizontal_space:
                    coords, to_check = get_text(table, row, col, HORIZONTAL)
                    # print(to_check)
                    if to_check == xmas:
                        xmas_coords.append(coords)
                    # Oblique Right
                    if vertical_space:
                        coords, to_check = get_text(table, row, col, BOTTOM_RIGHT)
                        if to_check == xmas:
                            xmas_coords.append(coords)
                    if vertical_reverse_space:
                        coords, to_check = get_text(table, row, col, TOP_RIGHT)
                        if to_check == xmas:
                            xmas_coords.append(coords)
                if horizontal_reverse_space:
                    coords, to_check = get_text(table, row, col, HORIZONTAL_REVERSE)
                    if to_check == xmas:
                        xmas_coords.append(coords)
                    # Oblique Left
                    if vertical_space:
                        coords, to_check = get_text(table, row, col, BOTTOM_LEFT)
                        if to_check == xmas:
                            xmas_coords.append(coords)
                    if vertical_reverse_space:
                        coords, to_check = get_text(table, row, col, TOP_LEFT)
                        if to_check == xmas:
                            xmas_coords.append(coords)
                # Vertical
                if vertical_space:
                    coords, to_check = get_text(table, row, col, VERTICAL)
                    if to_check == xmas:
                        xmas_coords.append(coords)
                if vertical_reverse_space:
                    coords, to_check = get_text(table, row, col, VERTICAL_REVERSE)
                    if to_check == xmas:
                        xmas_coords.append(coords)
    return xmas_coords


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
        print(len(xmas_counter(input_string)))
        print(xmas == ['X', 'M', 'A', 'S'])
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(2)
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(3)
