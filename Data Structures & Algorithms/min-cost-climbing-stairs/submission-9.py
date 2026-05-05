class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        self.min_cost_to_step = {0:0, 1:0}

        def get_cost_to_destination(step):

            if step in self.min_cost_to_step and step > 1:
                return self.min_cost_to_step[step]

            while step < len(cost):
                min_cost = min(cost[step]+get_cost_to_destination(step+1),
                                cost[step]+get_cost_to_destination(step+2))

                if step not in self.min_cost_to_step or self.min_cost_to_step[step] > min_cost:
                    self.min_cost_to_step[step] = min_cost
                return min_cost
                

            return 0

            

        return min(get_cost_to_destination(0), get_cost_to_destination(1))