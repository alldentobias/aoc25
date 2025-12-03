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
    print(f"Part 2 result: {part2(input_file_path)}")

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
    with open(file, 'r') as f:
        banks = f.read().splitlines()
        return sum(int(max_j(bank, 12)) for bank in banks)
                

def max_j(bank, remaining):
    if (remaining == 0): return ""
    max_index = max_index_in_subbank(bank[:len(bank)-remaining+1])
    return bank[max_index] + max_j(bank[max_index + 1:], remaining - 1)
    
    
def max_index_in_subbank(bank):
    max_index = 0
    for i,pos in enumerate(bank):
        if int(bank[i]) > int(bank[max_index]):
            max_index = i

    return max_index

if __name__ == "__main__":
    main()
    print("Help")

