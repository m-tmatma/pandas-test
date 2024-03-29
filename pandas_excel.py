'''
save dataframe to excel file with adjusted column width
'''
from io import BytesIO
import pandas as pd
from openpyxl import load_workbook

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

# BytesIOオブジェクトを再作成
output = BytesIO(excel_data)

# Excelデータを開く
wb = load_workbook(output)

# 最初のワークシートを取得
ws = wb.active

# 各列の幅を調整
for column in ws.columns:
    max_length = 0
    for cell in column:
        max_length = max(max_length, len(str(cell.value)))
    adjusted_width = max_length + 2
    ws.column_dimensions[column[0].column_letter].width = adjusted_width

# 変更を保存
wb.save("output.xlsx")
