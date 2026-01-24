class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Base case for n = 1
        # a: Number of ways to paint a row with 3 different colors (e.g., 123)
        # b: Number of ways to paint a row with 2 different colors (e.g., 121)
        a, b = 6, 6
        
        # Iterate from row 2 up to row n
        for _ in range(n - 1):
            # Calculate new counts based on the transition logic derived above
            # We use temporary variables or tuple unpacking to update simultaneously
            new_a = (2 * a + 2 * b) % MOD
            new_b = (2 * a + 3 * b) % MOD
            
            a, b = new_a, new_b
        
        # The result is the sum of both pattern types for the final row
        return (a + b) % MOD