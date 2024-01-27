def max_subarray_sum(nums):
    if not nums:
        return 0, []

    max_sum = current_sum = nums[0]
    start_index = end_index = 0
    current_start = 0

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            current_start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = current_start
            end_index = i

    return max_sum, nums[start_index:end_index + 1]

# Take user input for a list of integers
user_input = input("Enter a list of integers separated by spaces: ")
nums = list(map(int, user_input.split()))

# Calculate the result
max_sum, subarray = max_subarray_sum(nums)

# Print the result in the desired format
print(f"{max_sum} -> {subarray}")

