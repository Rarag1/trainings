N = int(input())
nums = []
elem = 1
sum = 0
for n in range(1,N+1):
    elem = (1+1/n)**n
    sum += elem
    nums.append(elem)
# print(nums)
print(sum)