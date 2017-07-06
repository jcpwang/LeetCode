# Author:   Jerry C. Wang <jcpwang@gmail.com>
# File:     AC_TwoSum.py

class Solution(object):
    def twoSum(self, nums, target):
        process={}
        for index in range(len(nums)):
            if target-nums[index] in process:
                return [process[target-nums[index]],index]
            process[nums[index]]=index

