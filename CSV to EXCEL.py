 # import csv
 # f = open('sample.csv', 'w', encoding='UTF-8', newline='')
 # wr = csv.writer(f)
 # wr.writerow(["きんにくまん","ごご"])
 # f.close()
#csv파일 생성, 1,2,3 써 넣기

# import openpyxl
#
# f = open('CSVtest.csv', "r", encoding='utf-8')
# list = f.readlines()
# f.close()
#
# file = openpyxl.load_workbook('CSVtoEXCEL.xlsx')
# sheet = file.active
#
# def ex():
#     for i in range(1, len(list)+1):
#         list1 = list[i-1].split(',')
#         for k in range(1, len(list1)+1):
#             sheet[chr(k+64) + str(i)].value = list1[k-1]
#     file.save('CSVtoEXCEL.xlsx')
#
# ex()

#엑셀 파일 생성하기
#CSV파일 을 엑셀 파일로 저장하기
#pandas read excel
import pandas as pd
#read_Excel = pd.read_csv(r'C:\Users\Dell\PycharmProjects\pythonProject\sample.csv', encoding='UTF8')
##디렉토리 앞에 ''r'을 붙여서 unicodedecode 에러 해소
#frame_Excel = pd.DataFrame(read_Excel)
#frame_Excel.to_excel("CSVtest.xlsx", encoding='UTF-8', index=False)
##index=False로 데이터 앞에 숫자를 출력 안함
##엑셀을 csv로 되돌리기 utf-8 -> utf-8-sig 로 변경
# read_Csv = pd.read_excel(r'C:\Users\Dell\PycharmProjects\pythonProject\CSVtest.xlsx')
# frame_csv = pd.DataFrame(read_Csv)
# frame_csv.to_csv("CSVtest2.csv", encoding='UTF-8-sig')





