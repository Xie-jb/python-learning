#1. 读取一个 TXT 文件，统计有多少行。
#2. 从 TXT 中筛选包含手机号的行。

num = 0
with open("customers.csv","r",encoding="utf-8") as file:
    line = file.readlines()
    for data in line[1:]:
        row = data.strip().split(",")
        if row[3] != "":
            print(data)
            num += 1
    print(num)


