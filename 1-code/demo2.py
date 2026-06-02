#3. 读取 CSV 客户名单，筛选指定城市客户。
#4. 把筛选结果写入新文件。



cityName = input("请输入指定城市，筛选客户：")
writeLine = []
with open("customers.csv","r",encoding="utf-8") as file:
    lineData = file.readlines()
    for data in lineData[1:]:
        dataEdit = data.strip().split(",")
        for city in dataEdit:
            if city == cityName:
                writeLine.append(data)
                #print(dataEdit)
    print(writeLine)
    
    with open("result.csv","w",encoding="utf-8-sig") as wfile:
        wfile.write("".join(writeLine))




