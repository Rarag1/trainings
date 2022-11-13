N = int(input())
nums = range(-N,N+1)
ind = list(map(int, input().split(" ")))
prod =1
for i in ind:
    prod *= nums[i]
print(prod)