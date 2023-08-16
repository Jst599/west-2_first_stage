"""
mydict = {12: "jst", 19: "abc"}
for x in mydict:
    if x % 2 == 0:
        mydict = mydict.pop(x)

print(mydict)
"""
#
mydict = {12: "jst", 19: "abc"}
for x in list(mydict):                  # 避免出现遍历字典时修改字典使程序出错的情况
    if x % 2 == 0:
        mydict.pop(x)

print(mydict)