import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
#Home-built Modules
import rssi2distance
import Bayesian_cal
from position_vector import posvector

# 요 친구가 Plot 최종 파일
print(np.__version__)
plt.figure(figsize=(160, 6))
# gs = gridspec.GridSpec(10, 10)
# ax1 = fig.add_subplot(gs[0:6, 0:7])
# ax2 = fig.add_subplot(gs[6:10, 0:7])
# ax3 = fig.add_subplot(gs[0:6, 7:10])

plt.grid()
plt.xlim([200, 800])
plt.ylim([-5, 25])

print('rssi2distance.sum_count')
print(rssi2distance.sum_count)
q = 0
for i in range(0, rssi2distance.sum_count):
    # count = 0
    for j in range(2):
        plt.scatter(rssi2distance.intercept[3 * i + 1][j]\
        + posvector(rssi2distance.intercept[3 * i + 2])[0], posvector(rssi2distance.intercept[3 * i + 2])[1], s=50, c='r', alpha=0.2)

        plt.scatter(posvector(rssi2distance.intercept[3 * i + 2])[0], \
                    rssi2distance.intercept[3 * i + 1][j + 2] + posvector(rssi2distance.intercept[3 * i + 2])[1], s=50, c='b', alpha=0.2)

    plt.title(rssi2distance.intercept[3 * i])
    # print('Check')
    # print(rssi2distance.intercept.index(rssi2distance.intercept[3 * i]))
    # print(rssi2distance.count.index(rssi2distance.count[i]))
    if (rssi2distance.intercept[3 * i] != rssi2distance.intercept[3 * (i + 1)]):  # 현재 시간과 다음 시간이 다르다면.
        plt.scatter(Bayesian_cal.Bayesian_result[q + 1], Bayesian_cal.Bayesian_result[q + 2],s=50, c='g', alpha=0.8)
        q = q + 3

        plt.pause(0.9)
        plt.clf()
        plt.grid()
        plt.xlim([200, 800])
        plt.ylim([-5, 25])

        # Check
        # print('+-+-+-+-+-+-+-+-+-+-+-+-')
        # print(Bayesian_cal.Bayesian_result[q + 1])
        # print(Bayesian_cal.Bayesian_result[q + 2])
        # print(Bayesian_cal.Bayesian_result[q + 1] \
        #     +  posvector(rssi2distance.intercept[3 * i + 2])[0], posvector(rssi2distance.intercept[3 * i + 2])[1])
        # print(posvector(rssi2distance.intercept[3 * i + 2])[0],\
        #     Bayesian_cal.Bayesian_result[q + 2] + posvector(rssi2distance.intercept[3 * i + 2])[1])
        # print(mu_sigma.result_summary[q])
        # print(mu_sigma.result_summary[q + 1])
        # print(rssi2distance.intercept[3 * i])
    # plt.savefig(str(i) + '.jpg')

plt.show()