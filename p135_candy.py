class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if ratings is None:
            return 0
        n = len(ratings)
        l = [0] * n
        r = [0] * n
        c = [0] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                l[i] = l[i-1] + 1
            else:
                l[i] = 0
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                r[i] = r[i+1] + 1
            else:
                r[i] = 0
        result = 0
        for i in range(n):
            c[i] = 1 + max(l[i], r[i])
            result += c[i]
        # print(l)
        # print(r)
        # print(c)
        return result


def test():
    import random
    lst = [random.randrange(10) for _ in range(10)]
    print(lst)
    print(Solution().candy(lst))

if __name__ == '__main__':
    test();