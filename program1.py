class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        m, n = len(message), len(pattern)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # Handle patterns starting with *
        for j in range(1, n + 1):
            if pattern[j-1] == '*':
                dp[0][j] = dp[0][j-1]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if pattern[j-1] == '*':
                    # * can match current char and continue, or skip current char
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif pattern[j-1] == '?' or pattern[j-1] == message[i-1]:
                    # ? matches any single char, or chars match exactly
                    dp[i][j] = dp[i-1][j-1]
                
        return dp[m][n]