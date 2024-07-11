import xlsxwriter
import os

path = './txt_dir'
dir_list = os.listdir(path)


for i in dir_list:
    workbook = xlsxwriter.Workbook("./output/"+i.split('.')[0]+'.xlsx')
    worksheet = workbook.add_worksheet()

    print('./txt_dir/'+i)
    with open('./txt_dir/'+i, 'r', encoding='utf-8') as f:
        listTmp = f.read().split('\n')
        key = 0
        while key < len(listTmp):
            item = listTmp[key].replace('	%','%').replace(' %','%')
            if(item.replace(' ','') != ""):
                lt = [v for v in item.split() if v != '']
                i = 0
                for x in lt:
                    worksheet.write(key+1, i, x)
                    i += 1
                print(lt)
            key = key + 1

        workbook.close()
