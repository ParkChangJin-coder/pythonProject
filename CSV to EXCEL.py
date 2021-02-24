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




