import csv
import itertools

#Home-built Modules
from apollonius import apollo
from position_vector import dirvector

# Load Data
data = []
file = open("Data/ho_3_5.csv", "r")
# file = open("Data/ho_total.csv", "r")
file_read = csv.reader(file)

for line in file_read:
    data.append(line)

file.close()
# Check
print('Data')
print(data)
a = len(data)
del data[0]     # ['time', 'minor', 'rssi'] 제외.
# Check
# del data[0]
print('Data')
print(data)

m = 3
# Initializing two-dimensional array.
real_data = [[0] * m for _ in range(a)]
for i in range(1, a - 1):
    time_split = data[i][0].split(':')  # CSV 파일에서 Time은 HH::MM:SS의 형태, 따라서 ':'로 H, M, S 구분.
    h, m, s = time_split
    time_after = ''.join([h, m, s])
    minor = data[i][1]
    rssi = data[i][2]
    real_data[i][0] = int(time_after)
    real_data[i][1] = minor
    real_data[i][2] = rssi
del real_data[0]

print('real_data')
print(real_data)
print(type(real_data[0][0]))

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

# Overlap되는 time을 없애기 위해 Set 사용.
time_ov = []
for i in real_data:
    time_ov.append(i[0])

time_ov_set = set(time_ov)

# Check
# print('time_ov')
# print(time_ov)
# print(len(time_ov))
# print('time_ov_set')
# print(time_ov_set)

time_ov_list = list(time_ov_set)
del time_ov_list[0]     # 앞에 0가 있기 때문에.

# Set을 하면 시간이 섞이기 때문에 시간 순서대로 정렬.
sorted_time_ov_list = sorted(time_ov_list)
lentime_ov_list = len(time_ov_list)

# Check
# print('time_ov_list')
# print(sorted_time_ov_list)
# print(lentime_ov_list)

# 같은 시간일 때, 해당되는 Data값을 append.
time_data = []
for i in sorted_time_ov_list:
    line = []
    for k in real_data:
        # print(k)
        if int(k[0]) == i:
            line.append([int(k[0]), k[1], int(k[2])])
    time_data.append(line)

lentime_data = len(time_data)

# Check
# print('Time_data')
# print(time_data)
# print(lentime_data)

Sample_data = []
count = []
# 같은 시간 Data에서 Combonation으로 2개씩 추출 후 Sample_data list에 저장.
for i in range(0, lentime_data):
    if len(time_data[i]) >= 2:
        Sample = list(itertools.combinations(time_data[i], 2))
        Sample_data.append(list(Sample))
        count.append(len(Sample))
        # Check
        # print(Sample)
        # print(len(Sample))
    elif len(time_data[i]) < 1:
        continue

sum_count = sum(count)
lenSample_data = len(Sample_data)
print('Sample_data')
print(Sample_data)
print(lenSample_data)

# ======================================================
# 출력을 통해 확인.
# print('count')
# print(count)
# print(count[0])
# print(count[6])
# print(count[9])
# print(count[10])
# print('sum(count)')
# print(sum(count))
# print('len(count)')
# print(len(count))

# print(lenSample_data)
# print('1')
# print(Sample_data[6])
# print('10')
# print(Sample_data[6][0])
# print('100')
# print(Sample_data[6][0][0])
# print(Sample_data[0][1])
# ======================================================

