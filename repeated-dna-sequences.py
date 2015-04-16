#!/bin/env python3

# author: Fei Gao
#
# Repeated Dna Sequences
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
# For example,
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
# Show Tags


class Solution:
    # @param s, a string
    # @return a string[]
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []
        from collections import Counter
        counter = Counter(s[i:i+10] for i in range(len(s)-10+1))
        dna = list()
        for subs, rept in counter.items():
            if rept > 1:
                dna.append(subs)
        return dna



def main():
    solver = Solution()
    tests = ["AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", '', 'AAAAAAAAAAA']
    for test in tests:
        print(test)
        print(' ->')
        result = solver.findRepeatedDnaSequences(test)
        print(result)
        print('~'*10)
    pass
if __name__ == '__main__':
    main()
    pass
