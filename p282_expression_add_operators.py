class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []

        if (len(num) > 2 and num[0] != '0'
                and (int(num) < abs(target) or int(num) == -target)):
            return []

        from collections import defaultdict
        try:
            self.cache[("0", '*')]
        except (AttributeError, KeyError) as e:
            self.cache = {("0", '*'): {0: ["0"]}}

        def valid(s):
            return len(s) == 1 or s[0] != '0'

        def work(num, ops):
            if (num, ops) in self.cache:
                return self.cache[(num, ops)]
            sol = defaultdict(set)
            if valid(num):
                sol[int(num)].add(num)
            for div in range(1, len(num)):
                left, right = num[:div], num[div:]
                if '*' in ops:
                    for lv, le in work(left, '*').items():
                        for rv, re in work(right, '*').items():
                            sol[int(lv) * int(rv)].update(
                                set([l + '*' + r for l in le for r in re]))
                if '+' in ops:
                    for lv, le in work(left, '+-*').items():
                        for rv, re in work(right, '*').items():
                            sol[int(lv) + int(rv)].update(
                                set([l + '+' + r for l in le for r in re]))
                if '-' in ops:
                    for lv, le in work(left, '+-*').items():
                        for rv, re in work(right, '*').items():
                            sol[int(lv) - int(rv)].update(
                                set([l + '-' + r for l in le for r in re]))
            self.cache[(num, ops)] = sol
            return sol

        work(num, "+-*")
        return list(self.cache[(num, "+-*")][target])


def main():
    fn = Solution().addOperators
    print(fn("123", 6))
    print(fn("232", 8))
    print(fn("105", 5))
    print(fn("00", 0))
    print(fn("", 5))
    print(fn("3456237490", 9191))
    print(len(fn("123456789", 45)))  # 121
    print((fn("2147483648", -2147483648)))


if __name__ == '__main__':
    main()
