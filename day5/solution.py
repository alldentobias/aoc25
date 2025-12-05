import os

def main():
    example_file_path = os.path.join(os.path.dirname(__file__), 'example.txt')
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

    expected_example_result_part1 = 3
    expected_example_result_part2 = 14
    
    print("Running example input for part 1...")
    ranges_example, items_example = parse(example_file_path)
    result = part1(ranges_example, items_example)
    print(f"Result for part 1: {result}, expected: {expected_example_result_part1}")
    assert result == expected_example_result_part1
    print("Example input for part 1 passed!")

    print("Running actual input for part 1...")
    ranges, items = parse(input_file_path)
    result = part1(ranges, items)
    print(f"Part 1 result: {result}")

    print("Running example input for part 2...")
    result = part2(ranges_example)
    print(f"Result for part 2: {result}")
    assert result == expected_example_result_part2
    print(f"Test result for part 2: {result}")
    print("Example input for part 2 passed!")
    print("Running actual input for part 2...")
    print(f"Part 2 result: {part2(ranges)}")

def parse(file):
    ranges = []
    items = []
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        max_int = 0
        
        for line in lines:
            if '-' in line:
                r = line.split('-')
                upper = int(r[1])
                if upper > max_int:
                    max_int = upper
                ranges.append((int(r[0]),upper))
            elif line == '':
                continue
            else:
                items.append(line)
    return ranges, items


def part1(ranges, items):
    sum = 0
    for item in items:
        value = int(item)
        if in_ranges(ranges, value):
            sum += 1

    return sum

def in_ranges(ranges, value):
    for range in ranges:
        if value >= range[0] and value <= range[1]:
            return True
    return False
    


def part2(ranges):
    if not ranges:
        return 0

    ranges.sort()

    non_overlapping_ranges = []
    open_lower = ranges[0][0]
    open_upper = ranges[0][1]
    valid_ids = 0
    
    for r in ranges[1:]:
        if r[0] <= open_upper:
            open_upper = max(r[1], open_upper)
        else:
            non_overlapping_ranges.append((open_lower, open_upper))
            open_lower = r[0]
            open_upper = r[1]
    non_overlapping_ranges.append((open_lower, open_upper))
    for r in non_overlapping_ranges:
        valid_ids += r[1] - r[0] + 1

    return valid_ids
                

if __name__ == "__main__":
    main()

