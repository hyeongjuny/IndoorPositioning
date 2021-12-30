import operator

# 좌표계 설정(초기 셋팅 필요)
# position = [[(0, 0)] * 2 for _ in range(100)]
# for numbeacon in range(101, 200):
#     m = ((numbeacon - 1) // 2) - 50
#     n = (numbeacon - 1) % 2
#     position[m][n] = (25 * m, 15 * n)
# 이렇게 배치하면 굳이 좌표계 array가 필요가 없음
# y 좌표 구성
#
# 102               104                 106
#
#
# 101               103                 105     x
###################################################

# 직접 입력받은 특정 minor 값 비콘의 좌표 탐색
'''numbeacon = input("위치를 알고 싶은 Beacon의 minor 값: ")
minor = [int(numbeacon[i]) for i in range(3)]
print(position[minor[1]][minor[2]])'''

# 위치 벡터 함수.
# Minor의 배치에 따라, 가로 세로 배치에 따라 Parameter 수정 필요.
def posvector(m):
    a = (int(m) - 1) // 2 - 50
    b = (int(m) - 1) % 2
    return (20 * int(a), 20 * int(b))

# 방향 벡터 함수.
# i을 기준점 O(0, 0)으로 설정한 (ii - i) 방향 벡터 tuple(a, b) 생성.
def dirvector(m,n):
    direction = tuple(map(operator.sub, posvector(int(m)), posvector(int(n))))
    return direction

# 아래는 모듈 직접 실행시 테스트 용. 이 모듈을 받아 쓰는 곳에서는 numbeaconii 와 numbeaconi을 각각 입력 혹은 정의 필요.
''' ex) numbeaconii = *
        numbeaconi = ** '''

if __name__ == "__main__":
    # 두 비콘의 minor 값을 직접 입력받았을 때, 한 비콘의 좌표를 기준점 O(0, 0)으로 설정한 방향 벡터 (a, b) 생성.
    numbeaconii, numbeaconi = map(int, input("방향벡터를 알고 싶은 두 Beacon의 minor 값(공백으로 구분, 기준점을 뒤에):").split())
    
    
    # 튜플형태의 Vector form 혹은 a, b 요소 각각 받아 사용 가능.
    
    # 벡터 그대로 tuple 형태로 저장할 때.
    vector = dirvector(numbeaconii, numbeaconi)
    
    # 벡터 요소별 a, b에 각각 저장할 때.
    a, b = dirvector(numbeaconii, numbeaconi)

    # 확인용 출력.
    print(vector)
    print(a, end=', ')
    print(b)

    # apollonius.apollo(r,a,b)