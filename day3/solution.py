import csv
import os

def main():
    example_file_path = os.path.join(os.path.dirname(__file__), 'example.txt')
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

    expected_example_result_part1 = 357
    expected_example_result_part2 = 3121910778619
    
    print("Running example input for part 1...")
    result = part1(example_file_path)
    print(f"Result for part 1: {result}, expected: {expected_example_result_part1}")
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
    #print(f"Part 2 result: {part2(input_file_path)}")

def part1(file):
    sum = 0
    with open(file, 'r') as f:
        banks = f.read().splitlines()
        for bank in banks:
            max_sum = 0
            pos = len(bank) - 2
            max_right = bank[len(bank) - 1]
            while pos >= 0:
                new_sum = int(bank[pos] + max_right)
                max_sum = max(max_sum, int(new_sum))
                max_right = max(max_right, bank[pos])
                pos -= 1
            sum += max_sum
        return sum

def part2(file):
    sum = 0
    with open(file, 'r') as f:
        banks = f.read().splitlines()
        for bank in banks:
            res = part2_help(bank, 0, 11)
            print(f"Bank: {bank}, res: {res}")
            sum += res
        return sum
                

def part2_help(bank, pos, pow, mem):
    if pow == 0 or pos == len(bank) - 1:
        return int(bank[pos])
    
    if pow > len(bank)-pos-1:
        return 0

    pow_num = 10**pow * int(bank[pos])
    return max(pow_num + part2_help(bank, pos+1, pow-1), part2_help(bank, pos+1, pow))

if __name__ == "__main__":
    main()

