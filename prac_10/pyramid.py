"""Cp1404 REcursion from scratch
By Greg McLindon
Calculate number of blocks needed to build 2D pyramid for n rows
"""


# def get_blocks(rows):
#     """Calculate blocks needed for pyramid for n rows (loop version)."""
#     count_blocks = 0
#     for x in range(0, rows):
#         count_blocks += rows
#         rows -= 1
#     print(count_blocks)

# get_blocks(4)

def get_blocks(rows):
    """Calculate blocks needed for pyramid for n rows (recursion version)."""
    if rows >= 0:
        return rows + get_blocks(rows-1)
    else:
        return 0

print(get_blocks(4))
