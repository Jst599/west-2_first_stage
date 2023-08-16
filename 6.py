
my_list = ["apple", "banana", "orange"]

# 使用循环将列表返回为字典
my_dict = {}
for i in range(len(my_list)):
    my_dict[i] = my_list[i]  # 将列表的值取出

print(my_dict)