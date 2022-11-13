N = int(input())
nums = []
elem = 1
for i in range(1,N+1):
    elem *= i
    nums.append(elem)
for num in nums:
    print(num, end=" ")