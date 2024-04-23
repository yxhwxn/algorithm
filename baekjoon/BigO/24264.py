# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }
# 코드1 이 49회 수행되고 알고리즘의 수행 시간이 n2에 비례한다.

n = int(input())
print(n**2)
print(2)