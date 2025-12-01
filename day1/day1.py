def main():
    part1()
    part2()

def part1():
    zeroes = 0
    pos = 50

    with open('input.txt', 'r') as f:
        for line in f:
            dir = 1 if line[0].lower() == 'r' else -1
            count = int(line[1:])
            pos = (pos + (dir * count)) % 100;

            if pos == 0: 
                zeroes += 1
    print(f"Ended on zeroes: {zeroes}")

def part2():
    zeroes = 0
    pos = 50
    lock = range(0,100)
    with open('input.txt', 'r') as f:
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

    print(f"Traversed zeroes: {zeroes}")



            


if __name__ == "__main__":
    main()

