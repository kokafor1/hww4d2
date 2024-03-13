# Pair of gloves
# Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of pair of gloves you can constitute from the gloves you have in your drawer.

# Given an array describing the color of each glove, return the number of pairs you can constitute, assuming that only gloves of the same color can form pairs.

# Examples:
# input = ["red", "green", "red", "blue", "blue"]
# result = 2 (1 red pair + 1 blue pair)

# input = ["red", "red", "red", "red", "red", "red"]
# result = 3 (3 red pairs)

def solution(gloves):
    color_counts = {}
    for color in gloves:
        color_counts[color] = color_counts.get(color, 0) + 1
    
    total_pairs = 0
    for count in color_counts.values():
        total_pairs += count // 2
    
    return total_pairs