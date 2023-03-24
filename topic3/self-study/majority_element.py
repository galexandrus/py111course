from typing import List


def majority_element(nums: List[int]) -> int:
    # answer field

    if not nums:
        return None

    min_val = nums[0]
    max_val = nums[-1]
    for value in nums:
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value
    keys = [i for i in range(min_val, max_val + 1)]

    count_dict = {key: 0 for key in keys}
    for value in nums:
        count_dict[value] += 1

    n = len(nums) / 2
    for key in count_dict:
        if count_dict[key] > n:
            return key

    return None


if __name__ == '__main__':
    seq = [3, 2, 3]
    print(majority_element(seq))
