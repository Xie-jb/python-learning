# Day 10：网页数据获取基础

## 今日目标

理解网页请求，能获取公开网页或公开 JSON 数据。

## 知识点

- HTTP 基础概念
- `requests`：发送网页请求
- 状态码：例如 `200` 表示成功
- 请求头 `headers`
- 保存网页 HTML
- JSON 数据读取

## 常见用法

```python
import requests

url = "https://example.com"
res = requests.get(url)
print(res.status_code)
print(res.text)
```

## 练习任务

1. 请求一个公开网页。
2. 保存网页 HTML 到本地。
3. 请求一个公开 JSON 接口。
4. 读取 JSON 中的字段并保存。

## 任务目标

- 能发起基础网页请求
- 能判断请求是否成功
- 能保存网页内容
- 能读取简单 JSON 数据

## 当天交付

- `day10_web_request.py`
- `day10_json_reader.py`
- 保存下来的 HTML 或 JSON 文件

## 接单关联

为简单爬虫打基础，例如采集公开商品标题、公告、列表数据。
