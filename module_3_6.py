data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(struct):
    sum = 0
    if isinstance(struct, dict):
        for key, value in struct.items():
            sum += calculate_structure_sum(key)
            sum += calculate_structure_sum(value)
    elif isinstance(struct, (list, tuple, set)):
        for item in struct:
            sum += calculate_structure_sum(item)
    elif isinstance(struct, str):
        sum += len(struct)
    elif isinstance(struct, (int, float)):
        sum += struct
    return sum
result = calculate_structure_sum(data_structure)
print(result)