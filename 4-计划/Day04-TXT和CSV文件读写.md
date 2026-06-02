# Day 4：TXT和CSV文件读写

## 今日目标

能读取和写入文本文件、CSV 文件，开始处理真实文件数据。

## 知识点

- `open()`：打开文件
- `read()`：读取全部内容
- `readlines()`：按行读取
- `write()`：写入文件
- `with open(...) as f`：自动关闭文件
- `csv` 模块：读写 CSV 表格数据
- 编码：优先使用 `encoding="utf-8"`

## 常见用法

```python
with open("students.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("result.txt", "w", encoding="utf-8") as f:
    f.write("处理完成")
```

## 练习任务

1. 读取一个 TXT 文件，统计有多少行。
2. 从 TXT 中筛选包含手机号的行。
3. 读取 CSV 客户名单，筛选指定城市客户。
4. 把筛选结果写入新文件。

## 任务目标

- 能打开和保存文件
- 能按行处理文本
- 能读写简单 CSV
- 能把处理结果保存成文件

## 当天交付

- `day4_txt_reader.py`
- `day4_csv_filter.py`
- 示例输入文件和输出文件

## 接单关联

常见订单：整理名单、筛选客户、清洗文本、转换文件格式。
