import xlrd

wb=xlrd.open_workbook("D:\mjunittest1\Testdata\Testdata.xlsx")
sheet1=wb.sheet_by_name("Userdata")
sheet2=wb.sheet_by_name("UserNegativeData")

def getUserData():
    entirelist=[]
    for i in range(1,sheet1.nrows):
        data=[]
        for j in range(0,sheet1.ncols):
            data.append(sheet1.cell_value(i,j))

        entirelist.append(data)

    return entirelist

def getUserNegativeData():
    entirelist1=[]
    for i in range(1,sheet2.nrows):
        data=[]
        for j in range(0,sheet2.ncols):
            data.append(sheet2.cell_value(i,j))

        entirelist1.append(data)

    return entirelist1

'''x=getUserData()
print(x)
y=getUserNegativeData()
print(y)
'''