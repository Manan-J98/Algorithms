class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city = set()
        for path in paths:
            city.add(path[0])
        for path in paths:
            if path[1] not in city:
                return path[1]
        return ""