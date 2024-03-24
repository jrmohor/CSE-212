def multiples_of(starting_number, num_of_multiples):
    return [starting_number * i for i in range(1, num_of_multiples + 1)]

# Example usage:
result = multiples_of(3, 5)
print(result)


