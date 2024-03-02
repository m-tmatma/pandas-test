import pandas as pd
from io import BytesIO

# DataFrameを作成
df = pd.DataFrame({'A': ['foo', 'bar', 'baz'],
                   'B': ['alpha', 'beta', 'gamma'],
                   'C': [10, 20, 30]})

# BytesIOオブジェクトを作成
output = BytesIO()

# DataFrameをExcel形式のバイナリデータとしてメモリに保存
with pd.ExcelWriter(output, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)

# バイナリデータを取得
excel_data = output.getvalue()

from openpyxl import load_workbook

# BytesIOオブジェクトを再作成
output = BytesIO(excel_data)

# Excelデータを開く
wb = load_workbook(output)

# 最初のワークシートを取得
ws = wb.active

# 各列の幅を調整
for column in ws.columns:
    max_length = 0
    column = [cell for cell in column]
    for cell in column:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(cell.value)
        except:
            pass
    adjusted_width = (max_length + 2)
    ws.column_dimensions[column[0].column_letter].width = adjusted_width

# 変更を保存
wb.save("output.xlsx")
