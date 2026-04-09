class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(pos, (target - pos) / spd) for pos, spd in zip(position, speed)]
        pairs.sort(reverse=True)

        fleet = 0
        cur_time = 0

        for pos, time in pairs:
            if time > cur_time:
                fleet += 1
                cur_time = time
        return fleet