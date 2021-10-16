#! /usr/bin/python
'''

'''

import collections


class Solution:
    def persistent_companies(self, logs):
        data = collections.defaultdict(list)
        for company, amount, date in logs:
            data[company].append((amount, date))

        out = []
        for company, value in data.items():
            if self.isPersistent(value):
                out.append(company)
        return out

    def isPersistent(self, value):
        if len(value) < 3:
            return False
        for i in range(1, len(value) - 1):
            if value[i-1][0] != value[i][0] or value[i + 1][0] != value[i][0] or value[i+1][1] - value[i][1] != value[i][1] - value[i-1][1]:
                return False
        return True

s = Solution()
data = [("Whole Foods", 48.11, 5), ("Comcast", 89.99, 10), ("Comcast", 89.99, 20), ("Comcast", 89.99, 30),
        ("T-Mobile", 40.00, 45), ("T-Mobile", 40.00, 55), ("T-Mobile", 40.33, 65), ("Jetblue", 20.11, 80),
        ("Jetblue", 20.11, 90), ("Jetblue", 20.11, 95)]

print(s.persistent_companies(data))

