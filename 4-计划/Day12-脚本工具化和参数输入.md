# Day 12：脚本工具化和参数输入

## 今日目标

让脚本可以复用，而不是每次都改代码。

## 知识点

- 命令行参数
- `argparse` 模块
- 输入文件路径
- 输出文件路径
- 配置项设计
- 使用说明文档

## 常见用法

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()

print(args.input, args.output)
```

## 练习任务

1. 把 Excel 工具改成可以指定输入输出路径。
2. 把文件整理工具改成可以指定文件夹路径。
3. 添加帮助信息。
4. 写一个简单使用说明。

## 任务目标

- 能让同一个脚本处理不同文件
- 能减少手动改代码
- 能写出别人看得懂的使用方法

## 当天交付

- `day12_excel_tool_cli.py`
- `使用说明.txt`

## 接单关联

客户每次给的文件都不一样。工具化后，只要换参数就能复用。
