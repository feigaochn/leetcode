class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        import re
        parts = re.findall(r'[A-Z][a-z]*|\d+|\(|\)', formula)
        stack = []
        for p in parts:
            if p.isalpha():
                stack.append((p, 1))
            elif p.isnumeric():
                p = int(p)
                sub, n = stack.pop()
                if type(sub) is not str:
                    for ssub, nn in sub:
                        stack.append((ssub, nn * n * p))
                else:
                    stack.append((sub, p * n))
            elif p == '(':
                stack.append(p)
            elif p == ')':
                sub = []
                while True:
                    tail = stack.pop()
                    if tail == '(':
                        break
                    else:
                        sub.append(tail)
                stack.append((sub[::-1], 1))
        counts = {}
        for k, c in stack:
            counts[k] = c + counts.get(k, 0)
        return ''.join(k + (str(c) if c > 1 else "")
                       for k, c in sorted(counts.items()))


fn = Solution().countOfAtoms
print(fn("H2O"), "?= H2O")
print(fn("H2O12"), "?= H2O12")
print(fn("Mg(OH)2"), "?= H2MgO2")
print(fn("K4(ON(SO3)2)2"), "?= K4N2O14S4")
print(fn("K4(ON(SO3)2)2K4(ON(SO3)2)2"), "?= K8N4O28S8")
