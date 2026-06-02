
## 练习任务

# 1. 列出某个文件夹下所有文件。
# 2. 按后缀分类文件，例如图片、文档、表格。
# 3. 批量给图片加编号。
# 4. 生成文件清单 TXT 或 Excel。

import os
from pathlib import Path
foldPath = Path("./2-file")
os.makedirs("./2-file/txt",exist_ok=True)
os.makedirs("./2-file/xlsx",exist_ok=True)
os.makedirs("./2-file/csv",exist_ok=True)
os.makedirs("./2-file/c",exist_ok=True)
index = 0
for file in foldPath.iterdir():
    if file.suffix == ".c":
        index += 1
        new_name = f"test_{index:03d}{file.suffix}"
        new_path = foldPath / new_name
        file.rename(new_path)
    #print(file)


