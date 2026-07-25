class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[pre].append(course)  # b -> a (pre -> course)
            
        # 0: unvisited, 1: visiting, 2: visited
        state = [0] * numCourses
        
        def has_cycle(course):
            state[course] = 1 # visiting
            for neighbor in graph[course]:
                if state[neighbor] == 1:
                    return True
                if state[neighbor] == 0:
                    if has_cycle(neighbor):
                        return True
            state[course] = 2 # visited
            return False
        
        for i in range(numCourses):
            if state[i] == 0:
                if has_cycle(i):
                    return False
        return True
