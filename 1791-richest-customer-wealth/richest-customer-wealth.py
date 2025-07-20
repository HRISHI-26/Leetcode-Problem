class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = len(accounts)
        n = len(accounts[0])
        rich = 0
        if m >= 1 and n <= 50:
            for i in range(m):
                wealth = []
                sum = 0
                for j in range(n):
                    if accounts[i][j] in range(1, 101):
                        sum += accounts[i][j]
                        wealth.append(sum)
                if sum > rich:
                    rich = sum
        return rich