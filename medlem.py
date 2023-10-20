import openpyxl
# load the Excel file
workbook = openpyxl.load_workbook("data.xlsx")

# select the first sheet
sheet = workbook.active

# read the first three columns of the first sheet
data = []
for row in sheet.iter_rows(min_row=1, max_col=3):
    row_data = []
    for cell in row:
        row_data.append(str(cell.value))  # convert cell value to string
    data.append(row_data)

# print the array
for row in data:
    with open("data.txt", "a") as f:
        f.write("<tr>"+'<td class="tal">'+row[0]+"</td>" +'<td class="tal">'+ row[1]+"</td>"+ '<td class="navn">'+row[2]+"</td>"+"\n")  # add a newline character at the end of each row

print(data)
