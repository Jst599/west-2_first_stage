
def add(x, y, z, m):
    mylist = [x, y, z, m]
    for n in mylist:
        if type(n) == str:
            mylist.remove(n)
    print(mylist)

add("jst", 3, 2, "abc")








