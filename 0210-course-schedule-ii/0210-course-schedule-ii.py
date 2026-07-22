class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order=[]
        g = defaultdict(list)
        for a,b in prerequisites:
            g[a].append(b)
        unvisited, visiting, visited = 0, 1, 2
        states = [unvisited] * numCourses
        def dfs(node):
            if states[node] == visited:
                return True
            if states[node] == visiting:
                return False
            states[node] = visiting
            for nei in g[node]:
                if not dfs(nei):
                    return  False
            states[node] = visited
            order.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return[]
        return order

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna