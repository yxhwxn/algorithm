# match case를 이용한 풀이(deque 사용)
# 덱은 스택과 큐를 합친 것 같은 자료 구조로 양 끝에서 자료를 넣고 뺄 수 있다.
import sys
from collections import deque

input = sys.stdin.readline

deque = deque([])

n = int(input())
for _ in range(n):
    order = input().split()
    match (order[0], len(deque) == 0):
        case ("1", _):
            deque.appendleft(int(order[1]))
        case ("2", _):
            deque.append(int(order[1]))
        case ("3", True):
            print(-1)
        case ("3", False):
            print(deque.popleft())
        case ("4", True):
            print(-1)
        case ("4", False):
            print(deque.pop())
        case ("5", _):
            print(len(deque))
        case ("6", True):
            print(1)
        case ("6", False):
            print(0)
        case ("7", True):
            print(-1)
        case ("7", False):
            print(deque[0])
        case ("8", True):
            print(-1)
        case ("8", False):
            print(deque[-1])