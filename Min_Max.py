def max_val(current_level, node_index, seq, total_level):
    if current_level == total_level:
        return seq[node_index]
    else:
        return max(min_val(current_level + 1, node_index * 2 + 1, seq, total_level),
                   min_val(current_level + 1, node_index * 2 + 2, seq, total_level))

def min_val(current_level, node_index, seq, total_level):
    if current_level == total_level:
        return seq[node_index]
    else:
        return min(max_val(current_level + 1, node_index * 2 + 1, seq, total_level),
                   max_val(current_level + 1, node_index * 2 + 2, seq, total_level))

def tree():
    seq = []
    total = 2 ** 3 - 1
    count = 0
    seq.append(5)
    while count < total:
        seq.append(2 * seq[count] + 2)
        seq.append(2 * seq[count] + 3)
        count += 1
    return seq

seq = [54, 55, 56, 57, 58, 59, 60, 61]

print(seq)

total_levels = 3
result = max_val(0, 0, seq, total_levels - 1)  # Call max_val for the root node
print("Result:", result)
result = min_val(0, 0, seq, total_levels - 1)  # Call max_val for the root node
print("Result:", result)
