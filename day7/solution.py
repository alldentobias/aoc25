import os

def main():
    example_file_path = os.path.join(os.path.dirname(__file__), 'example.txt')
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    expected_example_result_part1 = 21
    expected_example_result_part2 = 40
    print("Running example input for part 1...")
    example_data = parse(example_file_path)
    result = solution_1(example_data)
    print(f"Result for part 1: {result}, expected: {expected_example_result_part1}")
    assert result == expected_example_result_part1
    print("Example input for part 1 passed!")
    print("Running actual input for part 1...")
    data = parse(input_file_path)
    result = solution_1(data)
    print(f"Part 1 result: {result}")
    print("Running example input for part 2...")
    result = solution_2(example_data)
    print(f"Result for part 2: {result}")
    assert result == expected_example_result_part2
    print(f"Test result for part 2: {result}")
    print("Example input for part 2 passed!")
    print("Running actual input for part 2...")
    #data = parse_2(input_file_path)
    print(f"Part 2 result: {solution_2(data)}")

def parse(file):
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        return lines

def solution_1(data):
    splits = 0
    travelled = [[False for i in range(len(data[0])+1)] for j in range(len(data))]
    q = []
    starting = data[0].find('S')
    q.append((1, starting))

    while q:
        next_x, next_y = q.pop()
        if next_y < 0 or next_y >= len(data[0]) or next_x >= len(data) or travelled[next_x][next_y]:
            continue
        travelled[next_x][next_y] = True
        val = data[next_x][next_y]
        if val == '^':
            q.append((next_x, next_y-1))
            q.append((next_x, next_y+1))
            splits += 1
        else:
            q.append((next_x+1, next_y))
    
    return splits

def dfs_helper(x, y, data, mat):
    if mat[x][y] != -1:
        return mat[x][y]
    if x == len(data) -1:
        mat[x][y] = 1
        return mat[x][y]
    if data[x][y] == '^':
        right_timelines = 0
        left_timelines = 0
        if y > 0:
            left_timelines = dfs_helper(x, y-1, data, mat)
        if y < len(data[0])-1:
            right_timelines = dfs_helper(x, y+1, data, mat)
        mat[x][y] = right_timelines + left_timelines
        return mat[x][y]
    else:
        mat[x][y] = dfs_helper(x+1, y, data, mat)
        return mat[x][y]


def solution_2(data):
    start = data[0].find('S')
    dp_matrix = [[-1 for i in range(len(data[0]))] for j in range(len(data))]
    res = dfs_helper(1, start, data, dp_matrix)
    return res
    

if __name__ == "__main__":
    main()

