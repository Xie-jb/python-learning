# Excel读取筛选和保存练习

## 对应文件

- `1-code/demo3.py`
- `1-code/demo4.py`

## 练习目标

这两个文件主要练习用 `openpyxl` 操作 Excel：

- 读取已有 Excel
- 遍历每一行数据
- 筛选出“未付款”的订单
- 把筛选结果保存成新的 Excel 文件

## demo3.py：筛选未付款订单

### `load_workbook()`

用来打开一个已有的 Excel 文件。s

```python
wb = load_workbook(r"C:\...\orders.xlsx")
```

这里的 `r` 是原始字符串，适合写 Windows 文件路径，可以避免 `\` 被当成转义符。

### `wb.active`

获取当前默认工作表。

```python
sheet = wb.active
```

后面读取 Excel 数据时，就是从这个 `sheet` 里面读取。

### `sheet.iter_rows()`

按行读取 Excel 数据。

```python
for row in sheet.iter_rows(min_row=2, values_only=True):
```

- `min_row=2`：从第 2 行开始读，通常是跳过表头。
- `values_only=True`：只读取单元格里的值，不读取单元格对象。
- `row`：每次循环拿到一整行数据。

### 判断是否未付款

```python
for value in row:
    if value == "未付款":
        rowNew.append(row)
        print(row)
```

意思是：遍历这一行的每个值，如果发现有 `"未付款"`，就把整行保存到 `rowNew` 列表里，并打印出来。

## demo4.py：保存筛选结果

`demo4.py` 在筛选未付款订单的基础上，又练习了创建新 Excel 和保存文件。

### `Workbook()`

创建一个新的 Excel 工作簿。

```python
wbNew = Workbook()
```

### `wbNew.active`

获取新 Excel 的默认工作表。

```python
sheet2 = wbNew.active
```

筛选出来的数据会写入这个新工作表。

### `sheet2.append()`

把一整行数据写入 Excel。

```python
sheet2.append(row)
```

这里的 `row` 是原 Excel 中筛选出来的未付款订单。

### `wbNew.save()`

保存新的 Excel 文件。

```python
wbNew.save(r"C:\...\not_pay.xlsx")
```

这句会生成一个新的 Excel 文件，把筛选结果保存进去。

## 核心流程

```python
打开旧 Excel
获取工作表
从第 2 行开始遍历数据
判断这一行是否包含“未付款”
如果包含，就写入新 Excel
保存新 Excel
```

## 小提醒

代码里变量名用了 `str`，虽然可以运行，但不太推荐。因为 `str` 是 Python 自带的类型名，建议改成 `value` 更清楚。
