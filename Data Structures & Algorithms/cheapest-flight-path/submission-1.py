class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        src_dst_map = {} # {0:[1], 1:[2, 3], 2:[3]}
        src_dst_flight_price = {} # {"0_1": 200, "1_2": 100, "1_3": 300, "2_3": 100}

        for flight in flights:
            s = flight[0]
            d = flight[1]
            price = flight[2]

            if not src_dst_map.get(s):
                src_dst_map.update({s:[d]})
            else:
                src_dst_map[s].append(d)

            src_dst_flight_price.update({f"{s}_{d}": price})


        self.cheapest_flight = {}

        def flight_to_dst(start, stops, price):

            # return if stops are exceeding the limit
            if len(stops)-1 > k or (len(stops)-1 == k and start != dst):
                return

            # return if price already greater than whats known
            if self.cheapest_flight.get("price"):
                if price > self.cheapest_flight["price"]:
                    return 

            if start == dst:
                if not self.cheapest_flight:
                    self.cheapest_flight = {"stops": len(stops)-1, "price": price}
                elif (self.cheapest_flight["price"] == price and len(stops)-1 < self.cheapest_flight["stops"]) or price < self.cheapest_flight["price"]:
                    self.cheapest_flight = {"stops": len(stops)-1, "price": price}
                return

            if start not in src_dst_map:
                return

            for dest in src_dst_map[start]:
                # ignore the destination if already crossed in the path
                if dest in stops:
                    continue
                # ignore if flight returning to source
                if dest == src:
                    continue
                new_stops = stops[:] + [start]
                new_price = price + src_dst_flight_price[f"{start}_{dest}"]
                flight_to_dst(dest, new_stops, new_price) # (1, [0], 200), (2, [0, 1], 300), (3, [0, 1], 500)

            return


        flight_to_dst(src, [], 0)

        if not self.cheapest_flight:
            return -1
        else:
            return self.cheapest_flight["price"]

        
        