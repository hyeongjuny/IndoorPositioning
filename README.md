# IndoorPositioning
## 이론
### 1. 아폴로니우스의 원(Apollonius Circle)
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
ㅁㄴㄹ
### 2. 베이지안 추정(Bayesian Estimation)

