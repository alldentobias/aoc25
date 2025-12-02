import csv
import os

def main():
    example_file_path = os.path.join(os.path.dirname(__file__), 'example.txt')
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

    expected_example_result_part1 = 1227775554
    expected_example_result_part2 = 4174379265
    
    print("Running example input for part 1...")
    result = part1(example_file_path)
    assert result == expected_example_result_part1
    print("Example input for part 1 passed!")
    print("Running actual input for part 1...")
    result = part1(input_file_path)
    print(f"Part 1 result: {result}")

    print("Running example input for part 2...")
    result = part2(example_file_path)
    print(f"Result for part 2: {result}")
    assert result == expected_example_result_part2
    print(f"Test result for part 2: {result}")
    print("Example input for part 2 passed!")
    print("Running actual input for part 2...")
    print(f"Part 2 result: {part2(input_file_path)}")

def part1(file):
    sum = 0
    with open(file, 'r') as f:
        content = f.read().strip()
        all_ranges = content.split(",")

        for r in all_ranges:
            split = r.split("-")
            lower = int(split[0])
            upper = int(split[1])

            for i in range(lower, upper + 1):
                str_i = str(i)
                if len(str_i) % 2 != 0:
                    continue
                mid = len(str_i) // 2
                lower_half = str_i[:mid]
                upper_half = str_i[mid:]
                if lower_half == upper_half:
                    sum += i

    return sum

def part2(file):
    sum = 0
    with open(file, 'r') as f:
        content = f.read().strip()
        all_ranges = content.split(",")

        for r in all_ranges:
            split = r.split("-")
            lower = int(split[0])
            upper = int(split[1])

            for i in range(lower, upper + 1):
                str_i = str(i)
                s1 = (str_i + str_i)[1:-1]
                if str_i in s1:
                    sum += i

    return sum

if __name__ == "__main__":
    main()

