class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        layers = len(wall)
        width = sum(wall[0])
        brick_hash = defaultdict(int)
        for layer in wall:
            sum_bricks = 0
            for brick in layer:
                sum_bricks += brick
                if sum_bricks < width:
                    brick_hash[sum_bricks] += 1
        max_edges = 0
        for hash in brick_hash:
            max_edges = max(max_edges, brick_hash[hash])
        return layers - max_edges
        