import re

# Test data
# crazydata = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open("day3input.txt", "r", encoding="utf-8") as input_file:
    file_content = input_file.read()
# Find all `mul(...)` patterns in the data
matches = re.findall(r"mul\((\d+),\s*(\d+)\)", file_content)

# Calculate the total
TOTAL = 0
for x, y in matches:
    TOTAL += int(x) * int(y)

# Output the total
print(f"Total: {TOTAL}")


# Challenge 2
do_pattern = re.findall(r"do\(\)", file_content)  # sometimes it do be like that
dont_pattern = re.findall(r"don't\(\)", file_content)  # sometimes it don't be like that

precursor = re.search(r"do\(\)|don't\(\)", file_content)
if precursor:
    precursor_text = file_content[: precursor.start()]
else:
    precursor_text = file_content

PRE_MARKER_TOTAL = 0
for match in re.findall(r"mul\((\d+),\s*(\d+)\)", precursor_text):
    x, y = map(int, match)
    PRE_MARKER_TOTAL += x * y

do_positions = [m.start() for m in re.finditer(r"do\(\)", file_content)]

do_blocks = []
for i, do_pos in enumerate(do_positions):
    next_do_pos = do_positions[i + 1] if i + 1 < len(do_positions) else len(file_content)
    block = file_content[do_pos:next_do_pos]
    do_blocks.append(block)

print(f"Number of do blocks: {len(do_blocks)}")

cleaned_do_blocks = []
for block in do_blocks:
    dont_match = re.search(r"don't\(\)", block)
    if dont_match:
        cleaned_block = block[: dont_match.start()]
    else:
        cleaned_block = block
    cleaned_do_blocks.append(cleaned_block)

print(f"Number of cleaned do blocks: {len(cleaned_do_blocks)}")


DO_BLOCKS_TOTAL = 0
for block in cleaned_do_blocks:
    for match in re.findall(r"mul\((\d+),\s*(\d+)\)", block):
        x, y = map(int, match)
        DO_BLOCKS_TOTAL += x * y

# Combine totals
total = PRE_MARKER_TOTAL + DO_BLOCKS_TOTAL
print(f"Total: {total}")
