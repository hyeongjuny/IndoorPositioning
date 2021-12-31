# IndoorPositioning
## 사용 이론
### 1. 아폴로니우스의 원(Apollonius Circle)
<img width="346" alt="image" src="https://user-images.githubusercontent.com/96864406/147824648-29566a2b-3974-4185-ae0d-93834d9306ba.png">
  이웃한 두 개의 RSSI 신호를 이용하여 두 신호의 거리의 비가 일정한 점들의 자취 중 절편(Intercept)을 이용.
  
```
  def apollo(r, a, b):
    if r == 1 and a == 0:
        y1 = (b / 2)
        return False, False, False, y1
    elif r == 1 and b == 0:
        x1 = (a / 2)
        return x1, False, False, False
    elif r == 1 and (a != 0 and b != 0):
        x1 = (b ** 2) / (2 * a) + (a / 2)
        y1 = (a ** 2) / (2 * b) + (b / 2)
        return x1, False, y1, False
    else:
        l = 1 / (1 - r ** 2)
        x1 = a * l + (a ** 2 * l ** 2 - a ** 2 * l - b ** 2 * l - 9) ** (1/2)
        x2 = a * l - (a ** 2 * l ** 2 - a ** 2 * l - b ** 2 * l - 9) ** (1/2)
        y1 = b * l + (b ** 2 * l ** 2 - a ** 2 * l - b ** 2 * l - 9) ** (1/2)
        y2 = b * l - (b ** 2 * l ** 2 - a ** 2 * l - b ** 2 * l - 9) ** (1/2)
        return [x1, x2, y1, y2]
```

<img width="355" alt="image" src="https://user-images.githubusercontent.com/96864406/147824705-c16dd44d-fb4a-44d1-a074-fbfcffb387b0.png">

가로, 세로 또는 대각선의 신호를 이용할 때를 각각 조건문으로 구분

### 2. 베이지안 추정(Bayesian Estimation)
<img width="525" alt="image" src="https://user-images.githubusercontent.com/96864406/147824624-0ed60a14-80d8-4d80-88f1-c9f8aad7bbe4.png">

  데이터의 분포가 정규분포일 때 베이즈룰(bayes rule)에 따라 사후확률을 베이지안 방법으로 추정.




