n = int(input())

if n % 5 == 0:  # 5로
    print(n // 5)
else:
    p = 0
    while n > 0:
        n -= 3
        p += 1
        if n % 5 == 0:  # 3kg & 5kg
            p += n // 5
            print(p)
            break
        elif n == 1 or n == 2:  # 설탕 봉지만으로 나눌 수 없을 때
            print(-1)
            break
        elif n == 0:  # 3으로
            print(p)
            break