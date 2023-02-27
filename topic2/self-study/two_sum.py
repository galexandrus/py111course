from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # answer field
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))
