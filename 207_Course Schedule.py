class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # TC: O(n^2), SC:O(n)
        graph = collections.defaultdict(list)
        for i, j in prerequisites:
            graph[i].append(j)
        visited = [0] * numCourses  # if not marked, defualt is 0

        for i in range(numCourses):
            if self.dfs(graph, visited, i):  # check cycle, if cycle
                return False
        return True

    def dfs(self, graph, visited, i):  # check cycle
        if visited[i] == 1:
            return True
        if visited[i] == 2:
            return False
        visited[i] = 1
        for j in graph[i]:
            if self.dfs(graph, visited, j):
                return True
        visited[i] = 2
        return False
