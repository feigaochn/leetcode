"""
Given a list of positive integers, the adjacent integers will perform the
float division. For example, [2,3,4] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change the
priority of operations. You should find out how to add parenthesis to get the
maximum result, and return the corresponding expression in string format. Your
expression should NOT contain redundant parenthesis.
"""


class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        def opt_min(lb, rb):
            if rb - lb == 1:
                return (nums[lb], str(nums[lb]))
            else:
                best_v, best_l, best_r = 10**100, "", ""
                for p in range(lb + 1, rb):
                    v1, s1 = opt_min(lb, p)
                    v2, s2 = opt_max(p, rb)
                    if v1 / v2 < best_v:
                        best_v = v1 / v2
                        best_l, best_r = s1, s2
                return (best_v, best_l + "/" +
                        (best_r
                         if best_r.count('/') == 0 else '(' + best_r + ')'))

        def opt_max(lb, rb):
            if rb - lb == 1:
                return (nums[lb], str(nums[lb]))
            else:
                best_v, best_l, best_r = -10**100, "", ""
                for p in range(lb + 1, rb):
                    v1, s1 = opt_max(lb, p)
                    v2, s2 = opt_min(p, rb)
                    if v1 / v2 > best_v:
                        best_v = v1 / v2
                        best_l, best_r = s1, s2
                return (best_v,
                        best_l + "/" + (
                            best_r if best_r.count('/') == 0
                            else '(' + best_r + ')'))

        return opt_max(0, len(nums))[1]


fn = Solution().optimalDivision

print(fn([1000, 100, 10, 2]))
