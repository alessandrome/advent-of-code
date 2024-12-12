import math
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day_1.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    values_l = []
    values_r = []
    similarity_values = {}  # {value: [count_on_left_side, count_on_right_side]}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                values = [int(el) for el in line.split(' ' * 3)]

                # Counting for Day 1 - Part 2 solution
                if values[0] in similarity_values:
                    similarity_values[values[0]][0] += 1
                else:
                    similarity_values[values[0]] = [1, 0]

                if values[1] in similarity_values:
                    similarity_values[values[1]][1] += 1
                else:
                    similarity_values[values[1]] = [0, 1]

                values_l.append(values[0])
                values_r.append(values[1])
        print(f"Number of elements: {len(values_l)}")
        values_l.sort()
        values_r.sort()
        # Day 1 - Part 1
        total_sum = int(sum([math.fabs(values_r[i] - values_l[i]) for i in range(len(values_l))]))
        print(f"Sum: {total_sum}")
        # Day 1 - Part 2
        similarity_sum = sum([k * similarity_values[k][0] * similarity_values[k][1] for k in similarity_values.keys()])
        print(f"Similarity: {similarity_sum}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(2)
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(3)
