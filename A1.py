from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_abs_sum = 0
        min_abs_val = float('inf')
        negative_count = 0
        
        # Traverse every number in the matrix
        for row in matrix:
            for val in row:
                # 1. Add absolute value to total
                abs_val = abs(val)
                total_abs_sum += abs_val
                
                # 2. Count negatives
                if val < 0:
                    negative_count += 1
                
                # 3. Track the smallest absolute value found so far
                if abs_val < min_abs_val:
                    min_abs_val = abs_val
        
        # If we have an even number of negatives, we can make them ALL positive.
        if negative_count % 2 == 0:
            return total_abs_sum
        
        # If odd, one number must remain negative.
        # We subtract 2 * min_abs_val because we added it as positive initially.
        # (Total - min) removes the positive version.
        # (Total - min - min) effectively adds the negative version.
        else:
            return total_abs_sum - (2 * min_abs_val)