# 가로 세로의 길이 20m.
distance = 20
halfdis = distance / 2
intercept = []
position = []   # 계산이 잘 되고있나 확인하기 위해.
for i in range(0, lenSample_data - 1):
    len1 = len(Sample_data[i])
    for j in range(0, len1):
        if Sample_data[i][j][0][1] == Sample_data[i][j][1][1]:  # Minor가 같을 경우.
            continue
        else:
            # Sample_data에서 앞의 Data의 RSSI가 더 클 때.
            if Sample_data[i][j][0][2] > Sample_data[i][j][1][2]:
                a, b = dirvector(int(Sample_data[i][j][1][1]), int(Sample_data[i][j][0][1]))
                rssidif = abs(int(Sample_data[i][j][0][2]) - int(Sample_data[i][j][1][2]))
                ratio = 10 ** (rssidif / 20)
                apollo_data = apollo(ratio, a, b)
                if (a == 0 and b == distance) or (a == 0 and b == -distance) or \
                    (a == distance and b == 0) or (a == -distance and b == 0) or \
                    (a == distance and b == distance) or (a == distance and b == -distance) or \
                    (a == -distance and b == distance) or (a == -distance and b == -distance):
                    # rssidif가 1 ~ 5일 때 apollonius 원이 크게 그려지기 때문에 큰 값들 제거.
                    if rssidif < 6:
                        if apollo_data[0] > halfdis or apollo_data[0] < -halfdis:
                            apollo_data[0] = False
                        if apollo_data[1] > halfdis or apollo_data[1] < -halfdis:
                            apollo_data[1] = False
                        if apollo_data[2] > halfdis or apollo_data[2] < -halfdis:
                            apollo_data[2] = False
                        if apollo_data[3] > halfdis or apollo_data[3] < -halfdis:
                            apollo_data[3] = False

                    intercept.append(Sample_data[i][j][0][0])
                    intercept.append(apollo_data)
                    intercept.append(int(Sample_data[i][j][0][1]))
                    position.append(a)
                    position.append(b)
                    position.append(rssidif)
                    position.append(11111)
                    position.append(Sample_data[i][j][0][0])
                    position.append(apollo_data)

            # Sample_data에서 뒤의 Data의 RSSI가 더 클 때.
            elif Sample_data[i][j][0][2] < Sample_data[i][j][1][2]:
                a, b = dirvector(int(Sample_data[i][j][0][1]), int(Sample_data[i][j][1][1]))
                rssidif = abs(int(Sample_data[i][j][0][2]) - int(Sample_data[i][j][1][2]))
                ratio = 10 ** (rssidif / 20)
                apollo_data = apollo(ratio, a, b)
                if (a == 0 and b == distance) or (a == 0 and b == -distance) or \
                    (a == distance and b == 0) or (a == -distance and b == 0) or \
                    (a == distance and b == distance) or (a == distance and b == -distance) or \
                    (a == -distance and b == distance) or (a == -distance and b == -distance):
                    if rssidif < 6:
                        if apollo_data[0] > halfdis or apollo_data[0] < -halfdis:
                            apollo_data[0] = False
                        if apollo_data[1] > halfdis or apollo_data[1] < -halfdis:
                            apollo_data[1] = False
                        if apollo_data[2] > halfdis or apollo_data[2] < -halfdis:
                            apollo_data[2] = False
                        if apollo_data[3] > halfdis or apollo_data[3] < -halfdis:
                            apollo_data[3] = False

                    intercept.append(Sample_data[i][j][0][0])
                    intercept.append(apollo_data)
                    intercept.append(int(Sample_data[i][j][1][1]))
                    position.append(a)
                    position.append(b)
                    position.append(rssidif)
                    position.append(22222)
                    position.append(Sample_data[i][j][0][0])
                    position.append(apollo_data)

            # elif Sample_data[i][j][0][2] == Sample_data[i][j][1][2]:
            else:
                a, b = dirvector(int(Sample_data[i][j][1][1]), int(Sample_data[i][j][0][1]))
                rssidif = abs(int(Sample_data[i][j][0][2]) - int(Sample_data[i][j][1][2]))
                ratio = 10 ** (rssidif / 20)
                apollo_data = apollo(ratio, a, b)

                if (a == 0 and b == distance) or (a == 0 and b == -distance) or \
                    (a == distance and b == 0) or (a == -distance and b == 0) or \
                    (a == distance and b == distance) or (a == distance and b == -distance) or \
                    (a == -distance and b == distance) or (a == -distance and b == -distance):

                    intercept.append(Sample_data[i][j][0][0])
                    intercept.append(apollo_data)
                    intercept.append(int(Sample_data[i][j][0][1]))
                    position.append(a)
                    position.append(b)
                    position.append(rssidif)
                    position.append(33333)
                    position.append(Sample_data[i][j][0][0])
                    position.append(apollo_data)

lenintercept = len(intercept)
print('intercept')
print(intercept)
print(lenintercept)

# intercept와 position을 csv파일로 출력.
if __name__ == "__main__":
    with open("results/intercept_chh_3-11.csv", "w") as export:
        exportfile = csv.writer(export)
        exportfile.writerows(list_chunk(intercept, 3))
    with open("results/intercept_position_chh_3-11.csv", "w") as export:
        exportfile = csv.writer(export)
        exportfile.writerows(list_chunk(position, 6))