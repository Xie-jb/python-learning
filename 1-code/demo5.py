
## 练习任务

# 1. 列出某个文件夹下所有文件。
# 2. 按后缀分类文件，例如图片、文档、表格。
# 3. 批量给图片加编号。
# 4. 生成文件清单 TXT 或 Excel。

import os
import shutil
from pathlib import Path
from openpyxl import load_workbook, Workbook
rPath = Path(__file__).resolve().parent.parent / "2-file"

Path(rPath / "txt").mkdir(exist_ok=True)
Path(rPath / "xlsx").mkdir(exist_ok=True)
Path(rPath / "csv").mkdir(exist_ok=True)
Path(rPath / "c").mkdir(exist_ok=True)

c_path = rPath / "c"
index = 0
# for file in rPath.iterdir():
#     if file.suffix == ".c":
#         index += 1
#         new_name = f"test_{index:03d}{file.suffix}"
#         new_path = rPath / new_name
#         file.rename(new_path)
#         shutil.move(file, c_path)
#     elif file.suffix.lower() == ".txt":
#         suffix = file.suffix.lstrip(".").lower()
#         new_path = rPath / suffix
#         #print(new_path)
#         shutil.move(file,new_path)
#     elif file.suffix.lower() == ".xlsx":
#         suffix = file.suffix.lstrip(".").lower()
#         new_path = rPath / suffix
#         #print(new_path)
#         shutil.move(file,new_path)
#     elif file.suffix.lower() == ".csv":
#         suffix = file.suffix.lstrip(".").lower()
#         new_path = rPath / suffix
#         #print(new_path)
#         shutil.move(file,new_path)
wb = Workbook()
fileNum = wb.active
for file in rPath.iterdir():
    if not file.is_file():
        fpath = rPath / file
        for fileData in fpath.iterdir():
            fileNum.append([fileData.name,str(fileData)])
    else:
        fileNum.append([file.name,str(file)])
wb.save(rPath / "fileTotal.xlsx")




