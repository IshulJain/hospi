import xlrd
file_location="college-list.xlsx"
workbook=xlrd.open_workbook(file_location) 
sheet=workbook.sheet_by_index(0)
name=[sheet.cell_value(r,1) for r in range(0,575)]
ids=[sheet.cell_value(r,2) for r in range(0,575)]
ids=map(int, ids)
city=[sheet.cell_value(r,4) for r in range(0,575)]
state=[sheet.cell_value(r,5) for r in range(0,575)]
college_data(name,ids,city,state)