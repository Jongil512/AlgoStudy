import collections


def solution(cacheSize, cities):
    time = 0

    cache = collections.deque(maxlen=cacheSize)

    for s in cities:
        city = s.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            cache.append(city)
            time += 5

    return time