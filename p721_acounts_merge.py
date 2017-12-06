#!/usr/bin/env python
# coding: utf-8

"""
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
"""


class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        adjacent = defaultdict(set)

        for uid, (name, *emails) in enumerate(accounts):
            for email in emails:
                adjacent[uid].add(email)
                adjacent[email].add(uid)
        # print(adjacent)
        seen = set()
        merged = []
        for uid in range(len(accounts)):
            if uid in seen:
                pass
            else:
                group = {uid}
                front = {uid}
                while front:
                    emails = set()
                    for name in front:
                        emails |= adjacent[name]
                    group |= front
                    front = set()
                    for email in emails:
                        front |= adjacent[email]
                    # print(uid,  front, emails, group)
                    front -= group
                merged.append(group)
                seen |= group
        output = []
        for uids in merged:  # type: set
            emails = set()
            for uid in uids:
                emails |= adjacent[uid]
            output.append([accounts[uids.pop()][0]] + sorted(list(emails)))
        return output


if __name__ == '__main__':
    sol = Solution().accountsMerge
    print(sol([["John", "johnsmith@mail.com", "john00@mail.com"],
               ["John", "johnnybravo@mail.com"],
               ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
               ["Mary", "mary@mail.com"]]))
