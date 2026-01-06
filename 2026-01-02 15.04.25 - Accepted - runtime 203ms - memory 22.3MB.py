class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True
        
        blocked_set = set(map(tuple, blocked))
        # Max area that can be enclosed by n blocks is n*(n-1)/2
        max_blocked_area = len(blocked) * (len(blocked) - 1) // 2
        
        def bfs(start, end):
            queue = [tuple(start)]
            visited = {tuple(start)}
            
            while queue and len(visited) <= max_blocked_area:
                curr = queue.pop(0)
                
                if curr == tuple(end):
                    return True
                
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = curr[0] + dx, curr[1] + dy
                    
                    if 0 <= nx < 10**6 and 0 <= ny < 10**6:
                        if (nx, ny) not in visited and (nx, ny) not in blocked_set:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
            
            # If we explored more than max_blocked_area, we escaped
            return len(visited) > max_blocked_area
        
        # Check both directions
        return bfs(source, target) and bfs(target, source)