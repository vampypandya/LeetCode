class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if(len(costs) == 0):
            return 0
        else:
        
            paint_cost = [[0 for i in range(3)] for _ in range(len(costs))]
            # print paint_cost
            paint_cost[0] = costs[0]

            for house in range(1,len(costs)):
                paint_cost[house][0] = min(paint_cost[house-1][1],paint_cost[house-1][2]) + costs[house][0]
                paint_cost[house][1] = min(paint_cost[house-1][0],paint_cost[house-1][2]) + costs[house][1]
                paint_cost[house][2] = min(paint_cost[house-1][1],paint_cost[house-1][0]) + costs[house][2]
                # print paint_cost

            return min(paint_cost[-1])
            
