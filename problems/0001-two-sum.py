#!/usr/bin/env python
# -- coding: utf-8 --
"""
@AUTHOR : zlikun <zlikun-dev@hotmail.com>
@DATE   : 2019/02/28 11:24:53
@DESC   : 两数之和
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        一次哈希迭代实现需求
        :param nums:
        :param target:
        :return:
        """
        dic = {}
        for i, m in enumerate(nums):
            # m + n = target
            if (target - m) in dic:
                return i, dic[target - m]
            else:
                dic[m] = i


if __name__ == '__main__':
    """
    Python3：    耗时56ms，内存14.2MB
    GoLang：     耗时08ms，内存03.7MB
    
    相同算法，Python3性能差GoLang很多!!
    """
    nums = [12, 15, 18, 12]
    target = 30
    r = Solution().twoSum(nums, target)
    assert sum(map(lambda x: nums[x], r)) == target
