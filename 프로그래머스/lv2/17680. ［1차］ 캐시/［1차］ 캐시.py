from collections import deque


def solution(cacheSize, cities):
    answer = 0
    buffer = deque()

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()

        if city in buffer:
            answer += 1
            buffer.remove(city)

        else:
            answer += 5

        buffer.append(city)

        if len(buffer) > cacheSize:
            buffer.popleft()

    return answer