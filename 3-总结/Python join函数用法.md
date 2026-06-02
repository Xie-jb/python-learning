# Python join 函数用法

#Python #字符串 #列表 #文件写入

## 1. join 是什么？

`join()` 是字符串的方法，用来把多个字符串连接成一个新的字符串。

基本格式：

```python
"连接符".join(字符串列表)
```

可以理解成：

```python
"用什么连接".join(要连接的内容)
```

## 2. 基本例子

```python
names = ["张三", "李四", "王五"]

result = ",".join(names)
print(result)
```

输出：

```text
张三,李四,王五
```

这里的 `","` 是连接符，表示用英文逗号连接列表中的每个元素。

## 3. 常见连接符

### 用空格连接

```python
words = ["hello", "world"]
result = " ".join(words)
print(result)
```

输出：

```text
hello world
```

### 用逗号连接

```python
items = ["a", "b", "c"]
result = ",".join(items)
print(result)
```

输出：

```text
a,b,c
```

### 不加任何连接符

```python
parts = ["py", "thon"]
result = "".join(parts)
print(result)
```

输出：

```text
python
```

### 每个元素占一行

```python
lines = ["第一行", "第二行", "第三行"]
result = "\n".join(lines)
print(result)
```

输出：

```text
第一行
第二行
第三行
```

## 4. 写入 txt 文件

如果想把列表写入 txt 文件，并且不显示列表元素之间默认的逗号，可以用 `join()`。

```python
lst = ["a,b", "c,d"]

with open("result.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(lst))
```

写入文件后的内容：

```text
a,b c,d
```

注意：这里去掉的是两个列表元素之间的分隔符，元素里面原本的 `,` 会保留。

如果想每个元素写一行：

```python
lst = ["a,b", "c,d"]

with open("result.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lst))
```

写入文件后的内容：

```text
a,b
c,d
```

## 5. join 和 str(list) 的区别

不推荐这样写：

```python
lst = ["a,b", "c,d"]

with open("result.txt", "w", encoding="utf-8") as f:
    f.write(str(lst))
```

写入结果：

```text
['a,b', 'c,d']
```

这样会把列表的中括号、引号、元素之间的逗号都写进去。

推荐这样写：

```python
lst = ["a,b", "c,d"]

with open("result.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(lst))
```

写入结果：

```text
a,b c,d
```

## 6. 注意事项

`join()` 只能连接字符串。

下面这样会报错：

```python
nums = [1, 2, 3]
result = ",".join(nums)
```

因为列表里是数字，不是字符串。

正确写法：

```python
nums = [1, 2, 3]
result = ",".join(map(str, nums))
print(result)
```

输出：

```text
1,2,3
```

## 7. 一句话总结

`join()` 的作用是：用指定的连接符，把多个字符串连接成一个字符串。

记忆公式：

```python
"连接符".join(字符串列表)
```

常用场景：

- 把列表转换成字符串
- 控制元素之间用空格、逗号还是换行连接
- 写入 txt 文件时去掉列表本身的格式
- 保留元素内部的内容，只改变元素之间的连接方式
