import gspread

sa = gspread.service_account(filename = "scenic-helper-394306-09cb42f03d0b.json")
#sh = sa.open("chirugss")

#ws = sh.worksheets
#print(ws)

#ws = sh.add_worksheet(title="page3",rows=2,cols=3)

#ws = sh.worksheet("Sheet1")
#print(ws.row_count, ws.col_count)

#print(ws.acell('A2').value)
#print(ws.cell(2,3))
#print(ws.get('A2:C6'))
#print(ws.get_all_records())
#print(ws.get_all_cells())
#print(ws.get_all_values())
#print(ws.update('A2',"kiran"))
#print(ws.update('A2:B3',[["ram",23],["raju",25]]))
#print(ws.update('D2','=UPPER(A2)',raw=False))

#ws.delete_columns(4)
#ws.delete_rows(5)

#------
#sh = sa.open_by_key('1ar47abv_EyB23A-YbzSVajTtSYzOqoes6k0sZekdzhM')
sh = sa.open_by_url('https://docs.google.com/spreadsheets/d/1ar47abv_EyB23A-YbzSVajTtSYzOqoes6k0sZekdzhM/edit?usp=sharing')
ws = sh.sheet1

#res = ws.get_all_records()
#res = ws.get_all_values()
#res = ws.row_values(2)
#res = ws.col_values(1)
#res = ws.get('A2')
#res = ws.get('A2:c3')
#res = ws.insert_row(["jan",28,2008],3)
#res = ws.append_row(["manu",30,2010])
#res = ws.update_cell(2,3,2000)
#print(res)

#-----
#res = ws.range('A2:C3')
#for cell in ws.range('A2:C3'):
#    print(cell.value)
res = ws.update_acell('A3','pavan')
print(res)

