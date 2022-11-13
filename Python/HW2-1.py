# num = float(input())
# sum = 0
# num = int(abs(num*10000))
# while num != 0:
#     sum += int(num % 10)
#     num = int(num/10)
# print(sum)

num = input()
sum = 0
for elem in num:
    if elem.isdigit():
        sum += int(elem)
print(sum)