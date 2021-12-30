import numpy as np
import scipy as sp
import scipy.stats
#Home-built Modules
import mu_sigma

# 완전 초기값.
# 이 후에는 이전 초의 mu0, sigma20가 사전확률분포로.
# mu, sigma => 기댓값.
# mu0, sigma0 => 사전확률분포.
xmu0 = []
xsigma20 = []
xmu0.append(0)
xsigma20.append(1)
ymu0 = []
ysigma20 = []
ymu0.append(0)
ysigma20.append(1)

# 리스트로 안할 때.
# xmu0 = 0
# xsigma20 = 1
# ymu0 = 0
# ysigma20 = 1

Bayesian_result = []

data_len = mu_sigma.lenresultsum

for i in range(0, data_len, 6):
    # Time Check.
    # print('time')
    # print(mu_sigma.result_summary[i])
    Bayesian_result.append(mu_sigma.result_summary[i])
    xavg = mu_sigma.result_summary[i + 1]       # xmu
    yavg = mu_sigma.result_summary[i + 2]       # ymu
    xsigma = mu_sigma.result_summary[i + 3]     # xsigma
    xsigma2 = xsigma ** 2                       # xsigma2
    ysigma = mu_sigma.result_summary[i + 4]     # ysigma
    ysigma2 = ysigma ** 2                       # ysigma2
    X_N = mu_sigma.result_summary[i + 5][0]     # 원소 x의 갯수
    Y_N = mu_sigma.result_summary[i + 5][1]     # 원소 y의 갯수

    # xx = np.linspace(1.8, 2.2, 1000)
    np.random.seed(1)
    # Intercept avg, sigma => mu, sigma
    # 이전 mu, sigma => mu0, sigma0
    for j in range(4):  # 3차 추정.
        # 데이터를 정규 분포로.
        x = sp.stats.norm(xavg).rvs(X_N)
        y = sp.stats.norm(yavg).rvs(Y_N)
        X_Hypermu0 = xsigma2 / (X_N * xsigma20[-1] + xsigma2) * xmu0[-1] + \
                     (X_N * xsigma20[-1]) / (X_N * xsigma20[-1] + xsigma2) * x.mean()
        X_Hypersigma20 = 1 / (1 / xsigma20[-1] + X_N / xsigma2)
        Y_Hypermu0 = ysigma2 / (Y_N * ysigma20[-1] + ysigma2) * ymu0[-1] + \
                     (Y_N * ysigma20[-1]) / (Y_N * ysigma20[-1] + ysigma2) * y.mean()
        Y_Hypersigma20 = 1 / (1 / ysigma20[-1] + Y_N / ysigma2)

        if xmu0 == 0 or xsigma20 == 0:
            X_Hypermu0 = xmu0[-1]
            X_Hypersigma20 = xsigma20[-1]
        if Y_Hypermu0 == 0 or Y_Hypersigma20 == 0:
            Y_Hypermu0 = ymu0[-1]
            Y_Hypersigma20 = ysigma20[-1]

        # 리스트로 안할 때.
        # xmu0 = xsigma2 / (X_N * xsigma20 + xsigma2) * xmu0 + \
        #              (X_N * xsigma20) / (X_N * xsigma20 + xsigma2) * x.mean()
        # xsigma20 = 1 / (1 / xsigma20 + X_N / xsigma2)
        # ymu0 = ysigma2 / (Y_N * ysigma20 + ysigma2) * ymu0 + \
        #              (Y_N * ysigma20) / (Y_N * ysigma20 + ysigma2) * y.mean()
        # ysigma20 = 1 / (1 / ysigma20 + Y_N / ysigma2)
        # if xmu0 == 0 and xsigma20 == 0:
        #     xmu0 = xmu0[-1]
        #     xsigma20 = xsigma20[-1]
        # if ymu0 == 0 or ysigma20 == 0:
        #     ymu0 = 0
        #     ymu0 = 1

        xmu0.append(X_Hypermu0)
        xsigma20.append(X_Hypersigma20)
        ymu0.append(Y_Hypermu0)
        ysigma20.append(Y_Hypersigma20)

    Bayesian_result.append(xmu0[-1])
    Bayesian_result.append(ymu0[-1])

print('Bayesian_result')
print(Bayesian_result)


    # ==================================================================================================================
    # if X_N < 3 or Y_N < 3:
    #     continue
    # else:
    #     for j in range(2):
    #         x = sp.stats.norm(xavg).rvs(X_N)
    #         y = sp.stats.norm(yavg).rvs(Y_N)
    #
    #         # X_Hypermu0 = ((xsigma2 * xmu0[-1]) + (X_N * xsigma20[-1] * x.mean())) / (X_N * xsigma20[-1] + xsigma2)
    #         # X_Hypersigma20 = 1 / ((1 / xsigma20[-1]) + (X_N / xsigma2))
    #         xmu0 = ((xsigma2 * xmu0[-1]) + (X_N * xsigma20[-1] * x.mean())) / (X_N * xsigma20[-1] + xsigma2)
    #         xsigma20 = 1 / ((1 / xsigma20[-1]) + (X_N / xsigma2))
    #         # X_Hypersigma20 = xsigma20[-1] = 1 / (1 / xsigma20[-1] + X_N / xsigma2)
    #
    #         # Y_Hypermu0 = ((ysigma2 * ymu0[-1]) + (Y_N * ysigma20[-1] * y.mean())) / (Y_N * ysigma20[-1] + ysigma2)
    #         # Y_Hypersigma20 = 1 / ((1 / ysigma20[-1]) + (Y_N / ysigma2))
    #         ymu0 = ((ysigma2 * ymu0[-1]) + (Y_N * ysigma20[-1] * y.mean())) / (Y_N * ysigma20[-1] + ysigma2)
    #         ysigma20 = 1 / ((1 / ysigma20[-1]) + (Y_N / ysigma2))
    #         # Y_Hypersigma20 = ysigma20[-1] = 1 / (1 / ysigma20[-1] + Y_N / ysigma2)
    #
    #         # xmu0.append(xmu0)
    #         # xsigma20.append(xsigma20)
    #         # ymu0.append(ymu0)
    #         # ysigma20.append(ysigma20)
    #
    #         print('X_Hypermu0')
    #         print(xmu0)
    #         print('Y_Hypermu0')
    #         print(ymu0)
    # ==================================================================================================================