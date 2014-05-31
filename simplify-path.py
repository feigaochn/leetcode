# author: Fei Gao
#
# Simplify Path
#
# Given an absolute path for a file (Unix-style), simplify it.
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# click to show corner cases.
# Corner Cases:
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".


class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        if len(path) == 0:
            return '/'
        paths = path.split('/')
        # print(paths)
        p_list = []
        for p in paths:
            if len(p) == 0:
                continue
            elif p == '.':
                continue
            elif p == '..':
                if len(p_list) > 0:
                    p_list.pop()
            else:
                p_list.append(p)

        return '/' + '/'.join(p_list)
        pass


def main():
    solver = Solution()
    for path in ["/a/./b/../../c/", "/home/", "/../", "/home//foo/"]:
        print(path + " --> ", solver.simplifyPath(path))
    pass


if __name__ == '__main__':
    main()
    pass
