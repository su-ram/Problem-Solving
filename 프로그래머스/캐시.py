import heapq


def solution(cacheSize, cities):
    answer = 0
    cache = {}
    hit = 1
    miss = 5

    for time, city in enumerate(cities):
        city = city.lower()
        print(cache)
        if cache.get(city) is not None:
            answer += hit
            cache[city][0] = time
            continue

        elif len(cache) == cacheSize:
            if cacheSize == 0:
                answer += miss
                continue
            print(list(cache.values()))
            removed = heapq.heappop(list(cache.values()))
            cache.pop(removed[-1])

        cache[city] = [time, city]
        answer += miss

    return answer

c = 5
city =["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]






print(solution(c,city))


