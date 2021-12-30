import csv
import numpy as np
#Home-built Modules
import rssi2distance
from position_vector import posvector

apollo_intercept = rssi2distance.intercept
print('apollo_intercept')
print(apollo_intercept)

result_apollo = []
q = 0
for i in range(0, len(apollo_intercept), 3):
    result_apollo.append(apollo_intercept[i])
    line = []
    for j in range(2):
        if apollo_intercept[i + 1][j] != False:
            xy1 = apollo_intercept[i + 1][j] + posvector(apollo_intercept[i + 2])[0], \
                  posvector(apollo_intercept[i + 2])[1]
            line.append(xy1)
        if apollo_intercept[i + 1][j + 2] != False:
            xy2 = posvector(apollo_intercept[i + 2])[0], apollo_intercept[i + 1][j + 2] + \
                  posvector(apollo_intercept[i + 2])[1]
            line.append(xy2)
    result_apollo.append(line)

print('result_apollo')
print(result_apollo)


x_lst, y_lst = [], []        # sigma를 계산하기 위한 list 선언.
x_cnt, y_cnt = 0, 0
avg = [x_lst, y_lst]
std = [x_cnt, y_cnt]         # 해당 초의 좌표들의 갯수. (False는 제외)
result = [0, avg, std]


# 최종 형태: [초, X avg, Y avg, X sigma2, Y sigma2, [X 개수, Y 개수]]
# 기존 3 * i로 되어있었던 것을 3씩 증가시키는 형태로 변경.
for i in range(0, len(result_apollo), 2):
    # 초기화.
    x_lst, y_lst = [], []
    x_cnt, y_cnt = 0, 0
    avg = [x_lst, y_lst]
    std = [x_cnt, y_cnt]
    # print(result_apollo[i])
    # 현재 초와 값과 다르다면 result에 "초"와 form을 추가.
    if result[-3] != result_apollo[i]:
        # Time
        result.append(result_apollo[i])
        result.append(avg)
        result.append(std)
    for q in range(len(result_apollo[i + 1])):
        x = result_apollo[i + 1][q][0]
        y = result_apollo[i + 1][q][1]
        result[-2][0].append(x)
        result[-2][1].append(y)
        # Check
        print('--==--==--==--==--==')
        print(result_apollo[i + 1][q])

    result[-1][0] = len(result[-2][0])  # x의 개수.
    result[-1][1] = len(result[-2][1])  # y의 개수.

print('result')
print(result)

# =================================
#         # Check
#         # print('========================')
#         # print(result_apollo[i])
#         # print(result_apollo[i + 1][0])
# #     # result_apollo x1, y1, x2, y2의 형태로 되어있기 때문에.
# #     if result_apollo[i + 1][0] != False:
#     x1 = result_apollo[i + 1][0]
#     x2 = result_apollo[i + 2][0]
#     x3 = result_apollo[i + 3][0]
#     x4 = result_apollo[i + 4][0]
#
#     y1 = result_apollo[i + 1][1]
#     y2 = result_apollo[i + 2][1]
#     y3 = result_apollo[i + 3][1]
#     y4 = result_apollo[i + 4][1]
#         #  = result_apollo[i + 4][1]
#
#     # print('========================')
#     # print(result_apollo[i])
#     # print(x1)
#     # print(x2)
#     # result.append(x1)
#     # result.append(x2)
#     # result.append(y1)
#     # result.append(y2)
#
#     result[-2][0].append(x1)
#     result[-2][0].append(x2)
#     result[-2][0].append(x3)
#     result[-2][0].append(x4)
#
#     result[-2][1].append(y1)
#     result[-2][1].append(y2)
#     result[-2][1].append(y3)
#     result[-2][1].append(y4)
#
# #     result[-2][0].append(x1)    # x_lst에 값 추가.
# # #     if result_apollo[i + 1][1] != False:
# #     result[-2][1].append(y1)    # y_lst에 값 추가.
# # # #     # if result_apollo[i + 1][2] != False:
# #     result[-2][0].append(x2)    # x_lst에 값 추가.
# # # # #     # if result_apollo[i + 1][3] != False:
# #     result[-2][1].append(y2)    # y_lst에 값 추가.
# #
# #         # print(result_apollo[i])
# #         # print(result_apollo[i + 1])
# #         # print(result)
# #
#     result[-1][0] = len(result[-2][0])  # x의 개수.
#     result[-1][1] = len(result[-2][1])  # y의 개수.
# #
# # Check
# print('=-=-=-=-=-=-=-=-=-=-=-')
# print(result)
# # print(result[-2][0])
# # print(result[-2][1])
# x_temp, y_temp = 0, 0
#
# del result[0]
# del result[1]
# del result[2]
#
# # Check
# print('-=-=-=-=-=-=-=')
# print('result')
# print(result)

# 계산을 위해 lst에 저장한 후 결과값을 result_summary에 저장.
result_summary = []
for i in range(3, len(result), 3):
    result_summary.append(result[i])
    result_summary.append(np.average(result[i + 1][0]))
    result_summary.append(np.average(result[i + 1][1]))
    result_summary.append(np.std(result[i + 1][0]))
    result_summary.append(np.std(result[i + 1][1]))
    result_summary.append(result[i + 2])

    # Check
    # print('+_+_+_+_+_+_+_+_')
    # print(result[i])
    # print('1111')
    # print(result[i + 1])
    # print('2222')
    # print(result[i + 1][0])
    # print('3333')
    # print(result[i + 1][1])
    # print(result[i + 2])

# del result_summary[0:10]
print('-=-=-=-=-=-=-=')
print('result_summary')
print(result_summary)
lenresultsum = len(result_summary)

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

with open("results/result_summary.csv", "w") as export:
    exportfile = csv.writer(export)
    exportfile.writerows(list_chunk(result_summary, 6))
# with open("results/intercept_position_chh_3-11.csv", "w") as export:
#     exportfile = csv.writer(export)
#     exportfile.writerows(list_chunk(position, 6))