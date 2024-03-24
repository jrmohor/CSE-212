def next_greater_element(nums):
    result = [-1] * len(nums)
    stack = []

    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)

    return result

# Example Usage:
print(next_greater_element([4, 5, 2, 10, 8]))  # Output: [5, 10, 10, -1, -1]