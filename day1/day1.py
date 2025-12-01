def main():
    expected_example_result_part1 = 3
    expected_example_result_part2 = 6
    
    print("Running example input for part 1...")
    assert(part1('example.txt') == expected_example_result_part1)
    print("Example input for part 1 passed!")
    print("Running actual input for part 1...")
    print(f"Part 1 result: {part1('input.txt')}")

    print("Running example input for part 2...")
    assert(part2('example.txt') == expected_example_result_part2)
    print("Example input for part 2 passed!")
    print("Running actual input for part 2...")
    print(f"Part 2 result: {part2('input.txt')}")

def part1(file):
    zeroes = 0
    pos = 50

    with open(file, 'r') as f:
        for line in f:
            dir = 1 if line[0].lower() == 'r' else -1
            count = int(line[1:])
            pos = (pos + (dir * count)) % 100;

            if pos == 0: 
                zeroes += 1
    return zeroes

def part2(file):
    zeroes = 0
    pos = 50
    lock = range(0,100)
    with open(file, 'r') as f:
        for line in f:
            dir = 1 if line[0].lower() == 'r' else -1
            count = int(line[1:])

            for _ in range(count):
                pos += dir
                if pos < 0:
                    pos = 99
                elif pos > 99:
                    pos = 0

                if pos == 0:
                    zeroes += 1

    return zeroes

if __name__ == "__main__":
    main()

