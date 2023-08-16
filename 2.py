a = 1  # 行数
b = 1 #每一行累加数
for a in range(1, 10):
    for b in range(1, a + 1):
        print(f"{a} * {b} = {a * b}\t", end=' ')
        b += 1
    print()
    a += 1