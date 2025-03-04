# nums = ["4", "23", "15", "8"]
# max_num = max(map(int, nums))
# print(str(max_num))

# max_num = max([int(num) for num in nums])
# print(str(max_num))

# max_num = max(nums, key=lambda num: int(num))
# print(max_num)

# max_num = list(map(int, nums))
# print(max_num)

nums = [1, 2, 5, 6]
step = [2, 3, 4, 5]
new = list(map(lambda x, y: x **y, nums, step))
print(new)