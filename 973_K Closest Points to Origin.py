class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        # solution1: brute force, we use sort and we give the k th pair
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
        """

        # solution 2 : we should use heap as a regular solution
        dis = []
        for point in points:
            heapq.heappush(dis, [point[0] ** 2 + point[1] ** 2, point])

        K_points = []
        while K > 0:
            K_points.append(heapq.heappop(dis)[1])
            K -= 1
        return K_points