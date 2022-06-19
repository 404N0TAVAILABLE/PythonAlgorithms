### Original code from https://walkccc.me/LeetCode/problems/1048/

from functools import lru_cache

### Returns 4 (ans is initialized to 1 at start)
#words = ["a","b","ba","bca","bda","bdca"]
### Returns 1 (ans is initialized to 1 at start)
#words = ["abcd","dbqca"]
### Returns 5; 4 + 1 (ans is initialized to 1 at start)
words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]

# Approach 1: Top-down
class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        wordSet = set(words)
        print(f'wordset {wordSet}')

        # dp(s) := longest chain where s is the last word
        @lru_cache(None)
        def dp(s: str) -> int:
            ans = 1
            for i in range(len(s)):
                pred = s[:i] + s[i + 1:]
                if pred in wordSet:
                    ans = max(ans, dp(pred) + 1)
            return ans

        return max(dp(word) for word in words)


# Approach 2: Bottom-Up
class Solution2:
    def longestStrChain(self, words: list[str]) -> int:
        # dictionary to contain numbers & words (key)
        dp = {}

        # key = len - sorts by length only
        for word in sorted( words, key = len ):
            # dp.get(key, default_value if nothing is returned)
            dp[word] = max( dp.get(word[:i] + word[i + 1:], 0) +
                    1 for i in range(len(word)))

        return max(dp.values())
    

res = Solution()
#res = Solution2()

print(res.longestStrChain(words))



