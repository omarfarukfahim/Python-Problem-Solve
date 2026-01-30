from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        inf = float('inf')
        min_costs = [[inf] * 26 for _ in range(26)]
        
        for i in range(26):
            min_costs[i][i] = 0
            
        for o, c, z in zip(original, changed, cost):
            start = ord(o) - ord('a')
            end = ord(c) - ord('a')
            min_costs[start][end] = min(min_costs[start][end], z)
            
        for k in range(26): 
            for i in range(26): 
                for j in range(26): 
                    min_costs[i][j] = min(
                        min_costs[i][j], 
                        min_costs[i][k] + min_costs[k][j]
                    )
        
        total_cost = 0
        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue
                
            s_idx = ord(s_char) - ord('a')
            t_idx = ord(t_char) - ord('a')
            
            curr_cost = min_costs[s_idx][t_idx]
            
            if curr_cost == inf:
                return -1
            
            total_cost += curr_cost
            
        return total_cost