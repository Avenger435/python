from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target-num
            if complement in num_dict:
                # print(num_dict)
                return [num_dict[complement], i]
            num_dict[num] = i
        return []

    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSumTwoPointer(self, nums: List[int], target: int) -> List[int]:
        # This method assumes that the input list is sorted.
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return [left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(result)  # Output: [0, 1]
    result_brute_force = solution.twoSumBruteForce(nums, target)
    print(result_brute_force)  # Output: [0, 1]
    result_two_pointer = solution.twoSumTwoPointer(sorted(nums), target)
    print(result_two_pointer)  # Output: [2, 3]
