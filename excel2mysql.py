import xlrd
import pymysql

book = xlrd.open_workbook('D:\Ducument\data_text.xlsx')
sheet = book.sheet_by_name('Sheet1')
# 建立数据库连接
connect = pymysql.connect(
    host='10.10.10.226',
    user='root',
    passwd='123456mysql',
    db='solr',
    port=3306,
    charset='utf8mb4'
)
# 获得游标
cur = connect.cursor()
# sql_select = 'SELECT * FROM product;'
# cur.execute(sql_select)
# rowcount = cur.rowcount
# print(cur.rowcount)
# for n in range(0, rowcount):
#     print(cur.fetchone())

#cur.executemany()

ops = []
for i in range(1, sheet.nrows):
    # print(sheet.cell(i, 0))
    # cell = sheet.cell(i, 1).value
    cell = (sheet.cell(i, 0).value, sheet.cell(i, 1).value)
    ops.append(cell)
    #print(cell)
cur.executemany('insert into text_big(id, text) values(%s, %s)', ops)
cur.close()
connect.commit()
connect.close()
print('导入数据成功。。。')

