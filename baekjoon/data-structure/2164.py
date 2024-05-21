# 내가 푼 방법
from collections import deque

def find_last_card(N):
    queue = deque(range(1, N+1))

    while len(queue) > 1:
        queue.popleft() 
        queue.append(queue.popleft())
    return queue[0]

N = int(input())
print(find_last_card(N))

# log 함수 이용
import math

def find_last_card(N):
    M = 2 ** math.floor(math.log2(N))
    last_card = 2 * (N - M)
    return last_card if last_card != 0 else N

N=int(input())
print(find_last_card(N))