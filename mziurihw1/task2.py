def num_sum(num):
    nums_sum = 0
    str_num = str(num)
    for i in range(len(str_num)):
        nums_sum += int(str_num[i])
    return nums_sum


print(num_sum(121))
print(num_sum(12345))
