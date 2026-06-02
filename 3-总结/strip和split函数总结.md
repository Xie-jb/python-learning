# strip 和 split 速览

## strip()

作用：去掉字符串两边的空格、换行符 `\n`、制表符 `\t`。

常用场景：读取文件的一行后，去掉末尾换行。

```python
line = "张三,北京,13800138000\n"
line = line.strip()
print(line)
```

结果：

```python
张三,北京,13800138000
```

记住：`strip()` 只清理两边，不清理中间。

## split()

作用：按指定符号切割字符串，返回列表。

按逗号切割：

```python
line = "张三,北京,13800138000"
data = line.split(",")
print(data)
```

结果：

```python
['张三', '北京', '13800138000']
```

取数据：

```python
name = data[0]
city = data[1]
phone = data[2]
```

## 最常用组合

读取 CSV 或逗号分隔文本时，常用：

```python
data = line.strip().split(",")
```

含义：

```text
strip()       先去掉换行
split(",")   再按逗号切成列表
```

## 易错点

```python
data = "C001,张三,北京,13800138000"
print(data[3])
```

这里的 `data[3]` 是第 4 个字符，不是第 4 列。

正确写法：

```python
row = data.split(",")
print(row[3])
```

## 一句话记忆

`strip()`：清理一行。

`split(",")`：拆成多列。

`line.strip().split(",")`：文件读取里最常用。
