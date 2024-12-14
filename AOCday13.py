import re

def parse_clusters(file_path):
    clusters = []
    with open(file_path, 'r', encoding = 'utf-8') as f:
        data = f.read()
        raw_clusters = data.strip().split('\n\n')  # Split clusters by blank lines
        for cluster in raw_clusters:
            # re, hate to love it, love to hate it
            horiz_a, vert_a = map(int, re.findall(r'Button A: X\+(\d+), Y\+(\d+)', cluster)[0])
            horiz_b, vert_b = map(int, re.findall(r'Button B: X\+(\d+), Y\+(\d+)', cluster)[0])
            x_end, y_end = map(int, re.findall(r'Prize: X=(\d+), Y=(\d+)', cluster)[0])

            # Uncomment this to accomplish part 2
            # Add 10^13 to the X and Y positions, it's all that's neded
            # x_end += 10**13
            # y_end += 10**13

            clusters.append({
                "horiz_a": horiz_a, "vert_a": vert_a,
                "horiz_b": horiz_b, "vert_b": vert_b,
                "x_end": x_end, "y_end": y_end
            })
    return clusters

def doin_the_math(horiz_a, vert_a, horiz_b, vert_b, x_end, y_end):
    try:
        num_a = (vert_b * x_end - horiz_b * y_end) / (vert_b * horiz_a - horiz_b * vert_a)
        num_b = (x_end - horiz_a * num_a) / horiz_b

        # No floats, buttons can't be partially pressed in game
        if not num_a.is_integer() or not num_b.is_integer():
            return None, None, None


        # Drop cluster if values are invalid
        if num_a < 0 or num_b < 0:
            return None, None, None  # Mark cluster as invalid

        # Calculate cost
        cost = 3 * num_a + 1 * num_b
        return num_a, num_b, cost
    except ZeroDivisionError:
        return None, None, None  # Handle division by zero edge cases, just in case.

def main():
    # Parse input file
    file_path = 'AOC2024Day13input.txt'  # Replace with your actual file path
    clusters = parse_clusters(file_path)

    # Process clusters
    total_cost = 0
    for cluster in clusters:
        num_a, num_b, cost = doin_the_math(
            cluster["horiz_a"], cluster["vert_a"],
            cluster["horiz_b"], cluster["vert_b"],
            cluster["x_end"], cluster["y_end"]
        )
        if num_a is not None and num_b is not None:
            total_cost += cost

    # Output total cost only
    print(total_cost)

if __name__ == "__main__":
    main()
