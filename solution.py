 
from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, managers: List[int], informTime: List[int]) -> int:
        dictionary = defaultdict(lambda: [])

        for i, manager in enumerate(managers):
            if manager != -1:
                dictionary[manager].append(i)
        
        return self.helper(headID, dictionary, informTime)

    def helper(self, headID: int, dictionary, informTime: List[int]) -> int:
        largestInformTime = 0

        for employee in dictionary[headID]:
            if employee in dictionary:
                time = self.helper(employee, dictionary, informTime)
                if largestInformTime < time:
                    largestInformTime = time

        return informTime[headID] + largestInformTime;
