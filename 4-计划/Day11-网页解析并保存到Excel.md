# Day 11：网页解析并保存到Excel

## 今日目标

能解析公开网页中的列表数据，并保存到 Excel。

## 知识点

- `BeautifulSoup`
- HTML 标签
- `find()`
- `find_all()`
- CSS 选择器基础
- 网页数据保存到 Excel

## 常见用法

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
titles = soup.find_all("h2")

for title in titles:
    print(title.get_text(strip=True))
```

## 练习任务

1. 解析一个公开网页标题。
2. 提取列表页中的名称、链接、价格或日期。
3. 保存到 Excel。
4. 给脚本添加请求失败提示。

## 任务目标

- 能从 HTML 中定位数据
- 能提取文本和链接
- 能保存采集结果
- 知道简单爬虫的边界

## 当天交付

- `day11_web_to_excel.py`
- `网页采集结果.xlsx`

## 接单关联

可以接简单公开网页数据采集单，但要避开登录、验证码、付费内容和违规采集。
