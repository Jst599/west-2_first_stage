my_str = "地球ol"
if my_str.count("ol") > 0:
    my_str = my_str.replace("ol", "fzu")
    my_str = my_str[:: -1]
    print(my_str)

