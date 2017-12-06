# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: maximum product of word lengths
#
#     Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters.
#     You may assume that each word will contain only lower case letters.
#     If no such two words exist, return 0.
# 
# Example 1:
# 
#     Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
#     Return 16
#     The two words can be "abcw", "xtfn".
# 
# Example 2:
# 
#     Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
#     Return 4
#     The two words can be "ab", "cd".
# 
# Example 3:
# 
#     Given ["a", "aa", "aaa", "aaaa"]
#     Return 0
#     No such pair of words.    
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Bit Manipulation

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # word -> (bitmap, len)
        ws = [(sum(2 ** (ord(x) - ord('a')) for x in set(w)), len(w)) for w in words]
        ws.sort(key=lambda w: w[1], reverse=True)
        r = 0
        for iw, w in enumerate(ws):
            if w[1] ** 2 <= r:
                break
            for x in ws[iw + 1:]:
                if w[1] * x[1] <= r:
                    break
                if w[0] & x[0] == 0:
                    r = max(r, x[1] * w[1])
        return r


def main():
    solver = Solution()
    tests = [
        ((["abcw", "baz", "foo", "bar", "xtfn", "abcdef"],), 16),
        ((["a", "ab", "abc", "d", "cd", "bcd", "abcd"],), 4),
        ((["a", "aa", "aaa", "aaaa"],), 0),
        ((["fdeeaedbebc", "edfd", "beecbafddbccffad", "ccddfdbefadacbbe", "acbaba", "beaaea", "aadfcffd", "cbaedeaadf",
           "daffafacfcbcdbb", "ecaeacde", "addaeddccbbdaeeabd", "aacabefe", "bcacccfdeafaebd", "ccdcbabafccbceefcbea",
           "abdcebfddec", "feeeebdffcdfadd", "cdcfbefdefabfadeb", "faabcab", "fbababbfebfa", "baeb",
           "efaaaeffcbeddcbcf", "accadbadaa", "eefccbacbebfccafedccb", "dffceebdee", "ebcadbbbcbfeaadbbd",
           "feceadaacefdedfdddec", "cdacdfbcdbbbfabaabaeb", "eadfcfcedddaafecba", "acd", "ddebfbcacefacafddcfa",
           "dfbdac", "bc", "eccbadcabcdebcfec", "bcddbbfdcadf", "eccaea", "cdcfdbdaacfbeaaab", "edbadadbecaafcaebac",
           "be", "ef", "bdddc", "dcbfbfd", "dfdcdfcfedcabecddeef", "faaababebf", "daffbefabbdbd",
           "bfafcccdfbbddedeecbad", "baea", "baafbdedefeadafe", "afb", "ebe", "debcdcfcbecf", "bccfd",
           "dfeebdcbecaabdf", "edaccaebaedebf", "ddbcecedbdeaffcd", "aefbdfcdcbaceaaadbbd", "fefadebacbdafaba",
           "aeedfecaaafddb", "dfabdacfabceedffac", "fedd", "edaf", "eadceaadcdebbbff", "befadddcadeedceffacd",
           "fcabfacaafeedd", "fabcdaebcffeabdbaaccb", "ecefeeceaf", "ebafcbabebadb", "defeafa", "dfddcceadfdcffede",
           "aaeafeaeebbebcef", "edfbaddeabbbc", "bcdcdcaf", "fceffbabfc", "efedeeab", "beedeadcbebdeafc", "ebfecbabaec",
           "feb", "fcafcfd", "eecffceabffcccfcc", "eaccadfdcfeeade", "dbecabfbdddab", "aaaeedeeadcefcba", "ecafe",
           "dcccdee", "cffadcaecdaaeadcd", "bfbabbfdeed", "eaeeffadeeecdcfddfba", "cebfcefdfdcfdadcbbf", "fabdeefdada",
           "aaceaffaaace", "bfeccfbacfcbbbcbcdf", "befcbafbadfaebaaded", "deccccbebd", "edfdcecaebfeaebbdaeab",
           "dcaddc", "eabdaeaafcacdaec", "afcdadccbeffebbe", "aeeaefeeedfaeabbaca", "caeaddeaafdc", "cbeeeeaadbbaeeecf",
           "cfbdebcac", "bafedbedebfafaaaea", "afcedecccddbeafcddcbc", "ebbfabfccbbafef", "beffbcf", "dbcaebfaadbfbbea",
           "ffcafbd", "effdfbaf", "dffeeeecaccbdca", "ccfbeeecadffcdeea", "deafdebedefbfafead", "acccbefeafafb",
           "acaedbbfbfc", "cbefadddcadbabcdf", "daaeecaeedefc", "fcbfddabcadc", "ffddcceaceabcbfcc", "facd", "bccdfa",
           "caddabecabaadeeacc", "caddfdefaabbeaccbfda", "ecceedc", "bcbaceafebbcfee", "adcdbaeaa", "afccf",
           "cfdcdbcfedaacdbaeb", "bdfeccc", "babcaddacbe", "dfbcbcb", "ec", "ed", "dcadaeebdec", "daefafdbad",
           "deadaacadacab", "babaeabfaec", "faeaac", "ddecccdcbecfdedb", "fc", "fdfda", "dceaaaafeecafeededfb",
           "bfaefab", "dfacbbefbabaf", "ceabbdb", "ccabeafccaf", "fcfadbfdeac", "bdfaacdabfabebee", "dcdd",
           "cceabceabbefdaaaeedb", "fedbcffedbbcaeeb", "fadbdeddcfcefdbdba", "dbbdacdcdcdfdc", "eacdf",
           "ffcddcefbbcadfed", "eddebebedbbabcbb", "afbcafaaffcebefafe", "eadbcaeeadadc", "dafcfbefdabfbaadaa",
           "aaffafefbe", "abcdfda", "ffddecfff", "abeeafebdb", "fcddffbaaccfbec", "feeaaacdfe", "dfeeefeacbbafed",
           "dcfaaaaafedefb", "feccfddbafbfadcfcb", "eedefebc", "efffcceefbeeaeccacfc", "ddaafafedacbfc",
           "eadbeeeffdcaf", "dfefb", "aadcaba", "ba", "bfbbbcbfbdbda", "edcfd", "dddadddcfa", "defbecfbe",
           "afbdccdfeabcaeeecb", "fbdfee", "aabcfbeeebdcccdba", "ffafdbaffccb", "cdaebb", "eeadfdadcf",
           "adcfaeccaafdeeecfd", "afe", "bdbccfe", "daaaebcfcaadd", "abffbbcfbddbbffcbebfa", "ebfccaeefaacdeaece",
           "feeb", "eddbfefdaefeea", "dadafadecac", "fbfeefbdfb", "fbcc", "eeebd", "adedeebafabdcbaebc", "cc",
           "dffddbdf", "cfebadbadffceca", "cbaefcbeddddfaabaefae", "eaecbcbebaaebe", "bdabafabbabdafaacd",
           "feebefebbaeccafafedc", "cdcfbcbaf", "faafccafdcafeadf", "ecdcede", "fdafceadacff", "aafdffbcffcfa",
           "eefcfebadcecadcc", "adebefcdaefbbeaeabff", "cfcceadbdeadcababea", "beca", "bdbbcffcdceadcfefba"],), None)
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.maxProduct(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
