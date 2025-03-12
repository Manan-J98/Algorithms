class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            
            visited.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            visited.remove(course)
            preMap[course] = [] # don't need to dfs in future
            return True
        
        for course in preMap.keys():
            if not dfs(course): return False
        return True