from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Time Complexity: O(V + E) where V is numCourses and E is the length of prerequisites.
        Space Complexity: O(V + E) to store the adjacency list and in-degrees.
        """
        # Graph representation
        adj = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
            
        # Queue for courses with 0 prerequisites
        q = deque([n for n in indegree if indegree[n] == 0])
        count = 0
        
        while q:
            curr = q.popleft()
            count += 1
            
            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
                    
        return count == numCourses

# Quick test
if __name__ == "__main__":
    sol = Solution()
    assert sol.canFinish(2, [[1,0]]) == True
    assert sol.canFinish(2, [[1,0],[0,1]]) == False
    print("All tests passed.")
