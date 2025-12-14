import os
from functools import reduce
from operator import add, mul

operator_func = {
    '+': add,
    '*': mul,
}
def main():
    example_file_path = os.path.join(os.path.dirname(__file__), 'example.txt')
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    expected_example_result_part1 = 4277556
    expected_example_result_part2 = 3263827
    print("Running example input for part 1...")
    data = parse(example_file_path)
    result = solution(data)
    print(f"Result for part 1: {result}, expected: {expected_example_result_part1}")
    assert result == expected_example_result_part1
    print("Example input for part 1 passed!")
    print("Running actual input for part 1...")
    data = parse(input_file_path)
    result = solution(data)
    print(f"Part 1 result: {result}")
    print("Running example input for part 2...")
    data = parse_2(example_file_path)
    result = solution(data)
    print(f"Result for part 2: {result}")
    assert result == expected_example_result_part2
    print(f"Test result for part 2: {result}")
    print("Example input for part 2 passed!")
    print("Running actual input for part 2...")
    data = parse_2(input_file_path)
    print(f"Part 2 result: {solution(data)}")

def parse(file):
    data = []
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        lines = [line.split(' ') for line in lines]
        lines = [[x for x in line if x] for line in lines]
        data = [(None, []) for i in range(len(lines[0]))]


        for num_line in lines[:-1]: # Number Lines
            for index, num in enumerate(num_line):
                data[index][1].append(int(num))

        for index, operator in enumerate(lines[-1]): # Operator Line
            operator = operator_func[operator]
            data[index] = (operator, data[index][1])
        return data

def parse_2(file):
    data = []
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        operator_line = lines[-1]
        opearator_ranges = []
        current_operator_range_start = 0
        current_operator = operator_func[operator_line[0]]

        for index, character in enumerate(operator_line[1:]):
            if character not in ('+', '*'):
                continue
            opearator_ranges.append((current_operator_range_start, index-1, current_operator))
            current_operator = operator_func[character]
            current_operator_range_start = index+1

        opearator_ranges.append((current_operator_range_start, len(operator_line)-1, current_operator))
        number_lines = lines[:-1]

        for start, end, operator in opearator_ranges:
            numbers = []
            for col in range(start, end+1):
                current_string = ''
                for line in number_lines:
                    if line[col] == '':
                        continue
                    else:
                        current_string += line[col]
                numbers.append(int(current_string))
            data.append((operator, numbers))
    return data


def solution(data):
    sum = 0
    for (operator, values) in data:
        sum += reduce(operator, values)
    return sum

if __name__ == "__main__":
    main()

