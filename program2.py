def decode_message( s: str, p: str) -> bool:

# write your code here
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True
        
        for i in range(1, len(p) + 1):
                if p[i - 1] == '*':
                        dp[i][0] = dp[i - 1][0]
                else:
                        break
        
        for i in range(1, len(p) + 1):
                for j in range(1, len(s) + 1):
                        if p[i - 1] == s[j - 1] or p[i - 1] == '?':
                                dp[i][j] = dp[i - 1][j - 1]
                        elif p[i - 1] == '*':
                                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        
        return dp[len(p)][len(s)]
        return False