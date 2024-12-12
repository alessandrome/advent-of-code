import math
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    values_l = []
    values_r = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                values = line.split(' ' * 3)
                values_l.append(int(values[0]))
                values_r.append(int(values[1]))
        print(f"Number of elements: {len(values_l)}")
        values_l.sort()
        values_r.sort()
        # Day 1 - Part 1
        total_sum = int(sum([math.fabs(values_r[i] - values_l[i]) for i in range(len(values_l))]))
        print(f"Sum: {total_sum}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(2)
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(3)
