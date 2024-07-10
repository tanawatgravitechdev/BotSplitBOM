import xlsxwriter

workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()


f = open('./BOM.txt', 'r+')
listTmp = f.read().split('\n')
key = 0
while key < len(listTmp):
    item = listTmp[key]
    if(item.replace(' ','') != ""):
        lt = [v for v in item.split('  ') if v != '']
        i = 0
        for x in lt:
            worksheet.write(key+1, i, x)
            i += 1
        print(lt)
    key = key + 1

workbook.close()
