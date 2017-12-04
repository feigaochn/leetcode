class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        bits = reversed(bits)
        zeros = ones = 0
        for bit in bits:
            if ones > 0 and bit == 0:
                break
            elif bit == 0:
                zeros += 1
            elif bit == 1:
                ones += 1
        if zeros >= 2:
            # if more than two 0 at last, must be 1-bit char
            return True
        if zeros == 0:
            # if no last zeros, must be 2-bit char 11
            return False
        # case: 1..10
        if ones % 2 == 0:
            return True
        else:
            return False


def main():
    sol = Solution().isOneBitCharacter
    print(sol([1, 0, 0]))
    print(sol([1, 1, 1, 0]))
    print(sol([1, 1, 1, 1, 0]))
    print(sol([]))


if __name__ == '__main__':
    main()
