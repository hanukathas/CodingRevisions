import heapq


def max_team_performance(n: int, speed: list, efficiency: list, k: int):
    team = sorted(zip(efficiency, speed), reverse= True) # descending order of speed, ascending order of efficiency
    heap = []
    speed_sum = 0
    max_output = 0
    MOD = 10**9 + 7

    for eff, sp in team:
        heapq.heappush(heap, sp)
        speed_sum += sp

        if len(heap) > k:
            speed_sum -= heapq.heappop(heap)
        max_output  = max(max_output, speed_sum * eff)
    return max_output % MOD

if __name__ == '__main__':
    print(max_team_performance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2))
