
from openpyxl import Workbook 


wb = Workbook()
ws = wb.active

ws.title = "Interface_DUT_Data"

ws.append(["Interface","Master/Slave","ClockCycles"])

data = [
    ('APB','Master',100),
    ('AHB','Slave',200),
    ('USB','Master',300),
    ('AXI','Master',400)
]

for row in data:
    ws.append(row)

wb.save("interface_data.xlsx")

