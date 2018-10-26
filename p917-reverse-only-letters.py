class Solution:
    def reverseOnlyLetters(self, ss):
        """
        :type ss: str
        :rtype: str
        """
        from string import ascii_letters
        ss = list(ss)
        i = 0
        j = len(ss) - 1
        while i <= j:
            while i < j and ss[i] not in ascii_letters:
                i += 1
            while i < j and ss[j] not in ascii_letters:
                j -= 1
            if i >= j:
                break
            ss[i], ss[j] = ss[j], ss[i]
            i += 1
            j -= 1
        return ''.join(ss)
        
        
        