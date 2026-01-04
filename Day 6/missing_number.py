# def missing_bumber_list(nums):
#     expected_sum = 0
#     actual_sum = 0
#     for i in range(1, len(nums) + 2):
#         expected_sum += i
#     for num in nums:
#         actual_sum += num
#     return expected_sum - actual_sum
# print(missing_bumber_list([1, 2, 4, 5, 6]))
#

def mising_number(nums):
    for i in range(1,max(nums)+1):
        if i not in nums:
            return i

print(mising_number([1,2,3,5,6,7,8,9]))

