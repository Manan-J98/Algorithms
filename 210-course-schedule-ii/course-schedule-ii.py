class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)

        visited, cycle = set(), set()
        output = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for crs in preMap[course]:
                if not dfs(crs):
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return output