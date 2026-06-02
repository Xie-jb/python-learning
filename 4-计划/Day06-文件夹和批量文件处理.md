# Day 6：文件夹和批量文件处理

## 今日目标

能遍历文件夹，按规则批量处理文件。

## 知识点

- `os` 模块：系统和文件操作
- `pathlib` 模块：更现代的路径处理方式
- 获取文件夹下的文件
- 判断文件后缀
- 创建文件夹
- 批量重命名文件
- 移动文件

## 常见用法

```python
from pathlib import Path

folder = Path("files")

for file in folder.iterdir():
    if file.suffix == ".jpg":
        print(file.name)
```

## 练习任务

1. 列出某个文件夹下所有文件。
2. 按后缀分类文件，例如图片、文档、表格。
3. 批量给图片加编号。
4. 生成文件清单 TXT 或 Excel。

## 任务目标

- 能安全遍历文件夹
- 能判断不同文件类型
- 能批量重命名文件
- 能整理文件到不同目录

## 当天交付

- `day6_file_rename.py`
- `day6_file_sorter.py`
- 示例文件夹

## 接单关联

常见订单：批量改名、整理图片、按格式分类资料、生成文件目录。
