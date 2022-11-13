list1 = list(map(int, input().split(" ")))
for i in range(len(list1)):
    if list1[i]%2 == 0 and i > 0:
        list1[i], list1[i-1] = list1[i-1], list1[i]
    elif list1[i]%2 != 0 and i < len(list1) - 1:
        list1[i+1], list1[i] = list1[i], list1[i+1]
# print(list1)
for num in list1:
    print(num, end=" ")