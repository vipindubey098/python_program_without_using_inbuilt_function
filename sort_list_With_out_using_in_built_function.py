my_list = [20, -15, -26, 15, 1, 23, -64, 23, 76]
len_my_list = len(my_list)
for i in range(len_my_list):
    for j in range(i+1, len_my_list):
        if my_list[i] > my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]
print(my_list)
