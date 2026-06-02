# Day 5：Excel自动化基础

## 今日目标

能读取 Excel，筛选数据，生成新的 Excel 文件。

## 知识点

- `openpyxl`：处理 Excel 的常用库
- 打开工作簿：`load_workbook()`
- 获取工作表：`wb.active`
- 遍历行：`iter_rows()`
- 创建新 Excel：`Workbook()`
- 保存文件：`save()`

## 常见用法

```python
from openpyxl import load_workbook, Workbook

wb = load_workbook("orders.xlsx")
sheet = wb.active

for row in sheet.iter_rows(min_row=2, values_only=True):
    print(row)
```

## 练习任务

1. 读取订单 Excel。
2. 统计订单总金额。
3. 筛选“未付款”订单。
4. 把筛选结果保存成新的 Excel。

## 任务目标

- 能读取 Excel 表格
- 能按列获取数据
- 能筛选符合条件的行
- 能生成新的 Excel 文件

## 当天交付

- `day5_excel_read.py`
- `day5_order_filter.py`
- `orders.xlsx`
- `未付款订单.xlsx`

## 接单关联

Excel 自动化是最容易接到的小单之一，例如合并、筛选、统计、生成报表。
