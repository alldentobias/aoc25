import os
import heapq

def main():
    example_file_path = os.path.join(os.path.dirname(__file__), 'example.txt')
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

    expected_example_result_part1 = 13
    expected_example_result_part2 = 43
    
    print("Running example input for part 1...")
    lines_example = compute_lines(example_file_path)
    result = part1(lines_example)
    print(f"Result for part 1: {result}, expected: {expected_example_result_part1}")
    assert result == expected_example_result_part1
    print("Example input for part 1 passed!")

    print("Running actual input for part 1...")
    lines = compute_lines(input_file_path)
    result = part1(lines)
    print(f"Part 1 result: {result}")

    print("Running example input for part 2...")
    result = part2(lines_example)
    print(f"Result for part 2: {result}")
    assert result == expected_example_result_part2
    print(f"Test result for part 2: {result}")
    print("Example input for part 2 passed!")
    print("Running actual input for part 2...")
    print(f"Part 2 result: {part2(lines)}")

def compute_lines(file):
    with open(file, 'r') as f:
        return f.read().splitlines()
        

dirs = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0,1), (1,-1), (1,0), (1,1)]

def part1(stock):
    sum = 0
    for x, line in enumerate(stock):
        for y, char in enumerate(line):
            if char == '.':
                continue
            if surrounding(stock, x, y) < 4:
                sum+=1


    return sum

def decrease_surrounding(matrix, count_matrix, heap, x, y):
    for dx, dy in dirs:
        x2 = x + dx
        y2 = y + dy
        if x2 < 0 or x2 >= len(matrix):
            continue
        if y2 < 0 or y2 >= len(matrix[0]):
            continue
        if matrix[x2][y2] == '@' and count_matrix[x2][y2] != -1:
            count_matrix[x2][y2] -= 1
            if count_matrix[x2][y2] < 4:
                heapq.heappush(heap, (x2, y2))
                


def surrounding(matrix, x, y):
    surrounding = 0
    for dx, dy in dirs:
        x2 = x + dx
        y2 = y + dy
        if x2 < 0 or x2 >= len(matrix):
            continue
        if y2 < 0 or y2 >= len(matrix[0]):
            continue
        if matrix[x2][y2] == '@':
            surrounding += 1
    return surrounding


def part2(stock):
    removed = 0
    queue = []
    count_matrix = [[-1 for _ in range(len(stock[0]))] for _ in range(len(stock))]
    for x, line in enumerate(stock):
        for y, char in enumerate(line):
            if char == '.':
                continue
            else:
                count = surrounding(stock, x, y)
                count_matrix[x][y] = count
                if count < 4:
                    queue.append((x,y))

    heapq.heapify(queue)
    while queue:
        remove_x, remove_y = heapq.heappop(queue)
        if count_matrix[remove_x][remove_y] == -1:
            continue
        removed += 1
        count_matrix[remove_x][remove_y] = -1
        decrease_surrounding(stock, count_matrix, queue, remove_x, remove_y)

    return removed


                

if __name__ == "__main__":
    main()

