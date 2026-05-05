class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        neighbors = {k:0} #store the min_cost to neighbors

        processed_nodes = set()

        def node_neighbors(node):

            if node in processed_nodes:
                return
            else:
                processed_nodes.add(node)

            neighbors_to_process = []

            for time in times:

                if time[0] != node:
                    continue

                dst = time[1]
                cost = time[2]

                cost_from_k = neighbors[node]+cost

                if dst in neighbors and neighbors[dst] > cost_from_k:
                    neighbors[dst] = cost_from_k

                    # re-run compute on the node if the existing value has changed
                    if dst in processed_nodes:
                        processed_nodes.remove(dst)

                elif dst not in neighbors:
                    neighbors.update({dst: cost_from_k})

                # only process the new node if a new shortest path is found
                if neighbors[dst] == cost_from_k:
                    neighbors_to_process.append(dst)

            for node in neighbors_to_process:
                node_neighbors(node)
        
        node_neighbors(k)

        if len(neighbors.keys()) != n:
            return -1

        return max(neighbors.values())

                    
                    
        